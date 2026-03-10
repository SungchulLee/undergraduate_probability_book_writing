# Joint PDF of the Bivariate Normal

The bivariate normal distribution is the joint distribution of two random variables whose dependence is fully captured by five parameters: two means, two standard deviations, and the correlation coefficient. It is the foundation for modeling correlated continuous data.

## Definition

Let $\mathbf{x} = (x, y)^T$ follow a bivariate normal $N(\boldsymbol{\mu}, \boldsymbol{\Sigma})$ with mean vector $\boldsymbol{\mu} = (\mu_X, \mu_Y)^T$ and covariance matrix

$$
\boldsymbol{\Sigma} = \begin{pmatrix} \sigma_X^2 & \rho\sigma_X\sigma_Y \\ \rho\sigma_X\sigma_Y & \sigma_Y^2 \end{pmatrix}
$$

The joint PDF is

$$
f(x, y) = \frac{1}{2\pi\sigma_X\sigma_Y\sqrt{1 - \rho^2}} \exp\!\left(-\frac{\tilde{x}^2 + \tilde{y}^2 - 2\rho\tilde{x}\tilde{y}}{2(1 - \rho^2)}\right)
$$

where $\tilde{x} = (x - \mu_X)/\sigma_X$ and $\tilde{y} = (y - \mu_Y)/\sigma_Y$. The covariance matrix must satisfy $|\rho| < 1$ for the distribution to be non-degenerate.

## Explanation

### Matrix form

In matrix notation the PDF is

$$
f(\mathbf{x}) = \frac{1}{\sqrt{(2\pi)^2 |\boldsymbol{\Sigma}|}} \exp\!\left(-\frac{1}{2}(\mathbf{x} - \boldsymbol{\mu})^T \boldsymbol{\Sigma}^{-1} (\mathbf{x} - \boldsymbol{\mu})\right)
$$

The determinant and inverse of the covariance matrix are

$$
|\boldsymbol{\Sigma}| = \sigma_X^2 \sigma_Y^2 (1 - \rho^2)
$$

$$
\boldsymbol{\Sigma}^{-1} = \frac{1}{(1 - \rho^2)\sigma_X^2 \sigma_Y^2} \begin{pmatrix} \sigma_Y^2 & -\rho\sigma_X\sigma_Y \\ -\rho\sigma_X\sigma_Y & \sigma_X^2 \end{pmatrix}
$$

### Independent components

When $\rho = 0$ the cross term vanishes and the PDF factors into a product of marginals:

$$
f(x, y) = \frac{1}{\sqrt{2\pi}\sigma_X} e^{-\tilde{x}^2/2} \cdot \frac{1}{\sqrt{2\pi}\sigma_Y} e^{-\tilde{y}^2/2} = f_X(x) \cdot f_Y(y)
$$

This confirms that $\rho = 0$ implies independence for the bivariate normal.

### Standard bivariate normal

When $\mu_X = \mu_Y = 0$ and $\sigma_X = \sigma_Y = 1$, the PDF simplifies to

$$
f(x, y) = \frac{1}{2\pi\sqrt{1 - \rho^2}} \exp\!\left(-\frac{x^2 + y^2 - 2\rho xy}{2(1 - \rho^2)}\right)
$$

## Examples

Compute the density at the mean and verify with scipy.

```python
import numpy as np
from scipy.stats import multivariate_normal

mu_x, mu_y = 1.0, -1.0
sigma_x, sigma_y, rho = 2.0, 3.0, 0.5

# Manual scalar formula
norm_const = 2 * np.pi * sigma_x * sigma_y * np.sqrt(1 - rho**2)
f_at_mean = 1.0 / norm_const
print(f"f(mu_x, mu_y) = {f_at_mean:.6f}")

# Verify with scipy
Sigma = [[sigma_x**2, rho * sigma_x * sigma_y],
         [rho * sigma_x * sigma_y, sigma_y**2]]
rv = multivariate_normal(mean=[mu_x, mu_y], cov=Sigma)
print(f"scipy check:    {rv.pdf([mu_x, mu_y]):.6f}")

# Verify factorization when rho = 0
np.random.seed(42)
Sigma0 = [[sigma_x**2, 0], [0, sigma_y**2]]
samples = np.random.multivariate_normal([mu_x, mu_y], Sigma0, 50_000)
p_joint = np.mean((samples[:, 0] > mu_x) & (samples[:, 1] > mu_y))
p_marginals = np.mean(samples[:, 0] > mu_x) * np.mean(samples[:, 1] > mu_y)
print(f"\nrho=0 independence check:")
print(f"P(X>mu, Y>mu)       = {p_joint:.4f}")
print(f"P(X>mu) * P(Y>mu)   = {p_marginals:.4f}")
```
