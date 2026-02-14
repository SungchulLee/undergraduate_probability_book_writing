"""
Side-by-Side Dashboard: Why Do Sums Always Look Normal?

This script visualizes the sum of two iid random variables from various
distributions, demonstrating that even with n=2, the sum already begins
to look more "bell-shaped" than the original distribution.

As n increases (try changing n=2 to n=5, 10, 30), the distributions
converge to Normal by the Central Limit Theorem.

Based on: Distributions related to the Poisson point process, Figure 2.
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

np.random.seed(42)

n = 2           # Number of variables to sum (S_n = X_1 + ... + X_n)
n_sim = 10000   # Number of simulations
n_bins = 100    # Number of histogram bins

distributions = {
    'Bernoulli(0.7)': lambda size: np.random.binomial(1, 0.7, size),
    'Exp(1)':         lambda size: np.random.exponential(1.0, size),
    'Po(1)':          lambda size: np.random.poisson(1.0, size),
    'N(0,1)':         lambda size: np.random.normal(0, 1, size),
    'Beta(1,5)':      lambda size: np.random.beta(1, 5, size),
    'F(20,10)':       lambda size: np.random.f(20, 10, size),
}

fig, axes = plt.subplots(3, 2, figsize=(12, 12))
axes = axes.flatten()

for idx, (name, sampler) in enumerate(distributions.items()):
    # Generate n_sim copies of S_n = X_1 + ... + X_n
    samples = np.array([sampler(n_sim) for _ in range(n)])
    sums = samples.sum(axis=0)

    ax = axes[idx]
    ax.hist(sums, bins=n_bins, density=True, alpha=0.7,
            color='steelblue', edgecolor='none')
    ax.set_title(f'S_{n} where X_i ~ {name}', fontsize=11)
    ax.set_ylabel('Density')
    ax.grid(True, alpha=0.3)

    # Add Normal overlay for comparison
    mu = np.mean(sums)
    sigma = np.std(sums)
    if sigma > 0:
        x_norm = np.linspace(mu - 4*sigma, mu + 4*sigma, 200)
        ax.plot(x_norm, stats.norm.pdf(x_norm, mu, sigma),
                'r-', lw=1.5, alpha=0.7, label='Normal fit')
        ax.legend(fontsize=9)

plt.suptitle(f'Empirical Distribution of S_{n} = X_1 + X_2 + ... + X_{n}\n'
             f'(n = {n}, {n_sim:,} simulations)',
             fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('clt_dashboard.png', dpi=150, bbox_inches='tight')
plt.show()

# Print summary statistics
print(f"\n{'Distribution':<18} {'Mean':>8} {'Std Dev':>10} {'Skewness':>10} {'Kurtosis':>10}")
print("-" * 60)
for name, sampler in distributions.items():
    samples = np.array([sampler(n_sim) for _ in range(n)])
    sums = samples.sum(axis=0)
    print(f"{name:<18} {np.mean(sums):8.4f} {np.std(sums):10.4f} "
          f"{stats.skew(sums):10.4f} {stats.kurtosis(sums):10.4f}")
