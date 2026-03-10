# 2D Simple Random Walk

At each step the walker moves to one of four neighboring lattice points with equal probability — a recurrent process that returns to the origin with probability 1.

## Definition

Starting at $(0, 0)$, the position after $m$ steps is:

$$
(S_m^x, S_m^y) = \sum_{k=1}^m (X_k, Y_k)
$$

where $(X_k, Y_k)$ is chosen uniformly from $\{(\pm 1, 0), (0, \pm 1)\}$.

## Explanation

### Recurrence (Polya's Theorem)

The 2D simple random walk is **recurrent**: it returns to the origin with probability 1. However, the expected return time is infinite.

In contrast, the 3D walk is **transient** — the return probability is approximately 0.3405. The critical dimension is $d = 2$: walks in $d \le 2$ are recurrent, $d \ge 3$ are transient.

### Displacement

Each coordinate is an independent 1D random walk with step probabilities $P(\pm 1) = 1/4$, $P(0) = 1/2$. After $m$ steps:

$$
E[S_m^x] = 0, \quad \operatorname{Var}(S_m^x) = m/2
$$

The expected squared distance from the origin grows linearly: $E[\lVert S_m \rVert^2] = m$.

## Examples

**Example.** Simulate a 2D walk of 10,000 steps and check displacement.

```python
import numpy as np

np.random.seed(42)
m = 10_000

directions = np.array([[1,0], [-1,0], [0,1], [0,-1]])
choices = np.random.randint(0, 4, m)
increments = directions[choices]
walk = np.cumsum(increments, axis=0)

final = walk[-1]
dist = np.sqrt(final[0]**2 + final[1]**2)

print(f"Final position: ({final[0]}, {final[1]})")
print(f"Distance from origin: {dist:.2f}")
print(f"Expected |S|² = m = {m}, actual |S|² = {final[0]**2 + final[1]**2}")

# Check if walk returned to origin
at_origin = np.all(walk == 0, axis=1)
n_returns = at_origin.sum()
print(f"Returns to origin: {n_returns}")
```
