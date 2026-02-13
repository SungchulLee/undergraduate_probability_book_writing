# Discrete Uniform Distribution Properties

## Mean and Variance

!!! info "Moments of Discrete Uniform"
    If $X \sim \text{DiscreteUniform}(a, a+1, \ldots, b)$ (taking $n = b - a + 1$ equally likely values), then:

    $$E[X] = \frac{a + b}{2}, \qquad \text{Var}(X) = \frac{n^2 - 1}{12}$$

    where $n = b - a + 1$ is the number of values.

**Derivation of mean.** By symmetry of the PMF about $(a+b)/2$, or directly:

$$E[X] = \frac{1}{n}\sum_{k=a}^{b} k = \frac{1}{n} \cdot \frac{n(a+b)}{2} = \frac{a+b}{2}$$

**Derivation of variance.** For $X \sim \text{DiscreteUniform}(1, 2, \ldots, n)$:

$$E[X^2] = \frac{1}{n}\sum_{k=1}^{n} k^2 = \frac{(n+1)(2n+1)}{6}$$

$$\text{Var}(X) = \frac{(n+1)(2n+1)}{6} - \left(\frac{n+1}{2}\right)^2 = \frac{n^2 - 1}{12}$$

For the general case $X \sim \text{DiscreteUniform}(a, \ldots, b)$, note $X = a - 1 + Y$ where $Y \sim \text{DiscreteUniform}(1, \ldots, n)$, so $\text{Var}(X) = \text{Var}(Y) = \frac{n^2-1}{12}$.

## Special Cases

**Fair die:** $X \sim \text{DiscreteUniform}(1, 2, 3, 4, 5, 6)$

$$E[X] = 3.5, \qquad \text{Var}(X) = \frac{35}{12} \approx 2.917$$

**Fair coin (0/1):** $X \sim \text{DiscreteUniform}(0, 1) = \text{Bernoulli}(1/2)$

$$E[X] = 0.5, \qquad \text{Var}(X) = \frac{3}{12} = 0.25$$

## Connection to Classical Probability

The discrete uniform distribution is the mathematical formalization of **equally likely outcomes**. If a sample space has $n$ outcomes and all are equally likely, then any numerical function of the outcome follows a discrete uniform or a function of it.

## CDF

The CDF of $X \sim \text{DiscreteUniform}(1, \ldots, n)$ is a **staircase function**:

$$F(x) = \frac{\lfloor x \rfloor}{n}, \quad 1 \leq x \leq n$$

## MGF

The moment generating function is:

$$M_X(t) = \frac{1}{n}\sum_{k=1}^{n} e^{tk} = \frac{e^t(1 - e^{nt})}{n(1 - e^t)}, \quad t \neq 0$$

This is a geometric series with ratio $e^t$.

## Sum of Independent Discrete Uniforms

If $X_1, X_2$ are independent $\text{DiscreteUniform}(1, \ldots, n)$, the PMF of $S = X_1 + X_2$ is a **triangular** shape on $\{2, 3, \ldots, 2n\}$:

$$P(S = s) = \frac{n - |s - (n+1)|}{n^2}$$

The most familiar case is rolling two dice: $P(S = 7)$ is maximal.

## Python Implementation

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

fig, axes = plt.subplots(1, 3, figsize=(16, 5))

# --- Panel 1: PMF and CDF for different n ---
for n, color in zip([4, 6, 10], ['blue', 'red', 'green']):
    vals = np.arange(1, n + 1)
    pmf = np.ones(n) / n
    axes[0].bar(vals + (n - 6) * 0.15, pmf, width=0.3, alpha=0.6,
                color=color, label=f'n={n}, E={n/2+.5:.1f}')

axes[0].set_title('Discrete Uniform PMF')
axes[0].set_xlabel('x')
axes[0].set_ylabel('P(X=x)')
axes[0].legend()
axes[0].grid(True, alpha=0.3)

# --- Panel 2: Sum of two dice ---
n_die = 6
sums = np.arange(2, 2 * n_die + 1)
pmf_sum = np.array([min(s - 1, 2 * n_die + 1 - s)
                     for s in sums]) / n_die**2

axes[1].bar(sums, pmf_sum, color='steelblue', alpha=0.7)
axes[1].set_title('Sum of Two Fair Dice')
axes[1].set_xlabel('Sum')
axes[1].set_ylabel('Probability')
for s, p in zip(sums, pmf_sum):
    axes[1].text(s, p + 0.005, f'{p:.3f}', ha='center', fontsize=7, rotation=45)
axes[1].grid(True, alpha=0.3)

# --- Panel 3: CLT for sum of discrete uniforms ---
np.random.seed(42)
n_sim = 100000
ns_sum = [1, 2, 5, 12]
n_die = 6

for n, color in zip(ns_sum, ['red', 'orange', 'green', 'blue']):
    s = np.sum(np.random.randint(1, n_die + 1, (n_sim, n)), axis=1)
    axes[2].hist(s, bins=range(n, n * n_die + 2), density=True,
                 alpha=0.3, color=color, label=f'n={n}')

    # Normal approximation
    mu = n * 3.5
    sigma = np.sqrt(n * 35 / 12)
    x = np.linspace(n, n * n_die, 200)
    axes[2].plot(x, stats.norm.pdf(x, mu, sigma), color=color, lw=1.5)

axes[2].set_title('Sum of n Dice → Normal (CLT)')
axes[2].set_xlabel('Sum')
axes[2].legend(fontsize=9)
axes[2].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('discrete_uniform_properties.png', dpi=150, bbox_inches='tight')
plt.show()
```
