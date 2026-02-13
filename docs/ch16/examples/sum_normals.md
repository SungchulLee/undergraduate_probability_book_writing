# Sum of Independent Normals (via Convolution)

## Result

!!! info "Convolution of Normal Distributions"
    If $X \sim N(\mu_1, \sigma_1^2)$ and $Y \sim N(\mu_2, \sigma_2^2)$ are independent, then:

    $$X + Y \sim N(\mu_1 + \mu_2, \; \sigma_1^2 + \sigma_2^2)$$

    The Normal family is **closed under convolution**: the sum of independent Normals is Normal.

## Proof via MGFs

The MGF approach is the most elegant:

$$M_{X+Y}(t) = M_X(t) \cdot M_Y(t) = e^{\mu_1 t + \sigma_1^2 t^2/2} \cdot e^{\mu_2 t + \sigma_2^2 t^2/2} = e^{(\mu_1+\mu_2)t + (\sigma_1^2+\sigma_2^2)t^2/2}$$

This is the MGF of $N(\mu_1 + \mu_2, \sigma_1^2 + \sigma_2^2)$. By uniqueness of MGFs, the result follows.

## Proof via Convolution Integral

For $X \sim N(0, 1)$ and $Y \sim N(0, 1)$ independent (standard case):

$$f_{X+Y}(a) = \int_{-\infty}^{\infty} \frac{1}{\sqrt{2\pi}} e^{-b^2/2} \cdot \frac{1}{\sqrt{2\pi}} e^{-(a-b)^2/2} \, db$$

Completing the square in the exponent and evaluating the Gaussian integral yields:

$$f_{X+Y}(a) = \frac{1}{\sqrt{4\pi}} e^{-a^2/4}$$

which is the PDF of $N(0, 2)$, confirming $N(0,1) + N(0,1) = N(0, 2)$.

## General Sum

If $X_1, X_2, \ldots, X_n$ are independent with $X_i \sim N(\mu_i, \sigma_i^2)$, then:

$$\sum_{i=1}^n X_i \sim N\!\left(\sum_{i=1}^n \mu_i, \; \sum_{i=1}^n \sigma_i^2\right)$$

For iid $X_i \sim N(\mu, \sigma^2)$:

$$\bar{X} = \frac{1}{n}\sum_{i=1}^n X_i \sim N\!\left(\mu, \; \frac{\sigma^2}{n}\right)$$

## Python Implementation

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

np.random.seed(42)
n_sim = 100000

mu1, sig1 = 2, 1.5
mu2, sig2 = -1, 2.0

X = np.random.normal(mu1, sig1, n_sim)
Y = np.random.normal(mu2, sig2, n_sim)
S = X + Y

mu_sum = mu1 + mu2
sig_sum = np.sqrt(sig1**2 + sig2**2)

fig, ax = plt.subplots(figsize=(8, 5))
ax.hist(S, bins=80, density=True, alpha=0.5, color='steelblue',
        label='Simulated X+Y')
x = np.linspace(mu_sum - 4*sig_sum, mu_sum + 4*sig_sum, 200)
ax.plot(x, stats.norm.pdf(x, mu_sum, sig_sum), 'r-', lw=2,
        label=f'N({mu_sum}, {sig_sum**2:.2f}) PDF')
ax.set_title(f'N({mu1},{sig1**2}) + N({mu2},{sig2**2}) = N({mu_sum},{sig_sum**2:.2f})')
ax.legend()
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('sum_normals.png', dpi=150, bbox_inches='tight')
plt.show()

print(f"Simulated: mean={np.mean(S):.4f}, var={np.var(S):.4f}")
print(f"Theory:    mean={mu_sum:.4f}, var={sig_sum**2:.4f}")
```
