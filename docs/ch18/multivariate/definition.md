# Definition via Mean Vector and Covariance Matrix


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

## Overview

The **multivariate normal distribution** generalizes the univariate and bivariate normal to arbitrary dimension $d$. It is defined constructively as an affine transformation of independent standard normals, and is completely characterized by its mean vector $\boldsymbol{\mu}$ and covariance matrix $\boldsymbol{\Sigma}$.

---

## PDF

For a $d$-dimensional random vector $\mathbf{x} = (x_1, x_2, \ldots, x_d)^T$ following $\mathbf{x} \sim N(\boldsymbol{\mu}, \boldsymbol{\Sigma})$:

$$
f(\mathbf{x}) = \frac{1}{\sqrt{(2\pi)^d |\boldsymbol{\Sigma}|}} \exp\left(-\frac{1}{2}(\mathbf{x} - \boldsymbol{\mu})^T \boldsymbol{\Sigma}^{-1} (\mathbf{x} - \boldsymbol{\mu})\right)
$$

where:

- $\boldsymbol{\mu} \in \mathbb{R}^d$ is the **mean vector**
- $\boldsymbol{\Sigma} \in \mathbb{R}^{d \times d}$ is the **covariance matrix** (symmetric positive definite)
- $|\boldsymbol{\Sigma}|$ is the determinant of $\boldsymbol{\Sigma}$

---

## Constructive Definition via Linear Transformation

A multivariate normal $\mathbf{x} \in \mathbb{R}^d$ can always be written as:

$$
\mathbf{x} = A\mathbf{z} + \boldsymbol{\mu}
$$

where:

- $\mathbf{z} = (z_1, z_2, \ldots, z_n)^T$ with $z_k \overset{\text{iid}}{\sim} N(0, 1)$
- $A \in \mathbb{R}^{d \times n}$ is a constant matrix
- $\boldsymbol{\mu} \in \mathbb{R}^d$ is a constant vector

This definition is fundamental because it tells us how to **construct** a multivariate normal from simple building blocks (independent standard normals).

---

## Computing Mean and Covariance

From $\mathbf{x} = A\mathbf{z} + \boldsymbol{\mu}$:

**Mean:**

$$
E[\mathbf{x}] = E[A\mathbf{z} + \boldsymbol{\mu}] = A \cdot E[\mathbf{z}] + \boldsymbol{\mu} = A \cdot \mathbf{0} + \boldsymbol{\mu} = \boldsymbol{\mu}
$$

**Covariance matrix:**

$$
\boldsymbol{\Sigma} = E[(\mathbf{x} - \boldsymbol{\mu})(\mathbf{x} - \boldsymbol{\mu})^T] = E[(A\mathbf{z})(A\mathbf{z})^T] = A \cdot E[\mathbf{z}\mathbf{z}^T] \cdot A^T = A I A^T = AA^T
$$

So $\boldsymbol{\Sigma} = AA^T$, which is automatically symmetric and positive semi-definite for any matrix $A$.

---

## Joint MGF

The moment generating function of the multivariate normal extends the univariate formula. Recall that for $X \sim N(\mu, \sigma^2)$:

$$
\varphi(t) = E[e^{tX}] = e^{\mu t + \frac{1}{2}\sigma^2 t^2}
$$

For $\mathbf{x} \sim N(\boldsymbol{\mu}, \boldsymbol{\Sigma})$, the joint MGF is:

$$
\varphi(\mathbf{t}) = E[e^{\mathbf{t}^T \mathbf{x}}] = e^{\mathbf{t}^T \boldsymbol{\mu} + \frac{1}{2}\mathbf{t}^T \boldsymbol{\Sigma} \mathbf{t}}
$$

### Derivation

Since $\mathbf{x} = A\mathbf{z} + \boldsymbol{\mu}$:

$$
\mathbf{t}^T \mathbf{x} = \mathbf{t}^T(A\mathbf{z} + \boldsymbol{\mu}) = \sum_k a_k z_k + b
$$

where $a_k$ are the components of $A^T\mathbf{t}$ and $b = \mathbf{t}^T\boldsymbol{\mu}$. This is a linear combination of independent standard normals, hence:

$$
\mathbf{t}^T \mathbf{x} \sim N(\mu_1, \sigma_1^2)
$$

