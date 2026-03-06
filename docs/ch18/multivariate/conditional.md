# Conditional Distributions in the Multivariate Case

## Overview

The conditional distribution of a subset of a multivariate normal vector, given the remaining components, is again multivariate normal. The formulas involve the **partitioned covariance matrix** and, equivalently, the **precision matrix** (inverse covariance). This section derives the conditional mean and variance using both approaches and extends to the important **linear-Gaussian model**.

---

## Partitioned Multivariate Normal

Partition the vector $\mathbf{x}$ and its parameters as:

$$

\mathbf{x} = \begin{pmatrix} \mathbf{x}_1 \\ \mathbf{x}_2 \end{pmatrix} \sim N\!\left(\begin{pmatrix} \boldsymbol{\mu}_1 \\ \boldsymbol{\mu}_2 \end{pmatrix},\; \begin{pmatrix} \boldsymbol{\Sigma}_{11} & \boldsymbol{\Sigma}_{12} \\ \boldsymbol{\Sigma}_{21} & \boldsymbol{\Sigma}_{22} \end{pmatrix}\right)

$$

where $\mathbf{x}_1 \in \mathbb{R}^{d_1}$ and $\mathbf{x}_2 \in \mathbb{R}^{d_2}$ with $d_1 + d_2 = d$.

---

## Marginal Distribution

The marginal of $\mathbf{x}_1$ is simply:

$$

\mathbf{x}_1 \sim N(\boldsymbol{\mu}_1, \boldsymbol{\Sigma}_{11})

$$

---

## Conditional Distribution

The conditional distribution of $\mathbf{x}_1$ given $\mathbf{x}_2$ is:

$$

\mathbf{x}_1 \mid \mathbf{x}_2 \;\sim\; N\!\left(\boldsymbol{\mu}_{1|2},\; \boldsymbol{\Sigma}_{1|2}\right)

$$

where:

$$

\boldsymbol{\mu}_{1|2} = \boldsymbol{\mu}_1 + \boldsymbol{\Sigma}_{12}\boldsymbol{\Sigma}_{22}^{-1}(\mathbf{x}_2 - \boldsymbol{\mu}_2)

$$

$$

\boldsymbol{\Sigma}_{1|2} = \boldsymbol{\Sigma}_{11} - \boldsymbol{\Sigma}_{12}\boldsymbol{\Sigma}_{22}^{-1}\boldsymbol{\Sigma}_{21}

$$

The matrix $\boldsymbol{\Sigma}_{1|2}$ is the **Schur complement** of $\boldsymbol{\Sigma}_{22}$ in $\boldsymbol{\Sigma}$.

---

## Precision Matrix Formulation

Define the **precision matrix** (information matrix) $\boldsymbol{\Lambda} = \boldsymbol{\Sigma}^{-1}$ with the partition:

$$

\boldsymbol{\Lambda} = \begin{pmatrix} \boldsymbol{\Lambda}_{11} & \boldsymbol{\Lambda}_{12} \\ \boldsymbol{\Lambda}_{21} & \boldsymbol{\Lambda}_{22} \end{pmatrix}

$$

The conditional parameters can be expressed directly in terms of $\boldsymbol{\Lambda}$:

$$

\boldsymbol{\Sigma}_{1|2} = \boldsymbol{\Lambda}_{11}^{-1}

$$

$$

\boldsymbol{\mu}_{1|2} = \boldsymbol{\mu}_1 - \boldsymbol{\Lambda}_{11}^{-1}\boldsymbol{\Lambda}_{12}(\mathbf{x}_2 - \boldsymbol{\mu}_2)

$$

!!! info "Why the Precision Matrix?"
    The precision matrix directly encodes **conditional independence** structure. If $\Lambda_{ij} = 0$, then $x_i$ and $x_j$ are conditionally independent given all other variables. This makes the precision matrix central to graphical models (Gaussian Markov random fields).

---

## Derivation: Properties of Sigma and Lambda

From the identity $\boldsymbol{\Sigma}\boldsymbol{\Lambda} = I$:

$$

\begin{pmatrix} \boldsymbol{\Sigma}_{11} & \boldsymbol{\Sigma}_{12} \\ \boldsymbol{\Sigma}_{21} & \boldsymbol{\Sigma}_{22} \end{pmatrix} \begin{pmatrix} \boldsymbol{\Lambda}_{11} & \boldsymbol{\Lambda}_{12} \\ \boldsymbol{\Lambda}_{21} & \boldsymbol{\Lambda}_{22} \end{pmatrix} = \begin{pmatrix} I_{11} & 0_{12} \\ 0_{21} & I_{22} \end{pmatrix}

$$

