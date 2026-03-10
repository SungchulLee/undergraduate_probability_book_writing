# Cauchy-Schwarz Inequality

The Cauchy-Schwarz inequality bounds the covariance by the product of standard deviations, proving that correlation lies in $[-1, 1]$.

## Definition

For any random variables $X$ and $Y$ with finite second moments:

$$
\bigl|E[XY]\bigr|^2 \le E[X^2]\,E[Y^2]
$$

Equivalently, in terms of covariance:

$$
\bigl|\text{Cov}(X, Y)\bigr| \le \text{SD}(X)\,\text{SD}(Y)
$$

Equality holds if and only if $Y = aX + b$ for some constants $a, b$ (i.e., $X$ and $Y$ are linearly related).

## Explanation

### Proof

For any real $t$, define $h(t) = E[(X + tY)^2] \ge 0$. Expanding:

$$
h(t) = E[X^2] + 2t\,E[XY] + t^2\,E[Y^2] \ge 0
$$

This is a quadratic in $t$ that is non-negative everywhere. A non-negative quadratic has non-positive discriminant:

$$
4(E[XY])^2 - 4\,E[X^2]\,E[Y^2] \le 0
$$

which gives $|E[XY]|^2 \le E[X^2]\,E[Y^2]$.

### Covariance Version

Apply the basic form to the centered variables $\tilde{X} = X - E[X]$ and $\tilde{Y} = Y - E[Y]$:

$$
|\text{Cov}(X,Y)|^2 = |E[\tilde{X}\tilde{Y}]|^2 \le E[\tilde{X}^2]\,E[\tilde{Y}^2] = \text{Var}(X)\,\text{Var}(Y)
$$

Dividing both sides by $\text{Var}(X)\,\text{Var}(Y)$ gives $|\rho(X,Y)| \le 1$.

### When Is Equality Achieved?

$|E[XY]|^2 = E[X^2]\,E[Y^2]$ iff the quadratic $h(t)$ has a real root, meaning $X + t^*Y = 0$ a.s. for some $t^*$. This means $X$ is a scalar multiple of $Y$ (plus a constant, after centering).

## Examples

**Example.** Verify with $X \sim \text{Uniform}(0,1)$ and $Y = 2X + 3$ (perfect linear relationship).

$$
\text{Cov}(X, Y) = 2\,\text{Var}(X) = 2/12 = 1/6
$$

$$
\text{SD}(X)\,\text{SD}(Y) = \frac{1}{\sqrt{12}} \cdot \frac{2}{\sqrt{12}} = \frac{2}{12} = 1/6
$$

Equality holds: $|\text{Cov}| = \text{SD}(X)\,\text{SD}(Y)$, confirming $|\rho| = 1$.

```python
import numpy as np

np.random.seed(42)
n_sim = 200_000

# Perfect linear: Y = 2X + 3
X = np.random.uniform(0, 1, n_sim)
Y_lin = 2 * X + 3
rho_lin = np.corrcoef(X, Y_lin)[0, 1]
print(f"|rho| for Y = 2X + 3: {abs(rho_lin):.6f}  (theory: 1.0)")

# Non-perfect: X, Z independent uniform
Z = np.random.uniform(0, 1, n_sim)
Y_mix = X + Z
rho_mix = np.corrcoef(X, Y_mix)[0, 1]
print(f"|rho| for Y = X + Z: {abs(rho_mix):.4f}  (theory: {1/np.sqrt(2):.4f})")

# Cauchy-Schwarz check: |E[XY]|^2 <= E[X^2] E[Y^2]
lhs = np.mean(X * Y_mix)**2
rhs = np.mean(X**2) * np.mean(Y_mix**2)
print(f"\n|E[XY]|^2 = {lhs:.6f}")
print(f"E[X^2]*E[Y^2] = {rhs:.6f}")
print(f"CS holds: {lhs <= rhs + 1e-10}")
```
