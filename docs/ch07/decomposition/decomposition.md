# Decomposition of Random Variables

Many important random variables decompose as sums of simpler pieces — often iid — making their mean and variance easy to compute.

## Definition

If $S = \sum_{i=1}^n X_i$ where $X_1, \ldots, X_n$ are independent:

$$
E[S] = \sum_{i=1}^n E[X_i], \qquad \text{Var}(S) = \sum_{i=1}^n \text{Var}(X_i)
$$

## Explanation

### Standard Decompositions

| Distribution | Decomposition | $E[S]$ | $\text{Var}(S)$ |
|:-------------|:-------------|:-------|:----------------|
| $\text{Bin}(n,p)$ | $\sum_{i=1}^n \text{Bern}(p)$ | $np$ | $np(1-p)$ |
| $\text{NB}(r,p)$ | $\sum_{i=1}^r \text{Geo}(p)$ | $r/p$ | $r(1-p)/p^2$ |
| Coupon collector | $\sum_{i=1}^n \text{Geo}((n-i+1)/n)$ | $nH_n$ | $\approx \frac{\pi^2}{6}n^2$ |

### Strategy

1. Identify the distribution as a sum of simpler variables
2. Verify independence
3. Compute $E[X_i]$ and $\text{Var}(X_i)$ for each piece
4. Sum to get $E[S]$ and $\text{Var}(S)$

## Examples

**Example.** Coupon collector with $n = 20$ toy types. The waiting time to collect all is $T = \sum_{i=1}^{20}\tau_i$ where $\tau_i \sim \text{Geo}((21-i)/20)$.

$$
E[T] = 20\!\left(1 + \tfrac{1}{2} + \cdots + \tfrac{1}{20}\right) = 20H_{20} \approx 71.5
$$

```python
import numpy as np

# Coupon collector: n=20
n = 20
H_n = sum(1/k for k in range(1, n+1))
E_T = n * H_n
Var_T = n**2 * sum(1/k**2 for k in range(1, n+1)) - n * H_n
print(f"E[T] = {E_T:.1f}, SD(T) = {np.sqrt(Var_T):.1f}")

# Simulate
np.random.seed(42)
T_sim = []
for _ in range(100_000):
    collected = set()
    t = 0
    while len(collected) < n:
        collected.add(np.random.randint(n))
        t += 1
    T_sim.append(t)
print(f"MC: E[T] = {np.mean(T_sim):.1f}, SD(T) = {np.std(T_sim):.1f}")
```
