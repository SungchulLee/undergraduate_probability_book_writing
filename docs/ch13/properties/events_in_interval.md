# Number of Events in an Interval

The count of Poisson process events in any interval of length $h$ follows $\text{Pois}(\lambda h)$, regardless of when the interval starts.

## Definition

For a Poisson process with rate $\lambda$, the number of events in any interval $(s, s+h]$ is

$$
N(s, s+h) = N(s+h) - N(s) \sim \text{Pois}(\lambda h)
$$

This depends only on the length $h$, not the starting point $s$.

## Explanation

### Moments

$$
E[N(s, s+h)] = \lambda h, \qquad \text{Var}(N(s, s+h)) = \lambda h
$$

### Tail Probabilities

For large $\lambda h$, the normal approximation applies:

$$
P(N(t) > k) \approx P\!\left(Z > \frac{k - \lambda t}{\sqrt{\lambda t}}\right)
$$

### Multiple Intervals

The counts in disjoint intervals are independent Poisson random variables. For intervals $I_1, I_2, \ldots, I_m$ of lengths $h_1, \ldots, h_m$:

$$
N(I_1), N(I_2), \ldots, N(I_m) \text{ are independent with } N(I_k) \sim \text{Pois}(\lambda h_k)
$$

## Examples

**Example.** Calls arrive at rate 10/hour. Count in the first 30 min: $\text{Pois}(5)$. Count in the next 2 hours: $\text{Pois}(20)$. Independent.

```python
import numpy as np
from scipy.stats import poisson

np.random.seed(42)
lam = 10  # per hour
n_sim = 100_000

# Simulate and count in [0, 0.5] and [0.5, 2.5]
count1, count2 = [], []
for _ in range(n_sim):
    arrivals = []
    t = 0
    while t < 2.5:
        t += np.random.exponential(1/lam)
        if t < 2.5:
            arrivals.append(t)
    arr = np.array(arrivals)
    count1.append(np.sum(arr <= 0.5))
    count2.append(np.sum((arr > 0.5) & (arr <= 2.5)))

c1, c2 = np.array(count1), np.array(count2)
print(f"[0, 0.5]: mean={c1.mean():.3f} var={c1.var():.3f}  (Pois(5))")
print(f"[0.5, 2.5]: mean={c2.mean():.3f} var={c2.var():.3f}  (Pois(20))")
print(f"Corr = {np.corrcoef(c1, c2)[0,1]:.4f}  (theory: 0)")
```
