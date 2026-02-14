"""Birthday Problem: find the minimum number of people for a 50% match probability."""
import numpy as np
import matplotlib.pyplot as plt


def main():
    # probability_B[k]: probability that first k people all have different birthdays
    probability_B = np.zeros(100)
    for k in range(100):
        if k == 0 or k == 1:
            probability_B[k] = 1
        else:
            probability_B[k] = probability_B[k - 1] * (1 - (k - 1) / 365)

    # probability_A[k]: probability of at least one birthday match among first k people
    probability_A = 1 - probability_B
    idx = np.where(probability_A >= 0.5)[0][0]

    plt.figure(figsize=(8, 5))
    plt.plot(probability_A, linewidth=2, label="P(match)")
    plt.plot(np.ones_like(probability_A) * 0.5, "--b", alpha=0.4, label="0.5")
    plt.plot([idx, idx], [0, probability_A[idx]], "--or")
    plt.title("Birthday Matching Probability")
    plt.xlabel("Number of People")
    plt.ylabel("Probability")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig("birthday_problem.png", dpi=150, bbox_inches="tight")
    plt.show()

    print(f"Smallest number of people with matching probability >= 0.5: {idx}")


if __name__ == "__main__":
    main()
