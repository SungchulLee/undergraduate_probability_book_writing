# Studentized Sample Mean

The studentized sample mean replaces the unknown $\sigma$ with $S$ in the standardized mean. Its $t_{n-1}$ distribution is the basis for $t$-confidence intervals and $t$-tests.

## Definition

For $X_1, \ldots, X_n$ iid from $N(\mu, \sigma^2)$:

$$
T = \frac{\bar{X} - \mu}{S/\sqrt{n}} \sim t_{n-1}
$$

## Explanation

### Derivation

Rewrite the statistic as a ratio of known quantities:

$$
T = \frac{\bar{X} - \mu}{\sigma/\sqrt{n}} \bigg/ \sqrt{\frac{(n-1)S^2/\sigma^2}{n-1}}
$$

The numerator is $N(0,1)$. The denominator contains $\chi^2_{n-1}/(n-1)$. Since $\bar{X}$ and $S^2$ are independent (by the zero-covariance argument for multivariate normals), the ratio has the form $Z/\sqrt{V/d}$ with $d = n-1$, which is $t_{n-1}$ by definition.

### Applications

This result provides:

- **$t$-confidence intervals**: $\bar{X} \pm t_{\alpha/2,\, n-1} \cdot S/\sqrt{n}$
- **One-sample $t$-tests**: reject $H_0\colon \mu = \mu_0$ when $|T|$ exceeds the critical value
- **Two-sample $t$-tests**: by extending the same logic to differences of means

## Examples

**Example 1.** Simulate the studentized mean and verify it follows $t_{n-1}$.

```python
import numpy as np
from scipy import stats

np.random.seed(42)
mu, sigma, n = 10, 3, 8
n_sim = 100_000

t_vals = np.array([
    (x.mean() - mu) / (x.std(ddof=1) / np.sqrt(n))
    for x in (np.random.normal(mu, sigma, n) for _ in range(n_sim))
])

print(f"Mean: {t_vals.mean():.4f}  (theory: 0)")
print(f"Var:  {t_vals.var():.4f}  (theory: {(n-1)/(n-3):.4f})")

stat, pval = stats.kstest(t_vals, 't', args=(n-1,))
print(f"KS test p-value: {pval:.4f}")
```
