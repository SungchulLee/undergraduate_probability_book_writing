# Exponential Distribution from Interarrival Times

## Motivation: Waiting for the First Arrival

In a **Poisson process** with rate $\lambda$, events occur randomly along the time axis. The **interarrival times** — the gaps between consecutive events — follow the **Exponential distribution**.

Let $T_1$ be the time of the first arrival after time $0$. Then:

$$P(T_1 > t) = P(\text{no arrivals in } [0, t]) = e^{-\lambda t}$$

since the number of arrivals in $[0, t]$ follows $\text{Po}(\lambda t)$, and $P(N(t) = 0) = e^{-\lambda t}$.

## Definition

!!! info "Exponential Distribution"
    A continuous random variable $X$ has the **Exponential distribution** with rate parameter $\lambda > 0$, written $X \sim \text{Exp}(\lambda)$, if its PDF is:

    $$f(x) = \lambda e^{-\lambda x}, \quad x \geq 0$$

### CDF and Survival Function

The **CDF** is:

$$F(x) = P(X \leq x) = 1 - e^{-\lambda x}, \quad x \geq 0$$

The **survival function** (tail probability) is:

$$\bar{F}(x) = P(X > x) = e^{-\lambda x}, \quad x \geq 0$$

The survival function has a particularly clean form, which makes the Exponential distribution easy to work with.

### Connection to the Poisson Process

In a Poisson process with rate $\lambda$:

- $T_1$, the time until the first arrival, follows $\text{Exp}(\lambda)$
- The interarrival times $T_1, T_2, T_3, \ldots$ between consecutive events are **independent and identically distributed** (iid) $\text{Exp}(\lambda)$

This is the fundamental link between the Poisson process (counting events) and the Exponential distribution (measuring waiting times).

### Relationship to the Geometric Distribution

The Exponential distribution is the **continuous analog** of the Geometric distribution:

| Property | Geometric | Exponential |
|----------|-----------|-------------|
| Domain | Discrete ($1, 2, 3, \ldots$) | Continuous ($[0, \infty)$) |
| Memoryless | Yes | Yes |
| Interpretation | Trials until first success | Time until first event |
| Parameter | $p$ (success probability) | $\lambda$ (rate) |
| Mean | $1/p$ | $1/\lambda$ |
| Variance | $q/p^2$ | $1/\lambda^2$ |

### Relationship to the Gamma Distribution

The Exponential distribution is a special case of the Gamma distribution:

$$\text{Exp}(\lambda) \stackrel{d}{=} \Gamma(1, \lambda)$$

This follows immediately from comparing the PDFs:

$$\lambda e^{-\lambda x} = \frac{\lambda(\lambda x)^{1-1} e^{-\lambda x}}{\Gamma(1)}, \quad x \geq 0$$

since $\Gamma(1) = 1$ and $(\lambda x)^0 = 1$.

## Simulation

To simulate $X \sim \text{Exp}(\lambda)$ from a uniform random variable $U \sim U(0,1)$, use the **inverse CDF method**:

$$X = F^{-1}(U) = -\frac{1}{\lambda} \log(1 - U)$$

Since $1 - U \sim U(0,1)$ when $U \sim U(0,1)$, this simplifies to:

$$X = -\frac{1}{\lambda} \log(U) \sim \text{Exp}(\lambda)$$

??? example "Example: Simulating Exp(0.5)"
    Given $U \sim U(0,1)$, generate $X \sim \text{Exp}(0.5)$.

    The CDF is $F(x) = 1 - e^{-0.5x}$ for $x \geq 0$.

    Setting $u = 1 - e^{-0.5x}$ and solving:

    $$x = -2\log(1 - u)$$

    Therefore $X = -2\log(1 - U) \sim \text{Exp}(0.5)$.

    Using the simplification: $X = -2\log(U) \sim \text{Exp}(0.5)$.

## Python Implementation

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Parameters
lam = 2.0  # rate parameter

# PDF and CDF
x = np.linspace(0, 4, 200)
pdf = lam * np.exp(-lam * x)
cdf = 1 - np.exp(-lam * x)

# Simulation via inverse CDF
np.random.seed(42)
n_sim = 10000
U = np.random.uniform(0, 1, n_sim)
X_sim = -np.log(U) / lam

fig, axes = plt.subplots(1, 3, figsize=(15, 4))

# PDF
axes[0].plot(x, pdf, 'b-', lw=2)
axes[0].set_title(f'PDF of Exp({lam})')
axes[0].set_xlabel('x')
axes[0].set_ylabel('f(x)')
axes[0].grid(True, alpha=0.3)

# CDF
axes[1].plot(x, cdf, 'r-', lw=2)
axes[1].set_title(f'CDF of Exp({lam})')
axes[1].set_xlabel('x')
axes[1].set_ylabel('F(x)')
axes[1].grid(True, alpha=0.3)

# Simulation histogram vs theoretical PDF
axes[2].hist(X_sim, bins=50, density=True, alpha=0.7, label='Simulated')
axes[2].plot(x, pdf, 'r-', lw=2, label='Theoretical PDF')
axes[2].set_title('Inverse CDF Simulation')
axes[2].set_xlabel('x')
axes[2].legend()
axes[2].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('exponential_definition.png', dpi=150, bbox_inches='tight')
plt.show()

# Verify moments
print(f"Theoretical mean: {1/lam:.4f}")
print(f"Simulated mean:   {np.mean(X_sim):.4f}")
print(f"Theoretical var:  {1/lam**2:.4f}")
print(f"Simulated var:    {np.var(X_sim):.4f}")
```
