"""Correlation Simulation: visualize correlation with scatter plots and marginal distributions."""
import numpy as np
import matplotlib.pyplot as plt


def main():
    np.random.seed(42)
    n_samples = 500

    # generate bivariate normal samples with different correlations
    rho_values = [-0.8, 0.0, 0.5, 0.95]

    fig, axes = plt.subplots(2, 2, figsize=(10, 10))
    axes = axes.ravel()

    for i, rho in enumerate(rho_values):
        # covariance matrix
        mu = np.array([0, 0])
        cov = np.array([[1, rho], [rho, 1]])

        # generate samples
        samples = np.random.multivariate_normal(mu, cov, size=n_samples)
        x, y = samples[:, 0], samples[:, 1]

        # compute sample correlation
        r = np.corrcoef(x, y)[0, 1]

        # scatter plot
        axes[i].scatter(x, y, alpha=0.4, s=15, color="steelblue")
        axes[i].set_xlabel("X")
        axes[i].set_ylabel("Y")
        axes[i].set_title(f"$\\rho$ = {rho}  (sample r = {r:.3f})")
        axes[i].set_xlim(-4, 4)
        axes[i].set_ylim(-4, 4)
        axes[i].set_aspect("equal")
        axes[i].grid(True, alpha=0.3)

    plt.suptitle("Bivariate Normal Samples with Different Correlations",
                 fontsize=13, y=1.01)
    plt.tight_layout()
    plt.savefig("correlation_simulation.png", dpi=150, bbox_inches="tight")
    plt.show()


if __name__ == "__main__":
    main()
