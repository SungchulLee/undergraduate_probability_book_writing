# Variance of a Sum (Independent Case)

## The Simplification

When random variables are independent, all covariance terms vanish, and the general formula collapses to a clean additive rule.

!!! info "Variance of a Sum of Independent Random Variables"
    If $X_1, X_2, \ldots, X_n$ are **independent**, then

    $$
    \text{Var}\!\left(\sum_{i=1}^n X_i\right) = \sum_{i=1}^n \text{Var}(X_i)
    $$

**Proof.** Independence implies $\text{Cov}(X_i, X_j) = 0$ for $i \neq j$. Substituting into the general formula:

$$
\text{Var}\!\left(\sum_{i=1}^n X_i\right) = \sum_{i=1}^n \text{Var}(X_i) + 2\sum_{i < j} \underbrace{\text{Cov}(X_i, X_j)}_{= 0} = \sum_{i=1}^n \text{Var}(X_i)
$$

$\blacksquare$

For a weighted sum of independent variables: $\text{Var}\!\left(\sum a_i X_i\right) = \sum a_i^2 \,\text{Var}(X_i)$.

---

## Applications to Standard Distributions

### Binomial Variance

If $S \sim \text{Binomial}(n, p)$, write $S = \sum_{i=1}^n X_i$ where $X_i \sim \text{Bernoulli}(p)$ are independent. Then:

$$
\text{Var}(S) = \sum_{i=1}^n \text{Var}(X_i) = n \cdot p(1-p) = npq
$$

### Negative Binomial Variance

If $S \sim \text{NB}(r, p)$, write $S = \sum_{i=1}^r X_i$ where $X_i \sim \text{Geo}(p)$ are independent. Then:

$$
\text{Var}(S) = r \cdot \frac{1-p}{p^2} = \frac{r(1-p)}{p^2}
$$

### Poisson Variance

If $X_i \sim \text{Poisson}(\lambda_i)$ are independent, then $\sum X_i \sim \text{Poisson}(\sum \lambda_i)$, and:

$$
\text{Var}\!\left(\sum_{i=1}^n X_i\right) = \sum_{i=1}^n \lambda_i
$$

---

## Variance of the Sample Mean

Let $X_1, \ldots, X_n$ be iid with variance $\sigma^2$. The sample mean $\bar{X}_n = \frac{1}{n}\sum X_i$ has:

$$
\text{Var}(\bar{X}_n) = \text{Var}\!\left(\frac{1}{n}\sum_{i=1}^n X_i\right) = \frac{1}{n^2}\sum_{i=1}^n \text{Var}(X_i) = \frac{n\sigma^2}{n^2} = \frac{\sigma^2}{n}
$$

!!! tip "The Square Root Law"
    The standard deviation of the sample mean is $\sigma/\sqrt{n}$. To halve the standard error, you need **four times** as many observations. This is the fundamental scaling law behind statistical estimation and the Law of Large Numbers.

---

## Summary Table

| Distribution | Decomposition | Variance |
|:---|:---|:---:|
| $\text{Binomial}(n,p)$ | $n$ iid $\text{Bernoulli}(p)$ | $npq$ |
| $\text{NB}(r,p)$ | $r$ iid $\text{Geo}(p)$ | $r(1-p)/p^2$ |
| $\text{Poisson}(\lambda_1 + \cdots + \lambda_n)$ | $n$ independent Poissons | $\sum \lambda_i$ |
| $\bar{X}_n$ (iid, var $\sigma^2$) | Average of $n$ iid | $\sigma^2/n$ |

---

## Example

??? example "Sum of Independent Dice"
    Roll $n = 10$ fair dice. Let $S = \sum_{i=1}^{10} X_i$ where each $X_i$ is a fair die roll.

    Each die has $\text{Var}(X_i) = 35/12$. By independence:

    $$
    \text{Var}(S) = 10 \cdot \frac{35}{12} = \frac{350}{12} \approx 29.17
    $$

    $$
    \text{SD}(S) = \sqrt{29.17} \approx 5.40
    $$

    Combined with $E[S] = 35$, we know the sum of 10 dice is approximately $35 \pm 5.4$.

---

## Python Verification

```python
import numpy as np

np.random.seed(42)
N = 500_000

# Binomial variance via iid Bernoullis
n, p = 20, 0.3
X = np.random.binomial(1, p, (N, n))
S = X.sum(axis=1)
print(f"Binomial({n},{p}): Var theory = {n*p*(1-p):.2f}, MC = {np.var(S):.2f}")

# Sample mean variance
sigma_sq = 4.0
n_obs = 50
samples = np.random.normal(0, np.sqrt(sigma_sq), (N, n_obs))
X_bar = samples.mean(axis=1)
print(f"\nVar(X_bar) theory = {sigma_sq/n_obs:.4f}, MC = {np.var(X_bar):.4f}")

# Sum of 10 dice
dice = np.random.randint(1, 7, (N, 10))
S_dice = dice.sum(axis=1)
print(f"\nVar(10 dice) theory = {10*35/12:.2f}, MC = {np.var(S_dice):.2f}")
```
