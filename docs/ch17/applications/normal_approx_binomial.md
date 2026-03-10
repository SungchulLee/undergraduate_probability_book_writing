# Normal Approximation to the Binomial


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

## Setup

Let $X \sim B(n, p)$. Since $X = \sum_{i=1}^n X_i$ where $X_i \sim \text{Bernoulli}(p)$ are iid, the CLT gives:

$$\frac{X - np}{\sqrt{np(1-p)}} \xrightarrow{d} N(0,1) \quad \text{as } n \to \infty$$

For large $n$:

$$X \approx N(np, \, np(1-p))$$

## When to Use

The normal approximation to the binomial is reasonable when both $np$ and $n(1-p)$ are at least 5–10.

!!! tip "Comparison with Poisson Approximation"
    - **Poisson approximation**: $n$ large, $p$ small, $np = \lambda$ moderate → $B(n,p) \approx \text{Po}(\lambda)$
    - **Normal approximation**: $n$ large, $p$ not too extreme → $B(n,p) \approx N(np, np(1-p))$

## Example: Psychology Course Enrollment

The number of students enrolling in a psychology course is a Poisson random variable with mean $100$. If $120$ or more enroll, the professor teaches two sections. What is the probability of teaching two sections?

**Exact (Poisson):**

$$P(X \geq 120) = \sum_{k=120}^{\infty} \frac{100^k}{k!} e^{-100} = 0.0282$$

**Normal approximation with continuity correction:**

Since $X \sim \text{Po}(100)$ can be written as $X = \sum_{i=1}^{100} Y_i$ where $Y_i \sim \text{Po}(1)$ iid, we have $\mu = 100$, $\sigma^2 = 100$.

$$P(X \geq 120) = P(X \geq 119.5) = P\left(\frac{X - 100}{\sqrt{100}} \geq \frac{119.5 - 100}{\sqrt{100}}\right)$$

$$\approx 1 - \Phi(1.95) = 1 - 0.9744 = 0.0256$$

The approximation $0.0256$ is close to the exact value $0.0282$.

## Python Implementation

```python
import numpy as np
from scipy import stats

# Exact Poisson
lam = 100
exact = 1 - stats.poisson.cdf(119, lam)
print(f"Exact (Poisson): {exact:.4f}")

# Normal approximation with continuity correction
z = (119.5 - 100) / np.sqrt(100)
approx = 1 - stats.norm.cdf(z)
print(f"Normal approx (with CC): {approx:.4f}")

# Normal approximation without continuity correction
z_no_cc = (120 - 100) / np.sqrt(100)
approx_no_cc = 1 - stats.norm.cdf(z_no_cc)
print(f"Normal approx (without CC): {approx_no_cc:.4f}")
```

**Output:**
```
Exact (Poisson): 0.0282
Normal approx (with CC): 0.0256
Normal approx (without CC): 0.0228
```
