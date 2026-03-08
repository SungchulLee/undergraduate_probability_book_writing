# Simulation of Gambler's Ruin

## Sample Path Simulation

A single sample path of the gambler's ruin shows the random walk of the gambler's capital over time. The walk terminates when it hits 0 (ruin) or $N$ (goal).

### Python Implementation — Single Path

```python
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

# Parameters
p = 0.49          # Probability of winning each bet
IC = 100          # Initial capital
Goal = 200        # Goal
n = 10000         # Maximum number of steps

# Generate path: +1 with prob p, -1 with prob q
steps = 2 * np.random.binomial(1, p, size=n) - 1
path = IC + np.cumsum(steps)
path = np.insert(path, 0, IC)

# Plot
plt.figure(figsize=(10, 5))
plt.plot(range(n + 1), path[:n + 1], linewidth=0.5)
plt.axhline(y=0, color='r', linewidth=1)
plt.axhline(y=Goal, color='r', linewidth=1)
plt.xlabel('Step')
plt.ylabel('Capital')
plt.title(f'Gambler\'s Ruin Sample Path (IC={IC}, Goal={Goal}, p={p})')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('gamblers_ruin_path.png', dpi=150, bbox_inches='tight')
plt.show()
```

## Monte Carlo Estimation of Ruin Probability

By simulating many independent gambler's ruin paths and counting the fraction that end in ruin, we obtain a Monte Carlo estimate of $Q(i)$.

### Python Implementation — Monte Carlo

```python
import numpy as np

np.random.seed(42)

# Parameters
p = 0.49
IC = 100
Goal = 200
n = 10000           # Max steps per simulation
num_simu = 1000     # Number of simulations

# Simulate all paths at once
steps = 2 * np.random.binomial(1, p, size=(num_simu, n)) - 1
paths = IC + np.cumsum(steps, axis=1)
paths = np.hstack([IC * np.ones((num_simu, 1)), paths])

# Append sentinel values to ensure hitting times are finite
paths = np.hstack([paths, np.zeros((num_simu, 1)), Goal * np.ones((num_simu, 1))])

ruin_counter = 0
success_counter = 0
undecided_counter = 0

for i in range(num_simu):
    path = paths[i, :]
    # Find first time hitting 0 and Goal
    hits_zero = np.where(path <= 0)[0]
    hits_goal = np.where(path >= Goal)[0]
    
    T_0 = hits_zero[0] if len(hits_zero) > 0 else n + 10
    T_Goal = hits_goal[0] if len(hits_goal) > 0 else n + 10
    
    if T_0 <= n and T_0 < T_Goal:
        ruin_counter += 1
    elif T_Goal <= n and T_Goal < T_0:
        success_counter += 1
    else:
        undecided_counter += 1

print(f"Ruin:      {ruin_counter}")
print(f"Success:   {success_counter}")
print(f"Undecided: {undecided_counter}")

decided = ruin_counter + success_counter
if decided > 0:
    ruin_prob_est = ruin_counter / decided
    print(f"\nEstimated ruin probability: {ruin_prob_est:.4f}")
```

### Typical Output

With $p = 0.49$, $IC = 100$, $Goal = 200$, and 100 simulations:

| Outcome | Count |
|---------|-------|
| Ruin | 89 |
| Success | 4 |
| Undecided | 7 |

$$
\hat{Q}(100) = \frac{89}{89 + 4} = 0.957
$$

This matches the theoretical value closely. The high ruin probability despite $p$ being close to $0.5$ illustrates why the problem is called "gambler's ruin."

## Numerical Solution via Linear System

The ruin probabilities for all initial capitals $i = 0, 1, \ldots, N$ can be computed exactly by solving the tridiagonal linear system arising from the recurrence relation (see [First Step Analysis](first_step_analysis.md)).

### Python Implementation — Exact Solution

```python
import numpy as np
from scipy.sparse import spdiags
from scipy.sparse.linalg import spsolve
import matplotlib.pyplot as plt

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

for idx, p in enumerate([0.49, 0.50]):
    q = 1 - p
    Goal = 200

    # Build tridiagonal system: -q*Q(i-1) + Q(i) - p*Q(i+1) = 0
    n = Goal - 1
    d = np.ones(n)
    diagonals = np.array([-q * d, d, -p * d])
    offsets = [-1, 0, 1]
    A = spdiags(diagonals, offsets, n, n, format='csc')

    # Right-hand side: b(1) = q (from boundary Q(0) = 1)
    b = np.zeros(n)
    b[0] = q

    # Solve
    Q_interior = spsolve(A, b)
    Q = np.concatenate([[1.0], Q_interior, [0.0]])

    # Plot
    axes[idx].plot(range(Goal + 1), Q)
    axes[idx].set_xlabel('Initial Capital')
    axes[idx].set_ylabel('Ruin Probability')
    axes[idx].set_title(f'p = {p}')
    axes[idx].grid(True, alpha=0.3)

plt.suptitle("Gambler's Ruin Probability")
plt.tight_layout()
plt.savefig('gamblers_ruin_exact.png', dpi=150, bbox_inches='tight')
plt.show()
```

The left plot ($q > 1/2$) shows the ruin probability approaching 1 exponentially fast as capital decreases. The right plot ($q = 1/2$) shows a linear relationship.
