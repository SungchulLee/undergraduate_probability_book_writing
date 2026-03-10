# Normal Distribution Definition

The normal (Gaussian) distribution is the most important continuous distribution in probability and statistics, arising naturally from the Central Limit Theorem and serving as the foundation for statistical inference.

## Definition

A continuous random variable $X$ has the **normal distribution** with mean $\mu$ and variance $\sigma^2$, written $X \sim N(\mu, \sigma^2)$, if its PDF is:

$$
f(x) = \frac{1}{\sqrt{2\pi\sigma^2}} \, e^{-\frac{(x - \mu)^2}{2\sigma^2}}, \quad -\infty < x < \infty
$$

The parameters are:

| Parameter | Meaning |
|-----------|---------|
| $\mu \in \mathbb{R}$ | Mean (center of the bell curve) |
| $\sigma^2 > 0$ | Variance (controls the spread) |
| $\sigma > 0$ | Standard deviation |

The **standard normal** distribution $N(0, 1)$ has $\mu = 0$ and $\sigma = 1$, with PDF:

$$
\phi(z) = \frac{1}{\sqrt{2\pi}} \, e^{-z^2/2}
$$

and CDF:

$$
\Phi(z) = \int_{-\infty}^{z} \frac{1}{\sqrt{2\pi}} e^{-s^2/2}\,ds
$$

The CDF $\Phi$ has no closed-form expression and must be computed numerically or looked up in a table.

## Explanation

### Why the PDF integrates to 1

The verification that the normal PDF is a valid density requires a clever polar-coordinates trick. Let $I = \int_{-\infty}^{\infty} e^{-x^2/2}\,dx$. Then:

$$
I^2 = \left(\int_{-\infty}^{\infty} e^{-x^2/2}\,dx\right)\left(\int_{-\infty}^{\infty} e^{-y^2/2}\,dy\right) = \int_0^{2\pi}\int_0^{\infty} e^{-r^2/2}\,r\,dr\,d\theta = 2\pi\left[-e^{-r^2/2}\right]_0^{\infty} = 2\pi
$$

Therefore $I = \sqrt{2\pi}$, confirming that $\int_{-\infty}^{\infty} \frac{1}{\sqrt{2\pi}} e^{-x^2/2}\,dx = 1$.

### Mean and variance of the standard normal

**Mean equals 0.** The integrand $x \cdot e^{-x^2/2}$ is an odd function, so:

$$
E[Z] = \frac{1}{\sqrt{2\pi}} \int_{-\infty}^{\infty} x \, e^{-x^2/2}\,dx = 0
$$

**Variance equals 1.** By integration by parts with $u = x$ and $dv = x e^{-x^2/2}\,dx$:

$$
E[Z^2] = \frac{1}{\sqrt{2\pi}} \int_{-\infty}^{\infty} x^2 e^{-x^2/2}\,dx = \frac{1}{\sqrt{2\pi}} \left(\left[-x \, e^{-x^2/2}\right]_{-\infty}^{\infty} + \int_{-\infty}^{\infty} e^{-x^2/2}\,dx\right) = 0 + 1 = 1
$$

### Effect of the parameters

- Changing $\mu$ **shifts** the bell curve left or right without changing its shape.
- Increasing $\sigma$ makes the curve **wider and shorter** (more spread out).
- Decreasing $\sigma$ makes the curve **narrower and taller** (more concentrated).
- The bell curve is always symmetric about $\mu$.
- The inflection points occur at $x = \mu \pm \sigma$.

### The 68-95-99.7 rule

For any $X \sim N(\mu, \sigma^2)$:

| Interval | Probability |
|----------|-------------|
| $\mu \pm \sigma$ | $\approx 68.3\%$ |
| $\mu \pm 2\sigma$ | $\approx 95.4\%$ |
| $\mu \pm 3\sigma$ | $\approx 99.7\%$ |

### CDF properties

| Property | Formula |
|----------|---------|
| Interval probability | $P(a \leq Z \leq b) = \Phi(b) - \Phi(a)$ |
| Symmetry | $\Phi(-z) = 1 - \Phi(z)$ |
| Right tail | $P(Z \geq z) = 1 - \Phi(z)$ |
| Median | $\Phi(0) = 0.5$ |

