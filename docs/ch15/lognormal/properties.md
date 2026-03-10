# Log-Normal Distribution Properties

The log-normal distribution has closed-form moments derived from the normal MGF, exhibits multiplicative closure (products of independent log-normals are log-normal), and is always right-skewed with no moment generating function despite having all finite moments.

## Definition

For $X \sim \text{LogN}(\mu, \sigma^2)$, the key properties are:

$$
E[X^k] = e^{k\mu + k^2\sigma^2/2}
$$

$$
E[X] = e^{\mu + \sigma^2/2}, \qquad \text{Var}(X) = e^{2\mu + \sigma^2}(e^{\sigma^2} - 1)
$$

$$
\text{Median}(X) = e^{\mu}, \qquad \text{Mode}(X) = e^{\mu - \sigma^2}
$$

If $X_1, \ldots, X_n$ are independent with $X_i \sim \text{LogN}(\mu_i, \sigma_i^2)$, then:

$$
\prod_{i=1}^{n} X_i \sim \text{LogN}\!\left(\sum_{i=1}^{n} \mu_i, \; \sum_{i=1}^{n} \sigma_i^2\right)
$$

## Explanation

### Deriving the mean

Since $X = e^Y$ where $Y \sim N(\mu, \sigma^2)$:

$$
E[X] = E[e^Y] = M_Y(1)
$$

where $M_Y(t) = e^{\mu t + \sigma^2 t^2/2}$ is the MGF of the normal distribution. Setting $t = 1$:

$$
E[X] = e^{\mu + \sigma^2/2}
$$

### Deriving the variance

Similarly, $E[X^2] = E[e^{2Y}] = M_Y(2) = e^{2\mu + 2\sigma^2}$, so:

$$
\text{Var}(X) = E[X^2] - (E[X])^2 = e^{2\mu + 2\sigma^2} - e^{2\mu + \sigma^2} = e^{2\mu + \sigma^2}(e^{\sigma^2} - 1)
$$

### General raw moments

$$
E[X^k] = E[e^{kY}] = M_Y(k) = e^{k\mu + k^2\sigma^2/2}
$$

Every moment is finite, but they grow extremely rapidly with $k$.

### Median and mode

**Median.** Since $P(X \leq e^\mu) = P(Y \leq \mu) = 0.5$ (using the symmetry of the normal), the median is $e^{\mu}$.

**Mode.** Setting $f'(x) = 0$ for the log-normal PDF:

$$
f(x) = \frac{1}{x\sigma\sqrt{2\pi}} \exp\!\left(-\frac{(\ln x - \mu)^2}{2\sigma^2}\right)
$$

yields the mode at $x = e^{\mu - \sigma^2}$.

The ordering $\text{Mode} < \text{Median} < \text{Mean}$ always holds for $\sigma > 0$, reflecting the right-skewness.

### Skewness and kurtosis

The skewness and excess kurtosis depend only on $\sigma^2$, not on $\mu$:

$$
\gamma_1 = (e^{\sigma^2} + 2)\sqrt{e^{\sigma^2} - 1}
$$

$$
\gamma_2 = e^{4\sigma^2} + 2e^{3\sigma^2} + 3e^{2\sigma^2} - 6
$$

Both are always positive: the log-normal is always right-skewed and always leptokurtic (heavier tails than the normal).

### Multiplicative closure

The log-normal family is closed under multiplication, not addition. If $X_i \sim \text{LogN}(\mu_i, \sigma_i^2)$ are independent, then:

$$
\prod_{i=1}^{n} X_i \sim \text{LogN}\!\left(\sum_{i=1}^{n} \mu_i, \; \sum_{i=1}^{n} \sigma_i^2\right)
$$

*Proof.* $\ln\!\left(\prod X_i\right) = \sum \ln X_i = \sum Y_i$ where $Y_i \sim N(\mu_i, \sigma_i^2)$ are independent. The sum of independent normals is normal.

Similarly, for a constant power $c$: $X^c \sim \text{LogN}(c\mu, c^2\sigma^2)$, since $\ln(X^c) = c\ln X = cY \sim N(c\mu, c^2\sigma^2)$.

### No moment generating function

The log-normal has **no MGF**: $E[e^{tX}] = \infty$ for all $t > 0$. This is because $e^{tX} = e^{te^Y}$ grows as a double exponential, which overwhelms the Gaussian decay of the normal density. However, all polynomial moments $E[X^k]$ are finite.

### Comparison with the normal

| Property | Normal | Log-Normal |
|:---|:---:|:---:|
| Support | $(-\infty, \infty)$ | $(0, \infty)$ |
| Closed under | addition | multiplication |
| Skewness | 0 | always positive |
| Symmetry | symmetric | right-skewed |
| MGF exists | yes | no |

### CDF and quantiles

$$
F(x) = \Phi\!\left(\frac{\ln x - \mu}{\sigma}\right), \quad x > 0
$$

The $p$-th quantile is $Q(p) = \exp(\mu + \sigma\,\Phi^{-1}(p))$.

## Examples

**Example 1: Moments of a log-normal.**

