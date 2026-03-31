"""CLT for coin flips: standardized sums converge to Standard Normal."""
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

np.random.seed(0)

p = 0.5
q = 1 - p
num_paths = 10_000
num_steps = 10_000

# Simulate coin flips: 1 = head, 0 = tail
flips = np.random.binomial(1, p, (num_paths, num_steps))
cumsum = flips.cumsum(axis=1)

fig, axes = plt.subplots(1, 4, figsize=(16, 4))
bins = np.linspace(-4, 4, 61)
y_norm = stats.norm.pdf(bins)

for ax, n in zip(axes, [10, 100, 1_000, 10_000]):
    S_n = cumsum[:, n - 1]
    Z_n = (S_n - n * p) / np.sqrt(n * p * q)
    ax.hist(Z_n, bins=bins, density=True, alpha=0.6, color="steelblue")
    ax.plot(bins, y_norm, "--r", lw=2, label="N(0,1)")
    ax.set_title(f"n = {n:,}")
    ax.set_xlim(-4, 4)
    ax.set_ylim(0, 0.5)
    ax.grid(True, alpha=0.3)
    ax.legend(fontsize=8)

plt.suptitle("CLT: Standardised Coin-Flip Sums → Standard Normal",
             fontsize=14, fontweight="bold")
plt.tight_layout()
plt.savefig("clt_coin_flips.png", dpi=150, bbox_inches="tight")
plt.show()
