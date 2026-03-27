# Variance-Covariance Matrix

## Motivation

When working with a random vector $\mathbf{X} = (X_1, X_2, \ldots, X_n)^T$, we need a compact way to encode all variances and pairwise covariances. The **variance-covariance matrix** (or simply **covariance matrix**) organizes this information into a single matrix, enabling elegant formulas for the variance of linear combinations.

---

## Definition

!!! info "Covariance Matrix"
    For a random vector $\mathbf{X} = (X_1, \ldots, X_n)^T$ with mean vector $\boldsymbol{\mu} = E[\mathbf{X}]$, the **covariance matrix** is the $n \times n$ matrix

    $$
    \boldsymbol{\Sigma} = \text{Cov}(\mathbf{X}) = E\bigl[(\mathbf{X} - \boldsymbol{\mu})(\mathbf{X} - \boldsymbol{\mu})^T\bigr]
    $$

    with entries $\Sigma_{ij} = \text{Cov}(X_i, X_j)$.

Written out:

$$
\boldsymbol{\Sigma} = \begin{pmatrix} \text{Var}(X_1) & \text{Cov}(X_1, X_2) & \cdots & \text{Cov}(X_1, X_n) \\ \text{Cov}(X_2, X_1) & \text{Var}(X_2) & \cdots & \text{Cov}(X_2, X_n) \\ \vdots & \vdots & \ddots & \vdots \\ \text{Cov}(X_n, X_1) & \text{Cov}(X_n, X_2) & \cdots & \text{Var}(X_n) \end{pmatrix}
$$

The diagonal entries are variances, and the off-diagonal entries are covariances.

---

## Properties

1. **Symmetric**: $\boldsymbol{\Sigma} = \boldsymbol{\Sigma}^T$, since $\text{Cov}(X_i, X_j) = \text{Cov}(X_j, X_i)$

2. **Positive semi-definite**: For any vector $\mathbf{a} \in \mathbb{R}^n$:

$$
\mathbf{a}^T \boldsymbol{\Sigma}\, \mathbf{a} = \text{Var}\!\left(\sum_{i=1}^n a_i X_i\right) \geq 0
$$

This holds because variance is always non-negative.

3. **Diagonal entries are non-negative**: $\Sigma_{ii} = \text{Var}(X_i) \geq 0$

4. **Independent components**: If $X_1, \ldots, X_n$ are independent, then $\boldsymbol{\Sigma}$ is diagonal

---

## Variance of a Linear Combination (Matrix Form)

The general formula $\text{Var}(\sum a_i X_i) = \sum_i \sum_j a_i a_j \text{Cov}(X_i, X_j)$ can be written compactly as:

$$
\text{Var}(\mathbf{a}^T \mathbf{X}) = \mathbf{a}^T \boldsymbol{\Sigma}\, \mathbf{a}
$$

This is a **quadratic form** in the weights $\mathbf{a}$.

---

## Bivariate Example

??? example "Covariance Matrix for Two Variables"
    Let $X$ and $Y$ have $\text{Var}(X) = 4$, $\text{Var}(Y) = 9$, and $\text{Cov}(X, Y) = -3$. Then:

    $$
    \boldsymbol{\Sigma} = \begin{pmatrix} 4 & -3 \\ -3 & 9 \end{pmatrix}
    $$

    For $\mathbf{a} = (2, 1)^T$:

    $$
    \text{Var}(2X + Y) = \begin{pmatrix} 2 & 1 \end{pmatrix} \begin{pmatrix} 4 & -3 \\ -3 & 9 \end{pmatrix} \begin{pmatrix} 2 \\ 1 \end{pmatrix} = \begin{pmatrix} 2 & 1 \end{pmatrix} \begin{pmatrix} 5 \\ 3 \end{pmatrix} = 13
    $$

    Check: $4(4) + 1(9) + 2(2)(1)(-3) = 16 + 9 - 12 = 13$. Consistent.

---

## Correlation Matrix

The **correlation matrix** $\mathbf{R}$ is the standardized version of $\boldsymbol{\Sigma}$:

$$
R_{ij} = \frac{\Sigma_{ij}}{\sqrt{\Sigma_{ii}\,\Sigma_{jj}}} = \rho(X_i, X_j)
$$

In matrix notation, if $\mathbf{D} = \text{diag}(\sigma_1, \ldots, \sigma_n)$, then:

$$
\mathbf{R} = \mathbf{D}^{-1} \boldsymbol{\Sigma}\, \mathbf{D}^{-1}
$$

The correlation matrix has ones on the diagonal and correlations off the diagonal.

---

## Linear Transformations

If $\mathbf{Y} = \mathbf{A}\mathbf{X} + \mathbf{b}$ for a matrix $\mathbf{A}$ and vector $\mathbf{b}$, then:

$$
\text{Cov}(\mathbf{Y}) = \mathbf{A}\,\boldsymbol{\Sigma}\,\mathbf{A}^T
$$

This generalizes the scalar rule $\text{Var}(aX + b) = a^2\text{Var}(X)$.

---

## Python Example

```python
import numpy as np

# Define covariance matrix
Sigma = np.array([[4, -3],
                  [-3, 9]])

# Check positive semi-definiteness
eigenvalues = np.linalg.eigvalsh(Sigma)
print(f"Eigenvalues: {eigenvalues}")  # both non-negative
print(f"Positive semi-definite: {all(eigenvalues >= 0)}")

# Variance of 2X + Y
a = np.array([2, 1])
var_linear = a @ Sigma @ a
print(f"Var(2X + Y) = {var_linear}")  # 13

# Correlation matrix
D_inv = np.diag(1 / np.sqrt(np.diag(Sigma)))
R = D_inv @ Sigma @ D_inv
print(f"Correlation matrix:\n{R}")
```
