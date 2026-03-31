"""Lognormal from Normal: compare direct lognormal sampling with exp(Normal)."""
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

np.random.seed(42)

mu, sigma = 2, 2
s, scale = sigma, np.exp(mu)

data_lognorm = stats.lognorm(s=s, scale=scale).rvs(10_000)
data_from_norm = np.exp(stats.norm(loc=mu, scale=sigma).rvs(10_000))

fig, (ax0, ax1) = plt.subplots(1, 2, figsize=(12, 4))
bins = np.linspace(0, 20, 100)

_, bins_out, _ = ax0.hist(data_lognorm, bins=bins, density=True, alpha=0.7,
                          color="steelblue")
y = stats.lognorm(s=s, scale=scale).pdf(bins_out)
ax0.plot(bins_out, y, "--r", lw=2)
ax0.set_title("Lognormal sampling")

ax1.hist(data_from_norm, bins=bins, density=True, alpha=0.7, color="steelblue")
ax1.plot(bins_out, y, "--r", lw=2)
ax1.set_title("exp(Normal) sampling")

for ax in (ax0, ax1):
    ax.grid(True, alpha=0.3)

plt.suptitle(f"LogNormal(μ={mu}, σ={sigma})", fontsize=14, fontweight="bold")
plt.tight_layout()
plt.savefig("lognormal_from_normal.png", dpi=150, bbox_inches="tight")
plt.show()