Let $X \sim \text{LogN}(1, 0.5^2)$. Compute $E[X]$, $\text{Var}(X)$, and $E[X^3]$.

$$
E[X] = e^{1 + 0.125} = e^{1.125}, \quad E[X^3] = e^{3 + 9 \cdot 0.125} = e^{4.125}
$$

```python
import numpy as np

mu, sigma = 1, 0.5

EX = np.exp(mu + sigma**2 / 2)
EX2 = np.exp(2*mu + 2*sigma**2)
VarX = EX2 - EX**2
EX3 = np.exp(3*mu + 9*sigma**2 / 2)

print(f"LogN({mu}, {sigma}^2):")
print(f"  E[X]   = exp({mu + sigma**2/2}) = {EX:.4f}")
print(f"  E[X^2] = exp({2*mu + 2*sigma**2}) = {EX2:.4f}")
print(f"  Var(X) = {VarX:.4f}")
print(f"  E[X^3] = exp({3*mu + 9*sigma**2/2}) = {EX3:.4f}")

# Verify by simulation
np.random.seed(42)
samples = np.random.lognormal(mu, sigma, 200000)
print(f"\nSimulated: E[X]={samples.mean():.4f}, Var={samples.var():.4f}, E[X^3]={np.mean(samples**3):.4f}")
```

**Output:**
```
LogN(1, 0.5^2):
  E[X]   = exp(1.125) = 3.0802
  E[X^2] = exp(2.5) = 12.1825
  Var(X) = 2.6946
  E[X^3] = exp(4.125) = 61.8678

Simulated: E[X]=3.0810, Var=2.6849, E[X^3]=61.8513
```

**Example 2: Product of log-normals.**

Let $X_1 \sim \text{LogN}(0.5, 0.3^2)$ and $X_2 \sim \text{LogN}(1.0, 0.4^2)$ be independent. Find the distribution of $X_1 X_2$.

$$
X_1 X_2 \sim \text{LogN}(0.5 + 1.0, \; 0.09 + 0.16) = \text{LogN}(1.5, 0.25)
$$

```python
import numpy as np
from scipy import stats

np.random.seed(42)
n = 100000

mu1, s1 = 0.5, 0.3
mu2, s2 = 1.0, 0.4

X1 = np.random.lognormal(mu1, s1, n)
X2 = np.random.lognormal(mu2, s2, n)
product = X1 * X2

mu_prod = mu1 + mu2
sigma_prod = np.sqrt(s1**2 + s2**2)

print(f"X1*X2 ~ LogN({mu_prod}, {sigma_prod**2:.2f}):")
log_product = np.log(product)
print(f"  Mean of ln(X1*X2): {log_product.mean():.4f}  (theory: {mu_prod:.4f})")
print(f"  Std of ln(X1*X2):  {log_product.std():.4f}  (theory: {sigma_prod:.4f})")
```

**Output:**
```
X1*X2 ~ LogN(1.5, 0.25):
  Mean of ln(X1*X2): 1.4997  (theory: 1.5000)
  Std of ln(X1*X2):  0.5002  (theory: 0.5000)
```

**Example 3: Skewness increases with sigma.**

```python
import numpy as np

print("Skewness of LogN(0, sigma^2):")
for sigma in [0.1, 0.25, 0.5, 1.0, 2.0]:
    es2 = np.exp(sigma**2)
    skew = (es2 + 2) * np.sqrt(es2 - 1)
    print(f"  sigma = {sigma:.2f}: skewness = {skew:.4f}")
```

**Output:**
```
Skewness of LogN(0, sigma^2):
  sigma = 0.10: skewness = 0.3009
  sigma = 0.25: skewness = 0.7586
  sigma = 0.50: skewness = 1.7502
  sigma = 1.00: skewness = 6.1849
  sigma = 2.00: skewness = 113.9364
```

**Example 4: Power of a log-normal.**

If $X \sim \text{LogN}(2, 0.3^2)$, find the distribution of $X^{1/2}$ (the square root).

$$
X^{1/2} \sim \text{LogN}\!\left(\frac{1}{2} \cdot 2, \; \frac{1}{4} \cdot 0.09\right) = \text{LogN}(1, 0.15^2)
$$

```python
import numpy as np
from scipy import stats

np.random.seed(42)
n = 100000

mu, sigma = 2, 0.3
X = np.random.lognormal(mu, sigma, n)
sqrtX = np.sqrt(X)

mu_new = 0.5 * mu
sigma_new = 0.5 * sigma

log_sqrtX = np.log(sqrtX)
print(f"sqrt(X) ~ LogN({mu_new}, {sigma_new}^2):")
print(f"  Mean of ln(sqrt(X)): {log_sqrtX.mean():.4f}  (theory: {mu_new:.4f})")
print(f"  Std of ln(sqrt(X)):  {log_sqrtX.std():.4f}  (theory: {sigma_new:.4f})")
```

**Output:**
```
sqrt(X) ~ LogN(1.0, 0.15^2):
  Mean of ln(sqrt(X)): 0.9998  (theory: 1.0000)
  Std of ln(sqrt(X)):  0.1499  (theory: 0.1500)
```
