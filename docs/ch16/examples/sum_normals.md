# Sum of Normals

The normal family is closed under convolution: a sum of independent normals is normal, with mean and variance adding.

## Definition

If $X \sim N(\mu_1, \sigma_1^2)$ and $Y \sim N(\mu_2, \sigma_2^2)$ are independent, then:

$$
X + Y \sim N(\mu_1 + \mu_2, \; \sigma_1^2 + \sigma_2^2)
$$

More generally, if $X_1, \ldots, X_n$ are independent with $X_i \sim N(\mu_i, \sigma_i^2)$:

$$
\sum_{i=1}^n X_i \sim N\!\left(\sum_{i=1}^n \mu_i, \; \sum_{i=1}^n \sigma_i^2\right)
$$

## Explanation

### Proof via MGFs

$$
M_{X+Y}(t) = M_X(t) \cdot M_Y(t) = e^{\mu_1 t + \sigma_1^2 t^2/2} \cdot e^{\mu_2 t + \sigma_2^2 t^2/2} = e^{(\mu_1+\mu_2)t + (\sigma_1^2+\sigma_2^2)t^2/2}
$$

This is the MGF of $N(\mu_1 + \mu_2, \sigma_1^2 + \sigma_2^2)$. By MGF uniqueness, the result follows.

### Proof via Convolution Integral

For $X, Y$ iid $N(0,1)$:

$$
f_{X+Y}(a) = \int_{-\infty}^{\infty} \frac{1}{\sqrt{2\pi}} e^{-b^2/2} \cdot \frac{1}{\sqrt{2\pi}} e^{-(a-b)^2/2} \, db
$$

Completing the square in $-b^2/2 - (a-b)^2/2 = -(b - a/2)^2 - a^2/4$ and evaluating the Gaussian integral yields $f_{X+Y}(a) = \frac{1}{\sqrt{4\pi}} e^{-a^2/4}$, the PDF of $N(0, 2)$.

### Sample Mean

For iid $X_i \sim N(\mu, \sigma^2)$:

$$
\bar{X} = \frac{1}{n}\sum_{i=1}^n X_i \sim N\!\left(\mu, \; \frac{\sigma^2}{n}\right)
$$

This is exact for normal populations, not just an approximation.

## Examples

**Example.** $X \sim N(2, 1.5^2)$ and $Y \sim N(-1, 2^2)$ independent. Then $X + Y \sim N(1, 6.25)$.

```python
import numpy as np
from scipy import stats

np.random.seed(42)
n_sim = 100_000

mu1, sig1 = 2, 1.5
mu2, sig2 = -1, 2.0

X = np.random.normal(mu1, sig1, n_sim)
Y = np.random.normal(mu2, sig2, n_sim)
S = X + Y

mu_sum = mu1 + mu2
var_sum = sig1**2 + sig2**2

print(f"Simulated: mean={S.mean():.4f}, var={S.var():.4f}")
print(f"Theory:    mean={mu_sum:.4f}, var={var_sum:.4f}")

# Verify normality with KS test
ks_stat, p_val = stats.kstest(S, 'norm', args=(mu_sum, np.sqrt(var_sum)))
print(f"KS test p-value: {p_val:.4f} (large => consistent with normal)")
```
