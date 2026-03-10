# Simulation of Gambler's Ruin

Monte Carlo simulation verifies the closed-form ruin probabilities and visualizes sample paths of the random walk.

## Definition

A **sample path** traces the gambler's capital over time: a random walk starting at $i$, stepping $+1$ or $-1$ with probabilities $p$ and $q$, absorbed at 0 and $N$.

The **Monte Carlo estimate** of $Q(i)$ is the fraction of simulated paths that hit 0 before $N$.

## Explanation

Each simulation runs one random walk until it hits a boundary. Repeating many times and counting ruin events estimates $Q(i)$. By the law of large numbers, the estimate converges to the true value as the number of simulations grows.

The exact solution can also be computed by solving the tridiagonal linear system from the first-step-analysis recurrence.

## Examples

**Example.** $p = 0.49$, $i = 100$, $N = 200$.

```python
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

def simulate_ruin(p, IC, Goal, n_steps=10000, n_sim=1000):
    """Monte Carlo estimate of ruin probability."""
    ruin, success = 0, 0
    for _ in range(n_sim):
        capital = IC
        for _ in range(n_steps):
            capital += 1 if np.random.random() < p else -1
            if capital <= 0:
                ruin += 1
                break
            if capital >= Goal:
                success += 1
                break
    decided = ruin + success
    return ruin / decided if decided > 0 else float('nan')

# Monte Carlo
p, IC, Goal = 0.49, 100, 200
mc_prob = simulate_ruin(p, IC, Goal)
theory = lambda i, N, p: (((1-p)/p)**N - ((1-p)/p)**i) / (((1-p)/p)**N - 1)

print(f"Monte Carlo Q(100): {mc_prob:.4f}")

# Exact solution via tridiagonal system
from scipy.sparse import diags
from scipy.sparse.linalg import spsolve

fig, axes = plt.subplots(1, 2, figsize=(12, 5))
for idx, p_val in enumerate([0.49, 0.50]):
    q_val = 1 - p_val
    n = Goal - 1
    main = np.ones(n)
    lower = -q_val * np.ones(n - 1)
    upper = -p_val * np.ones(n - 1)
    A = diags([lower, main, upper], [-1, 0, 1], format='csc')
    b = np.zeros(n)
    b[0] = q_val

    Q_int = spsolve(A, b)
    Q = np.concatenate([[1.0], Q_int, [0.0]])

    axes[idx].plot(range(Goal + 1), Q)
    axes[idx].set_xlabel('Initial Capital')
    axes[idx].set_ylabel('Ruin Probability')
    axes[idx].set_title(f'p = {p_val}')
    axes[idx].grid(True, alpha=0.3)

plt.suptitle("Gambler's Ruin Probability")
plt.tight_layout()
plt.savefig('gamblers_ruin_exact.png', dpi=150, bbox_inches='tight')
plt.show()
```
