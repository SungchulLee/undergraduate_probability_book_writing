# Confidence Intervals (Preview)

The CLT allows construction of confidence intervals for the population mean — inverting the normal approximation to bracket $\mu$ with a prescribed probability.

## Definition

A **$(1-\alpha)$ confidence interval** for $\mu$ based on $n$ iid observations with known $\sigma$ is:

$$
\bar{X}_n \pm z_{\alpha/2} \frac{\sigma}{\sqrt{n}}
$$

where $z_{\alpha/2}$ satisfies $\Phi(z_{\alpha/2}) = 1 - \alpha/2$.

| Confidence level | $z_{\alpha/2}$ |
|:---:|:---:|
| 90% | 1.645 |
| 95% | 1.960 |
| 99% | 2.576 |

## Explanation

### Derivation

The CLT gives $\frac{\bar{X}_n - \mu}{\sigma/\sqrt{n}} \approx N(0,1)$. Inverting:

$$
P\!\left(\bar{X}_n - z_{\alpha/2}\frac{\sigma}{\sqrt{n}} \le \mu \le \bar{X}_n + z_{\alpha/2}\frac{\sigma}{\sqrt{n}}\right) \approx 1 - \alpha
$$

### Sample Size Formula

To achieve margin of error $\varepsilon$ with confidence $1-\alpha$:

$$
n \ge \left(\frac{z_{\alpha/2} \cdot \sigma}{\varepsilon}\right)^2
$$

### Limitations

This formula assumes $\sigma$ is known. When $\sigma$ is estimated from data, the Student $t$-distribution (Chapter 19) replaces the normal, yielding wider intervals for small $n$.

## Examples

**Example.** Measurements have $\sigma = 2$. How many are needed for a 95% CI with margin $\pm 0.5$?

$$
n \ge \left(\frac{1.96 \times 2}{0.5}\right)^2 = 61.47 \implies n \ge 62
$$

```python
import numpy as np
from scipy import stats

sigma = 2.0
epsilon = 0.5
alpha = 0.05

z = stats.norm.ppf(1 - alpha / 2)
n_min = (z * sigma / epsilon) ** 2
print(f"z = {z:.4f}")
print(f"Minimum n = {n_min:.2f}, so need n ≥ {int(np.ceil(n_min))}")
```
