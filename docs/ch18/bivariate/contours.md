# Contours and Geometric Interpretation

The constant-density contours of the bivariate normal are ellipses whose shape, orientation, and size encode the covariance structure. Understanding these contours provides the geometric intuition behind correlation and the Mahalanobis distance.

## Definition

Setting $f(x, y) = c$ for some constant $c > 0$ is equivalent to requiring the quadratic form

$$
(\mathbf{x} - \boldsymbol{\mu})^T \boldsymbol{\Sigma}^{-1} (\mathbf{x} - \boldsymbol{\mu}) = k
$$

for a constant $k > 0$. This is the equation of an ellipse centered at $\boldsymbol{\mu}$. The quantity on the left is the squared **Mahalanobis distance** from $\mathbf{x}$ to the mean.

## Explanation

### Role of each parameter

The mean vector $\boldsymbol{\mu}$ controls the center. The marginal variances $\sigma_X^2, \sigma_Y^2$ control spread along each axis. The correlation $\rho$ controls the tilt and eccentricity:

| $\rho$ | Shape | Orientation |
|:---:|:---|:---|
| $0$ | Axis-aligned | No tilt |
| $> 0$ | Tilted toward $y = x$ | Positive slope |
| $< 0$ | Tilted toward $y = -x$ | Negative slope |
| $\to \pm 1$ | Collapses to a line | Perfect linear relationship |

### Eigenvalue interpretation

For the standard bivariate normal ($\sigma_X = \sigma_Y = 1$) the covariance matrix has eigenvalues $\lambda_1 = 1 + \rho$ and $\lambda_2 = 1 - \rho$, with eigenvectors along the 45-degree and 135-degree directions. The ellipse axes align with the eigenvectors, and their lengths are proportional to $\sqrt{\lambda_i}$. As $|\rho| \to 1$, one eigenvalue approaches zero and the ellipse degenerates.

### Mahalanobis distance and chi-squared

For a bivariate normal random vector $\mathbf{X}$, the squared Mahalanobis distance follows a chi-squared distribution:

$$
(\mathbf{X} - \boldsymbol{\mu})^T \boldsymbol{\Sigma}^{-1} (\mathbf{X} - \boldsymbol{\mu}) \sim \chi^2(2)
$$

The probability contained within the ellipse at squared Mahalanobis distance $k$ is $P(\chi^2(2) \leq k) = 1 - e^{-k/2}$.

## Examples

Verify the eigenvalue formulas and the chi-squared property numerically.

```python
import numpy as np
from scipy.stats import chi2

# Eigenvalues for standard bivariate normal
rho = 0.6
Sigma = np.array([[1, rho], [rho, 1]])
eigvals = np.linalg.eigvalsh(Sigma)
print(f"rho = {rho}")
print(f"Eigenvalues: {eigvals}")
print(f"Predicted:   [{1 - rho}, {1 + rho}]")

# Chi-squared property: fraction of samples inside ellipse at distance sqrt(k)
np.random.seed(42)
n = 100_000
mu = np.array([0.0, 0.0])
L = np.linalg.cholesky(Sigma)
samples = (L @ np.random.randn(2, n)).T

Sigma_inv = np.linalg.inv(Sigma)
d_sq = np.sum((samples - mu) @ Sigma_inv * (samples - mu), axis=1)

for k in [1, 2, 4, 6]:
    empirical = np.mean(d_sq <= k)
    theoretical = chi2.cdf(k, df=2)
    print(f"k={k}: P(d^2 <= k) empirical={empirical:.4f}, theory={theoretical:.4f}")
```
