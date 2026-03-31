"""Simulate a Poisson Process two ways: Bernoulli coin flips vs exponential interarrivals."""
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

LA = 1       # rate (lambda)
BT = 1 / LA  # mean interarrival time
N = 1000     # time-discretisation granularity
P = LA / N   # success probability per micro-interval
T = 8        # observation window [0, T]


def ppp_coin(ax):
    """Approximate PPP by flipping a biased coin in each micro-interval."""
    x = np.random.binomial(1, P, size=int(N * T))
    arrivals = [i / N for i, v in enumerate(x) if v]
    ax.plot(arrivals, np.zeros(len(arrivals)), "o", color="red", label="PPP via coin")


def ppp_expon(ax):
    """Exact PPP using exponential interarrival times."""
    interarrivals = np.random.exponential(scale=BT, size=int(LA * T * 10))
    arrivals = interarrivals.cumsum()
    arrivals = arrivals[arrivals < T]
    ax.plot(arrivals, np.ones(len(arrivals)), "o", color="blue", label="PPP via exponential")


def main():
    fig, ax = plt.subplots(figsize=(14, 2))
    ppp_coin(ax)
    ppp_expon(ax)
    ax.legend(loc="center right")
    ax.set_title(f"Poisson Process (λ = {LA}, T = {T})", fontsize=13)
    ax.set_xlabel("Time")
    ax.set_yticks([])
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_visible(False)
    plt.tight_layout()
    plt.savefig("poisson_process_simulation.png", dpi=150, bbox_inches="tight")
    plt.show()


if __name__ == "__main__":
    main()
