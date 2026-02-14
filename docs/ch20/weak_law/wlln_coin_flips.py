"""Weak Law of Large Numbers: distribution of sample mean concentrates around p."""
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)

p = 0.5
num_paths = 10_000
num_steps = 10_000

flips = np.random.binomial(1, p, (num_paths, num_steps))
cumsum = flips.cumsum(axis=1)

fig, axes = plt.subplots(1, 4, figsize=(16, 4))
for ax, n in zip(axes, [10, 100, 1_000, 10_000]):
    sample_means = cumsum[:, n - 1] / n
    ax.hist(sample_means, bins=40, density=True, alpha=0.7, color="steelblue")
    ax.axvline(p, color="r", linestyle="--", lw=2)
    ax.set_title(f"n = {n:,}")
    ax.set_xlim(0, 1)
    ax.grid(True, alpha=0.3)

plt.suptitle("WLLN: Distribution of X̄ₙ Concentrates Around p = 0.5",
             fontsize=14, fontweight="bold")
plt.tight_layout()
plt.savefig("wlln_coin_flips.png", dpi=150, bbox_inches="tight")
plt.show()
