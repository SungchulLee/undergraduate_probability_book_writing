"""Log of Lognormal samples follows a Normal distribution."""
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

np.random.seed(42)

mu, sigma = 2, 2
s, scale = sigma, np.exp(mu)

data = np.log(stats.lognorm(s=s, scale=scale).rvs(10_000))
data_from_norm = stats.norm(loc=mu, scale=sigma).rvs(10_000)

fig, (ax0, ax1) = plt.subplots(1, 2, figsize=(12, 4))

_, bins, _ = ax0.hist(data, bins=100, density=True, alpha=0.7, color="steelblue")
y = stats.norm(loc=mu, scale=sigma).pdf(bins)
ax0.plot(bins, y, "--r", lw=2)
ax0.set_title("log(Lognormal samples)")

ax1.hist(data_from_norm, bins=bins, density=True, alpha=0.7, color="steelblue")
ax1.plot(bins, y, "--r", lw=2)
ax1.set_title("Normal samples directly")

for ax in (ax0, ax1):
    ax.grid(True, alpha=0.3)

plt.suptitle(f"log(LogNormal) ~ Normal(μ={mu}, σ={sigma})", fontsize=14, fontweight="bold")
plt.tight_layout()
plt.savefig("log_of_lognormal.png", dpi=150, bbox_inches="tight")
plt.show()
