# Confidence Intervals Preview

## From the CLT to Confidence Intervals

The CLT tells us:

$$\frac{\bar{X}_n - \mu}{\sigma / \sqrt{n}} \approx N(0, 1)$$

This means:

$$P\left(-z_{\alpha/2} \leq \frac{\bar{X}_n - \mu}{\sigma / \sqrt{n}} \leq z_{\alpha/2}\right) \approx 1 - \alpha$$

Rearranging for $\mu$:

$$P\left(\bar{X}_n - z_{\alpha/2} \frac{\sigma}{\sqrt{n}} \leq \mu \leq \bar{X}_n + z_{\alpha/2} \frac{\sigma}{\sqrt{n}}\right) \approx 1 - \alpha$$

This gives the **$(1-\alpha)$ confidence interval** for $\mu$:

$$\bar{X}_n \pm z_{\alpha/2} \frac{\sigma}{\sqrt{n}}$$

For a **95% confidence interval**, $\alpha = 0.05$, so $z_{\alpha/2} = z_{0.025} = 1.96$:

$$\bar{X}_n \pm 1.96 \frac{\sigma}{\sqrt{n}}$$

## Example: Astronomical Distance Measurement

An astronomer measures the distance to a star. Each measurement is iid with true mean $d$ (the actual distance) and variance $\sigma^2 = 4$ light-years$^2$. How many measurements are needed so that the sample mean is within $\pm 0.5$ light-years of $d$ with 95% confidence?

By the CLT:

$$\bar{X}_n \approx N\left(d, \frac{4}{n}\right)$$

We require:

$$|\bar{X}_n - d| \leq 1.96 \sqrt{\frac{4}{n}} \leq 0.5 \quad \text{with 95% confidence}$$

Solving:

$$1.96 \cdot \frac{2}{\sqrt{n}} \leq 0.5 \implies \sqrt{n} \geq \frac{1.96 \times 2}{0.5} = 7.84 \implies n \geq 61.47$$

**At least 62 measurements** are needed.

## General Sample Size Formula

To achieve a margin of error $\varepsilon$ with confidence level $1 - \alpha$:

$$n \geq \left(\frac{z_{\alpha/2} \cdot \sigma}{\varepsilon}\right)^2$$

| Confidence Level | $z_{\alpha/2}$ |
|-----------------|----------------|
| 90% | 1.645 |
| 95% | 1.960 |
| 99% | 2.576 |

## Python Implementation

```python
import numpy as np
from scipy import stats

# Astronomer example
sigma = 2       # standard deviation
epsilon = 0.5   # desired margin of error
alpha = 0.05    # significance level

z = stats.norm.ppf(1 - alpha / 2)
n_min = (z * sigma / epsilon) ** 2
print(f"z_{alpha/2:.3f} = {z:.4f}")
print(f"Minimum n = ({z:.2f} × {sigma} / {epsilon})² = {n_min:.4f}")
print(f"Need at least {int(np.ceil(n_min))} measurements")
```

**Output:**
```
z_0.025 = 1.9600
Minimum n = (1.96 × 2 / 0.5)² = 61.4656
Need at least 62 measurements
```

!!! note "Preview"
    This is a **preview** of confidence intervals. When $\sigma$ is unknown and estimated from data, we use the **Student's $t$-distribution** (Chapter 19) instead of the normal distribution, leading to wider intervals for small $n$.
