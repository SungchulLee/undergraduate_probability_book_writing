# Sum of Independent Exponentials

## Result

!!! info "Convolution of Exponentials"
    If $X_1, X_2, \ldots, X_n$ are iid $\text{Exp}(\lambda)$, then:

    $$X_1 + X_2 + \cdots + X_n \sim \Gamma(n, \lambda)$$

    In convolution notation:

    $$\underbrace{\text{Exp}(\lambda) * \text{Exp}(\lambda) * \cdots * \text{Exp}(\lambda)}_{n \text{ times}} \stackrel{d}{=} \Gamma(n, \lambda)$$

## Proof: Two Exponentials

For independent $X \sim \text{Exp}(\lambda)$ and $Y \sim \text{Exp}(\lambda)$, and $a \geq 0$:

$$f_{X+Y}(a) = \int_0^a \lambda e^{-\lambda b} \cdot \lambda e^{-\lambda(a-b)} \, db = \lambda^2 e^{-\lambda a} \int_0^a db = \lambda^2 a \, e^{-\lambda a}$$

This is the PDF of $\Gamma(2, \lambda)$:

$$\frac{\lambda(\lambda a)^{2-1} e^{-\lambda a}}{\Gamma(2)} = \lambda^2 a \, e^{-\lambda a} \quad \checkmark$$

## Proof: General $n$ by Induction

If $S_{n-1} = X_1 + \cdots + X_{n-1} \sim \Gamma(n-1, \lambda)$ and $X_n \sim \text{Exp}(\lambda)$ are independent, then by the **Gamma additivity property**:

$$S_n = S_{n-1} + X_n \sim \Gamma(n-1, \lambda) * \Gamma(1, \lambda) = \Gamma(n, \lambda)$$

The additivity of the Gamma distribution (proved via convolution in Chapter 14) handles the inductive step.

## Different Rates

When the exponentials have **different** rates, the result is no longer a Gamma distribution. For $X \sim \text{Exp}(\lambda_1)$ and $Y \sim \text{Exp}(\lambda_2)$ with $\lambda_1 \neq \lambda_2$:

$$f_{X+Y}(a) = \frac{\lambda_1 \lambda_2}{\lambda_1 - \lambda_2}\left(e^{-\lambda_2 a} - e^{-\lambda_1 a}\right), \quad a \geq 0$$

This is a **hypoexponential** distribution, which is a mixture of exponential terms.

## Connection to the Poisson Process

The sum $S_n = X_1 + \cdots + X_n$ is the **$n$-th arrival time** in a Poisson process with rate $\lambda$. The fact that $S_n \sim \Gamma(n, \lambda)$ provides the link between:

- **Counting** (Poisson distribution): $N(t) \sim \text{Po}(\lambda t)$
- **Waiting** (Gamma distribution): $S_n \sim \Gamma(n, \lambda)$

## Python Implementation

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

np.random.seed(42)
n_sim = 100000
lam = 2.0

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Sum of n iid Exp(lambda) for various n
x = np.linspace(0, 10, 300)
for n in [1, 2, 3, 5, 10]:
    # Simulate
    samples = np.random.exponential(1/lam, (n_sim, n))
    sums = samples.sum(axis=1)

    # Plot simulation vs theory
    axes[0].hist(sums, bins=60, density=True, alpha=0.2)
    pdf = stats.gamma.pdf(x, a=n, scale=1/lam)
    axes[0].plot(x, pdf, lw=2, label=f'n={n}: Γ({n},{lam})')

axes[0].set_title(f'Sum of n iid Exp({lam})')
axes[0].set_xlabel('Sum')
axes[0].set_ylabel('Density')
axes[0].legend()
axes[0].grid(True, alpha=0.3)

# Different rates: Exp(1) + Exp(3)
l1, l2 = 1.0, 3.0
X1 = np.random.exponential(1/l1, n_sim)
X2 = np.random.exponential(1/l2, n_sim)
S = X1 + X2

a_vals = np.linspace(0, 6, 200)
pdf_hypo = l1 * l2 / (l1 - l2) * (np.exp(-l2 * a_vals) - np.exp(-l1 * a_vals))

axes[1].hist(S, bins=60, density=True, alpha=0.5, color='steelblue',
             label='Simulated')
axes[1].plot(a_vals, pdf_hypo, 'r-', lw=2, label='Hypoexponential PDF')
axes[1].set_title(f'Exp({l1}) + Exp({l2}) (different rates)')
axes[1].set_xlabel('Sum')
axes[1].set_ylabel('Density')
axes[1].legend()
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('sum_exponentials.png', dpi=150, bbox_inches='tight')
plt.show()

# Verify moments
for n in [2, 5, 10]:
    samples = np.random.exponential(1/lam, (n_sim, n))
    sums = samples.sum(axis=1)
    print(f"Sum of {n} Exp({lam}): mean={np.mean(sums):.4f} "
          f"(theory {n/lam:.4f}), var={np.var(sums):.4f} "
          f"(theory {n/lam**2:.4f})")
```
