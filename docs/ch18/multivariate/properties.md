# Properties and Linear Transformations

The multivariate normal is closed under linear transformations, marginalization, and conditioning. A distinctive feature is that zero covariance between components implies their independence, a property unique to this distribution family.

## Definition

Let $\mathbf{x} \sim N(\boldsymbol{\mu}, \boldsymbol{\Sigma})$. If $\boldsymbol{\Sigma}$ is diagonal, i.e., $\boldsymbol{\Sigma} = \text{diag}(\sigma_1^2, \ldots, \sigma_d^2)$, then the components $x_1, \ldots, x_d$ are **mutually independent**:

$$
\varphi(\mathbf{t}) = \prod_{i=1}^d \exp\!\left(\mu_i t_i + \tfrac{1}{2}\sigma_i^2 t_i^2\right)
$$

More generally, if $\Sigma_{ij} = 0$ for all $j \neq i$, then $x_i$ is independent of all other components.

## Explanation

### Proof via MGF factorization

When $\boldsymbol{\Sigma}$ is diagonal, $\mathbf{t}^T \boldsymbol{\Sigma}\,\mathbf{t} = \sum_i \sigma_i^2 t_i^2$, so the joint MGF factors into a product of marginal MGFs. Since the joint MGF equals the product of the marginals, the components are independent.

### Affine transformation

For $B \in \mathbb{R}^{m \times d}$ and $\mathbf{c} \in \mathbb{R}^m$:

$$
B\mathbf{x} + \mathbf{c} \sim N(B\boldsymbol{\mu} + \mathbf{c},\; B\boldsymbol{\Sigma}B^T)
$$

Special cases include scalar linear combinations $\mathbf{a}^T\mathbf{x} \sim N(\mathbf{a}^T\boldsymbol{\mu}, \mathbf{a}^T\boldsymbol{\Sigma}\,\mathbf{a})$ and marginalization by selecting a subvector (equivalent to multiplying by a selection matrix).

### Critical caveat

The zero-covariance-implies-independence property requires the joint distribution to be multivariate normal. For arbitrary random variables, zero covariance does not imply even pairwise independence.

## Examples

Verify that a diagonal covariance yields independent components, and that an affine transformation produces the predicted distribution.

```python
import numpy as np

np.random.seed(42)
n = 50_000

# Diagonal Sigma: components should be independent
mu = np.array([1.0, 2.0, 3.0])
Sigma_diag = np.diag([4.0, 3.0, 2.0])
L = np.linalg.cholesky(Sigma_diag)
x = mu[:, None] + L @ np.random.randn(3, n)

p_joint = np.mean((x[0] > 1) & (x[1] > 2))
p_prod = np.mean(x[0] > 1) * np.mean(x[1] > 2)
print("Diagonal Sigma independence test:")
print(f"  P(X1>1, X2>2)       = {p_joint:.4f}")
print(f"  P(X1>1) * P(X2>2)   = {p_prod:.4f}")

# Affine transformation y = Bx + c
B = np.array([[1, 1, 0], [0, 1, -1]])
c = np.array([10.0, 20.0])
y = B @ x + c[:, None]

print("\nAffine transformation y = Bx + c:")
print(f"  Sample mean: {y.mean(axis=1).round(3)}")
print(f"  Theory mean: {B @ mu + c}")
print(f"  Sample cov:\n{np.cov(y).round(3)}")
print(f"  Theory cov:\n{B @ Sigma_diag @ B.T}")
```
