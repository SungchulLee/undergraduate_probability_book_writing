# Marginal and Conditional Distributions

## Overview

One of the most powerful features of the bivariate normal distribution is that both **marginal** and **conditional** distributions are themselves normal. Moreover, the conditional distribution has a simple closed-form expression with a beautiful geometric interpretation: conditioning on $Y = y$ "slices" the bell surface, yielding a normal distribution whose mean shifts linearly in $y$.

---

## Marginal Distributions

If $(X, Y)^T \sim N(\boldsymbol{\mu}, \boldsymbol{\Sigma})$ with:

$$
\boldsymbol{\mu} = \begin{pmatrix} \mu_X \\ \mu_Y \end{pmatrix}, \qquad
\boldsymbol{\Sigma} = \begin{pmatrix} \sigma_X^2 & \rho\sigma_X\sigma_Y \\ \rho\sigma_X\sigma_Y & \sigma_Y^2 \end{pmatrix}
$$

then the marginal distributions are:

$$
X \sim N(\mu_X, \sigma_X^2), \qquad Y \sim N(\mu_Y, \sigma_Y^2)
$$

The marginals simply "read off" the diagonal of the covariance matrix. The correlation $\rho$ does not appear in the marginals — it only affects the joint behavior.

!!! warning "Converse is False"
    Two individually normal marginals do **not** guarantee a bivariate normal joint distribution. See the [counterexample](uncorrelated_independent.md) where $X$ and $Y = SX$ are each marginally normal but not jointly normal.

---

## Conditional Distribution: $X \mid Y = y$

The conditional distribution of $X$ given $Y = y$ is:

$$
X \mid Y = y \;\sim\; N\!\left(\mu_{X|Y},\; \sigma_{X|Y}^2\right)
$$

where:

$$
\mu_{X|Y} = \mu_X + \rho\frac{\sigma_X}{\sigma_Y}(y - \mu_Y)
$$

$$
\sigma_{X|Y}^2 = \sigma_X^2(1 - \rho^2)
$$

### Interpretation

- **Conditional mean** $\mu_{X|Y}$: This is the **regression function** $E[X \mid Y = y]$, which is linear in $y$. The slope $\rho \cdot \sigma_X / \sigma_Y$ determines how much the conditional mean shifts per unit change in $y$.
- **Conditional variance** $\sigma_{X|Y}^2$: This is **constant** — it does not depend on $y$. The factor $(1 - \rho^2)$ shows how much knowing $Y$ reduces uncertainty about $X$. When $|\rho| = 1$, the conditional variance is zero (perfect prediction).

By symmetry, the conditional distribution of $Y$ given $X = x$ is:

$$
Y \mid X = x \;\sim\; N\!\left(\mu_Y + \rho\frac{\sigma_Y}{\sigma_X}(x - \mu_X),\; \sigma_Y^2(1 - \rho^2)\right)
$$

---

## Derivation via Completing the Square

Starting from the joint PDF in standardized coordinates $\tilde{x} = (x - \mu_X)/\sigma_X$ and $\tilde{y} = (y - \mu_Y)/\sigma_Y$:

$$
f(x, y) \propto \exp\left(-\frac{\tilde{x}^2 + \tilde{y}^2 - 2\rho\tilde{x}\tilde{y}}{2(1 - \rho^2)}\right)
$$

To find $f(x \mid y)$, treat $\tilde{y}$ as fixed and collect terms in $\tilde{x}$:

$$
\tilde{x}^2 - 2\rho\tilde{y}\tilde{x} = (\tilde{x} - \rho\tilde{y})^2 - \rho^2\tilde{y}^2
$$

The $\rho^2\tilde{y}^2$ term is absorbed into the normalizing constant (it depends only on $y$), giving:

$$
f(x \mid y) \propto \exp\left(-\frac{(\tilde{x} - \rho\tilde{y})^2}{2(1 - \rho^2)}\right)
$$

Reverting to the original scale:

