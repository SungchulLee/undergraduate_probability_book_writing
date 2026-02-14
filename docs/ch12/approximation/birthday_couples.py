"""Poisson approximation for the number of couples sharing a birthday."""
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

n_samples = 100_000
n = 80_000       # number of couples (pairs)
p = 1 / 365     # probability a couple shares a birthday
la = n * p       # Poisson parameter

samples_binomial = np.random.binomial(n, p, n_samples)
samples_poisson = np.random.poisson(la, n_samples)

fig, (ax0, ax1) = plt.subplots(1, 2, figsize=(12, 4))
bins = np.arange(150, 300)

ax0.hist(samples_binomial, bins=bins, density=True, color="steelblue", edgecolor="black")
ax0.set_title("Binomial sampling")
ax0.grid(True, alpha=0.3)

ax1.hist(samples_poisson, bins=bins, density=True, color="steelblue", edgecolor="black")
ax1.set_title("Poisson sampling")
ax1.grid(True, alpha=0.3)

plt.suptitle(f"Number of couples sharing a birthday (n={n:,}, λ={la:.1f})",
             fontsize=13, fontweight="bold")
plt.tight_layout()
plt.savefig("birthday_couples.png", dpi=150, bbox_inches="tight")
plt.show()
