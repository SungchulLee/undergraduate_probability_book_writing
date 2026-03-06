# Jensen's Inequality

## Statement

If $g$ is a **convex** function and $X$ is a random variable with $E[X]$ and $E[g(X)]$ both finite, then

$$

E[g(X)] \geq g(E[X])

$$

If $g$ is **concave**, the inequality reverses:

$$

E[g(X)] \leq g(E[X])

$$

---

## Intuition

A convex function curves upward, so the average of the function values is at least the function value at the average. Geometrically, the chord of a convex function lies above the function.

---

## Common Applications

| Function $g$ | Convexity | Jensen's Statement |
|:---:|:---:|:---:|
| $g(x) = x^2$ | Convex | $E[X^2] \geq (E[X])^2$ |
| $g(x) = e^x$ | Convex | $E[e^X] \geq e^{E[X]}$ |
| $g(x) = \lvert x \rvert$ | Convex | $E[\lvert X\rvert] \geq \lvert E[X]\rvert$ |
| $g(x) = \log x$ | Concave | $E[\log X] \leq \log E[X]$ |
| $g(x) = \sqrt{x}$ | Concave | $E[\sqrt{X}] \leq \sqrt{E[X]}$ |

The first row implies $\text{Var}(X) = E[X^2] - (E[X])^2 \geq 0$.

---

## Application in Finance: Arithmetic vs Geometric Mean

For positive returns $R_1, \ldots, R_n$, since $\log$ is concave:

$$

\frac{1}{n}\sum \log R_i \leq \log\left(\frac{1}{n}\sum R_i\right)

$$

This means the **geometric mean** is always $\leq$ the **arithmetic mean**.

---

## Python Implementation

```python
import numpy as np

np.random.seed(42)
N = 1_000_000

X = np.random.exponential(1, N)

# E[X^2] >= (E[X])^2
print(f"E[X^2] = {np.mean(X**2):.4f}")
print(f"(E[X])^2 = {np.mean(X)**2:.4f}")
print(f"Jensen holds: {np.mean(X**2) >= np.mean(X)**2}")

# E[log(X)] <= log(E[X])
pos_X = X[X > 0]
print(f"\nE[log(X)] = {np.mean(np.log(pos_X)):.4f}")
print(f"log(E[X]) = {np.log(np.mean(pos_X)):.4f}")
print(f"Jensen holds: {np.mean(np.log(pos_X)) <= np.log(np.mean(pos_X))}")
```
