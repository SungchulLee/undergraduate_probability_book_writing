# Mean and Variance of the Exponential Distribution


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

## Mean

!!! info "Mean of Exp(λ)"
    If $X \sim \text{Exp}(\lambda)$, then:

    $$E[X] = \frac{1}{\lambda}$$

### Derivation

Using integration by parts with $u = x$, $dv = \lambda e^{-\lambda x} dx$:

$$E[X] = \int_0^\infty x \lambda e^{-\lambda x} \, dx = \left[-x e^{-\lambda x}\right]_0^\infty + \int_0^\infty e^{-\lambda x} \, dx = 0 + \frac{1}{\lambda} = \frac{1}{\lambda}$$

### Interpretation

The mean $1/\lambda$ is the **average waiting time** between events in a Poisson process with rate $\lambda$. If events occur at rate $\lambda = 5$ per hour, the average time between events is $1/5$ hour $= 12$ minutes.

## Variance

!!! info "Variance of Exp(λ)"
    If $X \sim \text{Exp}(\lambda)$, then:

    $$\text{Var}(X) = \frac{1}{\lambda^2}$$

### Derivation

First compute $E[X^2]$ using integration by parts (or the Gamma function technique):

$$E[X^2] = \int_0^\infty x^2 \lambda e^{-\lambda x} \, dx$$

Substituting $u = \lambda x$:

$$E[X^2] = \frac{1}{\lambda^2} \int_0^\infty u^2 e^{-u} \, du = \frac{\Gamma(3)}{\lambda^2} = \frac{2!}{\lambda^2} = \frac{2}{\lambda^2}$$

Therefore:

$$\text{Var}(X) = E[X^2] - (E[X])^2 = \frac{2}{\lambda^2} - \frac{1}{\lambda^2} = \frac{1}{\lambda^2}$$

### Standard Deviation

$$\text{SD}(X) = \frac{1}{\lambda} = E[X]$$

A notable property: for the Exponential distribution, the **standard deviation equals the mean**. This means the coefficient of variation is always $1$, regardless of the rate parameter.

## Higher Moments

Using the Gamma function, the $n$-th moment of $X \sim \text{Exp}(\lambda)$ is:

$$E[X^n] = \int_0^\infty x^n \lambda e^{-\lambda x} \, dx = \frac{\Gamma(n+1)}{\lambda^n} = \frac{n!}{\lambda^n}$$

## Summary Table

The Exponential distribution fits into a broader pattern relating discrete and continuous distributions:

| Distribution | Mean | Variance |
|:---:|:---:|:---:|
| $\text{Geo}(p)$ | $\dfrac{1}{p}$ | $\dfrac{q}{p^2}$ |
| $\text{NegBin}(n, p)$ | $\dfrac{n}{p}$ | $\dfrac{nq}{p^2}$ |
| $\text{Exp}(\lambda)$ | $\dfrac{1}{\lambda}$ | $\dfrac{1}{\lambda^2}$ |
| $\Gamma(n, \lambda)$ | $\dfrac{n}{\lambda}$ | $\dfrac{n}{\lambda^2}$ |
| $\Gamma(\alpha, \lambda)$ | $\dfrac{\alpha}{\lambda}$ | $\dfrac{\alpha}{\lambda^2}$ |

The Geometric is to the Negative Binomial as the Exponential is to the Gamma: the sum of $n$ iid copies.

## MGF of the Exponential

The moment generating function of $X \sim \text{Exp}(\lambda)$ is:

$$M_X(t) = E[e^{tX}] = \int_0^\infty e^{tx} \lambda e^{-\lambda x} \, dx = \frac{\lambda}{\lambda - t}, \quad t < \lambda$$

This can be used to verify the moments:

$$M_X'(0) = \frac{\lambda}{(\lambda - t)^2}\bigg|_{t=0} = \frac{1}{\lambda} = E[X]$$

$$M_X''(0) = \frac{2\lambda}{(\lambda - t)^3}\bigg|_{t=0} = \frac{2}{\lambda^2} = E[X^2]$$

## Python Implementation

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

np.random.seed(42)

# Compare mean and variance across different rates
rates = [0.5, 1.0, 2.0, 5.0]
n_sim = 50000

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

for lam in rates:
    X = np.random.exponential(1/lam, n_sim)
    x = np.linspace(0, 6, 200)
    pdf = lam * np.exp(-lam * x)

    axes[0].plot(x, pdf, lw=2, label=f'λ={lam}, E[X]={1/lam:.2f}')
    axes[0].axvline(1/lam, linestyle='--', alpha=0.3)

axes[0].set_title('Exponential PDFs with Means Marked')
axes[0].set_xlabel('x')
axes[0].set_ylabel('f(x)')
axes[0].legend()
axes[0].grid(True, alpha=0.3)

# Verify mean = std dev property
lam_range = np.linspace(0.2, 5, 50)
means = 1 / lam_range
stds = 1 / lam_range

axes[1].plot(lam_range, means, 'b-', lw=2, label='E[X] = 1/λ')
axes[1].plot(lam_range, stds, 'r--', lw=2, label='SD(X) = 1/λ')
axes[1].set_title('Mean Equals Standard Deviation')
axes[1].set_xlabel('λ')
axes[1].set_ylabel('Value')
axes[1].legend()
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('exponential_mean_variance.png', dpi=150, bbox_inches='tight')
plt.show()

# Numerical verification
for lam in rates:
    X = np.random.exponential(1/lam, n_sim)
    print(f"λ = {lam}: E[X] = {np.mean(X):.4f} (theory {1/lam:.4f}), "
          f"Var(X) = {np.var(X):.4f} (theory {1/lam**2:.4f})")
```
