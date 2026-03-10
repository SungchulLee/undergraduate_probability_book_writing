"""PMF Sampling: sample from a discrete random variable and compare with its PMF."""
import numpy as np
import matplotlib.pyplot as plt


# ========================================================================

def main():
    # define a discrete random variable X
    outcomes = np.array([-3, -1, 1, 2, 5])
    pmf = np.array([0.10, 0.10, 0.10, 0.50, 0.20])

    # generate samples
    n_samples = 10000
    samples = np.random.choice(outcomes, p=pmf, size=n_samples)

    # compute empirical frequencies
    empirical_probs = np.array([np.mean(samples == x) for x in outcomes])

    fig, axes = plt.subplots(1, 2, figsize=(13, 5))

    # Left panel: histogram of samples vs theoretical PMF
    width = 0.35
    axes[0].bar(outcomes - width / 2, empirical_probs, width,
                label="Empirical", color="steelblue", edgecolor="white")
    axes[0].bar(outcomes + width / 2, pmf, width,
                label="Theoretical PMF", color="coral", edgecolor="white")
    axes[0].set_xlabel("Outcome")
    axes[0].set_ylabel("Probability")
    axes[0].set_title(f"Empirical vs Theoretical PMF (n = {n_samples})")
    axes[0].set_xticks(outcomes)
    axes[0].legend()
    axes[0].grid(True, alpha=0.3, axis="y")

    # Right panel: convergence of empirical mean to E[X]
    expected_value = np.sum(outcomes * pmf)
    cumulative_means = np.cumsum(samples) / np.arange(1, n_samples + 1)
    axes[1].plot(cumulative_means, linewidth=0.8, color="steelblue",
                 label="Running sample mean")
    axes[1].axhline(expected_value, color="red", linestyle="--", linewidth=1.5,
                    label=f"E[X] = {expected_value:.2f}")
    axes[1].set_xlabel("Number of Samples")
    axes[1].set_ylabel("Sample Mean")
    axes[1].set_title("Convergence of Sample Mean to E[X]")
    axes[1].legend()
    axes[1].grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig("pmf_sampling.png", dpi=150, bbox_inches="tight")
    plt.show()

    print(f"Theoretical E[X] = {expected_value:.4f}")
    print(f"Sample mean       = {np.mean(samples):.4f}")


# ========================================================================

if __name__ == "__main__":
    main()
