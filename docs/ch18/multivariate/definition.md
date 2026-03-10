# Multivariate Normal Definition

The multivariate normal distribution generalizes the univariate normal to $d$ dimensions. It is completely characterized by its mean vector $\boldsymbol{\mu}$ and covariance matrix $\boldsymbol{\Sigma}$, and arises naturally as the distribution of affine transformations of independent standard normals.

## Definition

A random vector $\mathbf{x} \in \mathbb{R}^d$ follows a multivariate normal $N(\boldsymbol{\mu}, \boldsymbol{\Sigma})$ if it can be written as

$$
\mathbf{x} = A\mathbf{z} + \boldsymbol{\mu}
$$

where $\mathbf{z} = (z_1, \ldots, z_n)^T$ with $z_k \overset{\text{iid}}{\sim} N(0, 1)$, $A \in \mathbb{R}^{d \times n}$, and $\boldsymbol{\Sigma} = AA^T$. When $\boldsymbol{\Sigma}$ is positive definite the PDF exists and equals

$$
f(\mathbf{x}) = \frac{1}{\sqrt{(2\pi)^d |\boldsymbol{\Sigma}|}} \exp\!\left(-\frac{1}{2}(\mathbf{x} - \boldsymbol{\mu})^T \boldsymbol{\Sigma}^{-1} (\mathbf{x} - \boldsymbol{\mu})\right)
$$

## Explanation

### Mean and covariance from the construction

From $\mathbf{x} = A\mathbf{z} + \boldsymbol{\mu}$ we get $E[\mathbf{x}] = \boldsymbol{\mu}$ and

$$
\text{Cov}(\mathbf{x}) = A\,E[\mathbf{z}\mathbf{z}^T]\,A^T = AA^T = \boldsymbol{\Sigma}
$$

### Joint moment generating function

The MGF is

$$
\varphi(\mathbf{t}) = E[e^{\mathbf{t}^T \mathbf{x}}] = \exp\!\left(\mathbf{t}^T \boldsymbol{\mu} + \tfrac{1}{2}\mathbf{t}^T \boldsymbol{\Sigma}\, \mathbf{t}\right)
$$

Since the MGF depends only on $\boldsymbol{\mu}$ and $\boldsymbol{\Sigma}$, these two parameters uniquely determine the distribution.

### Closure under affine transformations

If $\mathbf{x} \sim N(\boldsymbol{\mu}, \boldsymbol{\Sigma})$ then for any matrix $B$ and vector $\mathbf{c}$:

$$
B\mathbf{x} + \mathbf{c} \sim N(B\boldsymbol{\mu} + \mathbf{c},\; B\boldsymbol{\Sigma}B^T)
$$

In particular, every scalar linear combination $\mathbf{a}^T\mathbf{x}$ is univariate normal with mean $\mathbf{a}^T\boldsymbol{\mu}$ and variance $\mathbf{a}^T\boldsymbol{\Sigma}\,\mathbf{a}$.

## Examples

Generate samples from a 3-dimensional multivariate normal using the constructive definition and verify the sample statistics and MGF.

```python
import numpy as np

mu = np.array([1.0, 2.0, -1.0])
Sigma = np.array([[4, 2, 1],
                   [2, 5, -1],
                   [1, -1, 3]])

# Verify positive definiteness
eigvals = np.linalg.eigvalsh(Sigma)
print(f"Eigenvalues: {eigvals}  (all positive: {all(eigvals > 0)})")

# Generate samples via x = mu + L @ z
np.random.seed(42)
n = 50_000
L = np.linalg.cholesky(Sigma)
z = np.random.randn(3, n)
x = mu[:, None] + L @ z

print(f"\nSample mean:  {x.mean(axis=1).round(3)}")
print(f"True mean:    {mu}")
print(f"Max cov error: {np.max(np.abs(np.cov(x) - Sigma)):.4f}")

# MGF check at t = (0.1, -0.2, 0.3)
t = np.array([0.1, -0.2, 0.3])
empirical_mgf = np.exp(t @ x).mean()
theoretical_mgf = np.exp(t @ mu + 0.5 * t @ Sigma @ t)
print(f"\nMGF empirical:    {empirical_mgf:.4f}")
print(f"MGF theoretical:  {theoretical_mgf:.4f}")
```
