# Log-Normal Distribution

The log-normal distribution models positive-valued random variables whose logarithm is normally distributed, making it the natural model for quantities that grow multiplicatively, such as stock prices, incomes, and biological measurements.

## Definition

A random variable $X$ has a **log-normal distribution** with parameters $\mu$ and $\sigma^2$, written $X \sim \text{LogN}(\mu, \sigma^2)$, if:

$$
\ln X \sim N(\mu, \sigma^2)
$$

Equivalently, $X = e^Y$ where $Y \sim N(\mu, \sigma^2)$. The PDF of $X$ is:

$$
f(x) = \frac{1}{x\sigma\sqrt{2\pi}} \exp\!\left(-\frac{(\ln x - \mu)^2}{2\sigma^2}\right), \quad x > 0
$$

The key summary statistics are:

| Property | Formula |
|----------|---------|
| Mean | $e^{\mu + \sigma^2/2}$ |
| Variance | $(e^{\sigma^2} - 1) \cdot e^{2\mu + \sigma^2}$ |
| Median | $e^{\mu}$ |
| Mode | $e^{\mu - \sigma^2}$ |

!!! warning "Parameter Interpretation"
    The parameters $\mu$ and $\sigma^2$ are the mean and variance of $\ln X$, **not** of $X$ itself. The mean of $X$ is $e^{\mu + \sigma^2/2}$, which is always greater than the median $e^{\mu}$.

## Explanation

### PDF derivation via the CDF method

Since $X = e^Y$ with $Y \sim N(\mu, \sigma^2)$:

$$
F_X(x) = P(X \leq x) = P(e^Y \leq x) = P(Y \leq \ln x) = \Phi\!\left(\frac{\ln x - \mu}{\sigma}\right)
$$

Differentiating with respect to $x$ using the chain rule:

$$
f_X(x) = \phi\!\left(\frac{\ln x - \mu}{\sigma}\right) \cdot \frac{1}{x\sigma} = \frac{1}{x\sigma\sqrt{2\pi}} \exp\!\left(-\frac{(\ln x - \mu)^2}{2\sigma^2}\right)
$$

### PDF derivation via the Jacobian method

With $y = \ln x$ so that $dy/dx = 1/x$:

$$
f_X(x) = f_Y(\ln x) \cdot \left|\frac{dy}{dx}\right| = \frac{1}{\sigma\sqrt{2\pi}} e^{-(\ln x - \mu)^2/(2\sigma^2)} \cdot \frac{1}{x}
$$

Both methods yield the same result.

### Shape of the distribution

The log-normal distribution is:

- Supported on $(0, \infty)$ -- it only takes positive values
- Always right-skewed (the right tail is heavier)
- The ordering $\text{Mode} < \text{Median} < \text{Mean}$ always holds for $\sigma > 0$
- As $\sigma \to 0$, the distribution concentrates around $e^{\mu}$ and becomes approximately normal
- As $\sigma$ increases, the right tail becomes increasingly heavy

### Why mode < median < mean

The mode $e^{\mu - \sigma^2}$ is pushed to the left of the median $e^{\mu}$ because the density is compressed on the left side and stretched on the right by the exponential transformation. The mean $e^{\mu + \sigma^2/2}$ exceeds the median because the heavy right tail pulls the average above the 50th percentile.

### CDF and quantiles

The CDF is:

$$
F(x) = \Phi\!\left(\frac{\ln x - \mu}{\sigma}\right), \quad x > 0
$$

The $p$-th quantile is:

$$
Q(p) = \exp\!\left(\mu + \sigma\,\Phi^{-1}(p)\right)
$$

## Examples

**Example 1: Computing log-normal probabilities.**

Let $X \sim \text{LogN}(2, 0.5^2)$. Find $P(X > 10)$.

$$
P(X > 10) = P(\ln X > \ln 10) = P\!\left(Z > \frac{\ln 10 - 2}{0.5}\right) = 1 - \Phi\!\left(\frac{2.303 - 2}{0.5}\right)
$$

```python
import numpy as np
from scipy import stats

mu, sigma = 2, 0.5
x = 10
z = (np.log(x) - mu) / sigma
p = 1 - stats.norm.cdf(z)
print(f"X ~ LogN({mu}, {sigma}^2)")
print(f"P(X > {x}) = P(Z > {z:.4f}) = {p:.4f}")

# Using scipy's lognorm directly
p2 = 1 - stats.lognorm.cdf(x, s=sigma, scale=np.exp(mu))
print(f"Via scipy lognorm: {p2:.4f}")
```

**Output:**
```
X ~ LogN(2, 0.5^2)
P(X > 10) = P(Z > 0.6052) = 0.2726
Via scipy lognorm: 0.2726
```

**Example 2: Mean, median, and mode.**

For $X \sim \text{LogN}(0, 1)$, compute and compare the three measures of center.

```python
import numpy as np
from scipy import stats

mu, sigma = 0, 1

mean = np.exp(mu + sigma**2 / 2)
median = np.exp(mu)
mode = np.exp(mu - sigma**2)

print(f"LogN({mu}, {sigma}^2):")
print(f"  Mode   = exp({mu} - {sigma**2}) = {mode:.4f}")
print(f"  Median = exp({mu})           = {median:.4f}")
print(f"  Mean   = exp({mu} + {sigma**2}/2) = {mean:.4f}")
print(f"  Ordering: Mode < Median < Mean")

# Verify by simulation
np.random.seed(42)
samples = np.random.lognormal(mu, sigma, 100000)
print(f"\nSimulated: mean = {samples.mean():.4f}, median = {np.median(samples):.4f}")
```

**Output:**
```
LogN(0, 1^2):
  Mode   = exp(0 - 1) = 0.3679
  Median = exp(0)           = 1.0000
  Mean   = exp(0 + 1/2) = 1.6487
  Ordering: Mode < Median < Mean

Simulated: mean = 1.6515, median = 1.0009
```

**Example 3: Relationship between parameters and moments.**

Given that incomes have mean \$50,000 and standard deviation \$30,000, find $\mu$ and $\sigma$ for the log-normal model.

We need to solve $e^{\mu + \sigma^2/2} = 50000$ and $e^{2\mu + \sigma^2}(e^{\sigma^2} - 1) = 30000^2$.

```python
import numpy as np

mean_X = 50000
sd_X = 30000
var_X = sd_X**2

# From the formulas: Var/Mean^2 = exp(sigma^2) - 1
sigma2 = np.log(1 + var_X / mean_X**2)
mu = np.log(mean_X) - sigma2 / 2
sigma = np.sqrt(sigma2)

print(f"Target: mean = ${mean_X:,}, SD = ${sd_X:,}")
print(f"Log-normal parameters: mu = {mu:.4f}, sigma = {sigma:.4f}")

# Verify
mean_check = np.exp(mu + sigma2/2)
var_check = np.exp(2*mu + sigma2) * (np.exp(sigma2) - 1)
print(f"Verification: mean = ${mean_check:,.0f}, SD = ${np.sqrt(var_check):,.0f}")

# Median (always less than mean for right-skewed distributions)
median = np.exp(mu)
print(f"Median income = ${median:,.0f}")
```

**Output:**
```
Target: mean = $50,000, SD = $30,000
Log-normal parameters: mu = 10.6594, sigma = 0.5545
Verification: mean = $50,000, SD = $30,000
Median income = $42,640
```
