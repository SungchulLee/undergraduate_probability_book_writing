"""Scatter plot of samples from a bivariate normal distribution."""
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats


# ========================================================================


def main():
    np.random.seed(42)

    mu1, mu2 = 0, 0
    sigma1, sigma2 = 1, 1
    rho = 0.8

    cov = [[sigma1**2, rho * sigma1 * sigma2],
           [rho * sigma1 * sigma2, sigma2**2]]
    samples = stats.multivariate_normal([mu1, mu2], cov).rvs(500)

    fig, ax = plt.subplots(figsize=(6, 6))
    ax.scatter(samples[:, 0], samples[:, 1], alpha=0.5, s=15)
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_title(f"Bivariate Normal Samples (ρ = {rho})")
    ax.set_aspect("equal")
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig("bivariate_normal_samples.png", dpi=150, bbox_inches="tight")
    plt.show()


# ========================================================================


if __name__ == "__main__":
    main()
