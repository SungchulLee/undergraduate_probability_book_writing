# Marginal and Conditional Distributions

Both marginal and conditional distributions of a bivariate normal are themselves normal. The conditional mean is a linear function of the conditioning variable, connecting the bivariate normal directly to linear regression.

## Definition

If $(X, Y)^T \sim N(\boldsymbol{\mu}, \boldsymbol{\Sigma})$ with parameters $\mu_X, \mu_Y, \sigma_X, \sigma_Y, \rho$, then the marginals are

$$
X \sim N(\mu_X, \sigma_X^2), \qquad Y \sim N(\mu_Y, \sigma_Y^2)
$$

and the conditional distribution of $X$ given $Y = y$ is

$$
X \mid Y = y \;\sim\; N\!\left(\mu_X + \rho\frac{\sigma_X}{\sigma_Y}(y - \mu_Y),\; \sigma_X^2(1 - \rho^2)\right)
$$

By symmetry, $Y \mid X = x \sim N\!\left(\mu_Y + \rho\frac{\sigma_Y}{\sigma_X}(x - \mu_X),\; \sigma_Y^2(1 - \rho^2)\right)$.

## Explanation

### Marginals

The marginals read off the diagonal of $\boldsymbol{\Sigma}$. The correlation $\rho$ does not appear in the marginal distributions -- it only affects the joint behavior.

!!! warning "Converse is false"
    Two individually normal marginals do **not** guarantee a bivariate normal joint distribution. See the [counterexample](uncorrelated_independent.md).

### Conditional mean as regression

The conditional expectation $E[X \mid Y = y] = \mu_X + \rho(\sigma_X / \sigma_Y)(y - \mu_Y)$ is linear in $y$ with slope

$$
\beta = \rho \cdot \frac{\sigma_X}{\sigma_Y} = \frac{\text{Cov}(X, Y)}{\text{Var}(Y)}
$$

This is exactly the ordinary least squares regression coefficient. For the bivariate normal, this linear predictor is also the best predictor overall, not just the best linear one.

### Conditional variance

The conditional variance $\sigma_X^2(1 - \rho^2)$ is constant -- it does not depend on $y$. The factor $(1 - \rho^2)$ measures how much knowing $Y$ reduces uncertainty about $X$. When $|\rho| = 1$, perfect prediction is possible.

### Derivation via completing the square

Starting from the exponent of the joint PDF in standardized coordinates, treat $\tilde{y}$ as fixed and complete the square in $\tilde{x}$:

$$
\tilde{x}^2 - 2\rho\tilde{y}\tilde{x} = (\tilde{x} - \rho\tilde{y})^2 - \rho^2\tilde{y}^2
$$

The $\rho^2\tilde{y}^2$ term is absorbed into the normalizing constant, giving

$$
f(x \mid y) \propto \exp\!\left(-\frac{(\tilde{x} - \rho\tilde{y})^2}{2(1 - \rho^2)}\right)
$$

Reverting to the original scale yields the conditional distribution formulas above.

## Examples

Compute the conditional distribution $X \mid Y = 3$ and verify with simulation.

```python
import numpy as np

mu_x, mu_y = 1.0, 2.0
sigma_x, sigma_y, rho = 2.0, 1.5, 0.7
y_given = 3.0

# Theoretical conditional parameters
mu_cond = mu_x + rho * (sigma_x / sigma_y) * (y_given - mu_y)
sigma_cond = sigma_x * np.sqrt(1 - rho**2)
print(f"X | Y={y_given}: mean = {mu_cond:.4f}, std = {sigma_cond:.4f}")

# Simulate and check
np.random.seed(42)
Sigma = [[sigma_x**2, rho * sigma_x * sigma_y],
         [rho * sigma_x * sigma_y, sigma_y**2]]
samples = np.random.multivariate_normal([mu_x, mu_y], Sigma, 200_000)

mask = np.abs(samples[:, 1] - y_given) < 0.05
x_slice = samples[mask, 0]
print(f"\nSimulated E[X | Y~{y_given}]: {x_slice.mean():.4f}")
print(f"Simulated Std[X | Y~{y_given}]: {x_slice.std():.4f}")

# Regression coefficient check
beta = rho * sigma_x / sigma_y
cov_xy = np.cov(samples.T)[0, 1]
var_y = np.var(samples[:, 1])
print(f"\nTheoretical beta: {beta:.4f}")
print(f"Empirical Cov/Var: {cov_xy / var_y:.4f}")
```
