# Functions of a Discrete Random Variable

## Motivation

Given a random variable $X$ with known distribution, we often need the distribution of $Y = g(X)$ for some function $g$. For example:

- $Y = X^2$ (squared deviations)
- $Y = |X|$ (absolute value)
- $Y = \mathbf{1}(X > 0)$ (indicator)
- $Y = \max(X, 0)$ (payoff of a call option)

## The Discrete Case

When $X$ is discrete, finding the distribution of $Y = g(X)$ is straightforward: group the values of $X$ that map to the same value of $Y$.

!!! info "PMF of g(X) — Discrete Case"
    If $X$ is discrete with PMF $p_X(x)$ and $Y = g(X)$, then $Y$ is discrete with PMF:

    $$p_Y(y) = P(Y = y) = \sum_{x:\, g(x) = y} p_X(x)$$

    That is, sum the probabilities of all $x$ values that map to $y$.

## Example: Squaring a Symmetric Distribution

Let $X$ take values $-2, -1, 0, 1, 2$ with equal probability $\frac{1}{5}$ each. Let $Y = X^2$.

| $x$ | $-2$ | $-1$ | $0$ | $1$ | $2$ |
|:---:|:---:|:---:|:---:|:---:|:---:|
| $g(x) = x^2$ | $4$ | $1$ | $0$ | $1$ | $4$ |
| $p_X(x)$ | \$1/5$ | \$1/5$ | \$1/5$ | \$1/5$ | \$1/5$ |

Grouping by $y$ values:

| $y$ | $0$ | $1$ | $4$ |
|:---:|:---:|:---:|:---:|
| $p_Y(y)$ | \$1/5$ | \$2/5$ | \$2/5$ |

Note that $Y$ takes only 3 values even though $X$ takes 5 — the function $g(x) = x^2$ is **not one-to-one**, so multiple $x$ values collapse to the same $y$.

## Example: Indicator Function

Let $X \sim \text{Binomial}(10, 0.3)$ and $Y = \mathbf{1}(X \geq 5)$. Then $Y$ is Bernoulli:

$$p_Y(1) = P(X \geq 5), \qquad p_Y(0) = P(X < 5)$$

This demonstrates that applying a function can drastically simplify the distribution.

## Example: Maximum with Zero

Let $X \sim \text{Uniform}\{-3, -2, -1, 0, 1, 2, 3\}$ and $Y = \max(X, 0)$. Then:

$$p_Y(0) = P(X \leq 0) = \frac{4}{7}, \quad p_Y(1) = p_Y(2) = p_Y(3) = \frac{1}{7}$$

This is a **mixed** case: $Y$ has a point mass at $0$ even though $X$ has no special concentration there.

## Python Implementation

```python
import numpy as np
import matplotlib.pyplot as plt

fig, axes = plt.subplots(1, 3, figsize=(16, 4.5))

# --- Example 1: X^2 ---
x_vals = np.array([-2, -1, 0, 1, 2])
px = np.ones(5) / 5
y_vals = x_vals**2

axes[0].bar(x_vals - 0.15, px, width=0.3, color='steelblue', alpha=0.7, label='X')
# Compute Y PMF
unique_y = np.unique(y_vals)
py = np.array([px[y_vals == y].sum() for y in unique_y])
axes[0].bar(unique_y + 0.15, py, width=0.3, color='coral', alpha=0.7, label='Y = X²')
axes[0].set_title('Y = X² (many-to-one)')
axes[0].set_xlabel('Value')
axes[0].set_ylabel('Probability')
axes[0].legend()
axes[0].grid(True, alpha=0.3)

# --- Example 2: Indicator ---
from scipy.stats import binom
n, p = 10, 0.3
x_binom = np.arange(0, 11)
px_binom = binom.pmf(x_binom, n, p)

p_y1 = px_binom[5:].sum()
p_y0 = px_binom[:5].sum()

axes[1].bar(x_binom, px_binom, color='steelblue', alpha=0.5, label='X ~ Bin(10, 0.3)')
axes[1].bar([0, 1], [p_y0, p_y1], color='coral', alpha=0.7, width=0.4,
            label=f'Y = 1(X≥5): P(0)={p_y0:.3f}, P(1)={p_y1:.3f}')
axes[1].set_title('Indicator: Y = 1(X ≥ 5)')
axes[1].set_xlabel('Value')
axes[1].legend(fontsize=8)
axes[1].grid(True, alpha=0.3)

# --- Example 3: max(X, 0) ---
x_unif = np.arange(-3, 4)
px_unif = np.ones(7) / 7
y_max = np.maximum(x_unif, 0)

unique_ym = np.unique(y_max)
py_max = np.array([px_unif[y_max == y].sum() for y in unique_ym])

axes[2].bar(unique_ym, py_max, color='coral', alpha=0.7)
axes[2].set_title('Y = max(X, 0) — point mass at 0')
axes[2].set_xlabel('y')
axes[2].set_ylabel('P(Y = y)')
for y, p in zip(unique_ym, py_max):
    axes[2].text(y, p + 0.02, f'{p:.2f}', ha='center', fontsize=9)
axes[2].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('functions_discrete.png', dpi=150, bbox_inches='tight')
plt.show()
```
