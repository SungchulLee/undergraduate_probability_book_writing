# Conditional Expectation Given an Event

Conditioning on an event replaces ordinary probabilities with conditional ones; the result is a number, not a random variable.

## Definition

The **conditional expectation of $X$ given $Y = y$** uses the conditional distribution of $X \mid Y = y$:

**Discrete:**

$$
E[X \mid Y = y] = \sum_x x \, P(X = x \mid Y = y)
$$

**Continuous:**

$$
E[X \mid Y = y] = \int_{-\infty}^{\infty} x \, f_{X \mid Y}(x \mid y) \, dx
$$

**Conditional LOTUS.** For any function $g$:

$$
E[g(X) \mid Y = y] = \begin{cases} \displaystyle\sum_x g(x)\,P(X = x \mid Y = y) & \text{(discrete)} \\[8pt] \displaystyle\int g(x)\,f_{X \mid Y}(x \mid y)\,dx & \text{(continuous)} \end{cases}
$$

## Explanation

### It Is a Number

For each fixed value $y$, $E[X \mid Y = y]$ is a single number — the weighted average of $X$ under the conditional distribution. Different values of $y$ generally produce different numbers, but each one is deterministic.

### Parallel with Unconditional Expectation

Every unconditional expectation formula has a conditional twin: replace marginal probabilities or densities with conditional ones. The shortcut formula also carries over:

$$
\text{Var}(X \mid Y = y) = E[X^2 \mid Y = y] - \bigl(E[X \mid Y = y]\bigr)^2
$$

### Properties

Conditional expectation given an event inherits all the usual linearity properties:

- **Linearity:** $E[aX + bZ \mid Y = y] = a\,E[X \mid Y = y] + b\,E[Z \mid Y = y]$
- **Constants pull out:** $E[c \mid Y = y] = c$
- **Independence simplification:** If $X \perp Y$, then $E[X \mid Y = y] = E[X]$

## Examples

**Example.** Joint PDF $f(x,y) = e^{-x/y}\,e^{-y}/y$ for $x > 0$, $y > 0$.

The conditional density of $X \mid Y = y$ is proportional to $e^{-x/y}/y$, which is $\text{Exp}(1/y)$. Therefore:

$$
E[X \mid Y = y] = y, \qquad \text{Var}(X \mid Y = y) = y^2
$$

```python
import numpy as np

np.random.seed(42)
n_sim = 200_000

# Sample Y ~ Exp(1), then X | Y=y ~ Exp(1/y)
Y = np.random.exponential(1, n_sim)
X = np.array([np.random.exponential(y) for y in Y])

# Verify E[X | Y=y] = y for a few values
for y_val in [0.5, 1.0, 2.0]:
    mask = (Y > y_val - 0.05) & (Y < y_val + 0.05)
    if mask.sum() > 100:
        print(f"E[X | Y≈{y_val}] = {X[mask].mean():.3f}  (theory: {y_val})")
```
