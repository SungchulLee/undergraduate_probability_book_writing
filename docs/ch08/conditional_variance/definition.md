# Conditional Variance

Conditional variance measures the residual spread of $X$ after learning $Y$ — the uncertainty that remains even when $Y$ is known.

## Definition

**As a number.** For fixed $y$:

$$
\text{Var}(X \mid Y = y) = E\bigl[(X - E[X \mid Y = y])^2 \mid Y = y\bigr]
$$

**Shortcut formula:**

$$
\text{Var}(X \mid Y = y) = E[X^2 \mid Y = y] - \bigl(E[X \mid Y = y]\bigr)^2
$$

**As a random variable.** Letting $y$ vary:

$$
\text{Var}(X \mid Y) = E[X^2 \mid Y] - (E[X \mid Y])^2
$$

## Explanation

### Interpretation

$\text{Var}(X \mid Y = y)$ quantifies how spread out $X$ remains after observing $Y = y$. Two extreme cases:

- **$\text{Var}(X \mid Y) = 0$:** Knowing $Y$ determines $X$ exactly ($X$ is a function of $Y$)
- **$\text{Var}(X \mid Y) = \text{Var}(X)$:** Knowing $Y$ provides no information ($X \perp Y$)

In general, $\text{Var}(X \mid Y)$ itself varies with $Y$ — some values of $Y$ may reduce uncertainty more than others.

### Relationship to $E[X \mid Y]$

The conditional variance captures what the conditional expectation misses. $E[X \mid Y]$ gives the best prediction of $X$ from $Y$; $\text{Var}(X \mid Y)$ gives the expected squared prediction error:

$$
\text{Var}(X \mid Y) = E\bigl[(X - E[X \mid Y])^2 \mid Y\bigr]
$$

## Examples

**Example.** Joint PDF $f(x,y) = e^{-x/y}\,e^{-y}/y$ for $x, y > 0$. Since $X \mid Y = y \sim \text{Exp}(1/y)$:

$$
E[X \mid Y = y] = y, \qquad \text{Var}(X \mid Y = y) = y^2
$$

As random variables: $E[X \mid Y] = Y$ and $\text{Var}(X \mid Y) = Y^2$. The residual uncertainty grows quadratically with $Y$ — large values of $Y$ produce more spread in $X$.

```python
import numpy as np

np.random.seed(42)
n_sim = 200_000

Y = np.random.exponential(1, n_sim)
X = np.array([np.random.exponential(y) for y in Y])

# Verify conditional variance for Y near specific values
for y_val in [0.5, 1.0, 2.0]:
    mask = (Y > y_val - 0.05) & (Y < y_val + 0.05)
    if mask.sum() > 100:
        cond_var = X[mask].var()
        print(f"Var(X | Y≈{y_val}) = {cond_var:.3f}  (theory: {y_val**2:.2f})")

# Compare: unconditional variance should be larger
print(f"\nVar(X) = {X.var():.3f}")
print(f"E[Var(X|Y)] = {np.mean(Y**2):.3f}")
```
