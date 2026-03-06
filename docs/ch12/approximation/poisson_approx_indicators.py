"""Poisson approximation for a sum of non-identical Bernoulli indicators."""
import numpy as np
import matplotlib.pyplot as plt


# ========================================================================


def main():
    np.random.seed(42)

    N_SAMPLES = 10_000
    n = 1000

    # Each indicator has a different (small, random) success probability
    P_vec = np.random.uniform(0.0, 1.0, (n, 1)) / 100
    uniform_samples = np.random.uniform(0.0, 1.0, (n, N_SAMPLES))
    X_i = (uniform_samples < P_vec).astype(int)
    S_n = X_i.sum(axis=0)

    LA = P_vec.sum()
    po_samples = np.random.poisson(lam=LA, size=N_SAMPLES)

    fig, (ax0, ax1, ax2) = plt.subplots(1, 3, figsize=(14, 4))
    bins = np.arange(int(3 * LA))

    ax0.hist(S_n, bins=bins, density=True, color="steelblue", edgecolor="black")
    ax0.set_title("Sum of non-identical indicators")

    ax1.hist(po_samples, bins=bins, density=True, color="steelblue", edgecolor="black")
    ax1.set_title(f"Poisson(λ ≈ {LA:.1f})")

    ax2.hist(S_n, bins=bins, density=True, label="Indicators sum", color="b",
             alpha=1, histtype="step", linewidth=2)
    ax2.hist(po_samples, bins=bins, density=True, label="Poisson", color="r",
             alpha=0.5, histtype="step", linewidth=2)
    ax2.set_title("Overlay Comparison")
    ax2.legend()

    for ax in (ax0, ax1, ax2):
        ax.grid(True, alpha=0.3)

    plt.suptitle("Poisson Approximation of Non-Identical Bernoulli Sum",
                 fontsize=13, fontweight="bold")
    plt.tight_layout()
    plt.savefig("poisson_approx_indicators.png", dpi=150, bbox_inches="tight")
    plt.show()


# ========================================================================


if __name__ == "__main__":
    main()
