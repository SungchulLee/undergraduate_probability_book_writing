# Linearity of Expectation for Sums

## Recap

In Chapter 7 we established the most powerful tool in probability: **linearity of expectation**. This section focuses on its application to sums of random variables, setting the stage for the variance formulas that follow.

!!! info "Linearity of Expectation"
    For **any** random variables $X_1, X_2, \ldots, X_n$ (not necessarily independent) and constants $a_1, \ldots, a_n$:

    $$
    E\left[\sum_{i=1}^n a_i X_i\right] = \sum_{i=1}^n a_i\,E[X_i]
    $$

The key word is **any**: no assumption on the joint distribution is needed.

---

## The Sample Mean

Let $X_1, \ldots, X_n$ be random variables (not necessarily iid) with a common mean $\mu = E[X_i]$. The sample mean is

$$
\bar{X}_n = \frac{1}{n}\sum_{i=1}^n X_i
$$

By linearity:

$$
E[\bar{X}_n] = \frac{1}{n}\sum_{i=1}^n E[X_i] = \frac{1}{n}(n\mu) = \mu
$$

The sample mean is an **unbiased** estimator of the population mean, regardless of dependence.

---

## Examples

### Symmetric Random Walk

Let $S_n = X_1 + X_2 + \cdots + X_n$ where each $X_i$ equals $+1$ or $-1$ with equal probability. The steps may be dependent (e.g., correlated increments). Regardless:

$$
E[S_n] = \sum_{i=1}^n E[X_i] = n \cdot 0 = 0
$$

### Weighted Portfolio Return

A portfolio has weights $w_1, \ldots, w_n$ with $\sum w_i = 1$. If asset $i$ has expected return $\mu_i$, then the portfolio's expected return is:

$$
E[R_p] = E\left[\sum_{i=1}^n w_i R_i\right] = \sum_{i=1}^n w_i \mu_i
$$

This holds whether the asset returns are correlated or not.

### Number of Fixed Points (Derangements Revisited)

A random permutation of $\{1, 2, \ldots, n\}$ is chosen uniformly. Let $D$ be the number of fixed points. Writing $D = \sum_{i=1}^n \mathbf{1}_{X_i = i}$, by linearity:

$$
E[D] = \sum_{i=1}^n P(X_i = i) = n \cdot \frac{1}{n} = 1
$$

The indicators are dependent (knowing one element is fixed affects others), but linearity applies without issue.

---

## What Linearity Does Not Give

!!! warning "Variance Is Not Linear"
    While $E\!\left[\sum X_i\right] = \sum E[X_i]$ always holds, in general:

    $$
    \text{Var}\!\left(\sum_{i=1}^n X_i\right) \neq \sum_{i=1}^n \text{Var}(X_i)
    $$

    The correct formula involves covariance terms (Section 9.3). This is precisely why covariance is so important: it captures the extra terms that arise in the variance of a sum.

---

## Python Verification

```python
import numpy as np

np.random.seed(42)
N = 500_000

# Random walk with n=100 steps (even with correlated steps)
n = 100
E_walk = 0  # each step has mean 0

# Monte Carlo: iid steps
walks = np.cumsum(np.random.choice([-1, 1], size=(N, n)), axis=1)
mc_mean = np.mean(walks[:, -1])
print(f"E[S_{n}] theory = {E_walk}")
print(f"E[S_{n}] Monte Carlo = {mc_mean:.4f}")

# Fixed points in random permutation
fixed_points = []
for _ in range(N):
    perm = np.random.permutation(n)
    fixed = np.sum(perm == np.arange(n))
    fixed_points.append(fixed)
print(f"\nE[fixed points] theory = 1")
print(f"E[fixed points] MC = {np.mean(fixed_points):.4f}")
```
