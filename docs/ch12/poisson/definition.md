# Poisson Distribution: Definition and Properties

## Definition

A random variable $X$ has a **Poisson distribution** with parameter $\lambda > 0$, written $X \sim \text{Po}(\lambda)$, if its probability mass function (PMF) is

$$

P(X = k) = \frac{e^{-\lambda} \lambda^k}{k!}, \quad k = 0, 1, 2, \ldots

$$

The parameter $\lambda$ represents both the **mean** and the **variance** of the distribution.

---

## Verifying the PMF Sums to 1

To confirm this is a valid probability distribution, we check that the PMF sums to 1:

$$

\sum_{k=0}^{\infty} \frac{e^{-\lambda} \lambda^k}{k!} = e^{-\lambda} \sum_{k=0}^{\infty} \frac{\lambda^k}{k!} = e^{-\lambda} \cdot e^{\lambda} = 1

$$

This uses the Taylor series expansion $e^{\lambda} = \sum_{k=0}^{\infty} \frac{\lambda^k}{k!}$.

---

## Intuition: Where the Poisson Comes From

The Poisson distribution arises naturally as an approximation to the Binomial distribution $B(n, p)$ when $n$ is large, $p$ is small, and $\lambda = np$ is held fixed.

| Distribution | Random Variable |
|:---|:---|
| $B(p)$ | Flip a $p$-coin and check whether we have a head |
| $B(n, p)$ | Flip a $p$-coin $n$ times and count the number of heads |
| $\text{Po}(\lambda) \approx B(n, p)$ | Flip a $p$-coin $n$ times and count the number of heads, where $np = \lambda$ is fixed and $n \to \infty$ |
| $\text{Geo}(p)$ | Flip a $p$-coin until first head and count the number of flips |
| $\text{NB}(r, p)$ | Flip a $p$-coin until $r$-th head and count the number of flips |

The Poisson distribution can be thought of as counting the number of "rare events" that occur in a fixed period of time or region of space, where each individual event has a very small probability of occurring at any given instant, but there are many opportunities for it to happen.

---

## Summary of Discrete Distribution Parameters

| Distribution | Expectation | Variance |
|:---|:---:|:---:|
| $B(p)$ | $p$ | $pq$ |
| $B(n, p)$ | $np$ | $npq$ |
| $\text{Po}(\lambda) \approx B(n, p)$ | $\lambda$ | $\lambda$ |
| $\text{Geo}(p)$ | $\frac{1}{p}$ | $\frac{q}{p^2}$ |
| $\text{NB}(r, p)$ | $\frac{r}{p}$ | $\frac{rq}{p^2}$ |

A distinctive feature of the Poisson distribution is that its mean equals its variance ($\lambda = \lambda$). This property is often used as a diagnostic: if data has mean approximately equal to variance, a Poisson model may be appropriate.

---

## PMF and CDF Visualization

The PMF of $\text{Po}(\lambda)$ is a discrete distribution concentrated on the non-negative integers. As $\lambda$ increases, the distribution shifts to the right and becomes more spread out (and more symmetric, approaching a Normal shape by the CLT).

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson

la = 10
m = 30
x = np.arange(0, m + 1)

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# PMF
pmf_vals = poisson.pmf(x, la)
axes[0].bar(x, pmf_vals, color='steelblue', alpha=0.7, edgecolor='black')
axes[0].set_title(f'PMF of Po({la})')
axes[0].set_xlabel('k')
axes[0].set_ylabel('P(X = k)')
axes[0].set_xlim(-0.5, m + 0.5)
axes[0].grid(True, alpha=0.3)

# CDF
cdf_vals = poisson.cdf(x, la)
axes[1].step(x, cdf_vals, where='mid', color='steelblue', linewidth=2)
axes[1].set_title(f'CDF of Po({la})')
axes[1].set_xlabel('k')
axes[1].set_ylabel('P(X ≤ k)')
axes[1].set_xlim(-0.5, m + 0.5)
axes[1].set_ylim(0, 1.05)
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('poisson_pmf_cdf.png', dpi=150, bbox_inches='tight')
plt.show()
```

---

## Key Properties

1. **Support**: $X$ takes values in $\{0, 1, 2, \ldots\}$ (the non-negative integers).

2. **Mode**: The mode of $\text{Po}(\lambda)$ is $\lfloor \lambda \rfloor$ when $\lambda$ is not an integer, and both $\lambda - 1$ and $\lambda$ when $\lambda$ is a positive integer.

3. **Ratio of successive probabilities**: For $k \geq 1$,

   $$

   \frac{P(X = k)}{P(X = k-1)} = \frac{\lambda}{k}

   $$

   This means probabilities increase when $k < \lambda$ and decrease when $k > \lambda$.

4. **Tail behavior**: The Poisson PMF decreases super-exponentially for large $k$ (faster than any geometric distribution), since $k!$ grows faster than any exponential.

5. **Mean equals variance**: $E[X] = \text{Var}(X) = \lambda$. This is a unique fingerprint of the Poisson among common distributions.

---

## Computing Poisson Probabilities in Python

```python
from scipy.stats import poisson

la = 10

# Individual probabilities
print(f"P(X = 5) = {poisson.pmf(5, la):.6f}")
print(f"P(X = 10) = {poisson.pmf(10, la):.6f}")

# Cumulative probabilities
print(f"P(X <= 8) = {poisson.cdf(8, la):.6f}")
print(f"P(X > 12) = {1 - poisson.cdf(12, la):.6f}")

# Quantiles
print(f"Median = {poisson.median(la)}")
print(f"95th percentile = {poisson.ppf(0.95, la)}")

# Mean and variance
print(f"Mean = {poisson.mean(la)}, Variance = {poisson.var(la)}")
```
