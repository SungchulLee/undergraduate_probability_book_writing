"""Why the t-distribution: (X̄ − μ)/(S/√n) follows t_{n-1} for normal data."""
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats


# ========================================================================


def main():
    np.random.seed(42)

    sample_size = 10_000
    mu, sigma = 0, 10
    n = 10

    # Draw n observations per experiment, repeat sample_size times
    x = np.random.normal(mu, sigma, (n, sample_size))
    x_bar = x.mean(axis=0)
    s = x.std(axis=0, ddof=1)

    # Studentized statistic
    t_stat = (x_bar - mu) / (s / np.sqrt(n))

    fig, ax = plt.subplots(figsize=(10, 5))
    bins = np.arange(-6, 6, 0.1)
    ax.hist(t_stat, bins=bins, density=True, alpha=0.6, color="steelblue",
            label="Simulated t-statistic")
    ax.plot(bins, stats.t(df=n - 1).pdf(bins), "--r", lw=2, label=f"t({n-1}) PDF")
    ax.plot(bins, stats.norm.pdf(bins), ":k", lw=1.5, label="N(0,1) PDF")
    ax.set_title(f"(X̄ − μ) / (S/√n)  ~  t({n-1})", fontsize=14)
    ax.legend()
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig("why_t_distribution.png", dpi=150, bbox_inches="tight")
    plt.show()


# ========================================================================


if __name__ == "__main__":
    main()
