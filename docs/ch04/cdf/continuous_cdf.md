# Continuous CDF

The CDF of a continuous random variable is a smooth, non-decreasing curve with no jumps — reflecting the fact that no single point carries positive probability.

## Definition

For a continuous random variable $X$ with PDF $f_X(x)$, the CDF is

$$
F_X(x) = P(X \le x) = \int_{-\infty}^{x} f_X(t)\,dt
$$

The CDF is continuous (no jumps), so $P(X = a) = 0$ for every $a$.

## Explanation

### CDF-PDF Relationship

By the Fundamental Theorem of Calculus, wherever $f_X$ is continuous:

$$
f_X(x) = F_X'(x) = \frac{d}{dx}F_X(x)
$$

The PDF is the derivative of the CDF. The CDF is the antiderivative (integral) of the PDF.

### Strict vs Non-Strict Inequalities

Since $P(X = a) = 0$ for continuous variables, strict and non-strict inequalities are interchangeable:

$$
P(a \le X \le b) = P(a < X < b) = P(a \le X < b) = F(b) - F(a)
$$

This simplification does not hold for discrete random variables, where $P(X = a) > 0$.

### Recognizing the CDF Shape

- Starts at 0, ends at 1
- Always increasing where $f_X(x) > 0$
- Steepest where the PDF is highest (most probability density)
- Has an inflection point where the PDF has its mode

## Examples

**Example 1.** $X \sim \text{Uniform}(0, 1)$ with $f(x) = 1$ on $[0,1]$.

$$
F(x) = \begin{cases} 0 & x < 0 \\ x & 0 \le x \le 1 \\ 1 & x > 1 \end{cases}
$$

Then $P(0.3 \le X \le 0.7) = F(0.7) - F(0.3) = 0.7 - 0.3 = 0.4$.

**Example 2.** $X \sim \text{Exp}(\lambda)$ with $f(x) = \lambda e^{-\lambda x}$ for $x \ge 0$.

$$
F(x) = \begin{cases} 0 & x < 0 \\ 1 - e^{-\lambda x} & x \ge 0 \end{cases}
$$

For $\lambda = 2$: $P(X > 1) = 1 - F(1) = e^{-2} \approx 0.1353$.

```python
import numpy as np

# Exponential(lambda=2) CDF
lam = 2
F = lambda x: 1 - np.exp(-lam * x) if x >= 0 else 0

print(f"F(0.5) = P(X <= 0.5) = {F(0.5):.4f}")
print(f"F(1.0) = P(X <= 1.0) = {F(1.0):.4f}")
print(f"P(X > 1) = {1 - F(1.0):.4f}")
print(f"P(0.5 < X <= 1.5) = {F(1.5) - F(0.5):.4f}")

# Verify: CDF derivative at x=1 should equal PDF at x=1
h = 1e-8
numerical_deriv = (F(1 + h) - F(1)) / h
pdf_at_1 = lam * np.exp(-lam * 1)
print(f"\nF'(1) = {numerical_deriv:.4f}, f(1) = {pdf_at_1:.4f}")
```
