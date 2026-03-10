# Gamma Distribution as Sum of Exponentials


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

## Definition

!!! info "Gamma Distribution"
    A continuous random variable $X$ has the **Gamma distribution** with shape parameter $\alpha > 0$ and rate parameter $\lambda > 0$, written $X \sim \Gamma(\alpha, \lambda)$, if its PDF is:

    $$f(x) = \frac{\lambda(\lambda x)^{\alpha - 1} e^{-\lambda x}}{\Gamma(\alpha)}, \quad x > 0$$

### Intuition: Waiting for the alpha-th Arrival

In a Poisson process with rate $\lambda$, the time until the **$\alpha$-th arrival** follows $\Gamma(\alpha, \lambda)$. When $\alpha$ is a positive integer $n$, this waiting time is the sum of $n$ iid interarrival times, each $\text{Exp}(\lambda)$.

## Construction as Sum of Exponentials

If $X_1, X_2, \ldots, X_n$ are iid $\text{Exp}(\lambda)$, then their sum follows the Gamma distribution:

$$S_n = X_1 + X_2 + \cdots + X_n \sim \Gamma(n, \lambda)$$

This builds up from a chain of convolutions:

| Sum | Distribution |
|:---:|:---:|
| $X_1$ | $\text{Exp}(\lambda) \stackrel{d}{=} \Gamma(1, \lambda)$ |
| $X_1 + X_2$ | $\text{Exp}(\lambda) * \text{Exp}(\lambda) \stackrel{d}{=} \Gamma(2, \lambda)$ |
| $X_1 + X_2 + X_3$ | $\Gamma(2, \lambda) * \text{Exp}(\lambda) \stackrel{d}{=} \Gamma(3, \lambda)$ |
| $X_1 + \cdots + X_n$ | $\Gamma(n, \lambda)$ |

### Verification: Exp(λ) = Γ(1, λ)

Setting $\alpha = 1$ in the Gamma PDF:

$$\frac{\lambda(\lambda x)^{1-1} e^{-\lambda x}}{\Gamma(1)} = \lambda e^{-\lambda x}$$

since $\Gamma(1) = 1$ and $(\lambda x)^0 = 1$. This is exactly the $\text{Exp}(\lambda)$ PDF.

## Additivity Property

!!! info "Additivity of Gamma"
    If $X \sim \Gamma(\alpha, \lambda)$ and $Y \sim \Gamma(\beta, \lambda)$ are **independent** (with the **same rate** $\lambda$), then:

    $$X + Y \sim \Gamma(\alpha + \beta, \lambda)$$

    In convolution notation: $\Gamma(\alpha, \lambda) * \Gamma(\beta, \lambda) \stackrel{d}{=} \Gamma(\alpha + \beta, \lambda)$

### Proof via Convolution

For independent $X \sim \Gamma(\alpha, \lambda)$ and $Y \sim \Gamma(\beta, \lambda)$, and $x \geq 0$:

$$f_{X+Y}(x) = \int_0^x f_X(s) \, f_Y(x - s) \, ds$$

$$= \int_0^x \frac{\lambda(\lambda s)^{\alpha - 1} e^{-\lambda s}}{\Gamma(\alpha)} \cdot \frac{\lambda(\lambda(x - s))^{\beta - 1} e^{-\lambda(x-s)}}{\Gamma(\beta)} \, ds$$

Factoring out terms that don't depend on $s$:

$$= \frac{1}{\Gamma(\alpha)\Gamma(\beta)} \left[\int_0^x \lambda(\lambda s)^{\alpha-1} \lambda(\lambda(x-s))^{\beta-1} \, ds \right] e^{-\lambda x}$$

Substituting $t = s/x$ (so $ds = x \, dt$):

$$= \frac{1}{\Gamma(\alpha)\Gamma(\beta)} \left[\int_0^1 t^{\alpha-1}(1-t)^{\beta-1} \, dt \right] \lambda(\lambda x)^{\alpha + \beta - 1} e^{-\lambda x}$$

The integral is the **Beta function** $B(\alpha, \beta) = \frac{\Gamma(\alpha)\Gamma(\beta)}{\Gamma(\alpha + \beta)}$, giving:

$$f_{X+Y}(x) = \frac{\lambda(\lambda x)^{(\alpha + \beta) - 1} e^{-\lambda x}}{\Gamma(\alpha + \beta)}$$

This is the PDF of $\Gamma(\alpha + \beta, \lambda)$.

## Related Distributions

| Distribution | Gamma Form | Description |
|:---:|:---:|:---|
| $\text{Exp}(\lambda)$ | $\Gamma(1, \lambda)$ | Time to 1st arrival |
| Erlang$(2, \lambda)$ | $\Gamma(2, \lambda)$ | Time to 2nd arrival |
| Erlang$(k, \lambda)$ | $\Gamma(k, \lambda)$ | Time to $k$-th arrival (integer $k$) |
| $\chi^2_1$ | $\Gamma(1/2, 1/2)$ | Square of standard normal |
| $\chi^2_d$ | $\Gamma(d/2, 1/2)$ | Sum of $d$ squared standard normals |

## Python Implementation

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Plot Gamma PDFs for different alpha values (fixed lambda)
lam = 2.0
x = np.linspace(0, 10, 500)
alphas = [1, 2, 3, 4, 5]
colors = ['blue', 'red', 'magenta', 'black', 'cyan']

fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# PDF plots
for alpha, color in zip(alphas, colors):
    # scipy uses shape=alpha, scale=1/lambda
    pdf = stats.gamma.pdf(x, a=alpha, scale=1/lam)
    axes[0].plot(x, pdf, color=color, lw=2, label=f'α={alpha}')

axes[0].set_title(f'PDF of Gamma Distribution (λ = {lam})')
axes[0].set_xlabel('x')
axes[0].set_ylabel('f(x)')
axes[0].set_ylim(0, 2)
axes[0].legend()
axes[0].grid(True, alpha=0.3)

# Demonstrate additivity: Γ(2,λ) + Γ(3,λ) = Γ(5,λ)
np.random.seed(42)
n_sim = 50000

X = np.random.gamma(shape=2, scale=1/lam, size=n_sim)  # Γ(2, λ)
Y = np.random.gamma(shape=3, scale=1/lam, size=n_sim)  # Γ(3, λ)
Z = X + Y  # Should be Γ(5, λ)

axes[1].hist(Z, bins=80, density=True, alpha=0.5, color='blue',
             label='X + Y (simulated)')
x_theory = np.linspace(0, 8, 200)
pdf_theory = stats.gamma.pdf(x_theory, a=5, scale=1/lam)
axes[1].plot(x_theory, pdf_theory, 'r-', lw=2,
             label='Γ(5, 2) PDF')
axes[1].set_title('Additivity: Γ(2,2) + Γ(3,2) = Γ(5,2)')
axes[1].set_xlabel('x')
axes[1].legend()
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('gamma_definition.png', dpi=150, bbox_inches='tight')
plt.show()

# Verify via sum of exponentials
print("=== Γ(n, λ) as Sum of n iid Exp(λ) ===")
for n in [2, 3, 5, 10]:
    exp_samples = np.random.exponential(1/lam, size=(n_sim, n))
    sums = exp_samples.sum(axis=1)
    gamma_samples = np.random.gamma(shape=n, scale=1/lam, size=n_sim)
    print(f"n={n}: Sum of Exp mean={np.mean(sums):.4f}, "
          f"Gamma mean={np.mean(gamma_samples):.4f}, "
          f"theory={n/lam:.4f}")
```
