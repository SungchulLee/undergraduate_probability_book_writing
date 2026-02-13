# Joint PDF of the Bivariate Normal

## Overview

The **bivariate normal distribution** is the simplest multivariate normal — a joint distribution of two random variables $X$ and $Y$ whose dependence structure is completely determined by five parameters: the two means, two standard deviations, and the correlation coefficient.

---

## PDF in Matrix Form

If $\mathbf{x} = (x, y)^T$ follows a bivariate normal $N(\boldsymbol{\mu}, \boldsymbol{\Sigma})$, the joint PDF is:

$$
f(\mathbf{x}) = \frac{1}{\sqrt{(2\pi)^2 |\boldsymbol{\Sigma}|}} \exp\left(-\frac{1}{2}(\mathbf{x} - \boldsymbol{\mu})^T \boldsymbol{\Sigma}^{-1} (\mathbf{x} - \boldsymbol{\mu})\right)
$$

where:

- $\boldsymbol{\mu} = (\mu_X, \mu_Y)^T$ is the **mean vector**
- $\boldsymbol{\Sigma}$ is the $2 \times 2$ **covariance matrix**
- $|\boldsymbol{\Sigma}|$ is the **determinant** of $\boldsymbol{\Sigma}$

---

## Covariance Matrix and Its Inverse

The covariance matrix for the bivariate case is:

$$
\boldsymbol{\Sigma} = \begin{pmatrix} \sigma_X^2 & \rho\sigma_X\sigma_Y \\ \rho\sigma_X\sigma_Y & \sigma_Y^2 \end{pmatrix}
$$

Its determinant is:

$$
|\boldsymbol{\Sigma}| = \sigma_X^2 \sigma_Y^2 (1 - \rho^2)
$$

and the inverse is:

$$
\boldsymbol{\Sigma}^{-1} = \frac{1}{(1 - \rho^2)\sigma_X^2 \sigma_Y^2} \begin{pmatrix} \sigma_Y^2 & -\rho\sigma_X\sigma_Y \\ -\rho\sigma_X\sigma_Y & \sigma_X^2 \end{pmatrix}
$$

Note that $|\boldsymbol{\Sigma}| > 0$ requires $|\rho| < 1$. When $\rho = \pm 1$, the distribution degenerates to a line in the plane.

---

## Explicit Scalar Form

Introducing the standardized variables $\tilde{x} = \frac{x - \mu_X}{\sigma_X}$ and $\tilde{y} = \frac{y - \mu_Y}{\sigma_Y}$, the quadratic form in the exponent becomes:

$$
(\mathbf{x} - \boldsymbol{\mu})^T \boldsymbol{\Sigma}^{-1} (\mathbf{x} - \boldsymbol{\mu}) = \frac{\tilde{x}^2 + \tilde{y}^2 - 2\rho\tilde{x}\tilde{y}}{1 - \rho^2}
$$

This gives the explicit scalar PDF:

$$
f(x, y) = \frac{1}{2\pi\sigma_X\sigma_Y\sqrt{1 - \rho^2}} \exp\left(-\frac{\tilde{x}^2 + \tilde{y}^2 - 2\rho\tilde{x}\tilde{y}}{2(1 - \rho^2)}\right)
$$

---

## Special Case: Independent Components ($\rho = 0$)

When $X$ and $Y$ are independent (i.e., $\rho = 0$), the cross term vanishes and the PDF factors:

$$
f(x, y) = \frac{1}{2\pi\sigma_X\sigma_Y} \exp\left(-\frac{\tilde{x}^2 + \tilde{y}^2}{2}\right) = \underbrace{\frac{1}{\sqrt{2\pi}\sigma_X} e^{-\tilde{x}^2/2}}_{f_X(x)} \cdot \underbrace{\frac{1}{\sqrt{2\pi}\sigma_Y} e^{-\tilde{y}^2/2}}_{f_Y(y)}
$$

This factorization confirms that $\rho = 0$ implies independence for the bivariate normal.

---

## Special Case: Standard Bivariate Normal

When $\mu_X = \mu_Y = 0$ and $\sigma_X = \sigma_Y = 1$:

$$
f(x, y) = \frac{1}{2\pi\sqrt{1 - \rho^2}} \exp\left(-\frac{x^2 + y^2 - 2\rho xy}{2(1 - \rho^2)}\right)
$$

---

## Python Implementation

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import multivariate_normal

def bivariate_normal_pdf(x, y, mu_x=0, mu_y=0, sigma_x=1, sigma_y=1, rho=0):
    """Compute the bivariate normal PDF explicitly."""
    x_tilde = (x - mu_x) / sigma_x
    y_tilde = (y - mu_y) / sigma_y
    z = (x_tilde**2 + y_tilde**2 - 2 * rho * x_tilde * y_tilde) / (1 - rho**2)
    return np.exp(-z / 2) / (2 * np.pi * sigma_x * sigma_y * np.sqrt(1 - rho**2))

# Plot the bivariate normal PDF
fig, axes = plt.subplots(1, 3, figsize=(15, 4))
x = np.linspace(-3, 3, 200)
y = np.linspace(-3, 3, 200)
X, Y = np.meshgrid(x, y)

for ax, rho, title in zip(axes, [0, 0.7, -0.7],
                           ['ρ = 0', 'ρ = 0.7', 'ρ = −0.7']):
    Z = bivariate_normal_pdf(X, Y, rho=rho)
    ax.contourf(X, Y, Z, levels=20, cmap='Blues')
    ax.contour(X, Y, Z, levels=8, colors='navy', linewidths=0.5)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title(title)
    ax.set_aspect('equal')

plt.suptitle('Standard Bivariate Normal PDF', y=1.02)
plt.tight_layout()
plt.show()
```

### Surface Plot

```python
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')

x = np.linspace(-3, 3, 100)
y = np.linspace(-3, 3, 100)
X, Y = np.meshgrid(x, y)
Z = bivariate_normal_pdf(X, Y, rho=0.5)

ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.8)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('f(x, y)')
ax.set_title('Bivariate Normal PDF (ρ = 0.5)')
plt.tight_layout()
plt.show()
```

---

## Key Takeaways

- The bivariate normal is characterized by five parameters: $\mu_X, \mu_Y, \sigma_X, \sigma_Y, \rho$.
- The matrix form $f(\mathbf{x}) \propto \exp\left(-\frac{1}{2}(\mathbf{x} - \boldsymbol{\mu})^T \boldsymbol{\Sigma}^{-1}(\mathbf{x} - \boldsymbol{\mu})\right)$ generalizes directly to higher dimensions.
- When $\rho = 0$, the joint PDF factors into a product of marginals, confirming independence.
- The covariance matrix must be positive definite ($|\rho| < 1$) for the distribution to be non-degenerate.
