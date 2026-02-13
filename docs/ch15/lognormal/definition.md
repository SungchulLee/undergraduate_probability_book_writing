# Log-Normal Distribution

## Definition

A random variable $X$ has a **Log-Normal distribution** with parameters $\mu$ and $\sigma^2$ if:

$$Y \sim N(\mu, \sigma^2) \quad \Longleftrightarrow \quad X = e^Y \sim \text{Log-N}(\mu, \sigma^2)$$

Equivalently, $X$ is Log-Normal if and only if $\log X$ is normal.

## PDF Derivation

### Via CDF Method

$$P(X \leq x) = P(e^Y \leq x) = P(Y \leq \log x) = \int_{-\infty}^{\log x} \frac{1}{\sqrt{2\pi\sigma^2}} e^{-\frac{(s - \mu)^2}{2\sigma^2}}\, ds$$

Differentiating with respect to $x$:

$$f_X(x) = \frac{1}{\sqrt{2\pi\sigma^2}} e^{-\frac{(\log x - \mu)^2}{2\sigma^2}} \cdot \frac{1}{x}, \quad x > 0$$

### Via Jacobian Method

With $y = \log x$, so $dy/dx = 1/x$:

$$f_X(x) = f_Y(y) \left|\frac{dy}{dx}\right| = \frac{1}{\sqrt{2\pi\sigma^2}} e^{-\frac{(\log x - \mu)^2}{2\sigma^2}} \cdot \frac{1}{x}, \quad x > 0$$

## PDF, Mean, and Variance

| Property | Formula |
|----------|---------|
| PDF | $\frac{1}{x\sqrt{2\pi\sigma^2}} \exp\!\left(-\frac{(\log x - \mu)^2}{2\sigma^2}\right)$ for $x > 0$ |
| Mean | $e^{\mu + \sigma^2/2}$ |
| Variance | $(e^{\sigma^2} - 1) \cdot e^{2\mu + \sigma^2}$ |
| Median | $e^{\mu}$ |
| Mode | $e^{\mu - \sigma^2}$ |

!!! note "Parameter Interpretation"
    The parameters $\mu$ and $\sigma^2$ are the mean and variance of the **log** of $X$, not of $X$ itself. The mean of $X$ is $e^{\mu + \sigma^2/2}$, which is always greater than the median $e^{\mu}$, reflecting the right skewness.

## Shape

The Log-Normal distribution is:

- Supported on $(0, \infty)$
- Right-skewed (skewness increases with $\sigma^2$)
- Has a heavier right tail than the normal
- Commonly used to model stock prices, income distributions, and particle sizes

## Python Implementation

```python
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

x = np.linspace(0.01, 10, 500)

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Varying sigma
ax = axes[0]
mu = 0
for sigma in [0.25, 0.5, 1.0, 1.5]:
    ax.plot(x, stats.lognorm.pdf(x, s=sigma, scale=np.exp(mu)),
            label=f'$\\sigma = {sigma}$')
ax.set_title(f'Log-Normal PDF ($\\mu = {mu}$, varying $\\sigma$)')
ax.set_xlabel('$x$'); ax.set_ylabel('$f(x)$')
ax.set_ylim(0, 1.5); ax.legend()

# Mean, median, mode comparison
ax = axes[1]
mu, sigma = 0, 1
ax.plot(x, stats.lognorm.pdf(x, s=sigma, scale=np.exp(mu)), 'b-', lw=2)
mean_val = np.exp(mu + sigma**2 / 2)
median_val = np.exp(mu)
mode_val = np.exp(mu - sigma**2)
ax.axvline(mode_val, color='g', ls='--', label=f'Mode = {mode_val:.2f}')
ax.axvline(median_val, color='orange', ls='--', label=f'Median = {median_val:.2f}')
ax.axvline(mean_val, color='r', ls='--', label=f'Mean = {mean_val:.2f}')
ax.set_title('Log-N(0, 1): Mode < Median < Mean')
ax.set_xlabel('$x$'); ax.set_ylabel('$f(x)$')
ax.legend()

plt.tight_layout()
plt.show()
```
