# Local Average Interpretation

$E[X \mid Y]$ acts as a local average: it replaces each value of $X$ with the average of $X$ over outcomes sharing the same $Y$ value.

## Definition

$E[X \mid Y]$ is a **smoothed version** of $X$. For each group of outcomes with $Y = y$, it assigns the value $E[X \mid Y = y]$ — the average of $X$ within that group.

As a random variable, $E[X \mid Y]$ satisfies two fundamental identities:

$$
E\bigl[E[X \mid Y]\bigr] = E[X] \qquad \text{(tower property)}
$$

$$
\text{Var}\bigl(E[X \mid Y]\bigr) \le \text{Var}(X) \qquad \text{(conditioning reduces variance)}
$$

## Explanation

### Why Variance Decreases

Averaging within groups smooths out variation. The random variable $E[X \mid Y]$ keeps only the variation *between* groups (explained by $Y$) and discards the variation *within* groups. Since both components are non-negative, the smoothed version can never be more variable than the original.

### Best Predictor

Among all functions $g(Y)$, the conditional expectation $E[X \mid Y]$ minimizes the mean squared error:

$$
E[X \mid Y] = \arg\min_{g(Y)} E\bigl[(X - g(Y))^2\bigr]
$$

This makes $E[X \mid Y]$ the best predictor of $X$ given $Y$ in the least-squares sense.

### Connection to Regression

In statistics, the regression function $m(y) = E[X \mid Y = y]$ describes how the mean of $X$ changes with $Y$. Linear regression approximates this function by a line $a + bY$, but the true regression function can be any shape.

## Examples

**Example.** Three fair coin flips with $X$ = total heads, $Y$ = first-flip indicator.

| Outcome | HHH | HHT | HTH | HTT | THH | THT | TTH | TTT |
|:--------|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| $X$     |  3  |  2  |  2  |  1  |  2  |  1  |  1  |  0  |
| $E[X \mid Y]$ | 2 | 2 | 2 | 2 | 1 | 1 | 1 | 1 |

Outcomes with $Y = 1$ all get the group average 2; outcomes with $Y = 0$ all get 1. The smoothed variable has $\text{Var}(E[X \mid Y]) = 1/4$, while $\text{Var}(X) = 3/4$.

```python
import numpy as np

np.random.seed(42)
n_sim = 200_000

flips = np.random.randint(0, 2, size=(n_sim, 3))
X = flips.sum(axis=1)
Y = flips[:, 0]

# Build E[X|Y] as a random variable
E_XY = np.where(Y == 1, 2.0, 1.0)

print(f"Var(X)       = {X.var():.4f}  (theory: 0.75)")
print(f"Var(E[X|Y])  = {E_XY.var():.4f}  (theory: 0.25)")
print(f"Ratio        = {E_XY.var() / X.var():.4f}  (theory: 1/3)")

# Best predictor check: MSE of E[X|Y] vs using E[X]
mse_cond = np.mean((X - E_XY)**2)
mse_uncond = np.mean((X - X.mean())**2)
print(f"\nMSE using E[X|Y]: {mse_cond:.4f}")
print(f"MSE using E[X]:   {mse_uncond:.4f}")
```
