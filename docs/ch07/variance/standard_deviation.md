# Standard Deviation


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

## Definition

The **standard deviation** of a random variable $X$ is

$$
\text{SD}(X) = \sigma_X = \sqrt{\text{Var}(X)}
$$

Standard deviation has the same units as $X$, making it more interpretable than variance (which has squared units).

---

## Interpretation

The standard deviation measures the "typical" distance of $X$ from its mean. By Chebyshev's inequality, at least $1 - 1/k^2$ of the probability lies within $k$ standard deviations of the mean:

$$
P(|X - \mu| \geq k\sigma) \leq \frac{1}{k^2}
$$

For the normal distribution, the probabilities are much tighter:

| Range | Probability |
|:---:|:---:|
| $\mu \pm 1\sigma$ | $\approx 68.3\%$ |
| $\mu \pm 2\sigma$ | $\approx 95.4\%$ |
| $\mu \pm 3\sigma$ | $\approx 99.7\%$ |

---

## Common Standard Deviations

| Distribution | $\text{SD}(X)$ |
|:---:|:---:|
| $\text{Bernoulli}(p)$ | $\sqrt{pq}$ |
| $\text{Binomial}(n,p)$ | $\sqrt{npq}$ |
| $\text{Poisson}(\lambda)$ | $\sqrt{\lambda}$ |
| $\text{Geometric}(p)$ | $\sqrt{q}/p$ |
| $\text{Uniform}(a,b)$ | $(b-a)/\sqrt{12}$ |
| $\text{Exponential}(\lambda)$ | $1/\lambda$ |
| $N(\mu, \sigma^2)$ | $\sigma$ |

---

## Python Implementation

```python
import numpy as np

# Standard deviations of common distributions
p = 0.3
n = 100
lam = 5.0

print(f"SD(Bernoulli({p})) = {np.sqrt(p*(1-p)):.4f}")
print(f"SD(Binomial({n},{p})) = {np.sqrt(n*p*(1-p)):.4f}")
print(f"SD(Poisson({lam})) = {np.sqrt(lam):.4f}")
print(f"SD(Geo({p})) = {np.sqrt(1-p)/p:.4f}")
print(f"SD(Uniform(0,1)) = {1/np.sqrt(12):.4f}")
print(f"SD(Exp({lam})) = {1/lam:.4f}")
```
