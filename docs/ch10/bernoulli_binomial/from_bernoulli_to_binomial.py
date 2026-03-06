"""Demonstrate that a sum of Bernoulli RVs follows the Binomial distribution."""
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats


# ========================================================================


def main():
    np.random.seed(42)

    n = 3
    p = 0.7
    n_sim = 10_000

    samples_bernoulli = np.random.binomial(1, p, size=(n, n_sim))
    samples_binomial = samples_bernoulli.sum(axis=0)

    x = np.arange(n + 1)
    pmf = stats.binom(n, p).pmf(x)

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.bar(x, pmf, alpha=0.4, label="Theoretical PMF", width=0.4)
    ax.hist(
        samples_binomial,
        bins=np.arange(-0.5, n + 1.5),
        density=True,
        histtype="step",
        linewidth=2,
        color="red",
        label=f"Sum of {n} Bernoulli({p}) samples",
    )
    ax.set_title(f"Binomial B({n}, {p}): Theory vs Simulation", fontsize=14)
    ax.set_xlabel("k")
    ax.set_ylabel("Probability")
    ax.legend()
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig("from_bernoulli_to_binomial.png", dpi=150, bbox_inches="tight")
    plt.show()


# ========================================================================


if __name__ == "__main__":
    main()
