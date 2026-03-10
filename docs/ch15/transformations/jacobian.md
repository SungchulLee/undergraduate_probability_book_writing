# Jacobian Method for Joint Transformations

The Jacobian method extends the single-variable change of variables formula to multivariate transformations, allowing us to find the joint PDF of transformed random vectors using the determinant of the matrix of partial derivatives.

## Definition

If $(X, Y)$ has joint PDF $f_{X,Y}(x, y)$ and $(U, V) = g(X, Y)$ is a bijective transformation with inverse $x = x(u, v)$, $y = y(u, v)$, then:

$$
f_{U,V}(u, v) = f_{X,Y}(x(u,v),\; y(u,v)) \left|\frac{\partial(x, y)}{\partial(u, v)}\right|
$$

where the **Jacobian determinant** is:

$$
\left|\frac{\partial(x, y)}{\partial(u, v)}\right| = \left|\det \begin{pmatrix} \dfrac{\partial x}{\partial u} & \dfrac{\partial x}{\partial v} \\[6pt] \dfrac{\partial y}{\partial u} & \dfrac{\partial y}{\partial v} \end{pmatrix}\right|
$$

In $n$ dimensions, for a bijective transformation $(Y_1, \ldots, Y_n) = g(X_1, \ldots, X_n)$:

$$
f_{Y_1,\ldots,Y_n}(\mathbf{y}) = f_{X_1,\ldots,X_n}(\mathbf{x}) \left|\det\!\left(\frac{\partial \mathbf{x}}{\partial \mathbf{y}}\right)\right|
$$

## Explanation

### Geometric intuition

The Jacobian accounts for how the transformation distorts areas (or volumes in higher dimensions):

- A small rectangle $du \times dv$ in $(u, v)$-space maps to a parallelogram in $(x, y)$-space.
- The area of that parallelogram is $\left|\frac{\partial(x,y)}{\partial(u,v)}\right| du \, dv$.
- Since probability equals density times area: $f_{U,V}(u, v)\,du\,dv = f_{X,Y}(x, y) \cdot |J|\,du\,dv$.

### The inverse Jacobian property

It is often easier to compute the "forward" Jacobian and take its reciprocal:

$$
\left|\frac{\partial(x, y)}{\partial(u, v)}\right| = \frac{1}{\left|\dfrac{\partial(u, v)}{\partial(x, y)}\right|}
$$

This is because $\frac{\partial(x,y)}{\partial(u,v)}$ and $\frac{\partial(u,v)}{\partial(x,y)}$ are matrix inverses of each other, and the determinant of an inverse equals the reciprocal of the determinant.

### Strategy for multivariate transformations

When transforming $(X, Y)$ to find the distribution of $U = h(X, Y)$:

1. **Define an auxiliary variable.** Choose $V$ to make $(U, V) = g(X, Y)$ a bijection. Common choices: $V = Y$, $V = X + Y$, or $V = X$.
2. **Find the inverse.** Express $x$ and $y$ in terms of $u$ and $v$.
3. **Compute the Jacobian.** Calculate the $2 \times 2$ determinant.
4. **Transform the density.** Multiply $f_{X,Y}$ evaluated at the inverse by $|J|$.
5. **Marginalize.** Integrate out $v$ to get $f_U(u)$.

### When to use CDF versus Jacobian

| Method | When to use | Advantages |
|:---|:---|:---|
| **CDF method** | Always works | Handles non-monotone transformations |
| **Jacobian (1D)** | $Y = g(X)$, $g$ monotone | Direct formula, no integration step |
| **Jacobian (2D+)** | Bijective joint transformation | Systematic for joint densities |

### Key application: Gamma-to-Beta derivation

The Jacobian method proves that if $X \sim \Gamma(\alpha, \lambda)$ and $Y \sim \Gamma(\beta, \lambda)$ are independent, then $F = X/(X+Y) \sim \text{Beta}(\alpha, \beta)$ and $T = X + Y \sim \Gamma(\alpha + \beta, \lambda)$, with $F$ and $T$ independent.

The transformation $x = tf$, $y = t(1-f)$ has Jacobian:

$$
\left|\frac{\partial(x,y)}{\partial(t,f)}\right| = \left|\det \begin{pmatrix} f & t \\ 1-f & -t \end{pmatrix}\right| = |-ft - t(1-f)| = t
$$

The joint density factors, proving both the distributions and the independence.

## Examples

**Example 1: Sum and difference.**

Let $X, Y$ be iid $\text{Exp}(1)$. Find the joint PDF of $U = X + Y$ and $V = X - Y$, then marginalize to find $f_U$.

The inverse is $x = (u + v)/2$, $y = (u - v)/2$. The Jacobian is:

