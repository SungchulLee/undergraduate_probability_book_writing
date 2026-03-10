# Stationary Increments

The distribution of the count in an interval depends only on the interval's length, not when it starts — the Poisson process is time-homogeneous.

## Definition

A counting process has **stationary increments** if for any $s \ge 0$:

$$
N(t+s) - N(s) \stackrel{d}{=} N(t)
$$

For the Poisson process: $N(t+s) - N(s) \sim \text{Pois}(\lambda t)$.

## Explanation

### Combined with Independence

The Poisson process is the only counting process with **both** stationary and independent increments (and unit jumps). This characterization theorem means the three axioms are equivalent to requiring stationarity + independence + no simultaneous events.

### Non-Homogeneous Case

A non-homogeneous Poisson process with rate $\lambda(t)$ has independent but **not** stationary increments:

$$
N(t+s) - N(s) \sim \text{Pois}\!\left(\int_s^{s+t}\lambda(u)\,du\right)
$$

This depends on $s$, breaking stationarity.

### Practical Implication

Stationarity means the "rush" doesn't change: the rate of events is the same whether you observe at 2 PM or 4 PM. If the real-world rate changes over time, the homogeneous model is inadequate.

## Examples

**Example.** Compare counts in $[0, 1]$, $[5, 6]$, and $[100, 101]$ — all $\text{Pois}(\lambda)$.

```python
import numpy as np

np.random.seed(42)
lam = 7
n_sim = 100_000

# All three intervals have the same distribution
for start in [0, 5, 100]:
    N = np.random.poisson(lam, n_sim)
    print(f"[{start}, {start+1}]: mean={N.mean():.3f}, var={N.var():.3f}")
```
