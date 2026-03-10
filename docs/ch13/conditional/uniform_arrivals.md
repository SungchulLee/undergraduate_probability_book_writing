# Uniform Distribution of Arrivals

Given that exactly $n$ events occurred in $[0, t]$, the $n$ arrival times are distributed as the order statistics of $n$ iid $\text{Uniform}(0, t)$ random variables.

## Definition

If $\{N(t)\}$ is a Poisson process with rate $\lambda$ and $N(t) = n$, then the arrival times $S_1 < S_2 < \cdots < S_n$ have the same joint distribution as the order statistics of $n$ iid $\text{Uniform}(0, t)$ draws.

Equivalently, each individual arrival time (unordered) is uniformly distributed on $[0, t]$, independently of the others.

## Explanation

### Why Uniform?

The Poisson process has stationary increments, so events are "equally likely" to fall anywhere in $[0, t]$. Conditioning on the total count removes the randomness in $N(t)$, leaving only the positions — which are uniform by symmetry.

### Conditional Density

For $n = 1$: $f_{S_1 \mid N(t) = 1}(s) = 1/t$ for $0 < s < t$.

For general $n$: the joint density of the order statistics is $n!/t^n$ on $0 < s_1 < s_2 < \cdots < s_n < t$.

### Applications

This result is the basis for:

- Simulating Poisson processes (generate $N \sim \text{Pois}(\lambda t)$, then $N$ uniform points)
- Testing whether data is consistent with a Poisson process
- Computing conditional expectations of arrival-time functionals

## Examples

**Example.** Given $N(10) = 5$, the 5 arrivals are like 5 sorted uniform draws from $[0, 10]$.

```python
import numpy as np

np.random.seed(42)

t = 10
lam = 2
n_sim = 50_000

# Method 1: Simulate via exponential interarrivals, condition on N(t)=5
arrivals_method1 = []
for _ in range(n_sim):
    times = np.cumsum(np.random.exponential(1/lam, 20))
    in_window = times[times <= t]
    if len(in_window) == 5:
        arrivals_method1.append(in_window)

# Method 2: Generate 5 uniform(0, t) and sort
arrivals_method2 = [np.sort(np.random.uniform(0, t, 5)) for _ in range(n_sim)]

# Compare distributions of the 3rd arrival
s3_m1 = [a[2] for a in arrivals_method1[:5000]]
s3_m2 = [a[2] for a in arrivals_method2[:5000]]

print(f"Mean of 3rd arrival (conditional): {np.mean(s3_m1):.3f}")
print(f"Mean of 3rd arrival (uniform):     {np.mean(s3_m2):.3f}")
print(f"Theory (3rd order stat of 5 from U(0,10)): {10*3/6:.3f}")
```
