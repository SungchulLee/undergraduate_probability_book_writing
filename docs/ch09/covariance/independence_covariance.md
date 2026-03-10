# Independence Implies Zero Covariance

Independent random variables are always uncorrelated, but uncorrelated random variables need not be independent.

## Definition

If $X$ and $Y$ are **independent**, then

$$
\text{Cov}(X, Y) = 0 \quad \text{equivalently} \quad E[XY] = E[X]\,E[Y]
$$

The converse is **false**: $\text{Cov}(X, Y) = 0$ does not imply independence.

## Explanation

### Proof

If $X \perp Y$, then $E[XY] = E[X]\,E[Y]$ (the expectation of a product of independent variables factors). By the shortcut formula:

$$
\text{Cov}(X, Y) = E[XY] - E[X]\,E[Y] = 0
$$

### Why the Converse Fails

Covariance only measures *linear* association. Two variables can be strongly dependent through a nonlinear relationship yet have zero covariance.

**Classic counterexample:** $X \sim \text{Uniform}(-1, 1)$ and $Y = X^2$.

- $E[XY] = E[X^3] = 0$ (odd function, symmetric distribution)
- $E[X]\,E[Y] = 0 \cdot E[X^2] = 0$
- So $\text{Cov}(X, Y) = 0$, yet $Y$ is completely determined by $X$

### Uncorrelated vs Independent

| Property | Uncorrelated | Independent |
|:---------|:-------------|:------------|
| Definition | $\text{Cov}(X,Y) = 0$ | $P(X \in A, Y \in B) = P(X \in A)\,P(Y \in B)$ for all $A, B$ |
| Implies the other? | No | Yes |
| Variance of sum | $\text{Var}(X+Y) = \text{Var}(X) + \text{Var}(Y)$ | Same (since independent $\Rightarrow$ uncorrelated) |
| $E[g(X)h(Y)] = E[g(X)]E[h(Y)]$? | Only for $g(x) = x$, $h(y) = y$ | For all measurable $g, h$ |

### Special Case: Joint Normal

For **jointly normal** random variables, uncorrelated *does* imply independent. This is one of the few cases where the converse holds.

## Examples

**Example.** $X \sim \text{Uniform}(-1, 1)$, $Y = X^2$.

```python
import numpy as np

np.random.seed(42)
n_sim = 200_000

X = np.random.uniform(-1, 1, n_sim)
Y = X**2

cov = np.mean((X - X.mean()) * (Y - Y.mean()))
rho = np.corrcoef(X, Y)[0, 1]

print(f"Cov(X, X^2) = {cov:.6f}  (theory: 0)")
print(f"Corr(X, X^2) = {rho:.6f}  (theory: 0)")
print(f"But Y = X^2, so clearly dependent!")

# Compare: jointly normal -> uncorrelated implies independent
from scipy import stats
mu = [0, 0]
Sigma = [[1, 0], [0, 1]]  # uncorrelated
XY = np.random.multivariate_normal(mu, Sigma, n_sim)
X_n, Y_n = XY[:, 0], XY[:, 1]

# Check factorization: P(X>0, Y>0) = P(X>0)*P(Y>0)?
p_joint = np.mean((X_n > 0) & (Y_n > 0))
p_product = np.mean(X_n > 0) * np.mean(Y_n > 0)
print(f"\nJoint normal, rho=0:")
print(f"P(X>0, Y>0) = {p_joint:.4f}")
print(f"P(X>0)*P(Y>0) = {p_product:.4f}  (match => independent)")
```
