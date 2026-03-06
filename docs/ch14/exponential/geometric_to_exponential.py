"""Show that Geometric(p)/n converges to Exponential(λ) as n → ∞ with p = λ/n."""
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats


# ========================================================================


def main():
    np.random.seed(42)

    LA = 20
    BT = 1 / LA
    N = 1000
    P = LA / N
    N_SIM = 10_000

    x_geo = stats.geom(P).rvs(N_SIM) / N
    x_exp = stats.expon(scale=BT).rvs(N_SIM)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 4))

    # --- Histogram overlay ---
    ax1.hist(x_geo, bins=100, density=True, alpha=0.3, color="blue", label="Geometric/n")
    ax1.hist(x_exp, bins=100, density=True, color="red", histtype="step",
             linewidth=2, label="Exponential")
    ax1.set_title("Geometric/n  vs  Exponential")
    ax1.legend()
    ax1.grid(True, alpha=0.3)

    # --- Geometric/n with theoretical PDF overlay ---
    _, bins, _ = ax2.hist(x_geo, bins=100, density=True, alpha=0.3, label="Geometric/n")
    ax2.plot(bins, stats.expon(scale=BT).pdf(bins), "--r", lw=2, label="Exp PDF")
    ax2.set_title(f"Geometric(p={P})/n  →  Exp(λ={LA})")
    ax2.legend()
    ax2.grid(True, alpha=0.3)

    plt.suptitle("Geometric-to-Exponential Convergence", fontsize=14, fontweight="bold")
    plt.tight_layout()
    plt.savefig("geometric_to_exponential.png", dpi=150, bbox_inches="tight")
    plt.show()


# ========================================================================


if __name__ == "__main__":
    main()
