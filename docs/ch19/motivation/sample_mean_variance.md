# Sample Mean and Sample Variance

The sample mean $\bar{X}$ and sample variance $S^2$ are the two fundamental summary statistics for normal populations. Their distributions and their surprising independence underpin all of classical normal-theory inference.

## Definition

For $X_1, \ldots, X_n$ iid from $N(\mu, \sigma^2)$, define:

$$
\bar{X} = \frac{1}{n}\sum_{i=1}^n X_i, \qquad S^2 = \frac{1}{n-1}\sum_{i=1}^n (X_i - \bar{X})^2
$$

Their sampling distributions are:

$$
\bar{X} \sim N\!\left(\mu, \frac{\sigma^2}{n}\right), \qquad \frac{(n-1)S^2}{\sigma^2} \sim \chi^2_{n-1}
$$

and $\bar{X}$ and $S^2$ are independent.

## Explanation

### Distribution of the sample mean

Since each $X_i \sim N(\mu, \sigma^2)$ independently, the sample mean is a linear combination of normals, hence normal. Standardizing gives:

$$
\frac{\bar{X} - \mu}{\sigma/\sqrt{n}} \sim N(0,1)
$$

### Distribution of the sample variance

The scaled sample variance $(n-1)S^2/\sigma^2$ follows a $\chi^2_{n-1}$ distribution. The proof (given in the chi-squared section) uses the decomposition identity and moment generating functions.

### Independence of mean and variance

For jointly normal random variables, zero covariance implies independence. Since $\operatorname{Cov}(\bar{X}, X_i - \bar{X}) = 0$ for every $i$, and $S^2$ is a function of the residuals $X_i - \bar{X}$, the two statistics are independent. This independence is specific to normal populations.

### The studentized mean

Combining these results:

$$
\frac{\bar{X} - \mu}{S/\sqrt{n}} = \frac{N(0,1)}{\sqrt{\chi^2_{n-1}/(n-1)}} \sim t_{n-1}
$$

## Examples

**Example 1.** Verify the sampling distributions and independence by simulation.

```python
import numpy as np
from scipy import stats

np.random.seed(42)
mu, sigma, n = 5, 3, 12
n_sim = 100_000

x_bars, s2s = [], []
for _ in range(n_sim):
    x = np.random.normal(mu, sigma, n)
    x_bars.append(x.mean())
    s2s.append(x.var(ddof=1))

x_bars, s2s = np.array(x_bars), np.array(s2s)

print(f"Mean of X-bar: {x_bars.mean():.3f}  (theory: {mu})")
print(f"Var of X-bar:  {x_bars.var():.4f}  (theory: {sigma**2/n:.4f})")

chi2_vals = (n - 1) * s2s / sigma**2
print(f"Mean of (n-1)S^2/sigma^2: {chi2_vals.mean():.3f}  (theory: {n-1})")

# Test independence via correlation
corr = np.corrcoef(x_bars, s2s)[0, 1]
print(f"Corr(X-bar, S^2): {corr:.4f}  (theory: 0)")
```
