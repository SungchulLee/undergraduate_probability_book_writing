# Standard Deviation

The standard deviation is the square root of the variance — it measures spread in the same units as the random variable itself.

## Definition

$$
\text{SD}(X) = \sigma_X = \sqrt{\text{Var}(X)}
$$

## Explanation

### Why Take the Square Root

Variance has squared units (if $X$ is in dollars, $\text{Var}(X)$ is in dollars$^2$). The standard deviation restores the original units, making it directly comparable to the mean and to observed values.

### Chebyshev's Bound

For any distribution, at least $1 - 1/k^2$ of the probability lies within $k$ standard deviations of the mean:

$$
P(|X - \mu| \ge k\sigma) \le \frac{1}{k^2}
$$

### Normal Distribution Rule of Thumb

| Range | Normal probability |
|:---:|:---:|
| $\mu \pm 1\sigma$ | $68.3\%$ |
| $\mu \pm 2\sigma$ | $95.4\%$ |
| $\mu \pm 3\sigma$ | $99.7\%$ |

### Common Standard Deviations

| Distribution | $\text{SD}(X)$ |
|:-------------|:----------------|
| $\text{Bern}(p)$ | $\sqrt{p(1-p)}$ |
| $\text{Bin}(n,p)$ | $\sqrt{np(1-p)}$ |
| $\text{Poi}(\lambda)$ | $\sqrt{\lambda}$ |
| $\text{Geo}(p)$ | $\sqrt{1-p}/p$ |
| $\text{Uniform}(a,b)$ | $(b-a)/\sqrt{12}$ |
| $\text{Exp}(\lambda)$ | $1/\lambda$ |
| $N(\mu,\sigma^2)$ | $\sigma$ |

## Examples

**Example.** $X \sim \text{Bin}(100, 0.3)$: $E[X] = 30$, $\text{SD}(X) = \sqrt{21} \approx 4.58$.

By Chebyshev: $P(|X - 30| \ge 14) \le 21/196 \approx 0.107$.

By normal approximation: $P(|X - 30| \ge 14) \approx P(|Z| \ge 3.06) \approx 0.002$.

```python
import numpy as np

n, p = 100, 0.3
sd = np.sqrt(n * p * (1-p))
print(f"Bin({n},{p}): SD = {sd:.4f}")

# Chebyshev bound for k=3
k = 3
print(f"Chebyshev P(|X-mu| >= {k}*SD): <= {1/k**2:.4f}")

# MC verification
np.random.seed(42)
samples = np.random.binomial(n, p, 1_000_000)
print(f"MC SD = {samples.std():.4f}")
print(f"MC P(|X-30| >= 3*SD) = {np.mean(np.abs(samples - 30) >= 3*sd):.4f}")
```
