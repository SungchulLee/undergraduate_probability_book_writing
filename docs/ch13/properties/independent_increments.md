# Independent Increments

Counts in non-overlapping time intervals are independent — the defining property that makes the Poisson process tractable.

## Definition

A counting process $\{N(t)\}$ has **independent increments** if for any $0 \le t_1 < t_2 < \cdots < t_n$:

$$
N(t_2) - N(t_1), \; N(t_3) - N(t_2), \; \ldots, \; N(t_n) - N(t_{n-1})
$$

are mutually independent.

## Explanation

### Why Independence Holds

In the Poisson process, the memoryless property of the exponential interarrival times ensures that the future evolution does not depend on the past. Knowing $N(s)$ does not affect the distribution of $N(t) - N(s)$ for $t > s$.

### Contrast with Non-Independent Processes

A **renewal process** with non-exponential interarrival times does *not* have independent increments. The time elapsed since the last event carries information about the next event.

### Joint Distribution

For $0 < t_1 < t_2 < \cdots < t_n$, let $X_k = N(t_k) - N(t_{k-1})$. Then:

$$
P(X_1 = x_1, \ldots, X_n = x_n) = \prod_{k=1}^n \frac{e^{-\lambda h_k}(\lambda h_k)^{x_k}}{x_k!}
$$

where $h_k = t_k - t_{k-1}$.

## Examples

**Example.** Verify independence: count in $[0,1]$ and $[1,3]$ are uncorrelated.

```python
import numpy as np

np.random.seed(42)
lam = 5
n_sim = 100_000

N1 = np.random.poisson(lam * 1, n_sim)   # [0, 1]
N2 = np.random.poisson(lam * 2, n_sim)   # [1, 3]

print(f"Corr(N1, N2) = {np.corrcoef(N1, N2)[0,1]:.4f}  (theory: 0)")
print(f"E[N1*N2] = {np.mean(N1*N2):.3f}")
print(f"E[N1]*E[N2] = {N1.mean()*N2.mean():.3f}")
```
