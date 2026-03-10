# Contours and Geometric Interpretation


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

## Overview

The contour plots of the bivariate normal distribution reveal how the **mean vector** controls the center and the **covariance matrix** controls the shape, orientation, and spread of the distribution. Understanding contours provides geometric intuition for correlation and dependence.

---

## Constant-Density Contours

The contours of the bivariate normal PDF are curves of constant density. Setting $f(x, y) = c$ for some constant $c > 0$ is equivalent to:

$$
(\mathbf{x} - \boldsymbol{\mu})^T \boldsymbol{\Sigma}^{-1} (\mathbf{x} - \boldsymbol{\mu}) = k
$$

for some constant $k > 0$. This is the equation of an **ellipse** centered at $\boldsymbol{\mu}$.

---

## Geometric Role of Parameters

### Mean Vector mu

The mean vector $\boldsymbol{\mu} = (\mu_X, \mu_Y)^T$ determines the **center** of the elliptical contours. Changing $\boldsymbol{\mu}$ translates the entire distribution without affecting its shape.

### Variances sigma_X^2 and sigma_Y^2

The marginal variances control the **spread** along each axis. Larger $\sigma_X^2$ stretches the ellipses horizontally; larger $\sigma_Y^2$ stretches them vertically.

### Correlation rho

The correlation coefficient $\rho$ controls the **orientation** (tilt) and **eccentricity** of the ellipses:

| $\rho$ | Shape | Orientation |
|:---:|:---|:---|
| $\rho = 0$ | Axes aligned with coordinate axes | No tilt |
| $\rho > 0$ | Tilted toward $y = x$ direction | Positive slope |
| $\rho < 0$ | Tilted toward $y = -x$ direction | Negative slope |
| $\rho \to \pm 1$ | Ellipses collapse to a line | Perfect linear relationship |

---

## Eigenvalue Interpretation

The axes of the contour ellipses correspond to the **eigenvectors** of $\boldsymbol{\Sigma}$, and their lengths are proportional to the square roots of the **eigenvalues**. Specifically, for the standard bivariate normal ($\sigma_X = \sigma_Y = 1$):

$$
\boldsymbol{\Sigma} = \begin{pmatrix} 1 & \rho \\ \rho & 1 \end{pmatrix}
$$

The eigenvalues are $\lambda_1 = 1 + \rho$ and $\lambda_2 = 1 - \rho$, with eigenvectors along the $45°$ and $135°$ directions. As $|\rho| \to 1$, one eigenvalue approaches zero and the ellipse degenerates.

---

## Python: Contour Gallery

The following code reproduces a grid of contour plots showing how the mean and covariance matrix affect the bivariate normal distribution. This mirrors the systematic exploration across 7 correlation values and 4 mean vectors.

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import multivariate_normal

fig, axes = plt.subplots(7, 4, figsize=(14, 20))

means = [
    [0, 0],
    [1, 0],
    [2, 0],
    [2, 2],
]

rhos = [-0.9, -0.6, -0.3, 0.0, 0.3, 0.6, 0.9]

x = np.linspace(-5, 5, 200)
y = np.linspace(-4, 4, 200)
X, Y = np.meshgrid(x, y)
pos = np.dstack((X, Y))

for i, rho in enumerate(rhos):
    for j, mu in enumerate(means):
        Sigma = [[1, rho], [rho, 1]]
        rv = multivariate_normal(mean=mu, cov=Sigma)
        Z = rv.pdf(pos)

        ax = axes[i, j]
        ax.contour(X, Y, Z, levels=6)
        ax.set_xlim(-5, 5)
        ax.set_ylim(-4, 4)
        ax.set_aspect('equal')

        if i == 0:
            ax.set_title(f'μ = {mu}', fontsize=9)
        if j == 0:
            ax.set_ylabel(f'ρ = {rho}', fontsize=9)

        ax.tick_params(labelsize=6)

plt.suptitle('Bivariate Normal Contours: Varying Mean and Correlation',
             fontsize=14, y=1.01)
plt.tight_layout()
plt.show()
```

---

## Mahalanobis Distance

The quadratic form $(\mathbf{x} - \boldsymbol{\mu})^T \boldsymbol{\Sigma}^{-1} (\mathbf{x} - \boldsymbol{\mu})$ defines the squared **Mahalanobis distance** from $\mathbf{x}$ to $\boldsymbol{\mu}$. Points on the same contour ellipse have the same Mahalanobis distance from the mean.

For the bivariate case, this squared distance follows a $\chi^2(2)$ distribution:

$$
(\mathbf{X} - \boldsymbol{\mu})^T \boldsymbol{\Sigma}^{-1} (\mathbf{X} - \boldsymbol{\mu}) \sim \chi^2(2)
$$

This means the probability contained within the ellipse at Mahalanobis distance $\sqrt{k}$ is $P(\chi^2(2) \leq k) = 1 - e^{-k/2}$.

---

## Key Takeaways

- Contours of the bivariate normal are **ellipses** centered at $\boldsymbol{\mu}$.
- $\boldsymbol{\mu}$ controls position; $\sigma_X, \sigma_Y$ control spread; $\rho$ controls tilt and eccentricity.
- The ellipse axes align with the eigenvectors of $\boldsymbol{\Sigma}$, with lengths proportional to the square roots of the eigenvalues.
- The Mahalanobis distance provides a scale-invariant measure of distance from the center.
