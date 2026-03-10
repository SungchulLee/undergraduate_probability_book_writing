# Arcsine Law — Time Spent Positive

The fraction of time a symmetric random walk spends above zero also follows the arcsine distribution — spending 50% of time positive is the least likely outcome.

## Definition

For a simple random walk $S_0 = 0, S_1, \ldots, S_{2n}$, a **stick** $(k-1, S_{k-1}) \to (k, S_k)$ is positive if $(S_{k-1} + S_k)/2 > 0$. Let $N_{2n}$ count positive sticks. Then:

$$
\frac{N_{2n}}{2n} \xrightarrow{d} \operatorname{Arcsine}
$$

with density $f(x) = \frac{1}{\pi\sqrt{x(1-x)}}$ on $(0, 1)$.

## Explanation

### Interpretation

The walk does **not** spend roughly half its time above and half below zero. Instead, it most likely spends nearly all its time on one side. The $U$-shaped arcsine density assigns the highest probability near $x = 0$ and $x = 1$.

### Connection to Other Arcsine Laws

This is the second of three classical arcsine laws, alongside the last visit time and time of the maximum. All share the same limiting distribution — a deep structural property of symmetric random walks.

## Examples

**Example.** Fraction of time positive for 1000 walks of length 10,000.

```python
import numpy as np

np.random.seed(42)
n = 10_000
n_sim = 1_000

fractions = np.zeros(n_sim)
for s in range(n_sim):
    steps = 2 * np.random.randint(0, 2, n) - 1
    walk = np.concatenate([[0], np.cumsum(steps)])
    centers = (walk[:-1] + walk[1:]) / 2
    fractions[s] = np.mean(centers > 0)

# U-shaped: more mass near 0 and 1 than near 0.5
print(f"Fraction in [0, 0.1]: {np.mean(fractions < 0.1):.3f}")
print(f"Fraction in [0.4, 0.6]: {np.mean((fractions > 0.4) & (fractions < 0.6)):.3f}")
print(f"Fraction in [0.9, 1]: {np.mean(fractions > 0.9):.3f}")
```
