# Mean and Variance of the Gamma Distribution

## Mean

!!! info "Mean of Γ(α, λ)"
    If $X \sim \Gamma(\alpha, \lambda)$, then:

    $$E[X] = \frac{\alpha}{\lambda}$$

### Derivation

$$E[X] = \int_0^\infty x \cdot \frac{\lambda(\lambda x)^{\alpha - 1} e^{-\lambda x}}{\Gamma(\alpha)} \, dx$$

The key technique is to **recognize a Gamma PDF inside the integral**. Multiply and divide to create the PDF of $\Gamma(\alpha + 1, \lambda)$:

$$E[X] = \frac{\Gamma(\alpha + 1)}{\lambda \, \Gamma(\alpha)} \int_0^\infty \underbrace{\frac{\lambda(\lambda x)^{(\alpha+1)-1} e^{-\lambda x}}{\Gamma(\alpha + 1)}}_{\text{PDF of } \Gamma(\alpha+1, \lambda)} \, dx = \frac{\alpha \, \Gamma(\alpha)}{\lambda \, \Gamma(\alpha)} = \frac{\alpha}{\lambda}$$

The integral equals $1$ because it integrates a valid PDF, and we used $\Gamma(\alpha + 1) = \alpha \, \Gamma(\alpha)$.

## Second Moment

$$E[X^2] = \int_0^\infty x^2 \cdot \frac{\lambda(\lambda x)^{\alpha - 1} e^{-\lambda x}}{\Gamma(\alpha)} \, dx$$

Similarly, create the PDF of $\Gamma(\alpha + 2, \lambda)$:

$$E[X^2] = \frac{\Gamma(\alpha + 2)}{\lambda^2 \, \Gamma(\alpha)} \int_0^\infty \underbrace{\frac{\lambda(\lambda x)^{(\alpha+2)-1} e^{-\lambda x}}{\Gamma(\alpha + 2)}}_{\text{PDF of } \Gamma(\alpha+2, \lambda)} \, dx = \frac{(\alpha + 1)\alpha \, \Gamma(\alpha)}{\lambda^2 \, \Gamma(\alpha)} = \frac{\alpha(\alpha + 1)}{\lambda^2}$$

using $\Gamma(\alpha + 2) = (\alpha + 1) \alpha \, \Gamma(\alpha)$.

## Variance

!!! info "Variance of Γ(α, λ)"
    If $X \sim \Gamma(\alpha, \lambda)$, then:

    $$\text{Var}(X) = \frac{\alpha}{\lambda^2}$$

### Derivation

$$\text{Var}(X) = E[X^2] - (E[X])^2 = \frac{\alpha(\alpha + 1)}{\lambda^2} - \frac{\alpha^2}{\lambda^2} = \frac{\alpha}{\lambda^2}$$

## The General Moment Technique

The derivations above illustrate a powerful technique: to compute $E[X^k]$ for a Gamma random variable, **reshape the integrand to be a Gamma PDF with shifted parameters**, then use the fact that a PDF integrates to 1.

In general, for $X \sim \Gamma(\alpha, \lambda)$:

$$E[X^k] = \frac{\Gamma(\alpha + k)}{\lambda^k \, \Gamma(\alpha)}$$

## Summary: Discrete–Continuous Analogy

| Distribution | Mean | Variance |
|:---:|:---:|:---:|
| $\text{Geo}(p)$ | $\dfrac{1}{p}$ | $\dfrac{q}{p^2}$ |
| $\text{NegBin}(n, p)$ | $\dfrac{n}{p}$ | $\dfrac{nq}{p^2}$ |
| $\text{Exp}(\lambda)$ | $\dfrac{1}{\lambda}$ | $\dfrac{1}{\lambda^2}$ |
| $\Gamma(n, \lambda)$ | $\dfrac{n}{\lambda}$ | $\dfrac{n}{\lambda^2}$ |
| $\Gamma(\alpha, \lambda)$ | $\dfrac{\alpha}{\lambda}$ | $\dfrac{\alpha}{\lambda^2}$ |

The pattern is clear: the shape parameter $\alpha$ scales both the mean and the variance linearly, while the rate parameter $\lambda$ appears in the denominator (once for the mean, squared for the variance).

## Python Implementation

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

np.random.seed(42)
n_sim = 100000

# Verify mean and variance for various (alpha, lambda) pairs
print("=== Mean and Variance Verification ===")
print(f"{'α':>5} {'λ':>5} | {'E[X] theory':>12} {'E[X] sim':>10} | "
      f"{'Var theory':>12} {'Var sim':>10}")
print("-" * 70)

params = [(1, 1), (2, 1), (3, 2), (5, 2), (0.5, 0.5), (10, 3)]
for alpha, lam in params:
    X = np.random.gamma(shape=alpha, scale=1/lam, size=n_sim)
    mean_theory = alpha / lam
    var_theory = alpha / lam**2
    print(f"{alpha:5.1f} {lam:5.1f} | {mean_theory:12.4f} {np.mean(X):10.4f} | "
          f"{var_theory:12.4f} {np.var(X):10.4f}")

# Visualize how mean and variance change with alpha
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

lam = 2.0
alphas = np.linspace(0.5, 10, 20)
x = np.linspace(0, 10, 300)

# PDFs with means marked
for alpha in [1, 2, 4, 8]:
    pdf = stats.gamma.pdf(x, a=alpha, scale=1/lam)
    mean = alpha / lam
    axes[0].plot(x, pdf, lw=2, label=f'α={alpha}, E[X]={mean:.1f}')
    axes[0].axvline(mean, linestyle=':', alpha=0.4)

axes[0].set_title(f'Gamma PDFs with Means (λ={lam})')
axes[0].set_xlabel('x')
axes[0].set_ylabel('f(x)')
axes[0].legend()
axes[0].grid(True, alpha=0.3)

# Mean and variance as functions of alpha
means = alphas / lam
variances = alphas / lam**2
sds = np.sqrt(variances)

axes[1].plot(alphas, means, 'b-', lw=2, label='E[X] = α/λ')
axes[1].plot(alphas, variances, 'r-', lw=2, label='Var(X) = α/λ²')
axes[1].plot(alphas, sds, 'g--', lw=2, label='SD(X) = √α/λ')
axes[1].set_title(f'Moments vs Shape Parameter (λ={lam})')
axes[1].set_xlabel('α')
axes[1].set_ylabel('Value')
axes[1].legend()
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('gamma_mean_variance.png', dpi=150, bbox_inches='tight')
plt.show()
```