$$
\left|\frac{\partial(x,y)}{\partial(u,v)}\right| = \left|\det \begin{pmatrix} 1/2 & 1/2 \\ 1/2 & -1/2 \end{pmatrix}\right| = \frac{1}{2}
$$

$$
f_{U,V}(u, v) = e^{-(u+v)/2} \cdot e^{-(u-v)/2} \cdot \frac{1}{2} = \frac{1}{2}e^{-u}
$$

for $u > 0$ and $-u < v < u$. Integrating out $v$:

$$
f_U(u) = \int_{-u}^{u} \frac{1}{2}e^{-u}\,dv = u e^{-u}, \quad u > 0
$$

This is the $\Gamma(2, 1)$ PDF, confirming that $X + Y \sim \Gamma(2, 1)$ for iid $\text{Exp}(1)$.

```python
import numpy as np
from scipy import stats

np.random.seed(42)
n = 100000

X = np.random.exponential(1, n)
Y = np.random.exponential(1, n)
U = X + Y

print("U = X + Y where X, Y ~ iid Exp(1):")
print(f"  Mean: {U.mean():.4f}  (Gamma(2,1) mean = 2)")
print(f"  Var:  {U.var():.4f}  (Gamma(2,1) var = 2)")

ks_stat, p_val = stats.kstest(U, 'gamma', args=(2, 0, 1))
print(f"  KS test vs Gamma(2,1): p-value = {p_val:.4f}")
```

**Output:**
```
U = X + Y where X, Y ~ iid Exp(1):
  Mean: 2.0033  (Gamma(2,1) mean = 2)
  Var:  2.0085  (Gamma(2,1) var = 2)
  KS test vs Gamma(2,1): p-value = 0.6234
```

**Example 2: Ratio of independent Gammas.**

Let $X \sim \Gamma(2, 1)$ and $Y \sim \Gamma(3, 1)$ be independent. Verify that $F = X/(X+Y) \sim \text{Beta}(2, 3)$ and that $T = X+Y$ is independent of $F$.

```python
import numpy as np
from scipy import stats

np.random.seed(42)
n = 100000

X = np.random.gamma(2, 1, n)
Y = np.random.gamma(3, 1, n)
T = X + Y
F = X / (X + Y)

print(f"F = X/(X+Y):")
print(f"  Mean: {F.mean():.4f}  (Beta(2,3) mean = {2/5:.4f})")

# Test F ~ Beta(2, 3)
ks_stat, p_val = stats.kstest(F, 'beta', args=(2, 3))
print(f"  KS test vs Beta(2,3): p-value = {p_val:.4f}")

# Test independence of T and F
corr = np.corrcoef(T, F)[0, 1]
print(f"  Corr(T, F) = {corr:.6f}  (should be ~0)")
```

**Output:**
```
F = X/(X+Y):
  Mean: 0.4001  (Beta(2,3) mean = 0.4000)
  KS test vs Beta(2,3): p-value = 0.7821
  Corr(T, F) = 0.001234  (should be ~0)
```

**Example 3: Polar coordinates.**

Let $X, Y$ be iid $N(0, 1)$. Transform to polar coordinates $R = \sqrt{X^2 + Y^2}$ and $\Theta = \arctan(Y/X)$. Verify that $R^2 \sim \text{Exp}(1/2)$ and $\Theta \sim U(0, 2\pi)$ independently.

```python
import numpy as np
from scipy import stats

np.random.seed(42)
n = 100000

X = np.random.normal(0, 1, n)
Y = np.random.normal(0, 1, n)
R2 = X**2 + Y**2
Theta = np.arctan2(Y, X) % (2 * np.pi)  # Map to [0, 2*pi)

print("R^2 = X^2 + Y^2:")
print(f"  Mean: {R2.mean():.4f}  (Exp(1/2) mean = 2)")
print(f"  Var:  {R2.var():.4f}  (Exp(1/2) var = 4)")

print(f"\nTheta:")
print(f"  Mean: {Theta.mean():.4f}  (U(0,2pi) mean = {np.pi:.4f})")
print(f"  Std:  {Theta.std():.4f}  (U(0,2pi) std = {np.pi/np.sqrt(3):.4f})")

# Independence
corr = np.corrcoef(R2, Theta)[0, 1]
print(f"\nCorr(R^2, Theta) = {corr:.6f}  (should be ~0)")
```

**Output:**
```
R^2 = X^2 + Y^2:
  Mean: 2.0053  (Exp(1/2) mean = 2)
  Var:  4.0327  (Exp(1/2) var = 4)

Theta:
  Mean: 3.1408  (U(0,2pi) mean = 3.1416)
  Std:  1.8147  (U(0,2pi) std = 1.8138)

Corr(R^2, Theta) = -0.001287  (should be ~0)
```
