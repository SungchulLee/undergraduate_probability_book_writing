"""Monty Hall Problem: simulate stick vs. switch strategies and show convergence."""
import numpy as np
import matplotlib.pyplot as plt
import random


class MontyStick:
    """Player always sticks with the first choice."""
    def run(self):
        car = random.choice([0, 1, 2])
        choice = random.choice([0, 1, 2])
        return 1 if choice == car else 0


class MontySwitch:
    """Player always switches after the host reveals a goat."""
    def run(self):
        car = random.choice([0, 1, 2])
        first = random.choice([0, 1, 2])
        # Host opens a door with a goat that is not the player's choice
        host_options = [d for d in [0, 1, 2] if d != car and d != first]
        host = random.choice(host_options)
        # Player switches to the remaining door
        final = [d for d in [0, 1, 2] if d != first and d != host][0]
        return 1 if final == car else 0


def main():
    n_tries = 2000
    np.random.seed(42)
    random.seed(42)

    stick_results = np.array([MontyStick().run() for _ in range(n_tries)])
    switch_results = np.array([MontySwitch().run() for _ in range(n_tries)])

    stick_cum = stick_results.cumsum() / np.arange(1, n_tries + 1)
    switch_cum = switch_results.cumsum() / np.arange(1, n_tries + 1)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

    ax1.plot(stick_cum, linewidth=2, label="Stick win rate")
    ax1.axhline(1 / 3, color="r", linestyle="--", alpha=0.6, label="1/3")
    ax1.set_title("Monty Hall — Stick Strategy")
    ax1.set_xlabel("Number of games")
    ax1.set_ylabel("Cumulative win rate")
    ax1.legend()
    ax1.grid(True, alpha=0.3)

    ax2.plot(switch_cum, linewidth=2, color="green", label="Switch win rate")
    ax2.axhline(2 / 3, color="r", linestyle="--", alpha=0.6, label="2/3")
    ax2.set_title("Monty Hall — Switch Strategy")
    ax2.set_xlabel("Number of games")
    ax2.set_ylabel("Cumulative win rate")
    ax2.legend()
    ax2.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig("monty_hall.png", dpi=150, bbox_inches="tight")
    plt.show()


if __name__ == "__main__":
    main()
