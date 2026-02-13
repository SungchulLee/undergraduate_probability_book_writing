# Distribution of the Studentized Sample Mean

## Motivation

When $\sigma$ is known, $\frac{\bar{X} - \mu}{\sigma/\sqrt{n}} \sim N(0,1)$ provides an exact pivot for inference about $\mu$.

When $\sigma$ is **unknown**, we replace it with $S$ and obtain the **studentized sample mean**:

$$T = \frac{\bar{X} - \mu}{S / \sqrt{n}}$$

## Derivation

### Step 1: Rewrite as a Ratio

$$T = \frac{\bar{X} - \mu}{S/\sqrt{n}} = \frac{\bar{X} - \mu}{\sigma/\sqrt{n}} \cdot \frac{\sigma}{S} = \frac{\bar{X} - \mu}{\sigma/\sqrt{n}} \bigg/ \frac{S}{\sigma}$$

### Step 2: Identify the Components

The numerator:

$$\frac{\bar{X} - \mu}{\sigma/\sqrt{n}} \sim N(0, 1)$$

The denominator involves the sample variance. Since $\frac{(n-1)S^2}{\sigma^2} \sim \chi^2_{n-1}$:

$$\frac{S}{\sigma} = \sqrt{\frac{S^2}{\sigma^2}} = \sqrt{\frac{(n-1)S^2/\sigma^2}{n-1}} = \sqrt{\frac{\chi^2_{n-1}}{n-1}}$$

### Step 3: Apply Independence

By the key fact (Section 19.2), $\bar{X}$ and $S^2$ are independent. Therefore the numerator $N(0,1)$ and the denominator $\sqrt{\chi^2_{n-1}/(n-1)}$ are independent.

### Step 4: Conclude

$$T = \frac{\bar{X} - \mu}{S/\sqrt{n}} = \frac{N(0,1)}{\sqrt{\chi^2_{n-1}/(n-1)}} \sim t_{n-1}$$

## Summary

$$\boxed{\frac{\bar{X} - \mu}{S/\sqrt{n}} \sim t_{n-1}}$$

This is the foundational result for:

- **$t$-confidence intervals** for $\mu$: $\bar{X} \pm t_{\alpha/2, \, n-1} \cdot \frac{S}{\sqrt{n}}$
- **One-sample $t$-tests** for $H_0: \mu = \mu_0$
- **Two-sample $t$-tests** for comparing means

## Python Verification

```python
import numpy as np
from scipy import stats

np.random.seed(42)
mu, sigma, n = 10, 3, 8
n_sim = 100_000

t_samples = []
for _ in range(n_sim):
    x = np.random.normal(mu, sigma, n)
    x_bar = x.mean()
    s = x.std(ddof=1)
    t_samples.append((x_bar - mu) / (s / np.sqrt(n)))

t_samples = np.array(t_samples)

print(f"Simulated mean: {t_samples.mean():.4f}  (theory: 0)")
print(f"Simulated var:  {t_samples.var():.4f}  (theory: {(n-1)/(n-3):.4f})")

# KS test against t(n-1)
stat, pval = stats.kstest(t_samples, 't', args=(n-1,))
print(f"KS test p-value: {pval:.4f}")
```

**Output:**
```
Simulated mean: 0.0011  (theory: 0)
Simulated var:  1.3991  (theory: 1.4000)
KS test p-value: 0.5123
```
