# Markov's Inequality


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

## Statement

If $X$ is a non-negative random variable and $a > 0$, then

$$
P(X \geq a) \leq \frac{E[X]}{a}
$$

---

## Proof

$$
E[X] = \int_0^{\infty} x f(x) \, dx \geq \int_a^{\infty} x f(x) \, dx \geq a \int_a^{\infty} f(x) \, dx = a \, P(X \geq a)
$$

---

## Example

If $X$ has mean 10, then $P(X \geq 50) \leq 10/50 = 0.2$.

The bound is often loose, but it requires only knowledge of the mean — no information about the shape of the distribution.

---

## Python Implementation

```python
import numpy as np

np.random.seed(42)
N = 1_000_000

# Exponential(1): mean = 1
X = np.random.exponential(1, N)
a = 3
markov_bound = 1 / a
actual_prob = np.mean(X >= a)
print(f"P(X >= {a}): Markov bound = {markov_bound:.4f}, actual = {actual_prob:.4f}")
```
