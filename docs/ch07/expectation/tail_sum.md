# Tail Sum Formula for Expectation


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

## Statement

### Non-negative Integer-Valued Random Variables

If $X$ is a non-negative integer-valued random variable, then

$$
E[X] = \sum_{k=1}^{\infty} P(X \geq k) = \sum_{k=0}^{\infty} P(X > k)
$$

### Non-negative Continuous Random Variables

If $X$ is a non-negative continuous random variable, then

$$
E[X] = \int_0^{\infty} P(X > t) \, dt = \int_0^{\infty} [1 - F_X(t)] \, dt
$$

---

## Proof (Discrete Case)

$$
\sum_{k=1}^{\infty} P(X \geq k) = \sum_{k=1}^{\infty} \sum_{j=k}^{\infty} P(X = j) = \sum_{j=1}^{\infty} \sum_{k=1}^{j} P(X = j) = \sum_{j=1}^{\infty} j \cdot P(X = j) = E[X]
$$

The key step is swapping the order of summation: each term $P(X = j)$ appears exactly $j$ times.

---

## Proof (Continuous Case)

$$
\int_0^{\infty} P(X > t) \, dt = \int_0^{\infty} \int_t^{\infty} f(x) \, dx \, dt = \int_0^{\infty} \int_0^{x} dt \, f(x) \, dx = \int_0^{\infty} x \, f(x) \, dx = E[X]
$$

---

## Examples

### Example 1: Geometric Distribution

If $X \sim \text{Geo}(p)$ (number of trials until first success), then

$$
P(X \geq k) = (1-p)^{k-1}
$$

By the tail sum formula:

$$
E[X] = \sum_{k=1}^{\infty} (1-p)^{k-1} = \frac{1}{1-(1-p)} = \frac{1}{p}
$$

### Example 2: Exponential Distribution

If $X \sim \text{Exp}(\lambda)$, then $P(X > t) = e^{-\lambda t}$. By the tail sum formula:

$$
E[X] = \int_0^{\infty} e^{-\lambda t} \, dt = \frac{1}{\lambda}
$$

---

## General Tail Sum Formula

For any random variable $X$ (not necessarily non-negative):

$$
E[X] = \int_0^{\infty} P(X > t) \, dt - \int_0^{\infty} P(X < -t) \, dt
$$

This decomposes $X$ into its positive and negative parts: $X = X^+ - X^-$ where $X^+ = \max(X, 0)$ and $X^- = \max(-X, 0)$.

---

## Python Implementation

```python
import numpy as np

# Tail sum for Geometric(p)
p = 0.3
# Exact
E_geo_exact = 1 / p
# Via tail sum (truncated)
E_geo_tail = sum((1 - p)**(k - 1) for k in range(1, 1000))
print(f"E[Geo({p})] exact = {E_geo_exact:.4f}")
print(f"E[Geo({p})] tail sum = {E_geo_tail:.4f}")

# Tail sum for Exponential(lambda)
lam = 2.0
from scipy import integrate
E_exp_exact = 1 / lam
E_exp_tail, _ = integrate.quad(lambda t: np.exp(-lam * t), 0, np.inf)
print(f"E[Exp({lam})] exact = {E_exp_exact:.4f}")
print(f"E[Exp({lam})] tail sum = {E_exp_tail:.4f}")

# Monte Carlo verification
np.random.seed(42)
N = 1_000_000
geo_samples = np.random.geometric(p, N)
exp_samples = np.random.exponential(1/lam, N)
print(f"MC E[Geo({p})] = {np.mean(geo_samples):.4f}")
print(f"MC E[Exp({lam})] = {np.mean(exp_samples):.4f}")
```
