"""2D Simple Random Walk: simulate and visualize a walk on the integer lattice."""
import numpy as np
import matplotlib.pyplot as plt


def main():
    np.random.seed(337)

    n_steps = 500
    n_paths = 3

    # directions: N, E, S, W
    directions = np.array([[0, 1], [1, 0], [0, -1], [-1, 0]])

    fig, axes = plt.subplots(1, 2, figsize=(13, 6))

    # Left panel: multiple 2D random walk paths
    for path_idx in range(n_paths):
        steps = directions[np.random.randint(0, 4, size=n_steps)]
        positions = np.vstack([[0, 0], np.cumsum(steps, axis=0)])

        axes[0].plot(positions[:, 0], positions[:, 1], linewidth=0.7,
                     alpha=0.8, label=f"Path {path_idx + 1}")
        axes[0].plot(0, 0, "go", markersize=8, zorder=5)
        axes[0].plot(positions[-1, 0], positions[-1, 1], "rx", markersize=8, zorder=5)

    bound = 1.5 * np.sqrt(n_steps)
    axes[0].set_xlim(-bound, bound)
    axes[0].set_ylim(-bound, bound)
    axes[0].set_aspect("equal")
    axes[0].set_xlabel("x")
    axes[0].set_ylabel("y")
    axes[0].set_title(f"2D Simple Random Walk ({n_steps} steps)")
    axes[0].legend(fontsize=9)
    axes[0].grid(True, alpha=0.3)

    # Right panel: distribution of final distances from origin
    n_simulations = 5000
    final_distances = np.zeros(n_simulations)
    for i in range(n_simulations):
        steps = directions[np.random.randint(0, 4, size=n_steps)]
        final_pos = np.sum(steps, axis=0)
        final_distances[i] = np.sqrt(final_pos[0] ** 2 + final_pos[1] ** 2)

    axes[1].hist(final_distances, bins=40, density=True, color="steelblue",
                 edgecolor="white", alpha=0.8)
    axes[1].axvline(np.mean(final_distances), color="red", linestyle="--",
                    linewidth=1.5, label=f"Mean = {np.mean(final_distances):.1f}")
    axes[1].axvline(np.sqrt(n_steps), color="orange", linestyle="--",
                    linewidth=1.5, label=f"$\\sqrt{{n}}$ = {np.sqrt(n_steps):.1f}")
    axes[1].set_xlabel("Distance from Origin")
    axes[1].set_ylabel("Density")
    axes[1].set_title(f"Final Distance Distribution ({n_simulations} walks)")
    axes[1].legend()
    axes[1].grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig("random_walk_2d.png", dpi=150, bbox_inches="tight")
    plt.show()

    print(f"Mean final distance:   {np.mean(final_distances):.2f}")
    print(f"Expected (sqrt(n)):    {np.sqrt(n_steps):.2f}")


if __name__ == "__main__":
    main()
