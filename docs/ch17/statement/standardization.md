# Standardization in the CLT

Standardization converts any sum into a mean-zero, variance-one quantity, allowing the CLT approximation via the standard normal CDF $\Phi$.

## Definition

For a random variable $X$ with mean $\mu$ and standard deviation $\sigma$:

$$
Z = \frac{X - \mu}{\sigma}
$$

has $E[Z] = 0$ and $\operatorname{Var}(Z) = 1$. The reverse transformation is $X = \mu + \sigma Z$.

## Explanation

### Standardized Sum

For iid $X_1, \ldots, X_n$ with mean $\mu$ and variance $\sigma^2$, the CLT says:

$$
Z_n = \frac{S_n - n\mu}{\sigma\sqrt{n}} \approx N(0,1) \quad \text{for large } n
$$

Reverse standardization gives the practical approximation $S_n \approx N(n\mu, n\sigma^2)$.

### Computing Probabilities

To approximate $P(a \le S_n \le b)$:

**Step 1.** Standardize both endpoints:

$$
P(a \le S_n \le b) = P\!\left(\frac{a - n\mu}{\sigma\sqrt{n}} \le Z_n \le \frac{b - n\mu}{\sigma\sqrt{n}}\right)
$$

**Step 2.** Apply the CLT:

$$
\approx \Phi\!\left(\frac{b - n\mu}{\sigma\sqrt{n}}\right) - \Phi\!\left(\frac{a - n\mu}{\sigma\sqrt{n}}\right)
$$

### Sample Mean Version

Since $\bar{X}_n = S_n / n$:

$$
\frac{\bar{X}_n - \mu}{\sigma / \sqrt{n}} \approx N(0,1)
$$

so $\bar{X}_n \approx N(\mu, \sigma^2/n)$.

## Examples

**Example.** $X_i$ iid with $\mu = 10$, $\sigma = 3$, $n = 100$. Find $P(S_{100} > 1030)$.

Standardize: $z = (1030 - 1000)/(3 \cdot 10) = 1.0$. Then $P(S_{100} > 1030) \approx 1 - \Phi(1) = 0.1587$.

```python
import numpy as np
from scipy import stats

mu, sigma, n = 10, 3, 100
threshold = 1030

z = (threshold - n * mu) / (sigma * np.sqrt(n))
p = 1 - stats.norm.cdf(z)
print(f"z = {z:.4f}")
print(f"P(S_100 > 1030) ≈ 1 - Φ({z:.2f}) = {p:.4f}")
```
