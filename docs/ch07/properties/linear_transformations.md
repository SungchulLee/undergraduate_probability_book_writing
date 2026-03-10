# Variance Under Linear Transformations

Shifting a random variable changes its mean but not its variance; scaling by $a$ multiplies the variance by $a^2$.

## Definition

For constants $a, b$:

$$
E[aX + b] = a\,E[X] + b
$$

$$
\text{Var}(aX + b) = a^2\,\text{Var}(X)
$$

## Explanation

### Proof

$$
\text{Var}(aX + b) = E[(aX + b - aE[X] - b)^2] = E[a^2(X - E[X])^2] = a^2\,\text{Var}(X)
$$

### Covariance Properties

1. $\text{Var}(X) = \text{Cov}(X, X)$
2. $\text{Cov}(aX + bY, Z) = a\,\text{Cov}(X, Z) + b\,\text{Cov}(Y, Z)$ (bilinearity)
3. $\text{Cov}(X, Y) = \text{Cov}(Y, X)$ (symmetry)
4. $\text{Cov}(X, c) = 0$ for any constant $c$
5. $X \perp Y \implies \text{Cov}(X, Y) = 0$ (converse is false)

!!! warning "Zero covariance does not imply independence"
    $\text{Cov}(X, Y) = 0$ means no *linear* relationship. $X$ and $Y$ can still be dependent.

## Examples

**Example.** $\text{Var}(X) = 2$, $\text{Var}(Y) = 2$, $\text{Var}(Z) = 3$, $\text{Cov}(X,Y) = 0.25$, $Z$ independent of both.

$V = X + 2Y - 3Z - 2$.

$$
\text{Var}(V) = \text{Var}(X) + 4\,\text{Var}(Y) + 9\,\text{Var}(Z) + 2 \cdot 2\,\text{Cov}(X,Y)
$$

$$
= 2 + 8 + 27 + 1 = 38
$$

```python
import numpy as np

np.random.seed(42)
N = 1_000_000

# Simulate: Var(X)=2, Var(Y)=2, Cov(X,Y)=0.25
mean = [0, 0]
cov_matrix = [[2, 0.25], [0.25, 2]]
XY = np.random.multivariate_normal(mean, cov_matrix, N)
X, Y = XY[:, 0], XY[:, 1]
Z = np.random.normal(0, np.sqrt(3), N)

V = X + 2*Y - 3*Z - 2
print(f"Var(V): theory = 38, MC = {V.var():.2f}")
```
