# Comparison with Binomial

The hypergeometric converges to the binomial when the population is large relative to the sample — sampling without replacement becomes indistinguishable from sampling with replacement.

## Definition

If $X \sim \text{HGeom}(N, K, n)$ and $Y \sim \text{Bin}(n, K/N)$ with $N \to \infty$ while $K/N \to p$:

$$
P(X = k) \to P(Y = k) = \binom{n}{k}p^k(1-p)^{n-k}
$$

**Rule of thumb:** the binomial approximation is good when $n/N < 0.05$ (sampling less than 5% of the population).

## Explanation

### Why the Approximation Works

When the population is large, removing one item barely changes the composition. The probability of success on each draw stays approximately $p = K/N$, making the draws approximately independent — the binomial assumption.

### Variance Comparison

| Distribution | Variance |
|:-------------|:---------|
| $\text{Bin}(n, p)$ | $npq$ |
| $\text{HGeom}(N, K, n)$ | $npq \cdot \frac{N-n}{N-1}$ |

The hypergeometric always has *smaller* variance (for $n > 1$). Intuitively, sampling without replacement gives more information because you never "waste" a draw on a previously seen item.

### Poisson Approximation

When $n$ is large and $p = K/N$ is small: $\text{HGeom}(N, K, n) \approx \text{Bin}(n, p) \approx \text{Poisson}(np)$. Both approximations apply in this regime.

## Examples

**Example.** A lot of $N = 10000$ items contains $K = 500$ defectives ($p = 0.05$). Sample $n = 50$.

```python
import numpy as np
from scipy import stats

N, K, n = 10000, 500, 50
p = K / N

hg = stats.hypergeom(N, K, n)
bn = stats.binom(n, p)

print("k   HGeom     Binom     Diff")
for k in range(8):
    h = hg.pmf(k)
    b = bn.pmf(k)
    print(f"{k}   {h:.6f}  {b:.6f}  {abs(h-b):.6f}")

print(f"\nHGeom Var = {hg.var():.4f}")
print(f"Binom Var = {bn.var():.4f}")
print(f"FPC = {(N-n)/(N-1):.4f}")

# Small population: approximation breaks down
N2, K2, n2 = 20, 10, 10
hg2 = stats.hypergeom(N2, K2, n2)
bn2 = stats.binom(n2, K2/N2)
print(f"\nSmall population (N=20, n=10):")
print(f"HGeom Var = {hg2.var():.4f}")
print(f"Binom Var = {bn2.var():.4f}")
```
