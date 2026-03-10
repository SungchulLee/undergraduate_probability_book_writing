# Functions of a Random Variable

If $X$ is a random variable and $g$ is a function, then $Y = g(X)$ is also a random variable whose distribution is determined by $g$ and the distribution of $X$.

## Definition

Let $X$ be a random variable and $g : \mathbb{R} \to \mathbb{R}$. The **function of a random variable** $Y = g(X)$ is itself a random variable, defined by $Y(\omega) = g(X(\omega))$ for each $\omega \in \Omega$.

**Discrete case:** If $X$ is discrete with PMF $p_X(x)$, then

$$
p_Y(y) = P(Y = y) = \sum_{x:\, g(x) = y} p_X(x)
$$

**Continuous case:** Use the CDF method or the change-of-variables formula (covered in the continuous functions page).

## Explanation

### Why Functions of Random Variables

Many quantities of interest are functions of simpler random variables:

- Squared deviations: $Y = (X - \mu)^2$
- Financial payoffs: $Y = \max(X - K, 0)$
- Indicators: $Y = \mathbf{1}(X > c)$
- Symmetric random walks: $Y = 2X - 1$ converts $\text{Bern}(1/2)$ to $\pm 1$

### The Grouping Principle (Discrete)

When $g$ is not one-to-one, multiple values of $X$ map to the same value of $Y$. The PMF of $Y$ collects (groups) these probabilities. The number of distinct values of $Y$ can be smaller than that of $X$.

### Bernoulli to Symmetric Walk

If $X \sim \text{Bern}(p)$, then $Y = 2X - 1$ gives

$$
P(Y = +1) = p, \qquad P(Y = -1) = 1 - p
$$

For $p = 1/2$, this converts a coin flip into the symmetric $\pm 1$ step used in random walks.

## Examples

**Example.** Let $X$ take values $-2, -1, 0, 1, 2$ each with probability $1/5$. Let $Y = X^2$.

| $x$ | $-2$ | $-1$ | $0$ | $1$ | $2$ |
|:---:|:---:|:---:|:---:|:---:|:---:|
| $g(x) = x^2$ | $4$ | $1$ | $0$ | $1$ | $4$ |
| $p_X(x)$ | $1/5$ | $1/5$ | $1/5$ | $1/5$ | $1/5$ |

Grouping by $y$:

| $y$ | $0$ | $1$ | $4$ |
|:---:|:---:|:---:|:---:|
| $p_Y(y)$ | $1/5$ | $2/5$ | $2/5$ |

Five values of $X$ collapse to three values of $Y$ because $g(x) = x^2$ is not one-to-one.

```python
import numpy as np
from collections import Counter

# X takes values -2, -1, 0, 1, 2 with equal probability
x_vals = [-2, -1, 0, 1, 2]
px = {x: 1/5 for x in x_vals}

# Y = X^2
g = lambda x: x**2
py = Counter()
for x, prob in px.items():
    py[g(x)] += prob

for y in sorted(py):
    print(f"P(Y = {y}) = {py[y]:.4f}")
print(f"Sum = {sum(py.values()):.4f}")
```
