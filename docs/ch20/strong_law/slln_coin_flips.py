"""Strong Law of Large Numbers: individual paths of X̄ₙ converge to p almost surely."""
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

p = 0.5
num_paths = 20
num_steps = 5_000

flips = np.random.binomial(1, p, (num_paths, num_steps))
cumsum = flips.cumsum(axis=1)
n_range = np.arange(1, num_steps + 1)

fig, ax = plt.subplots(figsize=(12, 5))
for i in range(num_paths):
    ax.plot(n_range, cumsum[i] / n_range, alpha=0.4, linewidth=0.8)

ax.axhline(p, color="r", linestyle="--", lw=2, label=f"p = {p}")
ax.set_title("SLLN: Sample Averages Converge to p (a.s.)", fontsize=14)
ax.set_xlabel("Number of coin flips (n)")
ax.set_ylabel("Running average X̄ₙ")
ax.set_ylim(0.2, 0.8)
ax.legend()
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig("slln_coin_flips.png", dpi=150, bbox_inches="tight")
plt.show()
