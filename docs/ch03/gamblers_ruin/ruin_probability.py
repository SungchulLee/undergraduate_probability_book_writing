"""Gambler's Ruin: compute ruin probability analytically via linear system (I-A)Q = b."""
import numpy as np
import matplotlib.pyplot as plt


def compute_ruin_probability(N, p):
    """Solve for ruin probability Q[i] for each initial capital i = 0, 1, ..., N."""
    q = 1 - p
    I = np.eye(N + 1)
    A = p * np.eye(N + 1, k=1) + q * np.eye(N + 1, k=-1)
    A[0, 1] = 0
    A[-1, -2] = 0
    b = np.zeros((N + 1, 1))
    b[0, 0] = 1
    Q = np.linalg.solve(I - A, b).reshape(N + 1)
    return Q


def main():
    N = 100  # goal
    p = 0.49

    Q = compute_ruin_probability(N, p)

    plt.figure(figsize=(8, 5))
    plt.plot(Q, linewidth=2)
    plt.title(f"Probability of Ruin (p = {p}, goal = {N})")
    plt.xlabel("Initial Capital")
    plt.ylabel("Ruin Probability")
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig("ruin_probability.png", dpi=150, bbox_inches="tight")
    plt.show()

    idx = np.where(Q <= 0.5)[0][0]
    print(f"Minimum initial capital with ruin probability <= 0.5: {idx}")


if __name__ == "__main__":
    main()