From the $(1,2)$ block: $\boldsymbol{\Sigma}_{11}\boldsymbol{\Lambda}_{12} + \boldsymbol{\Sigma}_{12}\boldsymbol{\Lambda}_{22} = \mathbf{0}$.

From the $(1,1)$ block: $\boldsymbol{\Sigma}_{11}\boldsymbol{\Lambda}_{11} + \boldsymbol{\Sigma}_{12}\boldsymbol{\Lambda}_{21} = I$.

From the $(2,1)$ block: $\boldsymbol{\Sigma}_{21}\boldsymbol{\Lambda}_{11} + \boldsymbol{\Sigma}_{22}\boldsymbol{\Lambda}_{21} = \mathbf{0}$, giving $\boldsymbol{\Lambda}_{21} = -\boldsymbol{\Sigma}_{22}^{-1}\boldsymbol{\Sigma}_{21}\boldsymbol{\Lambda}_{11}$.

Substituting into the $(1,1)$ equation:

$$

\boldsymbol{\Lambda}_{11}^{-1} = \boldsymbol{\Sigma}_{11} - \boldsymbol{\Sigma}_{12}\boldsymbol{\Sigma}_{22}^{-1}\boldsymbol{\Sigma}_{21}

$$

Similarly, from the $(1,2)$ block:

$$

\boldsymbol{\Lambda}_{11}^{-1}\boldsymbol{\Lambda}_{12} = -\boldsymbol{\Sigma}_{12}\boldsymbol{\Sigma}_{22}^{-1}

$$

These are the key identities connecting the covariance and precision parameterizations.

---

## Derivation: Completing the Square

Starting from the quadratic form in the exponent with $\mathbf{y}_i = \mathbf{x}_i - \boldsymbol{\mu}_i$:

$$

(\mathbf{x} - \boldsymbol{\mu})^T\boldsymbol{\Sigma}^{-1}(\mathbf{x} - \boldsymbol{\mu}) = \mathbf{y}_1^T\boldsymbol{\Lambda}_{11}\mathbf{y}_1 + \mathbf{y}_1^T\boldsymbol{\Lambda}_{12}\mathbf{y}_2 + \mathbf{y}_2^T\boldsymbol{\Lambda}_{21}\mathbf{y}_1 + \mathbf{y}_2^T\boldsymbol{\Lambda}_{22}\mathbf{y}_2

$$

Treating $\mathbf{y}_2$ as fixed and completing the square in $\mathbf{y}_1$:

$$

= (\mathbf{y}_1 - \boldsymbol{\alpha})^T\boldsymbol{\Lambda}_{11}(\mathbf{y}_1 - \boldsymbol{\alpha}) + \text{terms in } \mathbf{y}_2 \text{ only}

$$

where $\boldsymbol{\alpha} = -\boldsymbol{\Lambda}_{11}^{-1}\boldsymbol{\Lambda}_{12}\mathbf{y}_2$. Reverting to the original coordinates:

$$

\mathbf{x}_1 - \boldsymbol{\mu}_{1|2} = \mathbf{y}_1 - \boldsymbol{\alpha} = \mathbf{x}_1 - \left(\boldsymbol{\mu}_1 - \boldsymbol{\Lambda}_{11}^{-1}\boldsymbol{\Lambda}_{12}(\mathbf{x}_2 - \boldsymbol{\mu}_2)\right)

$$

This confirms $\boldsymbol{\mu}_{1|2} = \boldsymbol{\mu}_1 - \boldsymbol{\Lambda}_{11}^{-1}\boldsymbol{\Lambda}_{12}(\mathbf{x}_2 - \boldsymbol{\mu}_2)$ and $\boldsymbol{\Sigma}_{1|2} = \boldsymbol{\Lambda}_{11}^{-1}$.

---

## Linear-Gaussian Model

A particularly important application arises when $\mathbf{x}$ and $\mathbf{y}$ are related by a linear model with Gaussian noise:

$$

\mathbf{x} \sim N(\boldsymbol{\mu}_x, \boldsymbol{\Sigma}_x), \qquad \mathbf{y} = A\mathbf{x} + \mathbf{b} + \boldsymbol{\varepsilon}, \quad \boldsymbol{\varepsilon} \sim N(\mathbf{0}, \boldsymbol{\Sigma}_\varepsilon)

$$

where $\boldsymbol{\varepsilon}$ is independent of $\mathbf{x}$. Then the joint distribution is:

$$

\begin{pmatrix} \mathbf{x} \\ \mathbf{y} \end{pmatrix} \sim N\!\left(\begin{pmatrix} \boldsymbol{\mu}_x \\ A\boldsymbol{\mu}_x + \mathbf{b} \end{pmatrix},\; \begin{pmatrix} \boldsymbol{\Sigma}_x & \boldsymbol{\Sigma}_x A^T \\ A\boldsymbol{\Sigma}_x & A\boldsymbol{\Sigma}_x A^T + \boldsymbol{\Sigma}_\varepsilon \end{pmatrix}\right)

