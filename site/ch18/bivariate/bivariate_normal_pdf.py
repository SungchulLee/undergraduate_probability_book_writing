"""3-D surface plots of the bivariate normal PDF for different correlation values."""
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats


# ========================================================================


def main():
    n = 40
    mu1, mu2 = 0, 0
    sigma1, sigma2 = 1, 0.5
    rhos = (0.0, -0.8, 0.8)

    x = np.linspace(-3, 3, n)
    y = np.linspace(-3, 3, n)
    X, Y = np.meshgrid(x, y)
    pos = np.stack([X, Y], axis=-1)

    fig, axes = plt.subplots(1, 3, figsize=(16, 5), subplot_kw={"projection": "3d"})
    for ax, rho in zip(axes, rhos):
        cov = [[sigma1**2, rho * sigma1 * sigma2],
               [rho * sigma1 * sigma2, sigma2**2]]
        Z = stats.multivariate_normal([mu1, mu2], cov).pdf(pos)
        ax.plot_surface(X, Y, Z, cmap="viridis", linewidth=0, antialiased=True)
        ax.set_title(f"ρ = {rho}")
        ax.set_xlabel("X")
        ax.set_ylabel("Y")
        ax.view_init(30, -60)

    plt.suptitle("Bivariate Normal PDF", fontsize=14, fontweight="bold")
    plt.tight_layout()
    plt.savefig("bivariate_normal_pdf.png", dpi=150, bbox_inches="tight")
    plt.show()


# ========================================================================


if __name__ == "__main__":
    main()
