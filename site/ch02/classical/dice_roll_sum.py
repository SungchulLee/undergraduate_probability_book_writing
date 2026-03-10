"""Dice Roll Sum: compute exact and simulated probabilities for the sum of n dice."""
import itertools
import numpy as np
import matplotlib.pyplot as plt


# ========================================================================

def exact_probability(n, k):
    """Exact P(sum = k) when rolling n fair dice, via enumeration."""
    total = 6 ** n
    count = sum(1 for combo in itertools.product(range(1, 7), repeat=n)
                if sum(combo) == k)
    return count / total


# ========================================================================

def simulated_probability(n, k, n_simulations=100000):
    """Estimate P(sum = k) via Monte Carlo simulation."""
    rolls = np.random.randint(1, 7, size=(n_simulations, n))
    sums = rolls.sum(axis=1)
    return np.mean(sums == k)


# ========================================================================

def main():
    n_dice = 3  # number of dice
    possible_sums = np.arange(n_dice, 6 * n_dice + 1)

    exact_probs = [exact_probability(n_dice, k) for k in possible_sums]
    simulated_probs = [simulated_probability(n_dice, k) for k in possible_sums]

    fig, axes = plt.subplots(1, 2, figsize=(13, 5))

    # Left panel: exact vs simulated probabilities
    width = 0.35
    axes[0].bar(possible_sums - width / 2, exact_probs, width,
                label="Exact", color="steelblue", edgecolor="white")
    axes[0].bar(possible_sums + width / 2, simulated_probs, width,
                label="Simulated", color="coral", edgecolor="white", alpha=0.8)
    axes[0].set_xlabel("Sum")
    axes[0].set_ylabel("Probability")
    axes[0].set_title(f"P(Sum = k) for {n_dice} Dice")
    axes[0].legend()
    axes[0].grid(True, alpha=0.3, axis="y")

    # Right panel: sample space size growth
    dice_counts = np.arange(1, 7)
    space_sizes = [6 ** d for d in dice_counts]
    axes[1].bar(dice_counts, space_sizes, color="mediumpurple", edgecolor="white")
    axes[1].set_xlabel("Number of Dice")
    axes[1].set_ylabel("Sample Space Size")
    axes[1].set_title("Sample Space Growth ($6^n$)")
    axes[1].set_yscale("log")
    for i, s in enumerate(space_sizes):
        axes[1].text(dice_counts[i], s * 1.3, f"{s:,}", ha="center", fontsize=9)
    axes[1].grid(True, alpha=0.3, axis="y")

    plt.tight_layout()
    plt.savefig("dice_roll_sum.png", dpi=150, bbox_inches="tight")
    plt.show()

    print(f"Example: P(sum={3*3+1} with {n_dice} dice)")
    k_example = 10
    print(f"  Exact:     {exact_probability(n_dice, k_example):.4f}")
    print(f"  Simulated: {simulated_probability(n_dice, k_example):.4f}")


# ========================================================================

if __name__ == "__main__":
    main()
