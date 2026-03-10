# Standardization and Reverse Standardization


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

## Standardization

If $X$ has mean $\mu$ and standard deviation $\sigma$, the **standardized** version of $X$ is:

$$Z = \frac{X - \mu}{\sigma}$$

This transformation yields:

- $E[Z] = 0$
- $\text{SD}(Z) = 1$

If $X$ is **normal**, then $Z \sim N(0, 1)$.

### Why Standardize?

Standardization converts any random variable to a common scale, enabling comparison across different distributions. For the normal distribution specifically, it reduces every $N(\mu, \sigma^2)$ problem to a standard normal $N(0,1)$ table lookup.

## Reverse Standardization

If $Z$ has mean $0$ and standard deviation $1$, then:

$$X = \mu + \sigma Z$$

has mean $\mu$ and standard deviation $\sigma$.

If $Z \sim N(0, 1)$, then $X \sim N(\mu, \sigma^2)$.

## Summary

| Direction | Formula | Result |
|-----------|---------|--------|
| Standardize | $Z = \frac{X - \mu}{\sigma}$ | Mean $0$, SD $1$ |
| Reverse standardize | $X = \mu + \sigma Z$ | Mean $\mu$, SD $\sigma$ |

## Quantile Connection

The $\alpha$-quantile $q_\alpha$ of $N(\mu, \sigma^2)$ can be expressed in terms of the $\alpha$-quantile $z_\alpha$ of $N(0,1)$:

$$q_\alpha = \mu + \sigma \cdot z_\alpha$$

This follows directly from reverse standardization applied to the quantile.

## Python Implementation

```python
from scipy import stats

# Standardization example
mu, sigma = 70, 10
x = 85

z = (x - mu) / sigma
print(f"X = {x} with μ={mu}, σ={sigma}")
print(f"Standardized: Z = {z}")
print(f"P(X ≤ {x}) = P(Z ≤ {z}) = {stats.norm.cdf(z):.4f}")

# Reverse standardization: find x such that P(X ≤ x) = 0.95
z_95 = stats.norm.ppf(0.95)
x_95 = mu + sigma * z_95
print(f"\n95th percentile of N({mu},{sigma}²):")
print(f"z_0.95 = {z_95:.4f}")
print(f"q_0.95 = {mu} + {sigma} × {z_95:.4f} = {x_95:.4f}")
```

**Output:**
```
X = 85 with μ=70, σ=10
Standardized: Z = 1.5
P(X ≤ 85) = P(Z ≤ 1.5) = 0.9332

95th percentile of N(70,10²):
z_0.95 = 1.6449
q_0.95 = 70 + 10 × 1.6449 = 86.4485
```
