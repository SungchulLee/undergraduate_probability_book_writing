# Expectation of Products

For independent random variables, the expectation of a product equals the product of expectations.

## Definition

If $X_1, \ldots, X_n$ are **mutually independent**, then

$$
E\!\left[\prod_{i=1}^n X_i\right] = \prod_{i=1}^n E[X_i]
$$

More generally, if $X$ and $Y$ are independent, then for any functions $g$ and $h$:

$$
E[g(X)\,h(Y)] = E[g(X)]\,E[h(Y)]
$$

## Explanation

### Proof (Two Variables, Continuous)

$$
E[XY] = \int\!\!\int xy\,f_{X,Y}(x,y)\,dx\,dy = \int\!\!\int xy\,f_X(x)\,f_Y(y)\,dx\,dy = \left(\int x\,f_X(x)\,dx\right)\!\left(\int y\,f_Y(y)\,dy\right)
$$

The key step uses the factorization $f_{X,Y}(x,y) = f_X(x)\,f_Y(y)$, which is the definition of independence.

### When Independence Fails

Without independence, $E[XY] \ne E[X]\,E[Y]$ in general. The difference is exactly the covariance:

$$
E[XY] = E[X]\,E[Y] + \text{Cov}(X, Y)
$$

### Important Non-Example

Pairwise independence is **not** sufficient for the $n$-fold product formula. Mutual independence is required.

## Examples

**Example.** $X \sim \text{Uniform}(0,1)$, $Y \sim \text{Exp}(1)$, independent. Then:

$$
E[XY] = E[X]\,E[Y] = \frac{1}{2} \cdot 1 = \frac{1}{2}
$$

For dependent variables: $X \sim N(0,1)$, $Y = X$. Then $E[XY] = E[X^2] = 1 \ne 0 = E[X]\,E[Y]$.

```python
import numpy as np

np.random.seed(42)
n_sim = 200_000

# Independent case
X = np.random.uniform(0, 1, n_sim)
Y = np.random.exponential(1, n_sim)
print(f"E[XY] = {np.mean(X*Y):.4f}  (theory: 0.5)")
print(f"E[X]*E[Y] = {X.mean()*Y.mean():.4f}")

# Dependent case: Y = X
X2 = np.random.standard_normal(n_sim)
Y2 = X2  # perfectly dependent
print(f"\nDependent: E[XY] = {np.mean(X2*Y2):.4f}  (= E[X^2] = 1)")
print(f"E[X]*E[Y] = {X2.mean()*Y2.mean():.6f}  (≈ 0)")
```
