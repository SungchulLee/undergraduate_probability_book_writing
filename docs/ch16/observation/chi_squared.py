"""Sum of iid Chi-squared(1) random variables approaching Normal."""
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats


# ========================================================================


def main():
    np.random.seed(42)
    n_sim = 10000

    fig, axes = plt.subplots(2, 3, figsize=(14, 8))
    for idx, n in enumerate([2, 3, 5, 10, 30, 100]):
        ax = axes.flatten()[idx]
        S = np.sum(np.random.chisquare(1, (n, n_sim)), axis=0)
        ax.hist(S, bins=100, density=True, alpha=0.7, color='steelblue')
        mu, sigma = n, np.sqrt(2*n)
        x = np.linspace(max(0, mu - 4*sigma), mu + 4*sigma, 200)
        ax.plot(x, stats.norm.pdf(x, mu, sigma), 'r-', lw=2)
        ax.set_title(f'n = {n}')
        ax.grid(True, alpha=0.3)

    plt.suptitle('Sum of χ²(1) → Normal', fontsize=14, fontweight='bold')
    plt.tight_layout()
    plt.savefig('chi_squared_clt.png', dpi=150, bbox_inches='tight')
    plt.show()


# ========================================================================


if __name__ == "__main__":
    main()