$$

### Marginal of y

$$

\mathbf{y} \sim N(A\boldsymbol{\mu}_x + \mathbf{b},\; A\boldsymbol{\Sigma}_x A^T + \boldsymbol{\Sigma}_\varepsilon)

$$

### Posterior: x | y

Applying the conditional formulas:

$$

\boldsymbol{\mu}_{x|y} = \boldsymbol{\mu}_x + \boldsymbol{\Sigma}_x A^T (A\boldsymbol{\Sigma}_x A^T + \boldsymbol{\Sigma}_\varepsilon)^{-1}(\mathbf{y} - A\boldsymbol{\mu}_x - \mathbf{b})

$$

$$

\boldsymbol{\Sigma}_{x|y} = \boldsymbol{\Sigma}_x - \boldsymbol{\Sigma}_x A^T (A\boldsymbol{\Sigma}_x A^T + \boldsymbol{\Sigma}_\varepsilon)^{-1} A\boldsymbol{\Sigma}_x

$$

### Precision Form (via Woodbury Identity)

Using the Woodbury identity $(A + UCV)^{-1} = A^{-1} - A^{-1}U(C^{-1} + VA^{-1}U)^{-1}VA^{-1}$:

$$

\boldsymbol{\Sigma}_{x|y}^{-1} = \boldsymbol{\Sigma}_x^{-1} + A^T\boldsymbol{\Sigma}_\varepsilon^{-1} A

$$

$$

\boldsymbol{\mu}_{x|y} = \boldsymbol{\Sigma}_{x|y}\left(\boldsymbol{\Sigma}_x^{-1}\boldsymbol{\mu}_x + A^T\boldsymbol{\Sigma}_\varepsilon^{-1}(\mathbf{y} - \mathbf{b})\right)

$$

!!! note "Connection to Bayesian Inference"
    In the precision form, the posterior precision equals the prior precision plus the data precision. The posterior mean is a precision-weighted combination of the prior mean and the data. This is the **Bayesian update rule** for Gaussian models and forms the basis of the Kalman filter.

### Derivation of the Precision Matrix

From $\log p(\mathbf{x}, \mathbf{y}) = \log p(\mathbf{x}) + \log p(\mathbf{y} \mid \mathbf{x})$:

$$

\log p(\mathbf{x}, \mathbf{y}) \propto -\frac{1}{2}\tilde{\mathbf{x}}^T\boldsymbol{\Sigma}_x^{-1}\tilde{\mathbf{x}} - \frac{1}{2}(\tilde{\mathbf{y}} - A\tilde{\mathbf{x}})^T\boldsymbol{\Sigma}_\varepsilon^{-1}(\tilde{\mathbf{y}} - A\tilde{\mathbf{x}})

$$

where $\tilde{\mathbf{x}} = \mathbf{x} - \boldsymbol{\mu}_x$ and $\tilde{\mathbf{y}} = \mathbf{y} - A\boldsymbol{\mu}_x - \mathbf{b}$. Expanding:

$$

= -\frac{1}{2}\begin{pmatrix} \tilde{\mathbf{x}} \\ \tilde{\mathbf{y}} \end{pmatrix}^T \underbrace{\begin{pmatrix} \boldsymbol{\Sigma}_x^{-1} + A^T\boldsymbol{\Sigma}_\varepsilon^{-1}A & -A^T\boldsymbol{\Sigma}_\varepsilon^{-1} \\ -\boldsymbol{\Sigma}_\varepsilon^{-1}A & \boldsymbol{\Sigma}_\varepsilon^{-1} \end{pmatrix}}_{\boldsymbol{\Lambda}} \begin{pmatrix} \tilde{\mathbf{x}} \\ \tilde{\mathbf{y}} \end{pmatrix}

$$

Reading off the blocks:

$$

\boldsymbol{\Lambda}_{11} = \boldsymbol{\Sigma}_x^{-1} + A^T\boldsymbol{\Sigma}_\varepsilon^{-1}A, \qquad \boldsymbol{\Lambda}_{12} = -A^T\boldsymbol{\Sigma}_\varepsilon^{-1}

$$

Therefore:

$$

\boldsymbol{\Sigma}_{x|y} = \boldsymbol{\Lambda}_{11}^{-1} = (\boldsymbol{\Sigma}_x^{-1} + A^T\boldsymbol{\Sigma}_\varepsilon^{-1}A)^{-1}

$$

$$

