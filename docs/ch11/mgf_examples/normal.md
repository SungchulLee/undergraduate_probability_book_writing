# MGF of Normal


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

## MGF of N(mu, sigma^2)

$$M_{N(\mu, \sigma^2)}(t) = e^{\mu t + \frac{1}{2}\sigma^2 t^2}$$

### Derivation

$$M_X(t) = \int_{-\infty}^{\infty} e^{tx} \cdot \frac{1}{\sqrt{2\pi\sigma^2}} e^{-\frac{(x-\mu)^2}{2\sigma^2}} \, dx$$

Complete the square in the exponent. The exponent of the integrand is:

$$tx - \frac{(x - \mu)^2}{2\sigma^2} = -\frac{1}{2\sigma^2}\left[(x - \mu)^2 - 2\sigma^2 tx\right]$$

$$= -\frac{1}{2\sigma^2}\left[x^2 - 2(\mu + \sigma^2 t)x + \mu^2\right]$$

$$= -\frac{(x - (\mu + \sigma^2 t))^2}{2\sigma^2} + \mu t + \frac{1}{2}\sigma^2 t^2$$

Therefore:

$$M_X(t) = e^{\mu t + \frac{1}{2}\sigma^2 t^2} \int_{-\infty}^{\infty} \frac{1}{\sqrt{2\pi\sigma^2}} e^{-\frac{(x - (\mu + \sigma^2 t))^2}{2\sigma^2}} \, dx = e^{\mu t + \frac{1}{2}\sigma^2 t^2}$$

since the integral is the total mass of a $N(\mu + \sigma^2 t, \sigma^2)$ PDF, which equals $1$.

### Standard Normal Case

For $Z \sim N(0, 1)$:

$$M_Z(t) = e^{t^2/2}$$

## Properties of the Normal via MGFs

### Property 1: Linear Transformations

If $X \sim N(\mu, \sigma^2)$, then $aX + b \sim N(a\mu + b, \, a^2\sigma^2)$.

**Proof via MGF:**

$$M_{aX+b}(t) = E[e^{t(aX+b)}] = e^{bt} E[e^{(at)X}] = e^{bt} M_X(at)$$

$$= e^{bt} \cdot e^{\mu(at) + \frac{1}{2}\sigma^2(at)^2} = e^{(a\mu + b)t + \frac{1}{2}a^2\sigma^2 t^2} = M_{N(a\mu+b, \, a^2\sigma^2)}(t)$$

### Property 2: Sum of Independent Normals

If $X \sim N(\mu_1, \sigma_1^2)$ and $Y \sim N(\mu_2, \sigma_2^2)$ are **independent**, then:

$$X + Y \sim N(\mu_1 + \mu_2, \, \sigma_1^2 + \sigma_2^2)$$

**Proof via MGF:**

$$M_{X+Y}(t) = M_X(t) \cdot M_Y(t) = e^{\mu_1 t + \frac{1}{2}\sigma_1^2 t^2} \cdot e^{\mu_2 t + \frac{1}{2}\sigma_2^2 t^2}$$

$$= e^{(\mu_1 + \mu_2)t + \frac{1}{2}(\sigma_1^2 + \sigma_2^2)t^2} = M_{N(\mu_1 + \mu_2, \, \sigma_1^2 + \sigma_2^2)}(t)$$

## Python Implementation

```python
import numpy as np
from scipy import stats

# Verify: X ~ N(3, 4), Y ~ N(-1, 9) independent
# X + Y should be N(2, 13)
np.random.seed(42)
n = 100000
X = np.random.normal(3, 2, n)     # N(3, 4)
Y = np.random.normal(-1, 3, n)    # N(-1, 9)
Z = X + Y

print("X + Y: simulated vs theoretical N(2, 13)")
print(f"  Mean: {Z.mean():.4f} vs 2.0000")
print(f"  Var:  {Z.var():.4f} vs 13.0000")

# Verify: 2X + 1 should be N(7, 16)
W = 2 * X + 1
print(f"\n2X + 1: simulated vs theoretical N(7, 16)")
print(f"  Mean: {W.mean():.4f} vs 7.0000")
print(f"  Var:  {W.var():.4f} vs 16.0000")
```
