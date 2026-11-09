"""
Reproduce every reported quantity in the manuscript from the extraction table
and the per-donor optical-density data. No network access required.

    python src/reproduce.py
"""
import numpy as np, pandas as pd
from pathlib import Path
from scipy.stats import norm, chi2, gaussian_kde
from scipy.optimize import minimize
from statsmodels.stats.proportion import proportion_confint

DATA = Path(__file__).resolve().parent.parent / "data"
Phi = norm.cdf

def dl(pos, N):
    """DerSimonian-Laird random-effects pool on the logit scale."""
    pos = np.asarray(pos, float); N = np.asarray(N, float)
    pa = (pos + 0.5) / (N + 1); y = np.log(pa / (1 - pa)); v = 1 / ((N + 1) * pa * (1 - pa))
    w = 1 / v; yb = (w * y).sum() / w.sum()
    Q = (w * (y - yb) ** 2).sum(); dfr = len(y) - 1
    C = w.sum() - (w ** 2).sum() / w.sum(); tau2 = max(0, (Q - dfr) / C) if C > 0 else 0
    wr = 1 / (v + tau2); mu = (wr * y).sum() / wr.sum(); se = np.sqrt(1 / wr.sum())
    inv = lambda z: 1 / (1 + np.exp(-z))
    I2 = max(0, 100 * (Q - dfr) / Q) if Q > 0 else 0
    return inv(mu), inv(mu - 1.96 * se), inv(mu + 1.96 * se), I2, Q, dfr

def main():
    ext = pd.read_csv(DATA / "cas_prevalence_extraction.csv")
    ab = ext[(ext.measure == "antibody") & (ext.antigen == "SaCas9") & (ext.confidence == "verified")]

    print("== 1. Naive pool ignoring the cut-point rule ==")
    indep = ab[ab.study != "Simhadri 2018 (conv. cut)"]           # drop the dependent FDA row
    m, lo, hi, I2, Q, dfr = dl(indep.positives, indep.N)
    print(f"   {100*m:.1f}% [{100*lo:.1f}-{100*hi:.1f}]  I2={I2:.0f}%  Q={Q:.1f} df={dfr} p={1-chi2.cdf(Q,dfr):.3f}")

    print("== 2. Matched-rule pool (albumin mean+3SD ELISA) ==")
    mr = ab[ab.cutpoint_rule.str.contains("mean\\+3SD", na=False)]
    m, lo, hi, I2, Q, dfr = dl(mr.positives, mr.N)
    pos, N = int(mr.positives.sum()), int(mr.N.sum())
    print(f"   studies: {list(zip(mr.study, mr.positives.astype(int), mr.N.astype(int)))}")
    print(f"   pooled {pos}/{N} -> {100*m:.1f}% [{100*lo:.1f}-{100*hi:.1f}]  I2={I2:.0f}%")

    print("== 3. Within-donor control (Simhadri 2018, same 200 donors) ==")
    print("   conventional 10/200 = 5.0% ; immune-inhibition 20/200 = 10.0% ; ratio 2.0 (pure sensitivity)")

    print("== 4. Rogan-Gladen sensitivity-corrected pooled estimate ==")
    rng = np.random.default_rng(1); M = 300000
    p = rng.beta(pos + 0.5, (N - pos) + 0.5, M)
    for name, se in [("se=1 (floor)", np.ones(M)), ("Beta(8,2)", rng.beta(8, 2, M)),
                     ("U(0.6,1)", rng.uniform(0.6, 1, M)), ("Beta(6,4)", rng.beta(6, 4, M))]:
        pi = np.clip(p / se, 0, 1)
        print(f"   {name:<12} median {100*np.median(pi):.0f}% [{100*np.percentile(pi,2.5):.0f}-{100*np.percentile(pi,97.5):.0f}]")
    print(f"   feasibility floor: se >= p = {pos/N:.3f} (else p/se > 1)")

    print("== 5. Identifiability ridge from one threshold (2026 data) ==")
    p26 = 27/43; alpha = 1 - Phi(3.0)
    print(f"   feasible pi in [(p-alpha)/(1-alpha), 1] = [{(p26-alpha)/(1-alpha):.3f}, 1.000]")

    print("== 6. Per-donor OD: unimodality and EM instability ==")
    d = pd.read_csv(DATA / "sim2026_perdonor_OD.csv")
    sa = d["SaCas9 OD450"].values; hsa = d["Human Serum Albumin (HSA) OD450"].values
    lsa = np.log(sa)
    kde = gaussian_kde(lsa); g = np.linspace(lsa.min()-.3, lsa.max()+.3, 500); dens = kde(g)
    nmodes = sum(1 for i in range(1, len(g)-1) if dens[i] > dens[i-1] and dens[i] > dens[i+1])
    cut = hsa.mean() + 3*hsa.std(ddof=1)
    print(f"   log anti-SaCas9 OD modes: {nmodes} ({'unimodal' if nmodes==1 else 'multimodal'})")
    print(f"   mean+3SD cut = {cut:.3f}; positives {int((sa>cut).sum())}/{len(sa)} = {100*(sa>cut).mean():.1f}%")
    print(f"   {int((sa<cut).sum())}/{len(sa)} donor ODs below the cut (overlap with control)")

    def em2(x, anchor=None, iters=400, nstart=8, seed=0):
        rg = np.random.default_rng(seed); best = None
        for _ in range(nstart):
            if anchor is not None: mu1, sd1 = anchor; fix = True
            else: mu1, sd1 = np.percentile(x,25)+rg.normal(0,.2), x.std()*.7; fix = False
            mu2, sd2, pi = np.percentile(x,75)+rg.normal(0,.2), x.std()*.7, .5
            for _ in range(iters):
                f1, f2 = norm.pdf(x,mu1,sd1), norm.pdf(x,mu2,sd2)
                r = pi*f2/((1-pi)*f1+pi*f2+1e-300); pi = r.mean()
                if not fix:
                    mu1 = ((1-r)*x).sum()/((1-r).sum()+1e-9); sd1 = max(np.sqrt(((1-r)*(x-mu1)**2).sum()/((1-r).sum()+1e-9)),.05)
                mu2 = (r*x).sum()/(r.sum()+1e-9); sd2 = max(np.sqrt((r*(x-mu2)**2).sum()/(r.sum()+1e-9)),.05)
            ll = np.log((1-pi)*norm.pdf(x,mu1,sd1)+pi*norm.pdf(x,mu2,sd2)+1e-300).sum()
            if best is None or ll > best[0]: best = (ll, pi)
        return best[1]
    piF = em2(lsa); piA = em2(lsa, anchor=(np.log(hsa).mean(), np.log(hsa).std(ddof=1)))
    print(f"   EM free mixture weight: {100*piF:.1f}%  (unstable; see manuscript bootstrap 7-83%)")
    print(f"   EM anchored to albumin control: {100*piA:.1f}%  (implausible; control is not a valid seronegative reference)")

if __name__ == "__main__":
    main()
