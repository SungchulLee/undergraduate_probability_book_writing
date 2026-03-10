# Unbiased Estimation

An estimator is unbiased if its expectation equals the parameter being estimated. The sample mean $\bar{X}$ is unbiased for $\mu$; the sample variance with $n-1$ divisor is unbiased for $\sigma^2$.

## Definition

An estimator $\hat\theta = f(X_1, \ldots, X_n)$ is **unbiased** for $\theta$ if $E[\hat\theta] = \theta$.

**Sample mean:** $\bar{X} = \frac{1}{n}\sum_{i=1}^n X_i$ is unbiased for $\mu$.

**Sample variance:** $S^2 = \frac{1}{n-1}\sum_{i=1}^n(X_i - \bar{X})^2$ is unbiased for $\sigma^2$.

## Explanation

### Sample Mean

$E[\bar{X}] = \mu$ by linearity. Its variance is $\text{Var}(\bar{X}) = \sigma^2/n$, so the **standard error** is $\sigma/\sqrt{n}$.

### Why $n-1$ in Sample Variance

Using $n$ in the denominator gives $E[\frac{1}{n}\sum(X_i - \bar{X})^2] = \frac{n-1}{n}\sigma^2 < \sigma^2$ — systematically underestimates $\sigma^2$. The $n-1$ correction (called **Bessel's correction**) accounts for the lost degree of freedom from estimating $\mu$ by $\bar{X}$.

### Proof Sketch

$E[(X_i - \bar{X})^2] = \sigma^2 - \sigma^2/n = \sigma^2(n-1)/n$. Summing: $E[\sum(X_i - \bar{X})^2] = (n-1)\sigma^2$. Dividing by $n-1$ gives $\sigma^2$.

## Examples

**Example.** 10 iid samples from $N(5, 4)$. $\bar{X}$ targets $\mu = 5$ with SE $= 2/\sqrt{10} \approx 0.632$. $S^2$ targets $\sigma^2 = 4$.

```python
import numpy as np

np.random.seed(42)
mu, sigma = 5, 2
n = 10
N_datasets = 100_000

means = []
vars_n1 = []
vars_n = []
for _ in range(N_datasets):
    X = np.random.normal(mu, sigma, n)
    means.append(X.mean())
    vars_n1.append(X.var(ddof=1))
    vars_n.append(X.var(ddof=0))

print(f"E[X_bar] = {np.mean(means):.4f} (target: {mu})")
print(f"SE(X_bar) = {np.std(means):.4f} (theory: {sigma/np.sqrt(n):.4f})")
print(f"E[S^2, n-1] = {np.mean(vars_n1):.4f} (target: {sigma**2})")
print(f"E[S^2, n] = {np.mean(vars_n):.4f} (biased: {(n-1)/n*sigma**2:.4f})")
```
