# From Counting to the Poisson Process

The Poisson process bridges static counting (Poisson distribution) and dynamic event arrival (exponential waiting times) into a unified framework.

## Definition

Consider $n$ independent events in $[0, t]$, each occurring at a uniformly random time. As $n \to \infty$ with the expected number $\lambda t$ fixed, the counting process converges to a Poisson process with rate $\lambda$.

Formally, subdivide $[0, t]$ into $n$ intervals of length $t/n$. Each interval has an event with probability $p = \lambda t / n$. The total count is $\text{Bin}(n, p) \to \text{Pois}(\lambda t)$.

## Explanation

### The Limiting Argument

1. Divide time into $n$ tiny slots of width $\Delta t = t/n$
2. Each slot has at most one event (probability $\lambda\Delta t$)
3. Slots are independent
4. Total count in $[0, t]$ is $\text{Bin}(n, \lambda t/n) \to \text{Pois}(\lambda t)$

This construction shows the Poisson process as the continuous-time limit of a sequence of Bernoulli trials.

### Two Equivalent Constructions

| Construction | Description |
|:-------------|:------------|
| **Count-based** | $N(t) \sim \text{Pois}(\lambda t)$ with independent increments |
| **Interarrival-based** | $T_i \stackrel{\text{iid}}{\sim} \text{Exp}(\lambda)$; $N(t) = \max\{n : S_n \le t\}$ |

Both produce the same process.

## Examples

**Example.** Compare $\text{Bin}(n, 10/n)$ counts with $\text{Pois}(10)$ for increasing $n$.

```python
import numpy as np

np.random.seed(42)
n_sim = 100_000
lam_t = 10

for n in [20, 100, 1000]:
    counts = np.random.binomial(n, lam_t/n, n_sim)
    print(f"Bin({n}, {lam_t/n:.4f}): mean={counts.mean():.3f}, "
          f"var={counts.var():.3f}  (Pois(10): mean=var=10)")
```
