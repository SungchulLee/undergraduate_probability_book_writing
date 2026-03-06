"""Sum of iid Bernoulli(0.7) random variables approaching Normal."""
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats


# ========================================================================


def main():
    np.random.seed(42)
    n_sim = 10000
    p = 0.7

    fig, axes = plt.subplots(2, 3, figsize=(14, 8))
    for idx, n in enumerate([2, 5, 10, 20, 50, 100]):
        ax = axes.flatten()[idx]
        S = np.random.binomial(n, p, n_sim)
        ax.hist(S, bins=range(int(S.min()), int(S.max())+2), density=True,
                alpha=0.7, color='steelblue', edgecolor='black', align='left')
        mu, sigma = n*p, np.sqrt(n*p*(1-p))
        x = np.linspace(mu - 4*sigma, mu + 4*sigma, 200)
        ax.plot(x, stats.norm.pdf(x, mu, sigma), 'r-', lw=2)
        ax.set_title(f'Bin({n}, {p})')
        ax.grid(True, alpha=0.3)

    plt.suptitle('Sum of Bernoulli(0.7) -> Normal', fontsize=14, fontweight='bold')
    plt.tight_layout()
    plt.savefig('bernoulli_binomial_clt.png', dpi=150, bbox_inches='tight')
    plt.show()


# ========================================================================


if __name__ == "__main__":
    main()
