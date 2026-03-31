# Law of the Unconscious Statistician (LOTUS)

## Motivation

Suppose we know the distribution of $X$ and want to compute $E[g(X)]$ for some function $g$. One approach is to first find the distribution of $Y = g(X)$ and then compute $E[Y]$. LOTUS provides a shortcut: we can compute $E[g(X)]$ directly from the distribution of $X$, without finding the distribution of $g(X)$.

---

## Statement

### Discrete Case

If $X$ is discrete with PMF $p(x)$, then

$$
E[g(X)] = \sum_{x} g(x) \, p(x)
$$

### Continuous Case

If $X$ is continuous with PDF $f(x)$, then

$$
E[g(X)] = \int_{-\infty}^{\infty} g(x) \, f(x) \, dx
$$

---

## Why "Unconscious Statistician"?

The name is humorous: the formula looks like one is "unconsciously" treating $g(x)$ as if it were the random variable itself and computing the expectation using the distribution of $X$ rather than the distribution of $g(X)$. Despite the name, the result is a rigorous theorem.

---

## Examples

### Example 1: $E[X^2]$ for a Fair Die

Let $X$ be the face value of a fair die. By LOTUS:

$$
E[X^2] = \sum_{k=1}^{6} k^2 \cdot \frac{1}{6} = \frac{1 + 4 + 9 + 16 + 25 + 36}{6} = \frac{91}{6} \approx 15.17
$$

Note: $(E[X])^2 = 3.5^2 = 12.25 \neq E[X^2]$ in general.

### Example 2: $E[e^X]$ for Exponential

If $X \sim \text{Exp}(\lambda)$ with $f(x) = \lambda e^{-\lambda x}$ for $x \geq 0$, then

$$
E[e^{tX}] = \int_0^{\infty} e^{tx} \cdot \lambda e^{-\lambda x} \, dx = \frac{\lambda}{\lambda - t}, \quad t < \lambda
$$

This is the **moment generating function** of the exponential distribution.

### Example 3: $E[X^2]$ for Continuous Uniform

If $X \sim \text{Uniform}(0, 1)$, then

$$
E[X^2] = \int_0^1 x^2 \cdot 1 \, dx = \frac{1}{3}
$$

---

## LOTUS for Joint Distributions

LOTUS extends to functions of multiple random variables.

### Discrete Case

$$
E[g(X, Y)] = \sum_x \sum_y g(x, y) \, p(x, y)
$$

### Continuous Case

$$
E[g(X, Y)] = \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} g(x, y) \, f(x, y) \, dx \, dy
$$

---

## Application: Computing Variance

LOTUS is essential for computing variance via the shortcut formula:

$$
\text{Var}(X) = E[X^2] - (E[X])^2
$$

where $E[X^2]$ is computed using LOTUS with $g(x) = x^2$.

---

## Python Implementation

```python
import numpy as np
from scipy import integrate

# E[X^2] for fair die using LOTUS
values = np.arange(1, 7)
probs = np.ones(6) / 6
E_X2 = np.sum(values**2 * probs)
E_X = np.sum(values * probs)
print(f"E[X^2] = {E_X2:.4f}")        # 15.1667
print(f"(E[X])^2 = {E_X**2:.4f}")    # 12.25

# E[X^2] for Uniform(0,1) using numerical integration
result, _ = integrate.quad(lambda x: x**2 * 1, 0, 1)
print(f"E[X^2] for Uniform(0,1) = {result:.4f}")  # 0.3333

# E[e^(tX)] for Exp(lambda) - MGF
lam = 2.0
t = 0.5
mgf_exact = lam / (lam - t)
mgf_numerical, _ = integrate.quad(lambda x: np.exp(t*x) * lam * np.exp(-lam*x), 0, np.inf)
print(f"MGF exact = {mgf_exact:.4f}")
print(f"MGF numerical = {mgf_numerical:.4f}")

# Monte Carlo verification
np.random.seed(42)
N = 1_000_000
samples = np.random.exponential(1/lam, N)
print(f"Monte Carlo E[e^(tX)] = {np.mean(np.exp(t * samples)):.4f}")
```
