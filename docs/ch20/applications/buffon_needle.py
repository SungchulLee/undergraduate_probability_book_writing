"""Buffon's Needle: estimate π by dropping needles on parallel lines."""
import numpy as np
import matplotlib.pyplot as plt


# ========================================================================


def main():
    np.random.seed(42)

    n = 10_000
    x = np.random.uniform(0, 1, (n, 2))  # col 0 = centre height, col 1 = angle/π
    h = x[:, 0] + np.sin(np.pi * x[:, 1])  # height of upper tip
    crosses = (h >= 1).astype(int)

    N_cum = crosses.cumsum()
    idx = np.arange(1, n + 1)
    pi_est = 2 * idx / np.maximum(N_cum, 1)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(pi_est[10:], linewidth=1.5, label="Estimate of π")
    ax.axhline(np.pi, color="r", linestyle="--", lw=2, label=f"π ≈ {np.pi:.5f}")
    ax.set_title("Buffon's Needle: Estimating π", fontsize=14)
    ax.set_xlabel("Number of needles")
    ax.set_ylabel("Estimated π")
    ax.legend()
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig("buffon_needle.png", dpi=150, bbox_inches="tight")
    plt.show()

    print(f"Final estimate of π (n = {n:,}): {pi_est[-1]:.5f}")


# ========================================================================


if __name__ == "__main__":
    main()