### Why the normal distribution is so important

The normal distribution arises naturally from the **Central Limit Theorem**: the sum of many independent random variables, regardless of their individual distributions, converges to a normal distribution. This explains why bell curves appear throughout nature -- heights, measurement errors, test scores, and thermal fluctuations all follow approximately normal distributions because they result from the aggregate effect of many small independent factors.

### Integration trick

To evaluate integrals of the form $\int_{-\infty}^{\infty} e^{-ax^2 + bx + c}\,dx$, complete the square in the exponent and recognize the normal PDF. For example:

$$
\int_{-\infty}^{\infty} e^{-x^2 - 2x}\,dx = e \int_{-\infty}^{\infty} e^{-(x+1)^2}\,dx = e \cdot \sqrt{\pi}
$$

since $-x^2 - 2x = -(x+1)^2 + 1$ and $\int_{-\infty}^{\infty} e^{-u^2}\,du = \sqrt{\pi}$.

## Examples

**Example 1: CDF calculations with the standard normal.**

Compute $P(-1 \leq Z \leq 2)$ where $Z \sim N(0, 1)$.

$$
P(-1 \leq Z \leq 2) = \Phi(2) - \Phi(-1) = \Phi(2) - (1 - \Phi(1)) = 0.9772 - 0.1587 = 0.8186
$$

```python
from scipy import stats

# Interval probability for standard normal
z1, z2 = -1, 2
prob = stats.norm.cdf(z2) - stats.norm.cdf(z1)
print(f"P(-1 <= Z <= 2) = Phi(2) - Phi(-1) = {stats.norm.cdf(z2):.4f} - {stats.norm.cdf(z1):.4f} = {prob:.4f}")
```

**Output:**
```
P(-1 <= Z <= 2) = Phi(2) - Phi(-1) = 0.9772 - 0.1587 = 0.8186
```

**Example 2: Verifying the 68-95-99.7 rule.**

```python
from scipy import stats

for k in [1, 2, 3]:
    prob = stats.norm.cdf(k) - stats.norm.cdf(-k)
    print(f"P(-{k} <= Z <= {k}) = {prob:.4f}  ({100*prob:.1f}%)")
```

**Output:**
```
P(-1 <= Z <= 1) = 0.6827  (68.3%)
P(-2 <= Z <= 2) = 0.9545  (95.4%)
P(-3 <= Z <= 3) = 0.9973  (99.7%)
```

**Example 3: General normal probability.**

Suppose exam scores follow $X \sim N(75, 10^2)$. Find the probability a student scores between 60 and 90.

$$
P(60 \leq X \leq 90) = P\!\left(\frac{60 - 75}{10} \leq Z \leq \frac{90 - 75}{10}\right) = P(-1.5 \leq Z \leq 1.5) = \Phi(1.5) - \Phi(-1.5)
$$

```python
from scipy import stats

mu, sigma = 75, 10
p = stats.norm.cdf(90, loc=mu, scale=sigma) - stats.norm.cdf(60, loc=mu, scale=sigma)
print(f"P(60 <= X <= 90) = {p:.4f}")

# Equivalently via standardization
z_low = (60 - mu) / sigma
z_high = (90 - mu) / sigma
p2 = stats.norm.cdf(z_high) - stats.norm.cdf(z_low)
print(f"P({z_low} <= Z <= {z_high}) = {p2:.4f}")
```

**Output:**
```
P(60 <= X <= 90) = 0.8664
P(-1.5 <= Z <= 1.5) = 0.8664
```

**Example 4: Quantile calculation.**

Find the value $z$ such that $P(Z \leq z) = 0.975$.

```python
from scipy import stats

z_975 = stats.norm.ppf(0.975)
print(f"z_0.975 = {z_975:.4f}")

# Quantile of a general normal
mu, sigma = 10, 3
q = mu + sigma * z_975
print(f"0.975 quantile of N({mu}, {sigma**2}) = {mu} + {sigma} * {z_975:.4f} = {q:.4f}")
```

**Output:**
```
z_0.975 = 1.9600
0.975 quantile of N(10, 9) = 10 + 3 * 1.9600 = 15.8800
```
