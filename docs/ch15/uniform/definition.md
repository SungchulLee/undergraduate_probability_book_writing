# Continuous Uniform Distribution


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

## Definition

!!! info "Continuous Uniform Distribution"
    A continuous random variable $X$ has the **Uniform distribution** on the interval $(a, b)$, written $X \sim U(a, b)$, if its PDF is:

    $$f(x) = \frac{1}{b - a}, \quad a < x < b$$

    Every value in the interval $(a, b)$ is equally likely in the sense that the probability of falling in any subinterval depends only on the subinterval's length.

### CDF

$$F(x) = \begin{cases} 0 & x \leq a \\ \dfrac{x - a}{b - a} & a < x < b \\ 1 & x \geq b \end{cases}$$

### Intuition from the Poisson Process

If a Poisson process $\text{NPP}(\lambda)$ has exactly one arrival in the interval $[a, b]$, then the position of that arrival is uniformly distributed on $[a, b]$. More generally, given $N([a,b]) = n$, the $n$ arrival positions are distributed as $n$ iid $U(a, b)$ random variables (after ordering, they become order statistics).

## Mean and Variance

!!! info "Moments of U(a, b)"

    $$E[X] = \frac{a + b}{2}, \qquad \text{Var}(X) = \frac{(b - a)^2}{12}$$

### Derivation of the Mean

$$E[X] = \int_a^b x f(x) \, dx = \frac{1}{b - a} \int_a^b x \, dx = \frac{1}{b - a} \left[\frac{x^2}{2}\right]_a^b = \frac{b^2 - a^2}{2(b-a)}$$

Using the factorization $a^2 - b^2 = (a+b)(a-b)$:

$$E[X] = \frac{(b+a)(b-a)}{2(b-a)} = \frac{a + b}{2}$$

### Derivation of the Variance

First compute $E[X^2]$:

$$E[X^2] = \int_a^b x^2 f(x) \, dx = \frac{1}{b - a} \int_a^b x^2 \, dx = \frac{1}{b - a} \left[\frac{x^3}{3}\right]_a^b = \frac{b^3 - a^3}{3(b-a)}$$

Using the factorization $a^3 - b^3 = (a - b)(a^2 + ab + b^2)$:

$$E[X^2] = \frac{(b - a)(b^2 + ab + a^2)}{3(b - a)} = \frac{a^2 + ab + b^2}{3}$$

Therefore:

$$\text{Var}(X) = E[X^2] - (E[X])^2 = \frac{a^2 + ab + b^2}{3} - \frac{(a+b)^2}{4}$$

$$= \frac{4(a^2 + ab + b^2) - 3(a^2 + 2ab + b^2)}{12} = \frac{a^2 - 2ab + b^2}{12} = \frac{(b - a)^2}{12}$$

### Useful Algebraic Identities

The derivations above use two factoring identities that appear frequently:

$$a^2 - b^2 = (a + b)(a - b)$$

$$a^3 - b^3 = (a - b)(a^2 + ab + b^2)$$

Also useful: $a^3 + b^3 = (a + b)(a^2 - ab + b^2)$.

## The Standard Uniform U(0, 1)

The most important special case is $U(0, 1)$:

$$f(x) = 1, \quad 0 < x < 1, \qquad F(x) = x, \quad 0 \leq x \leq 1$$

$$E[X] = \frac{1}{2}, \qquad \text{Var}(X) = \frac{1}{12}$$

The standard uniform is the foundation for random number generation and simulation.

## Python Implementation

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

fig, axes = plt.subplots(1, 3, figsize=(15, 4))

# PDF and CDF for different intervals
intervals = [(0, 1), (-2, 3), (1, 4)]
colors = ['blue', 'red', 'green']

for (a, b), color in zip(intervals, colors):
    x = np.linspace(a - 1, b + 1, 300)
    pdf = stats.uniform.pdf(x, loc=a, scale=b-a)
    cdf = stats.uniform.cdf(x, loc=a, scale=b-a)

    axes[0].plot(x, pdf, color=color, lw=2, label=f'U({a},{b})')
    axes[1].plot(x, cdf, color=color, lw=2, label=f'U({a},{b})')

axes[0].set_title('PDF of Uniform Distribution')
axes[0].set_xlabel('x')
axes[0].set_ylabel('f(x)')
axes[0].legend()
axes[0].grid(True, alpha=0.3)

axes[1].set_title('CDF of Uniform Distribution')
axes[1].set_xlabel('x')
axes[1].set_ylabel('F(x)')
axes[1].legend()
axes[1].grid(True, alpha=0.3)

# Verify mean and variance via simulation
np.random.seed(42)
n_sim = 100000
a, b = 2, 8
X = np.random.uniform(a, b, n_sim)

axes[2].hist(X, bins=50, density=True, alpha=0.7, color='steelblue')
axes[2].axvline(np.mean(X), color='red', lw=2, linestyle='--',
                label=f'Sample mean = {np.mean(X):.3f}')
axes[2].axvline((a+b)/2, color='black', lw=2, linestyle=':',
                label=f'Theory mean = {(a+b)/2:.3f}')
axes[2].set_title(f'U({a},{b}) Simulation')
axes[2].legend()
axes[2].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('uniform_definition.png', dpi=150, bbox_inches='tight')
plt.show()

print(f"U({a},{b}): E[X] = {np.mean(X):.4f} (theory {(a+b)/2:.4f})")
print(f"U({a},{b}): Var(X) = {np.var(X):.4f} (theory {(b-a)**2/12:.4f})")
```