with:

$$
\mu_1 = E[\mathbf{t}^T\mathbf{x}] = \mathbf{t}^T\boldsymbol{\mu}
$$

$$
\sigma_1^2 = \text{Var}(\mathbf{t}^T\mathbf{x}) = \mathbf{t}^T A E[\mathbf{z}\mathbf{z}^T] A^T \mathbf{t} = \mathbf{t}^T AA^T \mathbf{t} = \mathbf{t}^T \boldsymbol{\Sigma} \mathbf{t}
$$

Therefore:

$$
\varphi_{\mathbf{x}}(\mathbf{t}) = E[e^{\mathbf{t}^T\mathbf{x}}] = \varphi_{N(\mu_1, \sigma_1^2)}(1) = e^{\mu_1 + \frac{1}{2}\sigma_1^2} = e^{\mathbf{t}^T\boldsymbol{\mu} + \frac{1}{2}\mathbf{t}^T\boldsymbol{\Sigma}\mathbf{t}}
$$

---

## Key Properties

The joint MGF immediately yields important consequences.

**Property 1: $\boldsymbol{\mu}$ and $\boldsymbol{\Sigma}$ completely determine the distribution.**

Since the MGF is entirely determined by $\boldsymbol{\mu}$ and $\boldsymbol{\Sigma}$, and the MGF uniquely determines the distribution, two multivariate normal vectors with the same mean and covariance have the same distribution.

**Property 2: Linear combinations are normal.**

Any linear combination $\mathbf{a}^T\mathbf{x}$ is univariate normal:

$$
\mathbf{a}^T\mathbf{x} \sim N(\mathbf{a}^T\boldsymbol{\mu},\; \mathbf{a}^T\boldsymbol{\Sigma}\mathbf{a})
$$

More generally, any affine transformation $B\mathbf{x} + \mathbf{c}$ is multivariate normal:

$$
B\mathbf{x} + \mathbf{c} \sim N(B\boldsymbol{\mu} + \mathbf{c},\; B\boldsymbol{\Sigma}B^T)
$$

---

## Python Implementation

```python
import numpy as np
from scipy.stats import multivariate_normal

# Define a 3-dimensional multivariate normal
mu = np.array([1, 2, -1])
Sigma = np.array([
    [4,  2,  1],
    [2,  5, -1],
    [1, -1,  3]
])

# Verify positive definiteness
eigenvalues = np.linalg.eigvalsh(Sigma)
print(f"Eigenvalues of Σ: {eigenvalues}")
print(f"Positive definite: {all(eigenvalues > 0)}")

# Generate samples via constructive definition
np.random.seed(42)
n = 10_000
A = np.linalg.cholesky(Sigma)  # Σ = AA^T
z = np.random.randn(3, n)
x = A @ z + mu[:, np.newaxis]

print(f"\nSample mean: {x.mean(axis=1)}")
print(f"True mean:   {mu}")
print(f"\nSample covariance:\n{np.cov(x)}")
print(f"True covariance:\n{Sigma}")

# Verify joint MGF: E[exp(t^T x)] should equal exp(t^T μ + 0.5 t^T Σ t)
t = np.array([0.1, -0.2, 0.3])
empirical_mgf = np.exp((t @ x)).mean()
theoretical_mgf = np.exp(t @ mu + 0.5 * t @ Sigma @ t)
print(f"\nEmpirical MGF at t={t}: {empirical_mgf:.4f}")
print(f"Theoretical MGF:         {theoretical_mgf:.4f}")
```

---

## Key Takeaways

- The multivariate normal is defined constructively as $\mathbf{x} = A\mathbf{z} + \boldsymbol{\mu}$ where $\mathbf{z}$ has iid standard normal components.
- The covariance matrix is $\boldsymbol{\Sigma} = AA^T$, automatically symmetric positive semi-definite.
- The joint MGF $\varphi(\mathbf{t}) = e^{\mathbf{t}^T\boldsymbol{\mu} + \frac{1}{2}\mathbf{t}^T\boldsymbol{\Sigma}\mathbf{t}}$ uniquely determines the distribution through $\boldsymbol{\mu}$ and $\boldsymbol{\Sigma}$.
- Any linear combination or affine transformation of a multivariate normal is again multivariate normal.
