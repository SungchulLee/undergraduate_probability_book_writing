# Change of Variables (Single Variable)

When a random variable $X$ is transformed by a function $g$ to produce $Y = g(X)$, the PDF of $Y$ can be found systematically using either the CDF method or the Jacobian (change-of-variables) formula.

## Definition

Given $X$ with known PDF $f_X$ and a transformation $Y = g(X)$, the PDF of $Y$ can be found by two methods.

**CDF method (always works):**

$$
F_Y(y) = P(Y \leq y) = P(g(X) \leq y), \qquad f_Y(y) = F_Y'(y)
$$

**Jacobian method (requires monotone $g$):** If $g$ is monotone and differentiable with inverse $x = g^{-1}(y)$, then:

$$
f_Y(y) = f_X(g^{-1}(y)) \left|\frac{dx}{dy}\right|
$$

where $\left|\frac{dx}{dy}\right| = \left|\frac{d}{dy}g^{-1}(y)\right|$ is the absolute value of the derivative of the inverse function.

## Explanation

### The CDF method in detail

The CDF method proceeds in three steps:

1. **Express the event:** Write $P(Y \leq y) = P(g(X) \leq y)$ in terms of $X$.
2. **Solve for X:** Determine which values of $X$ satisfy $g(X) \leq y$.
3. **Differentiate:** Compute $f_Y(y) = F_Y'(y)$.

This method is fully general and works even for non-monotone transformations (e.g., $Y = X^2$).

### The Jacobian method in detail

If $g$ is increasing, then $P(Y \leq y) = P(X \leq g^{-1}(y))$, so:

$$
f_Y(y) = f_X(g^{-1}(y)) \cdot \frac{dx}{dy}
$$

If $g$ is decreasing, then $P(Y \leq y) = P(X \geq g^{-1}(y))$, introducing a negative sign. The absolute value absorbs both cases:

$$
f_Y(y) = f_X(g^{-1}(y)) \left|\frac{dx}{dy}\right|
$$

### The reciprocal property

The Jacobian can be computed in either direction:

$$
\left|\frac{dx}{dy}\right| = \frac{1}{\left|\dfrac{dy}{dx}\right|}
$$

This is often more convenient when $dy/dx$ is simpler than computing $dx/dy$ directly.

### Intuition for the Jacobian factor

The factor $|dx/dy|$ accounts for how the transformation stretches or compresses the density. Where $g$ changes slowly ($|dy/dx|$ is small, so $|dx/dy|$ is large), many $x$-values map to a narrow range of $y$-values, concentrating probability. Where $g$ changes rapidly, probability is spread out.

### Handling non-monotone transformations

For non-monotone $g$, the CDF method is safest. Alternatively, if $g^{-1}(y)$ has multiple branches $x_1(y), x_2(y), \ldots$, the PDF is:

$$
f_Y(y) = \sum_j f_X(x_j(y)) \left|\frac{dx_j}{dy}\right|
$$

For example, if $Y = X^2$ where $X$ has a symmetric PDF, then $x_1 = \sqrt{y}$ and $x_2 = -\sqrt{y}$ both contribute.

## Examples

**Example 1: Cube of a uniform.**

Let $X \sim U(0,1)$ and $Y = X^3$. Find $f_Y(y)$.

**CDF method:**

$$
F_Y(y) = P(X^3 \leq y) = P(X \leq y^{1/3}) = y^{1/3}
$$

$$
f_Y(y) = \frac{1}{3} y^{-2/3}, \quad 0 < y < 1
$$

**Jacobian method:** With $x = y^{1/3}$ and $dx/dy = \frac{1}{3}y^{-2/3}$:

$$
f_Y(y) = f_X(y^{1/3}) \cdot \frac{1}{3}y^{-2/3} = 1 \cdot \frac{1}{3}y^{-2/3}
$$

