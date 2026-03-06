"""Inverse Transform Sampling (Smirnov Transform) for discrete random variables."""
import numpy as np
import matplotlib.pyplot as plt


# ========================================================================


def main():
    np.random.seed(42)

    # Custom discrete distribution
    x_values = np.array([-3, -1, 1, 2, 5])
    pmf = np.array([0.1, 0.1, 0.1, 0.5, 0.2])
    n_sim = 10_000


    def inverse_transform_sample(pmf, x_values):
        """Sample one value using inverse CDF (Smirnov transform)."""
        cdf = np.cumsum(pmf)
        u = np.random.rand()
        idx = np.searchsorted(cdf, u)
        return x_values[idx]


    # Method 1: inverse transform
    samples_inv = np.array([inverse_transform_sample(pmf, x_values) for _ in range(n_sim)])

    # Method 2: np.random.choice (for comparison)
    samples_choice = np.random.choice(x_values, size=n_sim, p=pmf)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))

    bins = np.array([-4, -2, 0, 0.5, 1.5, 3.5, 6])

    ax1.hist(samples_inv, bins=bins, density=True, alpha=0.7, color="steelblue",
             edgecolor="black")
    ax1.set_title("Inverse Transform Sampling")
    ax1.set_xticks(x_values)
    ax1.grid(True, alpha=0.3)

    ax2.hist(samples_choice, bins=bins, density=True, alpha=0.7, color="steelblue",
             edgecolor="black")
    ax2.set_title("np.random.choice (reference)")
    ax2.set_xticks(x_values)
    ax2.grid(True, alpha=0.3)

    plt.suptitle("Inverse Transform Sampling for Discrete RVs", fontsize=14, fontweight="bold")
    plt.tight_layout()
    plt.savefig("inverse_transform_sampling.png", dpi=150, bbox_inches="tight")
    plt.show()


# ========================================================================


if __name__ == "__main__":
    main()
