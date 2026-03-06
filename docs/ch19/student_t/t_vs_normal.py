"""Compare t-distribution PDFs for various degrees of freedom with Standard Normal."""
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats


# ========================================================================


def main():
    x = np.linspace(-4, 4, 300)

    fig, ax = plt.subplots(figsize=(10, 5))
    for df in [1, 3, 5, 10, 30, 100]:
        ax.plot(x, stats.t(df).pdf(x), label=f"t({df})")

    ax.plot(x, stats.norm.pdf(x), "k--", lw=2, label="N(0,1)")
    ax.set_title("Student's t PDFs vs Standard Normal", fontsize=14)
    ax.set_xlabel("x")
    ax.set_ylabel("Density")
    ax.legend()
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig("t_vs_normal.png", dpi=150, bbox_inches="tight")
    plt.show()


# ========================================================================


if __name__ == "__main__":
    main()
