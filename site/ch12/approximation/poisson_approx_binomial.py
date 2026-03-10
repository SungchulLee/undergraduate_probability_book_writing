"""Poisson approximation to the Binomial: compare histograms for large n, small p."""
import numpy as np
import matplotlib.pyplot as plt


# ========================================================================


def main():
    np.random.seed(42)

    N = 1000       # large n
    P = 0.01       # small p
    LA = N * P     # lambda = np = 10
    N_SAMPLES = 10_000

    bin_samples = np.random.binomial(N, P, N_SAMPLES)
    po_samples = np.random.poisson(LA, N_SAMPLES)

    fig, (ax0, ax1, ax2) = plt.subplots(1, 3, figsize=(14, 4))

    bins = np.arange(int(3 * LA))

    ax0.hist(bin_samples, bins=bins, density=True, color="steelblue", edgecolor="black")
    ax0.set_title(f"Binomial({N}, {P})")

    ax1.hist(po_samples, bins=bins, density=True, color="steelblue", edgecolor="black")
    ax1.set_title(f"Poisson({LA:.0f})")

    ax2.hist(bin_samples, bins=bins, density=True, label="Binomial", color="b",
             alpha=1, histtype="step", linewidth=2)
    ax2.hist(po_samples, bins=bins, density=True, label="Poisson", color="r",
             alpha=0.5, histtype="step", linewidth=2)
    ax2.set_title("Overlay Comparison")
    ax2.legend()

    for ax in (ax0, ax1, ax2):
        ax.grid(True, alpha=0.3)

    plt.suptitle("Poisson Approximation of Binomial", fontsize=14, fontweight="bold")
    plt.tight_layout()
    plt.savefig("poisson_approx_binomial.png", dpi=150, bbox_inches="tight")
    plt.show()


# ========================================================================


if __name__ == "__main__":
    main()
