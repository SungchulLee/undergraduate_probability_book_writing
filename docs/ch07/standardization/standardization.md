# Standardization

Standardizing a random variable centers it at zero and scales it to unit variance, enabling comparison across different distributions.

## Definition

If $X$ has mean $\mu$ and standard deviation $\sigma > 0$, the **standardized** version is

$$
Z = \frac{X - \mu}{\sigma}
$$

with $E[Z] = 0$ and $\text{SD}(Z) = 1$.

**Reverse standardization:** $X = \mu + \sigma Z$.

## Explanation

### Why Standardize

- Converts any distribution to a common scale (mean 0, SD 1)
- For normal variables: $X \sim N(\mu, \sigma^2)$ implies $Z \sim N(0,1)$, reducing every normal problem to a standard normal table
- Quantile connection: the $\alpha$-quantile of $N(\mu, \sigma^2)$ is $q_\alpha = \mu + \sigma z_\alpha$

### Summary

| Direction | Formula | Result |
|:----------|:--------|:-------|
| Standardize | $Z = (X-\mu)/\sigma$ | Mean 0, SD 1 |
| Reverse | $X = \mu + \sigma Z$ | Mean $\mu$, SD $\sigma$ |

## Examples

**Example.** Test scores $\sim N(70, 100)$. What fraction score above 85?

$$
Z = \frac{85 - 70}{10} = 1.5
$$

$$
P(X > 85) = P(Z > 1.5) = 1 - \Phi(1.5) \approx 0.067
$$

```python
from scipy import stats

mu, sigma = 70, 10
x = 85
z = (x - mu) / sigma
print(f"Z = {z}, P(X > {x}) = {1 - stats.norm.cdf(z):.4f}")

# 95th percentile
z95 = stats.norm.ppf(0.95)
q95 = mu + sigma * z95
print(f"95th percentile = {q95:.2f}")
```
