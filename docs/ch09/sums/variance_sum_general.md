# Variance of a Sum (General Formula)

## Motivation

We know that $E[X + Y] = E[X] + E[Y]$ always. Does variance behave the same way? In general, **no**. The variance of a sum depends not only on the individual variances but also on how the variables co-vary.

---

## Two-Variable Case

!!! info "Variance of a Sum of Two Random Variables"
    For any random variables $X$ and $Y$:

    $$
    \text{Var}(X + Y) = \text{Var}(X) + \text{Var}(Y) + 2\,\text{Cov}(X, Y)
    $$

**Derivation.** Let $\mu_X = E[X]$ and $\mu_Y = E[Y]$.

$$
\text{Var}(X + Y) = E\bigl[(X + Y - \mu_X - \mu_Y)^2\bigr]
$$

$$
= E\bigl[((X - \mu_X) + (Y - \mu_Y))^2\bigr]
$$

$$
= E[(X - \mu_X)^2] + 2\,E[(X - \mu_X)(Y - \mu_Y)] + E[(Y - \mu_Y)^2]
$$

$$
= \text{Var}(X) + 2\,\text{Cov}(X, Y) + \text{Var}(Y)
$$

$\blacksquare$

For a **difference**: $\text{Var}(X - Y) = \text{Var}(X) + \text{Var}(Y) - 2\,\text{Cov}(X, Y)$.

---

## General Formula for n Variables

!!! info "Variance of a General Sum"
    For random variables $X_1, X_2, \ldots, X_n$:

    $$
    \text{Var}\!\left(\sum_{i=1}^n X_i\right) = \sum_{i=1}^n \text{Var}(X_i) + 2\sum_{1 \leq i < j \leq n} \text{Cov}(X_i, X_j)
    $$

Equivalently, using the double sum:

$$
\text{Var}\!\left(\sum_{i=1}^n X_i\right) = \sum_{i=1}^n \sum_{j=1}^n \text{Cov}(X_i, X_j)
$$

where the diagonal terms give $\text{Cov}(X_i, X_i) = \text{Var}(X_i)$ and the off-diagonal terms contribute the cross-covariances.

**Derivation.** Using bilinearity of covariance:

$$
\text{Var}\!\left(\sum_{i=1}^n X_i\right) = \text{Cov}\!\left(\sum_{i=1}^n X_i,\; \sum_{j=1}^n X_j\right) = \sum_{i=1}^n \sum_{j=1}^n \text{Cov}(X_i, X_j)
$$

Separating diagonal and off-diagonal:

$$
= \sum_{i=1}^n \text{Var}(X_i) + \sum_{\substack{i,j=1 \\ i \neq j}}^n \text{Cov}(X_i, X_j) = \sum_{i=1}^n \text{Var}(X_i) + 2\sum_{1 \leq i < j \leq n} \text{Cov}(X_i, X_j)
$$

$\blacksquare$

---

## Counting the Terms

For $n$ variables, the formula has:

- $n$ variance terms (diagonal)
- $\binom{n}{2} = \frac{n(n-1)}{2}$ distinct covariance terms (each counted once)

As $n$ grows, the number of covariance terms grows as $O(n^2)$, which can dominate. This is why correlations between variables are often more important than individual variances in applications.

---

## Weighted Sum

For constants $a_1, \ldots, a_n$:

$$
\text{Var}\!\left(\sum_{i=1}^n a_i X_i\right) = \sum_{i=1}^n a_i^2\,\text{Var}(X_i) + 2\sum_{1 \leq i < j \leq n} a_i a_j\,\text{Cov}(X_i, X_j)
$$

---

## Example

??? example "Variance of a Sum with Known Covariance"
    Let $X_1, X_2, X_3$ have $\text{Var}(X_i) = 4$ for all $i$, and suppose every pair has $\text{Cov}(X_i, X_j) = 1$ for $i \neq j$. Then:

    $$
    \text{Var}(X_1 + X_2 + X_3) = 3(4) + 2 \cdot 3(1) = 12 + 6 = 18
    $$

    Compare with naive addition of variances: $3(4) = 12$. The positive covariance increases the variance of the sum by 50%.

??? example "Negative Covariance Reduces Variance"
    If instead $\text{Cov}(X_i, X_j) = -1$ for all $i \neq j$ (with the same variances):

    $$
    \text{Var}(X_1 + X_2 + X_3) = 12 + 2(3)(-1) = 12 - 6 = 6
    $$

    Negative covariance leads to partial cancellation, reducing the overall variability. This is the principle behind **diversification** in portfolio theory.

---

## Python Verification

```python
import numpy as np

np.random.seed(42)
N = 500_000

# Three correlated normals with Var=4, Cov=1
mu = [0, 0, 0]
Sigma = [[4, 1, 1],
         [1, 4, 1],
         [1, 1, 4]]
samples = np.random.multivariate_normal(mu, Sigma, N)
S = samples.sum(axis=1)

print(f"Var(X1+X2+X3) theory = 18")
print(f"Var(X1+X2+X3) MC = {np.var(S):.2f}")

# Negative covariance case
Sigma_neg = [[4, -1, -1],
             [-1, 4, -1],
             [-1, -1, 4]]
samples_neg = np.random.multivariate_normal(mu, Sigma_neg, N)
S_neg = samples_neg.sum(axis=1)

print(f"\nVar (neg cov) theory = 6")
print(f"Var (neg cov) MC = {np.var(S_neg):.2f}")
```
