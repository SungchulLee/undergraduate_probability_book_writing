"""Sum of iid Beta(1,5) random variables approaching Normal."""
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats


# ========================================================================


def main():
    np.random.seed(42)
    n_sim = 10000
    a, b = 1, 5

    fig, axes = plt.subplots(2, 3, figsize=(14, 8))
    for idx, n in enumerate([2, 3, 5, 10, 30, 100]):
        ax = axes.flatten()[idx]
        S = np.sum(np.random.beta(a, b, (n, n_sim)), axis=0)
        ax.hist(S, bins=100, density=True, alpha=0.7, color='steelblue')
        mu = n * a / (a + b)
        sigma = np.sqrt(n * a * b / ((a+b)**2 * (a+b+1)))
        x = np.linspace(max(0, mu - 4*sigma), mu + 4*sigma, 200)
        ax.plot(x, stats.norm.pdf(x, mu, sigma), 'r-', lw=2)
        ax.set_title(f'n = {n}')
        ax.grid(True, alpha=0.3)

    plt.suptitle('Sum of Beta(1,5) → Normal', fontsize=14, fontweight='bold')
    plt.tight_layout()
    plt.savefig('beta_clt.png', dpi=150, bbox_inches='tight')
    plt.show()


# ========================================================================


if __name__ == "__main__":
    main()
