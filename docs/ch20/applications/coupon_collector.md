# Coupon Collector Problem

Collecting all $n$ coupon types requires about $n \ln n$ purchases — proved by decomposing the process into geometric phases and applying the WLLN.

## Definition

With $n$ coupon types, each purchase yields a uniformly random type. Let $T_n$ be the number of purchases to collect all $n$ types. Then:

$$
\frac{T_n}{n \ln n} \xrightarrow{p} 1
$$

## Explanation

### Phase Decomposition

Let $\tau_i$ = additional purchases needed for the $i$-th new coupon after holding $i-1$ distinct types. Then $T_n = \sum_{i=1}^n \tau_i$ where:

$$
\tau_i \sim \operatorname{Geom}\!\left(\frac{n - i + 1}{n}\right), \quad \text{independent}
$$

### Mean

$$
E[T_n] = \sum_{i=1}^n \frac{n}{n - i + 1} = n \sum_{k=1}^n \frac{1}{k} = n H_n \sim n \ln n
$$

### Variance

$$
\operatorname{Var}(T_n) = \sum_{i=1}^n \frac{n^2(1 - p_i)}{(n-i+1)^2 \cdot p_i^{-2}} \le n^2 \sum_{k=1}^n \frac{1}{k^2} \le \frac{\pi^2 n^2}{6}
$$

### Proof of Convergence

By Chebyshev: $P\!\left(\left\lvert \frac{T_n}{n\ln n} - \frac{H_n}{\ln n}\right\rvert > \varepsilon\right) \le \frac{Cn^2}{\varepsilon^2 n^2 (\ln n)^2} \to 0$. Since $H_n/\ln n \to 1$, we get $T_n/(n\ln n) \xrightarrow{p} 1$.

## Examples

**Example.** With $n = 100$ types, expect about $100 \ln 100 \approx 461$ purchases.

```python
import numpy as np

np.random.seed(42)

def coupon_collector(n):
    """Simulate collecting all n coupon types."""
    collected = set()
    count = 0
    while len(collected) < n:
        collected.add(np.random.randint(0, n))
        count += 1
    return count

n = 100
H_n = sum(1/k for k in range(1, n + 1))
E_T = n * H_n

trials = [coupon_collector(n) for _ in range(10_000)]
print(f"n={n}: E[T] = {E_T:.1f}, simulated mean = {np.mean(trials):.1f}")
print(f"n*ln(n) = {n * np.log(n):.1f}")
```