\boldsymbol{\mu}_{x|y} = \boldsymbol{\mu}_x - \boldsymbol{\Lambda}_{11}^{-1}\boldsymbol{\Lambda}_{12}\tilde{\mathbf{y}} = \boldsymbol{\Sigma}_{x|y}(\boldsymbol{\Sigma}_x^{-1}\boldsymbol{\mu}_x + A^T\boldsymbol{\Sigma}_\varepsilon^{-1}(\mathbf{y} - \mathbf{b}))

$$

---

## Python Implementation

```python
import numpy as np

def conditional_normal(mu, Sigma, idx1, idx2, x2_observed):
    """
    Compute conditional distribution of x[idx1] | x[idx2] = x2_observed.

    Parameters
    ----------
    mu : mean vector
    Sigma : covariance matrix
    idx1 : indices of variables to condition (output)
    idx2 : indices of observed variables
    x2_observed : observed values

    Returns
    -------
    mu_cond, Sigma_cond : conditional mean and covariance
    """
    mu1 = mu[idx1]
    mu2 = mu[idx2]
    S11 = Sigma[np.ix_(idx1, idx1)]
    S12 = Sigma[np.ix_(idx1, idx2)]
    S21 = Sigma[np.ix_(idx2, idx1)]
    S22 = Sigma[np.ix_(idx2, idx2)]

    S22_inv = np.linalg.inv(S22)
    mu_cond = mu1 + S12 @ S22_inv @ (x2_observed - mu2)
    Sigma_cond = S11 - S12 @ S22_inv @ S21
    return mu_cond, Sigma_cond


# Example: 3D multivariate normal
mu = np.array([1.0, 2.0, 3.0])
Sigma = np.array([
    [4.0, 2.0, 1.0],
    [2.0, 5.0, 3.0],
    [1.0, 3.0, 6.0]
])

# Condition on x2=3, x3=4
x2_obs = np.array([3.0, 4.0])
mu_cond, Sigma_cond = conditional_normal(mu, Sigma, [0], [1, 2], x2_obs)
print(f"X1 | X2=3, X3=4 ~ N({mu_cond[0]:.4f}, {Sigma_cond[0,0]:.4f})")

# Verify via precision matrix
Lambda = np.linalg.inv(Sigma)
print(f"\nPrecision matrix Λ:\n{Lambda}")
print(f"\nΛ11⁻¹ = {1/Lambda[0,0]:.4f}")
print(f"Σ_{'{1|2}'} = {Sigma_cond[0,0]:.4f}")


# Linear-Gaussian model example
print("\n=== Linear-Gaussian Model ===")
mu_x = np.array([0.0, 0.0])
Sigma_x = np.array([[1.0, 0.5], [0.5, 2.0]])
A = np.array([[1.0, 1.0]])
b = np.array([0.0])
Sigma_eps = np.array([[0.1]])

# Joint distribution
mu_joint = np.concatenate([mu_x, A @ mu_x + b])
Sigma_joint = np.block([
    [Sigma_x, Sigma_x @ A.T],
    [A @ Sigma_x, A @ Sigma_x @ A.T + Sigma_eps]
])
print(f"Joint mean: {mu_joint}")
print(f"Joint covariance:\n{Sigma_joint}")

# Posterior x|y
y_obs = np.array([2.0])
mu_post, Sigma_post = conditional_normal(
    mu_joint, Sigma_joint, [0, 1], [2], y_obs
)
print(f"\nPosterior mean: {mu_post}")
print(f"Posterior covariance:\n{Sigma_post}")

# Verify precision form
Sigma_x_inv = np.linalg.inv(Sigma_x)
Sigma_eps_inv = np.linalg.inv(Sigma_eps)
Sigma_post_inv = Sigma_x_inv + A.T @ Sigma_eps_inv @ A
Sigma_post_prec = np.linalg.inv(Sigma_post_inv)
mu_post_prec = Sigma_post_prec @ (Sigma_x_inv @ mu_x + A.T @ Sigma_eps_inv @ (y_obs - b))
print(f"\nPosterior mean (precision form): {mu_post_prec}")
print(f"Posterior cov (precision form):\n{Sigma_post_prec}")
```

---

## Key Takeaways

- The conditional distribution of a sub-vector of a multivariate normal is again multivariate normal, with closed-form expressions for the mean and covariance.
- The **covariance form** uses $\boldsymbol{\Sigma}_{12}\boldsymbol{\Sigma}_{22}^{-1}$; the **precision form** uses $\boldsymbol{\Lambda}_{11}^{-1}\boldsymbol{\Lambda}_{12}$. Both are equivalent.
- The conditional covariance $\boldsymbol{\Sigma}_{1|2} = \boldsymbol{\Lambda}_{11}^{-1}$ does not depend on the observed value — only the conditional mean shifts.
- The linear-Gaussian model leads to the Bayesian update: posterior precision = prior precision + data precision. This is the foundation of the Kalman filter.
