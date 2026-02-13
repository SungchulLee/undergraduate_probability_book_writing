# Distribution of Sample Variance

## The Three Key Results

For $X_1, \ldots, X_n$ iid from $N(\mu, \sigma^2)$, with $\bar{X} = \frac{\sum X_i}{n}$ and $S^2 = \frac{\sum(X_i - \bar{X})^2}{n-1}$:

1. **$\bar{X}$ and $S^2$ are independent**
2. $\frac{\bar{X} - \mu}{\sigma/\sqrt{n}} \sim N(0, 1)$ and $\frac{(n-1)S^2}{\sigma^2} = \sum_{i=1}^n \left(\frac{X_i - \bar{X}}{\sigma}\right)^2 \sim \chi^2_{n-1}$
3. $\frac{\bar{X} - \mu}{S/\sqrt{n}} = \frac{N(0,1)}{\sqrt{\chi^2_{n-1}/(n-1)}} \sim t_{n-1}$

## Key Fact: $\text{Cov}(\bar{X}, X_i - \bar{X}) = 0$

$$\text{Cov}(\bar{X}, X_i - \bar{X}) = \text{Cov}(\bar{X}, X_i) - \text{Cov}(\bar{X}, \bar{X})$$

$$= \text{Cov}\!\left(\frac{\sum_{j=1}^n X_j}{n}, X_i\right) - \text{Cov}\!\left(\frac{\sum_{j=1}^n X_j}{n}, \frac{\sum_{k=1}^n X_k}{n}\right)$$

$$= \frac{1}{n} \cdot \sigma^2 - \frac{1}{n^2} \cdot n\sigma^2 = 0$$

## Consequence: Independence of $\bar{X}$ and $S^2$

### Step 1: Multivariate Normality

The vector $(\bar{X}, X_1 - \bar{X}, X_2 - \bar{X}, \ldots, X_n - \bar{X})$ is a linear transformation of the multivariate normal vector $(X_1, \ldots, X_n)$, so it is itself multivariate normal.

### Step 2: Zero Covariance Implies Independence

For multivariate normal random variables, if the covariance matrix $\Sigma$ has $\Sigma_{ij} = 0$ for all $j \neq i$, then $X_i$ is independent of $(X_j)_{j \neq i}$.

Since $\text{Cov}(\bar{X}, X_i - \bar{X}) = 0$ for all $i$, we conclude:

$$\bar{X} \text{ is independent of } (X_1 - \bar{X}, \ldots, X_n - \bar{X})$$

Since $S^2$ is a function of $(X_1 - \bar{X}, \ldots, X_n - \bar{X})$, it follows that **$\bar{X}$ and $S^2$ are independent**.

## Proof: $\sum\left(\frac{X_i - \bar{X}}{\sigma}\right)^2 \sim \chi^2_{n-1}$

### Step 1: Decomposition Identity

$$\sum_{i=1}^n (X_i - \mu)^2 = \sum_{i=1}^n \big((X_i - \bar{X}) + (\bar{X} - \mu)\big)^2$$

Expanding:

$$= \sum_{i=1}^n (X_i - \bar{X})^2 + n(\bar{X} - \mu)^2 + 2(\bar{X} - \mu) \underbrace{\sum_{i=1}^n (X_i - \bar{X})}_{= \, 0}$$

Therefore:

$$\sum_{i=1}^n (X_i - \mu)^2 = \sum_{i=1}^n (X_i - \bar{X})^2 + n(\bar{X} - \mu)^2$$

### Step 2: Divide by $\sigma^2$

$$\underbrace{\sum_{i=1}^n \left(\frac{X_i - \mu}{\sigma}\right)^2}_{\chi^2_n} = \sum_{i=1}^n \left(\frac{X_i - \bar{X}}{\sigma}\right)^2 + \underbrace{\left(\frac{\bar{X} - \mu}{\sigma/\sqrt{n}}\right)^2}_{\chi^2_1}$$

### Step 3: MGF Argument

Taking MGFs of both sides and using the independence of $\bar{X}$ and $(X_1 - \bar{X}, \ldots, X_n - \bar{X})$:

$$(1 - 2t)^{-n/2} = \varphi_{\sum\left(\frac{X_i - \bar{X}}{\sigma}\right)^2}(t) \cdot (1 - 2t)^{-1/2}$$

Solving:

$$\varphi_{\sum\left(\frac{X_i - \bar{X}}{\sigma}\right)^2}(t) = (1 - 2t)^{-(n-1)/2}$$

This is the MGF of $\chi^2_{n-1}$. By the uniqueness theorem:

$$\sum_{i=1}^n \left(\frac{X_i - \bar{X}}{\sigma}\right)^2 \sim \chi^2_{n-1}$$

Or equivalently:

$$\frac{(n-1)S^2}{\sigma^2} \sim \chi^2_{n-1}$$

!!! info "Why $n-1$ Degrees of Freedom?"
    The $n$ residuals $X_1 - \bar{X}, \ldots, X_n - \bar{X}$ satisfy one linear constraint: $\sum(X_i - \bar{X}) = 0$. This reduces the effective number of independent squared terms from $n$ to $n-1$.

## Python Verification

```python
import numpy as np
from scipy import stats

np.random.seed(42)
mu, sigma, n = 5, 3, 10
n_sim = 100_000

chi2_samples = []
for _ in range(n_sim):
    x = np.random.normal(mu, sigma, n)
    s2 = np.var(x, ddof=1)
    chi2_samples.append((n - 1) * s2 / sigma**2)

chi2_samples = np.array(chi2_samples)
print(f"Simulated mean: {chi2_samples.mean():.3f}  (theory: {n-1})")
print(f"Simulated var:  {chi2_samples.var():.3f}  (theory: {2*(n-1)})")

# KS test against chi2(n-1)
stat, pval = stats.kstest(chi2_samples, 'chi2', args=(n-1,))
print(f"KS test p-value: {pval:.4f}")
```

**Output:**
```
Simulated mean: 9.003  (theory: 9)
Simulated var:  18.050  (theory: 18)
KS test p-value: 0.4521
```
