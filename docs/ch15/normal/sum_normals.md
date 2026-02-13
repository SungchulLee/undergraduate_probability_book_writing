# Sum of Independent Normals

## Main Result

If $X \sim N(\mu_1, \sigma_1^2)$ and $Y \sim N(\mu_2, \sigma_2^2)$ are **independent**, then:

$$X + Y \sim N(\mu_1 + \mu_2, \, \sigma_1^2 + \sigma_2^2)$$

More generally, for independent $X_1, \ldots, X_n$ with $X_i \sim N(\mu_i, \sigma_i^2)$:

$$\sum_{i=1}^n X_i \sim N\left(\sum_{i=1}^n \mu_i, \, \sum_{i=1}^n \sigma_i^2\right)$$

## Proof via MGF

$$M_{X+Y}(t) = M_X(t) \cdot M_Y(t) = e^{\mu_1 t + \frac{1}{2}\sigma_1^2 t^2} \cdot e^{\mu_2 t + \frac{1}{2}\sigma_2^2 t^2} = e^{(\mu_1 + \mu_2)t + \frac{1}{2}(\sigma_1^2 + \sigma_2^2)t^2}$$

This is the MGF of $N(\mu_1 + \mu_2, \sigma_1^2 + \sigma_2^2)$. By uniqueness of MGFs, the result follows.

## Linear Transformations

If $X \sim N(\mu, \sigma^2)$, then for constants $a, b$:

$$aX + b \sim N(a\mu + b, \, a^2\sigma^2)$$

**Proof via MGF:**

$$M_{aX+b}(t) = e^{bt} M_X(at) = e^{bt} \cdot e^{\mu(at) + \frac{1}{2}\sigma^2(at)^2} = e^{(a\mu + b)t + \frac{1}{2}a^2\sigma^2 t^2}$$

!!! warning "Independence Required"
    The sum of two normal random variables is **not necessarily normal** unless they are independent (or more generally, jointly normal). Counterexamples exist for dependent normals.

## Special Cases

For iid $X_1, \ldots, X_n \sim N(\mu, \sigma^2)$:

| Quantity | Distribution |
|----------|-------------|
| $S_n = \sum X_i$ | $N(n\mu, n\sigma^2)$ |
| $\bar{X}_n = S_n / n$ | $N(\mu, \sigma^2/n)$ |
| $\frac{S_n - n\mu}{\sigma\sqrt{n}}$ | $N(0, 1)$ exactly |

## Python Verification

```python
import numpy as np
from scipy import stats

np.random.seed(42)
n = 100000

X = np.random.normal(3, 2, n)   # N(3, 4)
Y = np.random.normal(-1, 3, n)  # N(-1, 9)
S = X + Y                       # Should be N(2, 13)

print("X + Y ~ N(2, 13)")
print(f"  Mean: {S.mean():.4f}  (expected: 2)")
print(f"  Var:  {S.var():.4f}  (expected: 13)")

# Normality test
_, p_value = stats.shapiro(S[:5000])
print(f"  Shapiro-Wilk p-value: {p_value:.4f}")
```
