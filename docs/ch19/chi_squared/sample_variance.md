# Distribution of Sample Variance

The scaled sample variance $(n-1)S^2/\sigma^2$ follows a $\chi^2_{n-1}$ distribution, and is independent of the sample mean. These two facts are the cornerstones of the Student's $t$ distribution and classical inference.

## Definition

For $X_1, \ldots, X_n$ iid from $N(\mu, \sigma^2)$ with $S^2 = \frac{1}{n-1}\sum(X_i - \bar{X})^2$:

$$
\frac{(n-1)S^2}{\sigma^2} = \sum_{i=1}^n \left(\frac{X_i - \bar{X}}{\sigma}\right)^2 \sim \chi^2_{n-1}
$$

and $\bar{X}$ is independent of $S^2$.

## Explanation

### Independence of mean and residuals

The covariance between $\bar{X}$ and each residual $X_i - \bar{X}$ is zero:

$$
\operatorname{Cov}(\bar{X},\; X_i - \bar{X}) = \frac{\sigma^2}{n} - \frac{\sigma^2}{n} = 0
$$

Since $(\bar{X}, X_1 - \bar{X}, \ldots, X_n - \bar{X})$ is a linear transformation of the multivariate normal vector $(X_1, \ldots, X_n)$, zero covariance implies independence. Because $S^2$ is a function of the residuals, $\bar{X}$ and $S^2$ are independent.

### Proof via the decomposition identity

Expanding $(X_i - \mu) = (X_i - \bar{X}) + (\bar{X} - \mu)$ and using $\sum(X_i - \bar{X}) = 0$:

$$
\sum_{i=1}^n \left(\frac{X_i - \mu}{\sigma}\right)^2 = \sum_{i=1}^n \left(\frac{X_i - \bar{X}}{\sigma}\right)^2 + \left(\frac{\bar{X} - \mu}{\sigma/\sqrt{n}}\right)^2
$$

The left side is $\chi^2_n$ and the last term is $\chi^2_1$. Taking MGFs and using independence:

$$
(1-2t)^{-n/2} = \varphi_{\sum(X_i - \bar{X})^2/\sigma^2}(t) \cdot (1-2t)^{-1/2}
$$

Solving gives $\varphi(t) = (1-2t)^{-(n-1)/2}$, the MGF of $\chi^2_{n-1}$.

### Why n - 1 degrees of freedom

The $n$ residuals satisfy $\sum(X_i - \bar{X}) = 0$, so only $n-1$ are free. This linear constraint reduces the degrees of freedom from $n$ to $n-1$.

## Examples

**Example 1.** Simulate $(n-1)S^2/\sigma^2$ and verify it follows $\chi^2_{n-1}$.

```python
import numpy as np
from scipy import stats

np.random.seed(42)
mu, sigma, n = 5, 3, 10
n_sim = 100_000

chi2_vals = np.array([
    (n - 1) * np.var(np.random.normal(mu, sigma, n), ddof=1) / sigma**2
    for _ in range(n_sim)
])

print(f"Mean: {chi2_vals.mean():.3f}  (theory: {n-1})")
print(f"Var:  {chi2_vals.var():.3f}  (theory: {2*(n-1)})")

stat, pval = stats.kstest(chi2_vals, 'chi2', args=(n-1,))
print(f"KS test p-value: {pval:.4f}")
```
