"""Monte Carlo estimation of π: random points in the unit square."""
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

N_POINTS = 5_000

x = np.random.uniform(0, 1, (2, N_POINTS))
inside = (x[0] ** 2 + x[1] ** 2) < 1

# --- Scatter plot ---
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

ax1.scatter(x[0, inside], x[1, inside], s=1, color="red", label="Inside")
ax1.scatter(x[0, ~inside], x[1, ~inside], s=1, color="blue", label="Outside")
theta = np.linspace(0, np.pi / 2, 200)
ax1.plot(np.cos(theta), np.sin(theta), "k-", lw=2)
ax1.set_aspect("equal")
ax1.set_title(f"Random Points (n = {N_POINTS:,})")
ax1.legend(markerscale=5)

# --- Convergence plot ---
pi_est = 4 * inside.cumsum() / np.arange(1, N_POINTS + 1)
ax2.plot(pi_est[10:], linewidth=1.5)
ax2.axhline(np.pi, color="r", linestyle="--", lw=2, label=f"π ≈ {np.pi:.5f}")
ax2.set_title("Monte Carlo Estimate of π")
ax2.set_xlabel("Number of points")
ax2.set_ylabel("Estimated π")
ax2.legend()
ax2.grid(True, alpha=0.3)

plt.suptitle("Monte Carlo Estimation of π", fontsize=14, fontweight="bold")
plt.tight_layout()
plt.savefig("monte_carlo_pi.png", dpi=150, bbox_inches="tight")
plt.show()

print(f"Final estimate of π: {pi_est[-1]:.5f}")
