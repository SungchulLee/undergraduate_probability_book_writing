"""Derangement Simulation: estimate the probability of no fixed points in a random permutation."""
import numpy as np
import matplotlib.pyplot as plt


def main():
    n = 100                    # permutation size
    n_simulations = 50000      # number of Monte Carlo trials
    x = np.arange(n)

    # running count of derangements (permutations with no fixed points)
    derangement_count = 0
    estimates = np.zeros(n_simulations)

    for i in range(n_simulations):
        y = np.random.permutation(n)
        if np.sum(x == y) == 0:
            derangement_count += 1
        estimates[i] = derangement_count / (i + 1)

    theoretical = np.exp(-1)

    # --- Plot convergence of simulated probability to e^{-1} ---
    fig, axes = plt.subplots(1, 2, figsize=(13, 5))

    # Left panel: convergence
    axes[0].plot(estimates, linewidth=0.8, label="Simulated P(derangement)")
    axes[0].axhline(theoretical, color="red", linestyle="--", linewidth=1.5,
                    label=f"$e^{{-1}} \\approx {theoretical:.4f}$")
    axes[0].set_xlabel("Number of Simulations")
    axes[0].set_ylabel("Estimated Probability")
    axes[0].set_title("Convergence of Derangement Probability")
    axes[0].legend()
    axes[0].grid(True, alpha=0.3)

    # Right panel: histogram of number of fixed points
    fixed_point_counts = []
    for _ in range(n_simulations):
        y = np.random.permutation(n)
        fixed_point_counts.append(np.sum(x == y))

    axes[1].hist(fixed_point_counts, bins=np.arange(-0.5, max(fixed_point_counts) + 1.5),
                 density=True, color="steelblue", edgecolor="white", alpha=0.8,
                 label="Simulated")
    # Poisson(1) PMF overlay
    k_vals = np.arange(0, max(fixed_point_counts) + 1)
    poisson_pmf = np.exp(-1) * np.ones_like(k_vals, dtype=float)
    for k in k_vals:
        poisson_pmf[k] = np.exp(-1) / np.math.factorial(k)
    axes[1].plot(k_vals, poisson_pmf, "ro-", markersize=6, linewidth=1.5,
                 label="Poisson(1) PMF")
    axes[1].set_xlabel("Number of Fixed Points")
    axes[1].set_ylabel("Probability")
    axes[1].set_title("Distribution of Fixed Points (Approx Poisson)")
    axes[1].legend()
    axes[1].grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig("derangements.png", dpi=150, bbox_inches="tight")
    plt.show()

    print(f"Simulated P(derangement) = {estimates[-1]:.4f}")
    print(f"Theoretical e^{{-1}}      = {theoretical:.4f}")


if __name__ == "__main__":
    main()
