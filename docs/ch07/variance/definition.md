# Variance

Variance measures the spread of a distribution around its mean — the expected squared deviation from the center.

## Definition

The **variance** of a random variable $X$ with mean $\mu = E[X]$ is

$$
\text{Var}(X) = E[(X - \mu)^2]
$$

**Discrete:** $\text{Var}(X) = \sum_x (x - \mu)^2\,p(x)$

**Continuous:** $\text{Var}(X) = \int_{-\infty}^{\infty}(x - \mu)^2\,f(x)\,dx$

## Explanation

### Properties

1. $\text{Var}(X) \ge 0$, with equality iff $X$ is constant a.s.
2. $\text{Var}(c) = 0$
3. $\text{Var}(aX + b) = a^2\,\text{Var}(X)$ (constants shift the mean but only scaling affects spread)
4. $\text{Var}(X)$ exists iff $E[X^2] < \infty$

### Shortcut Formula

$$
\text{Var}(X) = E[X^2] - (E[X])^2
$$

Often easier to compute since it avoids centering inside the square.

!!! warning "Numerical caution"
    The shortcut formula can suffer from catastrophic cancellation when $E[X^2]$ and $(E[X])^2$ are large and close. For numerical work, use stable one-pass algorithms.

## Examples

**Example 1.** $X \sim \text{Bern}(p)$: $E[X] = p$, $E[X^2] = p$, so $\text{Var}(X) = p - p^2 = p(1-p)$.

**Example 2.** Fair die: $E[X] = 3.5$, $E[X^2] = 91/6$, so $\text{Var}(X) = 91/6 - 12.25 = 35/12 \approx 2.917$.

**Example 3.** $X \sim \text{Uniform}(a,b)$: $\text{Var}(X) = (b-a)^2/12$.

```python
import numpy as np

# Fair die
values = np.arange(1, 7)
E_X = values.mean()
E_X2 = (values**2).mean()
print(f"Var(die) = {E_X2 - E_X**2:.4f}")

# Bernoulli
p = 0.3
print(f"Var(Bern({p})) = {p*(1-p):.4f}")

# Uniform(0,1)
print(f"Var(U(0,1)) = {1/12:.4f}")
```
