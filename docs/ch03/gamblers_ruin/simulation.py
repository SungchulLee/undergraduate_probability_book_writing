"""Gambler's Ruin: Monte Carlo simulation of a biased random walk."""
import numpy as np
import matplotlib.pyplot as plt


# ========================================================================


class GamblerRuin:
    def __init__(self, p=0.49, initial=10, goal=20):
        self.p = p
        self.q = 1 - p
        self.initial = initial
        self.goal = goal

    def simulate(self, num_paths=1, num_steps=200, seed=None):
        if seed is not None:
            np.random.seed(seed)
        steps = 2 * np.random.binomial(1, self.p, (num_paths, num_steps)) - 1
        path = self.initial + np.concatenate(
            [np.zeros((num_paths, 1)), steps.cumsum(axis=1)], axis=1
        )
        results = np.zeros(num_paths)
        for i in range(num_paths):
            for pos in path[i]:
                if pos >= self.goal:
                    results[i] = 1
                    break
                if pos <= 0:
                    results[i] = -1
                    break
        return path, results


# ========================================================================


def main():
    p = 0.49
    gambler = GamblerRuin(p=p, initial=10, goal=20)

    # --- Single path visualisation ---
    path, result = gambler.simulate(num_paths=1, num_steps=400, seed=0)
    fig, ax = plt.subplots(figsize=(12, 3))
    ax.plot(path[0], "-b")
    ax.axhline(0, color="r", linestyle="--", alpha=0.5)
    ax.axhline(20, color="r", linestyle="--", alpha=0.5)
    ax.set_title(f"Gambler's Ruin (p={p})")
    ax.set_xlabel("Step")
    ax.set_ylabel("Capital")
    plt.tight_layout()
    plt.savefig("gamblers_ruin_simulation.png", dpi=150, bbox_inches="tight")
    plt.show()

    # --- Many paths: estimate ruin probability ---
    _, results = gambler.simulate(num_paths=10_000, num_steps=2000, seed=42)
    num_ruin = np.sum(results == -1)
    num_win = np.sum(results == 1)
    print(f"Ruin probability (simulation): {num_ruin / (num_ruin + num_win):.4f}")


# ========================================================================


if __name__ == "__main__":
    main()
