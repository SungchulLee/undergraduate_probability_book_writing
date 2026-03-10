# Monte Carlo Simulation

The LLN guarantees that sample averages converge to expected values, providing the theoretical foundation for estimating integrals and probabilities via random sampling.

## Definition

To estimate $\theta = E[g(X)]$:

1. Draw $n$ iid samples $X_1, \ldots, X_n$ from the distribution of $X$
2. Compute $\hat{\theta}_n = \frac{1}{n}\sum_{i=1}^n g(X_i)$
3. By the SLLN, $\hat{\theta}_n \xrightarrow{a.s.} \theta$

The CLT gives the error: $\hat{\theta}_n \approx N(\theta, \operatorname{Var}(g(X))/n)$, so the standard error is $O(1/\sqrt{n})$.

## Explanation

### Estimating pi

Drop $n$ points uniformly in $[0,1]^2$. Let $X_i = \mathbf{1}(U_i^2 + V_i^2 \le 1)$. Then $E[X_i] = \pi/4$ and:

$$
\hat{\pi}_n = 4\bar{X}_n \xrightarrow{a.s.} \pi
$$

### Convergence Rate

The standard error is $\sigma/\sqrt{n}$. To halve the error, quadruple the sample size. This $O(1/\sqrt{n})$ rate is dimension-independent, making Monte Carlo competitive in high dimensions where deterministic quadrature fails.

## Examples

**Example.** Estimate $\pi$ and track convergence.

```python
import numpy as np

np.random.seed(42)
n = 100_000

U = np.random.uniform(0, 1, (n, 2))
inside = (U[:, 0]**2 + U[:, 1]**2) <= 1
pi_hat = 4 * np.cumsum(inside) / np.arange(1, n + 1)

for k in [100, 1000, 10000, 100000]:
    print(f"n={k:>6d}: π̂ = {pi_hat[k-1]:.6f}, error = {abs(pi_hat[k-1]-np.pi):.6f}")
```