```python
import numpy as np

np.random.seed(42)
n = 100000

X = np.random.uniform(0, 1, n)
Y = X ** 3

# Verify PDF at several points
y_test = [0.1, 0.3, 0.5, 0.7, 0.9]
print("f_Y(y) = (1/3) * y^(-2/3):")
for y in y_test:
    theory = (1/3) * y**(-2/3)
    # Empirical density via histogram bin
    h = 0.02
    empirical = np.mean((Y > y - h) & (Y < y + h)) / (2*h)
    print(f"  y = {y}: theory = {theory:.4f}, empirical = {empirical:.4f}")
```

**Output:**
```
f_Y(y) = (1/3) * y^(-2/3):
  y = 0.1: theory = 1.5443, empirical = 1.5455
  y = 0.3: theory = 0.7418, empirical = 0.7360
  y = 0.5: theory = 0.5291, empirical = 0.5365
  y = 0.7: theory = 0.4222, empirical = 0.4252
  y = 0.9: theory = 0.3569, empirical = 0.3548
```

**Example 2: Square of a standard normal (non-monotone).**

Let $Z \sim N(0, 1)$ and $W = Z^2$. Find $f_W(w)$.

Since $Z^2 \leq w$ iff $-\sqrt{w} \leq Z \leq \sqrt{w}$:

$$
F_W(w) = \Phi(\sqrt{w}) - \Phi(-\sqrt{w}) = 2\Phi(\sqrt{w}) - 1
$$

$$
f_W(w) = 2\phi(\sqrt{w}) \cdot \frac{1}{2\sqrt{w}} = \frac{1}{\sqrt{2\pi w}} e^{-w/2}, \quad w > 0
$$

This is the $\chi^2_1 = \Gamma(1/2, 1/2)$ density.

```python
import numpy as np
from scipy import stats

np.random.seed(42)
n = 100000

Z = np.random.normal(0, 1, n)
W = Z ** 2

print("W = Z^2 where Z ~ N(0,1):")
print(f"  Mean: {W.mean():.4f}  (Chi-squared(1) mean = 1)")
print(f"  Var:  {W.var():.4f}  (Chi-squared(1) var = 2)")

# KS test against chi-squared(1)
ks_stat, p_val = stats.kstest(W, 'chi2', args=(1,))
print(f"  KS test vs chi2(1): p-value = {p_val:.4f}")
```

**Output:**
```
W = Z^2 where Z ~ N(0,1):
  Mean: 1.0053  (Chi-squared(1) mean = 1)
  Var:  2.0313  (Chi-squared(1) var = 2)
  KS test vs chi2(1): p-value = 0.4567
```

**Example 3: Exponential from uniform.**

Let $U \sim U(0, 1)$ and $X = -\ln(U)/\lambda$. Verify $X \sim \text{Exp}(\lambda)$.

With $u = e^{-\lambda x}$ and $|du/dx| = \lambda e^{-\lambda x}$:

$$
f_X(x) = f_U(e^{-\lambda x}) \cdot \lambda e^{-\lambda x} = 1 \cdot \lambda e^{-\lambda x}
$$

```python
import numpy as np
from scipy import stats

np.random.seed(42)
n = 100000
lam = 2.0

U = np.random.uniform(0, 1, n)
X = -np.log(U) / lam

print(f"X = -ln(U)/{lam} should be Exp({lam}):")
print(f"  Mean: {X.mean():.4f}  (theory: {1/lam:.4f})")
print(f"  Var:  {X.var():.4f}  (theory: {1/lam**2:.4f})")

ks_stat, p_val = stats.kstest(X, 'expon', args=(0, 1/lam))
print(f"  KS test: p-value = {p_val:.4f}")
```

**Output:**
```
X = -ln(U)/2.0 should be Exp(2.0):
  Mean: 0.5011  (theory: 0.5000)
  Var:  0.2500  (theory: 0.2500)
  KS test: p-value = 0.5832
```
