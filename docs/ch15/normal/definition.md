# Normal Distribution Definition

## PDF of N(mu, sigma^2)

The **normal distribution** (or Gaussian distribution) with mean $\mu$ and variance $\sigma^2$ has PDF:

$$f(x) = \frac{1}{\sqrt{2\pi\sigma^2}} \, e^{-\frac{(x - \mu)^2}{2\sigma^2}}, \quad -\infty < x < \infty$$

### Parameters

| Parameter | Meaning |
|-----------|---------|
| $\mu$ | Mean (center of the bell curve) |
| $\sigma^2$ | Variance (controls the spread) |
| $\sigma$ | Standard deviation |

### Intuition

The normal distribution arises naturally from the **Central Limit Theorem**: if you flip a $p$-coin $n$ times, record the number of heads, standardize it, then as $n \to \infty$ the standardized count converges to $N(0, 1)$.

### Effect of Parameters

- Changing $\mu$ **shifts** the bell curve left or right without changing its shape.
- Increasing $\sigma$ makes the curve **wider and shorter** (more spread out).
- Decreasing $\sigma$ makes the curve **narrower and taller** (more concentrated).

## Standard Normal Distribution N(0, 1)

The **standard normal** has $\mu = 0$ and $\sigma = 1$:

$$\phi(x) = \frac{1}{\sqrt{2\pi}} \, e^{-x^2/2}$$

### Verification of Properties

**Total mass equals 1:**

Let $I = \int_{-\infty}^{\infty} e^{-x^2/2}\,dx$. Then:

$$I^2 = \left(\int_{-\infty}^{\infty} e^{-x^2/2}\,dx\right)\left(\int_{-\infty}^{\infty} e^{-y^2/2}\,dy\right) = \int_0^{2\pi}\int_0^{\infty} e^{-r^2/2}\,r\,dr\,d\theta = 2\pi\left[-e^{-r^2/2}\right]_0^{\infty} = 2\pi$$

Therefore $I = \sqrt{2\pi}$, confirming $\int_{-\infty}^{\infty} \frac{1}{\sqrt{2\pi}} e^{-x^2/2}\,dx = 1$.

**Mean equals 0:**

The integrand $x \cdot e^{-x^2/2}$ is an **odd function**, so:

$$\frac{1}{\sqrt{2\pi}} \int_{-\infty}^{\infty} x \, e^{-x^2/2}\,dx = 0$$

**Variance equals 1:**

By integration by parts with $u = x$ and $dv = -e^{-x^2/2}\,d(-x) = (e^{-x^2/2})'dx$:

$$\frac{1}{\sqrt{2\pi}} \int_{-\infty}^{\infty} x^2 e^{-x^2/2}\,dx = \frac{1}{\sqrt{2\pi}} \left(\left[-x \, e^{-x^2/2}\right]_{-\infty}^{\infty} + \int_{-\infty}^{\infty} e^{-x^2/2}\,dx\right) = 0 + 1 = 1$$

## CDF of the Standard Normal

$$\Phi(x) = \int_{-\infty}^{x} \frac{1}{\sqrt{2\pi}} e^{-s^2/2}\,ds$$

There is no closed-form expression; values are computed numerically.

### Key Properties

| Property | Formula |
|----------|---------|
| $P(a \leq Z \leq b)$ | $\Phi(b) - \Phi(a)$ |
| Symmetry | $P(Z \leq -x) = P(Z \geq x) = 1 - \Phi(x)$ |
| Complement | $P(Z \geq x) = 1 - \Phi(x)$ |
| Median | $P(Z \leq 0) = P(Z \geq 0) = 0.5$ |

### Example

$$P(-1 \leq Z \leq 2) = \Phi(2) - \Phi(-1) = 0.9772 - 0.1587 = 0.8186$$

## Integration Trick

To evaluate integrals of the form $\int_{-\infty}^{\infty} e^{-x^2 + bx + c}\,dx$, complete the square and recognize the normal PDF.

**Example:** Compute $\int_{-\infty}^{\infty} e^{-x^2 - 2x}\,dx$.

Complete the square: $-x^2 - 2x = -(x^2 + 2x + 1) + 1 = -(x+1)^2 + 1$

$$\int_{-\infty}^{\infty} e^{-x^2 - 2x}\,dx = e \int_{-\infty}^{\infty} e^{-(x+1)^2}\,dx = e \cdot \sqrt{\pi}$$

since $\int_{-\infty}^{\infty} e^{-u^2}\,du = \sqrt{\pi}$ (substituting $u = x + 1$).

## Python Implementation

```python
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

# CDF example
z1, z2 = -1, 2
prob = stats.norm.cdf(z2) - stats.norm.cdf(z1)
print(f"P(-1 ≤ Z ≤ 2) = Φ(2) - Φ(-1) = {stats.norm.cdf(z2):.4f} - {stats.norm.cdf(z1):.4f} = {prob:.4f}")

# Quantile example
q_alpha = stats.norm.ppf(0.975)
print(f"z_0.975 = {q_alpha:.4f}")

# Quantile of N(mu, sigma^2)
mu, sigma = 10, 3
q = mu + sigma * q_alpha
print(f"0.975 quantile of N({mu}, {sigma**2}) = {mu} + {sigma} × {q_alpha:.4f} = {q:.4f}")
```

**Output:**
```
P(-1 ≤ Z ≤ 2) = Φ(2) - Φ(-1) = 0.9772 - 0.1587 = 0.8186
z_0.975 = 1.9600
0.975 quantile of N(10, 9) = 10 + 3 × 1.9600 = 15.8800
```
