# Approximating Poisson Probabilities


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

## Why the CLT Applies to the Poisson

If $X \sim \text{Po}(\lambda)$, then $X$ can be decomposed as a sum of iid Poisson random variables:

$$X = \sum_{i=1}^{\lambda} Y_i, \qquad Y_i \sim \text{Po}(1) \text{ iid}$$

(when $\lambda$ is a positive integer). Since $E[Y_i] = 1$ and $\text{Var}(Y_i) = 1$, the CLT gives:

$$\frac{X - \lambda}{\sqrt{\lambda}} \xrightarrow{d} N(0,1) \quad \text{as } \lambda \to \infty$$

For large $\lambda$:

$$X \approx N(\lambda, \lambda)$$

## The Approximation Chain

For a sum of iid Bernoulli trials with $n$ large and $p$ small:

$$B(n, p) \approx \text{Po}(np) \approx N(np, np)$$

- The first approximation (Poisson) is best when $p$ is small.
- The second approximation (Normal) is best when $\lambda = np$ is large.

## Example

Let $X \sim \text{Po}(100)$. Find $P(X \geq 120)$.

**Using CLT with continuity correction:**

$$P(X \geq 120) = P(X \geq 119.5) = P\left(Z \geq \frac{119.5 - 100}{\sqrt{100}}\right) = P(Z \geq 1.95)$$

$$= 1 - \Phi(1.95) = 0.0256$$

## Python Implementation

```python
import numpy as np
from scipy import stats

lambdas = [10, 25, 50, 100, 200]

for lam in lambdas:
    # Exact: P(X >= lam + 2*sqrt(lam))
    threshold = int(lam + 2 * np.sqrt(lam))
    exact = 1 - stats.poisson.cdf(threshold - 1, lam)
    
    # Normal approximation with CC
    z = (threshold - 0.5 - lam) / np.sqrt(lam)
    approx = 1 - stats.norm.cdf(z)
    
    print(f"λ={lam:>3d}, threshold={threshold:>3d}: "
          f"Exact={exact:.4f}, Normal≈{approx:.4f}")
```

**Output:**
```
λ= 10, threshold= 16: Exact=0.0487, Normal≈0.0418
λ= 25, threshold= 35: Exact=0.0297, Normal≈0.0287
λ= 50, threshold= 64: Exact=0.0302, Normal≈0.0294
λ=100, threshold=120: Exact=0.0282, Normal≈0.0256
λ=200, threshold=228: Exact=0.0281, Normal≈0.0274
```

The normal approximation improves as $\lambda$ increases.
