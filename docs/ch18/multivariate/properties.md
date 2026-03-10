# Properties and Linear Transformations


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

## Overview

The multivariate normal has remarkable closure properties: it is closed under linear transformations, marginalization, and conditioning. This section focuses on the properties that follow from the joint MGF, particularly the relationship between zero covariance and independence.

---

## Property 1: Uniqueness via MGF

If two multivariate normal random vectors $\mathbf{x}$ and $\mathbf{y}$ share the same mean $\boldsymbol{\mu}$ and covariance matrix $\boldsymbol{\Sigma}$, then their joint MGFs are identical:

$$
\varphi_{\mathbf{x}}(\mathbf{t}) = e^{\mathbf{t}^T\boldsymbol{\mu} + \frac{1}{2}\mathbf{t}^T\boldsymbol{\Sigma}\mathbf{t}} = \varphi_{\mathbf{y}}(\mathbf{t})
$$

By the uniqueness theorem for MGFs, $\mathbf{x}$ and $\mathbf{y}$ have the same distribution.

---

## Property 2: Zero Off-Diagonals Imply Independence

If a multivariate normal $\mathbf{x} \sim N(\boldsymbol{\mu}, \boldsymbol{\Sigma})$ has a diagonal covariance matrix (all off-diagonal entries are zero), then all components $x_1, x_2, \ldots, x_d$ are **mutually independent**.

### Proof via MGF Factorization

When $\boldsymbol{\Sigma} = \text{diag}(\sigma_1^2, \sigma_2^2, \ldots, \sigma_d^2)$:

$$
\mathbf{t}^T\boldsymbol{\Sigma}\mathbf{t} = \sum_{i=1}^d \sigma_i^2 t_i^2
$$

So the joint MGF factors:

$$
\varphi_{\mathbf{x}}(\mathbf{t}) = e^{\sum_i \mu_i t_i + \frac{1}{2}\sum_i \sigma_i^2 t_i^2} = \prod_{i=1}^d \underbrace{e^{\mu_i t_i + \frac{1}{2}\sigma_i^2 t_i^2}}_{\varphi_{N(\mu_i, \sigma_i^2)}(t_i)}
$$

Since the joint MGF equals the product of the marginal MGFs, the components are independent.

---

## Property 3: Pairwise Zero Covariance Implies Independence

More generally, if for a fixed index $i$, we have $\Sigma_{ij} = 0$ for all $j \neq i$, then $x_i$ is independent of all other components $(x_j)_{j \neq i}$.

### Proof Sketch

Construct a vector $\mathbf{y}$ with the same mean and covariance as $\mathbf{x}$, where $y_i$ is independent of $y_j$ for $j \neq i$. Since the off-diagonal entries involving row/column $i$ are zero, the joint MGFs of $\mathbf{x}$ and $\mathbf{y}$ are identical. Hence $\mathbf{x}$ and $\mathbf{y}$ have the same distribution, and in particular $x_i$ is independent of the rest.

!!! note "Critical Caveat"
    This property requires the joint distribution to be multivariate normal. Pairwise zero covariance among arbitrary (non-jointly-normal) random variables does **not** imply pairwise independence.

---

## Linear Transformations

### Affine Transformation

If $\mathbf{x} \sim N(\boldsymbol{\mu}, \boldsymbol{\Sigma})$ and $\mathbf{y} = B\mathbf{x} + \mathbf{c}$ where $B \in \mathbb{R}^{m \times d}$ and $\mathbf{c} \in \mathbb{R}^m$, then:

$$
\mathbf{y} \sim N(B\boldsymbol{\mu} + \mathbf{c},\; B\boldsymbol{\Sigma}B^T)
$$

### Special Cases

**Scalar linear combination:** $a^T\mathbf{x} \sim N(\mathbf{a}^T\boldsymbol{\mu}, \mathbf{a}^T\boldsymbol{\Sigma}\mathbf{a})$

**Sum of components:** $\sum_i x_i \sim N\!\left(\sum_i \mu_i,\; \sum_i\sum_j \Sigma_{ij}\right)$

**Subvector (marginalization):** Selecting components $x_{i_1}, \ldots, x_{i_m}$ corresponds to multiplication by a selection matrix $B$, yielding a multivariate normal with the appropriate sub-mean and sub-covariance.

---

## Python: Verifying Properties

```python
import numpy as np

np.random.seed(42)
n = 50_000

# 3D multivariate normal
mu = np.array([1, 2, 3])
Sigma = np.array([
    [4, 0, 0],
    [0, 3, 0],
    [0, 0, 2]
])

# Generate samples
L = np.linalg.cholesky(Sigma)
z = np.random.randn(3, n)
x = L @ z + mu[:, np.newaxis]

# Property 2: diagonal Sigma → independence
# Test: P(X1 > 1, X2 > 2) should equal P(X1 > 1) * P(X2 > 2)
p_joint = np.mean((x[0] > 1) & (x[1] > 2))
p_x1 = np.mean(x[0] > 1)
p_x2 = np.mean(x[1] > 2)
print("=== Diagonal Σ: Independence Test ===")
print(f"P(X1>1, X2>2)     = {p_joint:.4f}")
print(f"P(X1>1) * P(X2>2) = {p_x1 * p_x2:.4f}")

# Linear transformation
B = np.array([[1, 1, 0], [0, 1, -1]])
c = np.array([10, 20])
y = B @ x + c[:, np.newaxis]

print("\n=== Affine Transformation y = Bx + c ===")
print(f"Sample mean of y: {y.mean(axis=1)}")
print(f"Theoretical mean:  {B @ mu + c}")
print(f"\nSample cov of y:\n{np.cov(y)}")
print(f"Theoretical cov:\n{B @ Sigma @ B.T}")

# Non-diagonal Sigma: verify pairwise independence breaks
Sigma2 = np.array([
    [4, 2, 0],
    [2, 3, 0],
    [0, 0, 2]
])
L2 = np.linalg.cholesky(Sigma2)
x2 = L2 @ z + mu[:, np.newaxis]

print("\n=== Non-diagonal Σ (X3 independent of X1, X2) ===")
p_joint13 = np.mean((x2[0] > 1) & (x2[2] > 3))
p_x1_2 = np.mean(x2[0] > 1)
p_x3_2 = np.mean(x2[2] > 3)
print(f"P(X1>1, X3>3)     = {p_joint13:.4f}")
print(f"P(X1>1) * P(X3>3) = {p_x1_2 * p_x3_2:.4f}")

p_joint12 = np.mean((x2[0] > 1) & (x2[1] > 2))
p_x2_2 = np.mean(x2[1] > 2)
print(f"\nP(X1>1, X2>2)     = {p_joint12:.4f}")
print(f"P(X1>1) * P(X2>2) = {p_x1_2 * p_x2_2:.4f}  (not equal — dependent)")
```

---

## Key Takeaways

- For the multivariate normal, $\boldsymbol{\mu}$ and $\boldsymbol{\Sigma}$ uniquely determine the distribution (via the MGF).
- Zero off-diagonal covariance entries imply independence of the corresponding components — a property **unique** to the multivariate normal family.
- The multivariate normal is **closed** under affine transformations: $B\mathbf{x} + \mathbf{c}$ is again multivariate normal.
- Marginalization is a special case of linear transformation (selecting components via a matrix).
