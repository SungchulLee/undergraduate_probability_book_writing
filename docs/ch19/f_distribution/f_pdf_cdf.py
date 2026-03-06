"""PDF and CDF of the F distribution."""
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats


# ========================================================================


def main():
    df1, df2 = 5, 10
    x = np.linspace(0, 5, 300)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(x, stats.f(df1, df2).pdf(x), label="PDF", linewidth=2)
    ax.plot(x, stats.f(df1, df2).cdf(x), label="CDF", linewidth=2)
    ax.set_title(f"F({df1}, {df2}) Distribution", fontsize=14)
    ax.set_xlabel("x")
    ax.set_ylabel("Value")
    ax.legend()
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig("f_pdf_cdf.png", dpi=150, bbox_inches="tight")
    plt.show()


# ========================================================================


if __name__ == "__main__":
    main()
