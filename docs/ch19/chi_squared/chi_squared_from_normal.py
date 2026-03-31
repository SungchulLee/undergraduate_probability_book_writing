"""Chi-squared as sum of squared standard normals: compare sampling methods."""
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

np.random.seed(42)
df = 5

data_direct = stats.chi2(df=df).rvs(10_000)
data_from_norm = np.sum(stats.norm.rvs(size=(df, 10_000)) ** 2, axis=0)

fig, (ax0, ax1) = plt.subplots(1, 2, figsize=(12, 4))

_, bins, _ = ax0.hist(data_direct, bins=100, density=True, alpha=0.7, color="steelblue")
y = stats.chi2(df=df).pdf(bins)
ax0.plot(bins, y, "--r", lw=2)
ax0.set_title("Direct χ² sampling")

ax1.hist(data_from_norm, bins=bins, density=True, alpha=0.7, color="steelblue")
ax1.plot(bins, y, "--r", lw=2)
ax1.set_title("Sum of squared N(0,1)")

for ax in (ax0, ax1):
    ax.grid(True, alpha=0.3)

plt.suptitle(f"χ²({df}) = Z₁² + Z₂² + ··· + Z_{df}²", fontsize=14, fontweight="bold")
plt.tight_layout()
plt.savefig("chi_squared_from_normal.png", dpi=150, bbox_inches="tight")
plt.show()
