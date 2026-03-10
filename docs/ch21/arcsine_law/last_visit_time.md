# Arcsine Law — Last Visit Time

The last time a symmetric random walk visits the origin follows the arcsine distribution — concentrating near the endpoints rather than the middle.

## Definition

For a simple random walk $S_0 = 0, S_1, \ldots, S_{2n}$ on $\mathbb{Z}$, let $L_{2n}$ be the last visit time to zero. Then as $n \to \infty$:

$$
\frac{L_{2n}}{2n} \xrightarrow{d} \operatorname{Arcsine}
$$

The **arcsine density** is:

$$
f(x) = \frac{1}{\pi\sqrt{x(1-x)}}, \quad 0 < x < 1
$$

with CDF $F(x) = \frac{2}{\pi}\arcsin(\sqrt{x})$.

## Explanation

### Counterintuitive Shape

The density is $U$-shaped: the last visit to zero is most likely near the beginning or end of the walk, not in the middle. The walk tends to stay on one side of zero for long stretches.

### Three Arcsine Laws

All three share the same limiting arcsine distribution:

1. **Last visit time** $L_{2n}/(2n)$
2. **Fraction of time positive** — proportion of steps above zero
3. **Time of the maximum** — when the walk achieves its peak

These results, due to Paul Levy, are among the most surprising in probability theory.

## Examples

**Example.** Simulate the last visit time for 1000 random walks of length 10,000.

```python
import numpy as np

np.random.seed(42)
n = 10_000
n_sim = 1_000

last_visits = np.zeros(n_sim)
for s in range(n_sim):
    steps = 2 * np.random.randint(0, 2, n) - 1
    walk = np.concatenate([[0], np.cumsum(steps)])
    zeros = np.where(walk == 0)[0]
    last_visits[s] = zeros[-1]

# Should be U-shaped (arcsine)
normalized = last_visits / n
print(f"Fraction near start (< 0.1): {np.mean(normalized < 0.1):.3f}")
print(f"Fraction near middle (0.4-0.6): {np.mean((normalized > 0.4) & (normalized < 0.6)):.3f}")
print(f"Fraction near end (> 0.9): {np.mean(normalized > 0.9):.3f}")
print(f"Mean: {normalized.mean():.3f} (theory: 0.5)")
```
