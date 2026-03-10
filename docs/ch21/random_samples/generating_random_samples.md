# Generating Random Samples

All simulation begins with pseudo-random number generators — uniform samples that can be transformed into any target distribution via the inverse CDF or other methods.

## Definition

A **pseudo-random number generator** (PRNG) produces a deterministic sequence that approximates iid $U(0,1)$ samples. Given $U \sim U(0,1)$, any target distribution can be obtained through transformations:

$$
X = F^{-1}(U) \sim F
$$

where $F^{-1}$ is the quantile function (inverse CDF).

## Explanation

### Core Functions (NumPy)

| Function | Distribution |
|:---|:---|
| `np.random.rand(n)` | $U(0,1)$ |
| `np.random.randn(n)` | $N(0,1)$ |
| `np.random.randint(a, b, n)` | Uniform on $\{a, \ldots, b-1\}$ |
| `np.random.exponential(1/lam, n)` | $\operatorname{Exp}(\lambda)$ |
| `np.random.poisson(lam, n)` | $\operatorname{Pois}(\lambda)$ |

### Reproducibility

Setting the seed (`np.random.seed(42)`) ensures the same sequence each run — essential for debugging and reproducible experiments.

### From Uniform to Everything

- **Bernoulli**: $B = \mathbf{1}(U > 1-p)$
- **Exponential**: $X = -\ln(U)/\lambda$
- **Normal**: Box-Muller or built-in `randn`
- **General**: Inverse CDF $F^{-1}(U)$

## Examples

**Example.** Generate Bernoulli and exponential samples from uniform.

```python
import numpy as np

np.random.seed(42)
n = 10_000

U = np.random.rand(n)

# Bernoulli(0.3) from uniform
p = 0.3
B = (U > 1 - p).astype(int)
print(f"Bernoulli({p}): mean={B.mean():.4f} (theory {p})")

# Exp(2) from uniform via inverse CDF
lam = 2.0
X = -np.log(1 - np.random.rand(n)) / lam
print(f"Exp({lam}): mean={X.mean():.4f} (theory {1/lam})")
```
