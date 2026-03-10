# Erlang as a Special Case of Gamma


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

## Definition

!!! info "Erlang Distribution"
    The **Erlang distribution** with shape parameter $k$ (a positive integer) and rate $\lambda > 0$ is the Gamma distribution restricted to integer shape:

    $$\text{Erlang}(k, \lambda) = \Gamma(k, \lambda)$$

    Its PDF is:

    $$f(x) = \frac{\lambda(\lambda x)^{k-1} e^{-\lambda x}}{(k-1)!}, \quad x > 0$$

    where we use $\Gamma(k) = (k-1)!$ for positive integers $k$.

## Why a Separate Name?

The Erlang distribution is named after A.K. Erlang, who introduced it in the early 20th century to model telephone call waiting times. While it is mathematically just a special case of the Gamma distribution, it has its own identity because:

- It predates the general Gamma distribution in applications
- Its integer shape parameter gives it a concrete interpretation as a **sum of iid Exponentials**
- Its CDF has a closed-form expression involving a finite sum (unlike the general Gamma)

## Special Cases

| Distribution | Parameters | Description |
|:---:|:---:|:---|
| $\text{Exp}(\lambda)$ | $\text{Erlang}(1, \lambda)$ | Single interarrival time |
| $\text{Erlang}(2, \lambda)$ | $\Gamma(2, \lambda)$ | Sum of 2 iid $\text{Exp}(\lambda)$ |
| $\text{Erlang}(k, \lambda)$ | $\Gamma(k, \lambda)$ | Sum of $k$ iid $\text{Exp}(\lambda)$ |

## CDF (Closed Form)

For integer $k$, the CDF of $\text{Erlang}(k, \lambda)$ has a closed form:

$$F(x) = 1 - \sum_{j=0}^{k-1} \frac{(\lambda x)^j}{j!} e^{-\lambda x}, \quad x \geq 0$$

This can be derived from the Poisson connection: $P(S_k \leq t) = P(N(t) \geq k)$ where $N(t) \sim \text{Po}(\lambda t)$.

## Moments

From the Gamma distribution:

$$E[X] = \frac{k}{\lambda}, \qquad \text{Var}(X) = \frac{k}{\lambda^2}$$

## Python Implementation

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

lam = 2.0
x = np.linspace(0, 8, 300)

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Erlang PDFs for different k
for k in [1, 2, 3, 5, 10]:
    pdf = stats.gamma.pdf(x, a=k, scale=1/lam)
    axes[0].plot(x, pdf, lw=2, label=f'Erlang({k}, {lam})')

axes[0].set_title(f'Erlang(k, λ={lam}) PDFs')
axes[0].set_xlabel('x')
axes[0].set_ylabel('f(x)')
axes[0].legend()
axes[0].grid(True, alpha=0.3)

# Verify: sum of k iid Exp(λ) = Erlang(k, λ)
np.random.seed(42)
n_sim = 50000
k = 5

# Method 1: sum of exponentials
exp_samples = np.random.exponential(1/lam, size=(n_sim, k))
sums = exp_samples.sum(axis=1)

# Method 2: direct Gamma sampling
gamma_samples = np.random.gamma(shape=k, scale=1/lam, size=n_sim)

axes[1].hist(sums, bins=60, density=True, alpha=0.4,
             label=f'Sum of {k} Exp({lam})', color='blue')
axes[1].hist(gamma_samples, bins=60, density=True, alpha=0.4,
             label=f'Γ({k}, {lam})', color='red')
pdf_theory = stats.gamma.pdf(x, a=k, scale=1/lam)
axes[1].plot(x, pdf_theory, 'k-', lw=2, label='Theory')
axes[1].set_title(f'Sum of {k} iid Exp({lam}) = Erlang({k}, {lam})')
axes[1].set_xlabel('x')
axes[1].legend()
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('erlang_distribution.png', dpi=150, bbox_inches='tight')
plt.show()
```