$$
x - \mu_X - \rho\frac{\sigma_X}{\sigma_Y}(y - \mu_Y) \sim N\!\left(0,\; \sigma_X^2(1 - \rho^2)\right)
$$

which gives the conditional distribution formulas above.

---

## Connection to Linear Regression

The conditional expectation $E[X \mid Y = y] = \mu_X + \rho(\sigma_X/\sigma_Y)(y - \mu_Y)$ is exactly the **best linear predictor** of $X$ given $Y$. For the bivariate normal, this linear predictor is also the **best predictor** overall (not just the best linear one).

The regression coefficient is:

$$
\beta = \rho \cdot \frac{\sigma_X}{\sigma_Y} = \frac{\text{Cov}(X, Y)}{\text{Var}(Y)}
$$

This connects directly to the ordinary least squares (OLS) slope coefficient.

---

## Python Implementation

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import multivariate_normal, norm

# Parameters
mu_x, mu_y = 1, 2
sigma_x, sigma_y = 2, 1.5
rho = 0.7

# Generate bivariate normal samples
mu = [mu_x, mu_y]
Sigma = [[sigma_x**2, rho * sigma_x * sigma_y],
         [rho * sigma_x * sigma_y, sigma_y**2]]

np.random.seed(42)
samples = np.random.multivariate_normal(mu, Sigma, 2000)

# Conditional distribution parameters for Y = y_given
y_given = 3.0
mu_cond = mu_x + rho * (sigma_x / sigma_y) * (y_given - mu_y)
sigma_cond = sigma_x * np.sqrt(1 - rho**2)

print(f"Conditional distribution X | Y={y_given}:")
print(f"  Mean: {mu_cond:.4f}")
print(f"  Std:  {sigma_cond:.4f}")

# Plot
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Left: joint distribution with conditional slice
ax = axes[0]
ax.scatter(samples[:, 0], samples[:, 1], s=2, alpha=0.3, label='Samples')
ax.axhline(y=y_given, color='red', linestyle='--', label=f'Y = {y_given}')
x_line = np.linspace(mu_x - 3*sigma_x, mu_x + 3*sigma_x, 100)
regression_line = mu_x + rho * (sigma_x / sigma_y) * (x_line - mu_x)  # E[Y|X=x]
# Actually plot E[X|Y=y] as the regression line
y_range = np.linspace(mu_y - 3*sigma_y, mu_y + 3*sigma_y, 100)
e_x_given_y = mu_x + rho * (sigma_x / sigma_y) * (y_range - mu_y)
ax.plot(e_x_given_y, y_range, 'g-', linewidth=2, label='E[X|Y=y]')
ax.plot(mu_cond, y_given, 'ro', markersize=8, zorder=5)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('Joint Distribution with Conditional Slice')
ax.legend(fontsize=8)

# Right: conditional PDF
ax = axes[1]
x_vals = np.linspace(mu_cond - 4*sigma_cond, mu_cond + 4*sigma_cond, 200)
cond_pdf = norm.pdf(x_vals, mu_cond, sigma_cond)
ax.plot(x_vals, cond_pdf, 'b-', linewidth=2)
ax.fill_between(x_vals, cond_pdf, alpha=0.2)
ax.axvline(mu_cond, color='red', linestyle='--', label=f'E[X|Y={y_given}] = {mu_cond:.2f}')
ax.set_xlabel('X')
ax.set_ylabel('Density')
ax.set_title(f'Conditional Distribution X | Y = {y_given}')
ax.legend()

plt.tight_layout()
plt.show()
```

---

## Key Takeaways

- Marginals of the bivariate normal are normal with parameters read directly from $\boldsymbol{\mu}$ and the diagonal of $\boldsymbol{\Sigma}$.
- The conditional distribution $X \mid Y = y$ is normal with a mean that shifts linearly in $y$ and a variance that is constant (independent of $y$).
- The conditional mean is the regression function, and the conditional variance quantifies the residual uncertainty after conditioning.
- The factor $(1 - \rho^2)$ measures the fraction of variance "explained" by the conditioning variable.
