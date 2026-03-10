# Probability Density Function

The PDF describes how probability is distributed continuously across the real line — it gives probability *density*, not probability itself.

## Definition

The **probability density function (PDF)** of a continuous random variable $X$ is a function $f_X(x)$ satisfying

$$
P(X \in A) = \int_A f_X(x)\,dx
$$

A valid PDF must satisfy:

1. **Non-negativity:** $f_X(x) \ge 0$ for all $x$
2. **Normalization:** $\displaystyle\int_{-\infty}^{\infty} f_X(x)\,dx = 1$

## Explanation

### Density, Not Probability

!!! warning "Common misconception"
    $f_X(x)$ is **not** a probability. It is a density, and $f_X(x)$ can exceed 1. For example, $X \sim \text{Uniform}(0, 1/3)$ has $f(x) = 3$ on $[0, 1/3]$.

The correct interpretation: $f_X(x)\,dx$ is the infinitesimal probability mass in the interval $[x, x+dx]$.

### Infinitesimal Interpretation

For small $\varepsilon > 0$:

$$
P(x \le X \le x + \varepsilon) \approx f_X(x) \cdot \varepsilon
$$

The PDF gives probability per unit length near $x$. To get an actual probability, you must integrate (i.e., multiply density by length and sum).

### Probability as Area

$$
P(a \le X \le b) = \int_a^b f_X(x)\,dx = \text{area under } f_X \text{ between } a \text{ and } b
$$

The total area under the entire PDF curve is 1.

### PMF vs PDF

| | PMF $p_X(x)$ | PDF $f_X(x)$ |
|:--|:-------------|:-------------|
| Meaning | Probability at $x$ | Density at $x$ |
| Range | $[0, 1]$ | $[0, \infty)$ |
| Total | $\sum p_X(x) = 1$ | $\int f_X(x)\,dx = 1$ |
| Read directly? | Yes: $P(X=x)$ | No: must integrate |

## Examples

**Example 1.** Let $f(x) = 2x$ for $0 \le x \le 1$, and $f(x) = 0$ otherwise.

Verification: $\int_0^1 2x\,dx = x^2\big|_0^1 = 1$.

$$
P(X > 0.5) = \int_{0.5}^{1} 2x\,dx = x^2\big|_{0.5}^{1} = 1 - 0.25 = 0.75
$$

Note: $f(0.8) = 1.6 > 1$ — the density exceeds 1, which is perfectly valid.

**Example 2.** $X \sim \text{Exp}(1)$ with $f(x) = e^{-x}$ for $x \ge 0$.

$$
P(1 \le X \le 2) = \int_1^2 e^{-x}\,dx = -e^{-x}\big|_1^2 = e^{-1} - e^{-2} \approx 0.2325
$$

```python
import numpy as np
from scipy import integrate

# Example 1: f(x) = 2x on [0, 1]
f1 = lambda x: 2 * x
norm, _ = integrate.quad(f1, 0, 1)
p_gt_half, _ = integrate.quad(f1, 0.5, 1)
print(f"f(x) = 2x: normalization = {norm:.4f}")
print(f"P(X > 0.5) = {p_gt_half:.4f}")
print(f"f(0.8) = {f1(0.8):.1f}  (density > 1 is OK)")

# Example 2: Exp(1)
f2 = lambda x: np.exp(-x)
p_12, _ = integrate.quad(f2, 1, 2)
print(f"\nExp(1): P(1 <= X <= 2) = {p_12:.4f}")
print(f"Exact: e^-1 - e^-2 = {np.exp(-1) - np.exp(-2):.4f}")
```
