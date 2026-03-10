# Change of Variables (Single Variable)


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

## Two Methods for Finding PDFs

Given a random variable $X$ with known PDF $f_X(x)$ and a transformation $Y = g(X)$, there are two systematic methods to find the PDF of $Y$.

## Method 1: CDF Method

!!! info "CDF Method"
    1. Find $F_Y(y) = P(Y \leq y) = P(g(X) \leq y)$
    2. Express in terms of $P(X \leq \cdot)$ or $P(X \geq \cdot)$
    3. Differentiate: $f_Y(y) = F_Y'(y)$

This method is fully general and works for any transformation, including non-monotone ones.

## Method 2: Jacobian Method

!!! info "Jacobian Method (Single Variable)"
    If $Y = g(X)$ where $g$ is a **monotone, differentiable** function with inverse $x = g^{-1}(y)$, then:

    $$f_Y(y) = f_X(x) \left|\frac{dx}{dy}\right|$$

    where $x = g^{-1}(y)$.

The absolute value ensures the PDF is non-negative regardless of whether $g$ is increasing or decreasing. The factor $|dx/dy|$ accounts for how the transformation stretches or compresses the density.

### Intuitive Justification

If $g$ is increasing, then $P(Y \leq y) = P(X \leq x)$, so:

$$f_Y(y) = f_X(x) \frac{dx}{dy}$$

If $g$ is decreasing, then $P(Y \leq y) = P(X \geq x)$, giving a negative sign that is absorbed by the absolute value.

### Connection Between the Methods

The Jacobian method is a shortcut derived from the CDF method. Using the chain rule:

$$F_Y(y) = P(X \leq g^{-1}(y)) \implies f_Y(y) = f_X(g^{-1}(y)) \cdot \frac{d}{dy}g^{-1}(y) = f_X(x)\left|\frac{dx}{dy}\right|$$

### Reciprocal Property

The Jacobian can be computed either way:

$$\left|\frac{dx}{dy}\right| = \frac{1}{\left|\dfrac{dy}{dx}\right|}$$

This is often easier when $dy/dx$ is simpler to compute than $dx/dy$ directly.

## Worked Example: Y = X^3 where X ~ U(0, 1)

??? example "Example: Cube of a Uniform"
    Let $X \sim U(0,1)$ and $Y = X^3$. Find $f_Y(y)$ for $0 < y < 1$.

    **Method 1: CDF**

    $$P(Y \leq y) = P(X^3 \leq y) = P(X \leq y^{1/3}) = y^{1/3}$$

    Differentiating:

    $$f_Y(y) = \frac{1}{3} y^{-2/3}, \quad 0 < y < 1$$

    **Method 2: Jacobian**

    With $y = x^3$, we have $x = y^{1/3}$:

    $$\frac{dy}{dx} = 3x^2 = 3(x^3)^{2/3} = 3y^{2/3}$$

    $$\left|\frac{dx}{dy}\right| = \frac{1}{3y^{2/3}} = \frac{1}{3}y^{-2/3}$$

    Therefore:

    $$f_Y(y) = f_X(x) \left|\frac{dx}{dy}\right| = 1 \cdot \frac{1}{3}y^{-2/3} = \frac{1}{3}y^{-2/3}, \quad 0 < y < 1$$

    Both methods agree. The density is concentrated near $y = 0$ because the cube function compresses values near $0$ and stretches values near $1$.

## Python Implementation

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

np.random.seed(42)
n_sim = 100000

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Y = X^3 where X ~ U(0,1)
X = np.random.uniform(0, 1, n_sim)
Y = X ** 3

y_vals = np.linspace(0.01, 0.99, 200)
pdf_theory = (1/3) * y_vals ** (-2/3)

axes[0].hist(Y, bins=80, density=True, alpha=0.5, color='steelblue',
             label='Y = X³ simulated')
axes[0].plot(y_vals, pdf_theory, 'r-', lw=2,
             label=r'$f_Y(y) = \frac{1}{3}y^{-2/3}$')
axes[0].set_title('Y = X³ where X ~ U(0,1)')
axes[0].set_xlabel('y')
axes[0].set_ylabel('Density')
axes[0].set_ylim(0, 5)
axes[0].legend()
axes[0].grid(True, alpha=0.3)

# CDF comparison
y_grid = np.linspace(0, 1, 200)
cdf_empirical = np.array([np.mean(Y <= y) for y in y_grid])
cdf_theory = y_grid ** (1/3)

axes[1].plot(y_grid, cdf_empirical, 'b-', lw=2, alpha=0.7,
             label='Empirical CDF')
axes[1].plot(y_grid, cdf_theory, 'r--', lw=2,
             label=r'$F_Y(y) = y^{1/3}$')
axes[1].set_title('CDF of Y = X³')
axes[1].set_xlabel('y')
axes[1].set_ylabel('F(y)')
axes[1].legend()
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('change_of_variables.png', dpi=150, bbox_inches='tight')
plt.show()
```
