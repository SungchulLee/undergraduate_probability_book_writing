# Standard Normal and Z-Scores

## Standard Normal Distribution

The **standard normal distribution** $N(0, 1)$ has PDF:

$$\phi(x) = \frac{1}{\sqrt{2\pi}} e^{-x^2/2}$$

and CDF:

$$\Phi(x) = \int_{-\infty}^{x} \frac{1}{\sqrt{2\pi}} e^{-s^2/2}\,ds$$

The CDF $\Phi$ has no closed-form expression and must be computed numerically.

## CDF Properties

| Property | Formula |
|----------|---------|
| Interval probability | $P(a \leq Z \leq b) = \Phi(b) - \Phi(a)$ |
| Left-tail symmetry | $P(Z \leq -x) = P(Z \geq x) = 1 - \Phi(x)$ |
| Right-tail complement | $P(Z \geq x) = 1 - \Phi(x)$ |
| Median | $P(Z \leq 0) = P(Z \geq 0) = 0.5$ |

## Z-Scores

Any normal random variable $X \sim N(\mu, \sigma^2)$ can be converted to a standard normal via:

$$Z = \frac{X - \mu}{\sigma} \sim N(0, 1)$$

The value $z = (x - \mu)/\sigma$ is called the **Z-score** of $x$. It measures how many standard deviations $x$ is away from the mean.

## CDF of General Normal

For $X \sim N(\mu, \sigma^2)$:

$$P(X \leq x) = P\left(Z \leq \frac{x - \mu}{\sigma}\right) = \Phi\left(\frac{x - \mu}{\sigma}\right)$$

## Quantiles

The $\alpha$-quantile $z_\alpha$ of $N(0,1)$ satisfies $\Phi(z_\alpha) = \alpha$.

For $X \sim N(\mu, \sigma^2)$, the $\alpha$-quantile is:

$$q_\alpha = \mu + \sigma \cdot z_\alpha$$

### Common Quantiles

| $\alpha$ | $z_\alpha$ |
|----------|-----------|
| $0.025$ | $-1.960$ |
| $0.05$ | $-1.645$ |
| $0.10$ | $-1.282$ |
| $0.50$ | $0$ |
| $0.90$ | $1.282$ |
| $0.95$ | $1.645$ |
| $0.975$ | $1.960$ |

## Python Implementation

```python
from scipy import stats

# Interval probability
p = stats.norm.cdf(2) - stats.norm.cdf(-1)
print(f"P(-1 ≤ Z ≤ 2) = {p:.4f}")

# CDF of general normal
mu, sigma = 100, 15
x = 130
z = (x - mu) / sigma
print(f"\nX ~ N({mu}, {sigma}²)")
print(f"P(X ≤ {x}) = Φ({z:.2f}) = {stats.norm.cdf(z):.4f}")

# Quantile
alpha = 0.975
z_alpha = stats.norm.ppf(alpha)
q_alpha = mu + sigma * z_alpha
print(f"\n{alpha} quantile of N({mu}, {sigma}²) = {q_alpha:.2f}")
```

**Output:**
```
P(-1 ≤ Z ≤ 2) = 0.8186

X ~ N(100, 15²)
P(X ≤ 130) = Φ(2.00) = 0.9772

0.975 quantile of N(100, 15²) = 129.40
```
