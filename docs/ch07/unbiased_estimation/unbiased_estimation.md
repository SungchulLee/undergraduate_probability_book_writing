# Unbiased Estimation of Mean and Variance

## Definitions

### Population Parameter

A **population parameter** $\theta$ is a numerical characteristic of the distribution (e.g., mean $\mu$, variance $\sigma^2$).

### Statistic

A **statistic** is any function $f(X_1, X_2, \ldots, X_n)$ of the observed samples.

### Estimator

An **estimator** of $\theta$ is a statistic $f(X_1, X_2, \ldots, X_n)$ used to estimate the population parameter $\theta$.

### Unbiased Estimator

An estimator $f(X_1, X_2, \ldots, X_n)$ of $\theta$ is **unbiased** if

$$
E[f(X_1, X_2, \ldots, X_n)] = \theta
$$

That is, on average, the estimator gives the correct value.

---

## Unbiased Estimator of the Mean

Let $X_1, X_2, \ldots, X_n$ be iid samples from a distribution with unknown mean $\mu$ and variance $\sigma^2$.

The **sample mean** is

$$
\bar{X} = \frac{\sum_{i=1}^n X_i}{n}
$$

**Unbiasedness**: By linearity of expectation,

$$
E[\bar{X}] = \frac{\sum_{i=1}^n E[X_i]}{n} = \frac{n\mu}{n} = \mu \quad \checkmark
$$

**Variance of the sample mean**:

$$
\text{Var}(\bar{X}) = \frac{1}{n^2} \text{Var}\left(\sum_{i=1}^n X_i\right) = \frac{1}{n^2} \sum_{i=1}^n \text{Var}(X_i) = \frac{\sigma^2}{n}
$$

!!! note "Standard Error"
    $\text{SE}(\bar{X}) = \text{SD}(\bar{X}) = \frac{\sigma}{\sqrt{n}}$ is called the **standard error** of the mean. It decreases as $n$ increases, meaning more data gives a more precise estimate.

---

## Unbiased Estimator of the Variance

The **sample variance** is

$$
S^2 = \frac{\sum_{i=1}^n (X_i - \bar{X})^2}{n - 1}
$$

**Unbiasedness**: We need to show $E[S^2] = \sigma^2$.

### Proof

**Step 1**: Expand $(X_i - \bar{X})^2$:

$$
(X_i - \bar{X})^2 = \left[(X_i - \mu) - (\bar{X} - \mu)\right]^2 = (X_i - \mu)^2 + (\bar{X} - \mu)^2 - 2(X_i - \mu)(\bar{X} - \mu)
$$

**Step 2**: Take expectations:

$$
E[(X_i - \bar{X})^2] = \sigma^2 + \frac{\sigma^2}{n} - 2E[(X_i - \mu)(\bar{X} - \mu)]
$$

**Step 3**: Compute $E[(X_i - \mu)(\bar{X} - \mu)]$:

$$
E[(X_i - \mu)(\bar{X} - \mu)] = E\left[(X_i - \mu) \cdot \frac{\sum_{j=1}^n (X_j - \mu)}{n}\right]
$$

$$
= E\left[(X_i - \mu) \cdot \frac{\sum_{j \neq i}(X_j - \mu)}{n} + \frac{(X_i - \mu)}{n}\right]
$$

Since $X_i$ and $X_j$ are independent for $j \neq i$, $E[(X_i - \mu)(X_j - \mu)] = 0$. Therefore:

$$
E[(X_i - \mu)(\bar{X} - \mu)] = \frac{1}{n}E[(X_i - \mu)^2] = \frac{\sigma^2}{n}
$$

**Step 4**: Combine:

$$
E[(X_i - \bar{X})^2] = \sigma^2 + \frac{\sigma^2}{n} - \frac{2\sigma^2}{n} = \sigma^2 \cdot \frac{n-1}{n}
$$

**Step 5**: Sum and divide:

$$
E[S^2] = \frac{\sum_{i=1}^n E[(X_i - \bar{X})^2]}{n-1} = \frac{n \cdot \frac{n-1}{n}\sigma^2}{n-1} = \sigma^2 \quad \checkmark
$$

---

## Why Divide by n - 1?

If we divided by $n$ instead, we would get

$$
E\left[\frac{\sum(X_i - \bar{X})^2}{n}\right] = \frac{n-1}{n}\sigma^2 < \sigma^2
$$

This is a **biased** estimator that systematically underestimates $\sigma^2$. Dividing by $n-1$ corrects for this bias.

The correction factor $n-1$ represents the **degrees of freedom**: we lose one degree of freedom because we estimated $\mu$ by $\bar{X}$.

---

## Summary

| Quantity | Estimator | Unbiased? | Variance of Estimator |
|:---:|:---:|:---:|:---:|
| $\mu$ | $\bar{X} = \frac{1}{n}\sum X_i$ | Yes | $\sigma^2/n$ |
| $\sigma^2$ | $S^2 = \frac{1}{n-1}\sum(X_i - \bar{X})^2$ | Yes | — |
| $\sigma^2$ | $\frac{1}{n}\sum(X_i - \bar{X})^2$ | No (biased low) | — |

---

## Python Implementation

```python
import numpy as np

np.random.seed(42)

# True parameters
mu_true = 5.0
sigma_true = 2.0

# Simulate many datasets to verify unbiasedness
N_datasets = 100_000
n = 10  # sample size per dataset

sample_means = []
sample_vars_unbiased = []
sample_vars_biased = []

for _ in range(N_datasets):
    X = np.random.normal(mu_true, sigma_true, n)
    sample_means.append(np.mean(X))
    sample_vars_unbiased.append(np.var(X, ddof=1))  # divides by n-1
    sample_vars_biased.append(np.var(X, ddof=0))    # divides by n

sample_means = np.array(sample_means)
sample_vars_unbiased = np.array(sample_vars_unbiased)
sample_vars_biased = np.array(sample_vars_biased)

print(f"True μ = {mu_true}")
print(f"E[X̄] = {np.mean(sample_means):.4f}  (should be {mu_true})")
print(f"Var(X̄) = {np.var(sample_means):.4f}  (should be {sigma_true**2/n:.4f})")
print()
print(f"True σ² = {sigma_true**2}")
print(f"E[S² (n-1)] = {np.mean(sample_vars_unbiased):.4f}  (unbiased)")
print(f"E[S² (n)]   = {np.mean(sample_vars_biased):.4f}  (biased, should be {(n-1)/n * sigma_true**2:.4f})")
```
