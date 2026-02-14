"""Sum of iid U(-0.5, 0.5) random variables approaching Normal."""
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

np.random.seed(42)
n_sim = 10000

fig, axes = plt.subplots(2, 3, figsize=(14, 8))
for idx, n in enumerate([2, 3, 5, 10, 30, 100]):
    ax = axes.flatten()[idx]
    S = np.sum(np.random.uniform(-0.5, 0.5, (n, n_sim)), axis=0)
    ax.hist(S, bins=100, density=True, alpha=0.7, color='steelblue')
    mu, sigma = 0, np.sqrt(n/12)
    x = np.linspace(mu - 4*sigma, mu + 4*sigma, 200)
    ax.plot(x, stats.norm.pdf(x, mu, sigma), 'r-', lw=2)
    ax.set_title(f'n = {n}')
    ax.grid(True, alpha=0.3)

plt.suptitle('Sum of U(-1/2, 1/2) -> Normal', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('uniform_clt.png', dpi=150, bbox_inches='tight')
plt.show()
