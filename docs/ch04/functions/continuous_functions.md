# Functions of a Continuous Random Variable


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

## The CDF Method (General)

For any function $g$ and continuous random variable $X$, the CDF method always works:

!!! info "CDF Method"
    To find the distribution of $Y = g(X)$:

    1. Compute $F_Y(y) = P(Y \leq y) = P(g(X) \leq y)$
    2. Express this as a probability involving $X$ alone
    3. Differentiate: $f_Y(y) = F_Y'(y)$

**Example: $Y = X^2$ where $X \sim N(0,1)$.**

For $y > 0$:

$$F_Y(y) = P(X^2 \leq y) = P(-\sqrt{y} \leq X \leq \sqrt{y}) = \Phi(\sqrt{y}) - \Phi(-\sqrt{y}) = 2\Phi(\sqrt{y}) - 1$$

Differentiating:

$$f_Y(y) = 2\phi(\sqrt{y}) \cdot \frac{1}{2\sqrt{y}} = \frac{1}{\sqrt{y}} \cdot \frac{1}{\sqrt{2\pi}} e^{-y/2} = \frac{y^{1/2 - 1} e^{-y/2}}{2^{1/2}\,\Gamma(1/2)}$$

This is the $\chi^2(1)$ distribution — a $\text{Gamma}(1/2, 1/2)$.

## The Change-of-Variables Formula (Monotone Case)

When $g$ is **strictly monotone** (either strictly increasing or strictly decreasing) and differentiable, there is a shortcut.

!!! info "Change-of-Variables Formula"
    If $Y = g(X)$ where $g$ is strictly monotone and differentiable with inverse $X = g^{-1}(Y)$, then:

    $$f_Y(y) = f_X\!\left(g^{-1}(y)\right) \cdot \left|\frac{d}{dy}\,g^{-1}(y)\right|$$

    The absolute value ensures $f_Y(y) \geq 0$ regardless of whether $g$ is increasing or decreasing.

**Derivation (increasing case).** If $g$ is strictly increasing:

$$F_Y(y) = P(g(X) \leq y) = P(X \leq g^{-1}(y)) = F_X(g^{-1}(y))$$

Differentiating by chain rule:

$$f_Y(y) = f_X(g^{-1}(y)) \cdot \frac{d}{dy}g^{-1}(y)$$

For the decreasing case, $P(g(X) \leq y) = P(X \geq g^{-1}(y))$, producing a negative sign that is absorbed by the absolute value.

## Example: Linear Transformation

Let $X$ be continuous with PDF $f_X$ and $Y = aX + b$ where $a \neq 0$.

- Inverse: $X = \frac{Y - b}{a}$
- Derivative: $\frac{dX}{dY} = \frac{1}{a}$

$$f_Y(y) = f_X\!\left(\frac{y - b}{a}\right) \cdot \frac{1}{|a|}$$

**Special case:** If $X \sim N(\mu, \sigma^2)$ and $Y = aX + b$, then $Y \sim N(a\mu + b,\; a^2\sigma^2)$.

## Example: Exponential Transformation

Let $X \sim \text{Uniform}(0, 1)$ and $Y = -\ln X$. Since $g(x) = -\ln x$ is **strictly decreasing** on $(0,1)$:

- Inverse: $X = e^{-Y}$
- Derivative: $\frac{dX}{dY} = -e^{-Y}$, so $\left|\frac{dX}{dY}\right| = e^{-Y}$

$$f_Y(y) = f_X(e^{-y}) \cdot e^{-y} = 1 \cdot e^{-y} = e^{-y}, \quad y > 0$$

This is $\text{Exponential}(1)$. This result is the basis of the **inverse CDF method** for simulation.

## Non-Monotone Functions: Partition Approach

When $g$ is not monotone, partition the domain of $X$ into intervals where $g$ is monotone, apply the formula on each piece, and sum.

!!! info "Non-Monotone Change of Variables"
    If $g$ is not monotone, but the domain can be partitioned into regions $A_1, A_2, \ldots, A_k$ on each of which $g$ is strictly monotone with local inverse $h_i = g^{-1}\big|_{A_i}$, then:

    $$f_Y(y) = \sum_{i=1}^{k} f_X(h_i(y)) \cdot |h_i'(y)|$$

**Example: $Y = X^2$ where $X$ has PDF $f_X$ on $(-\infty, \infty)$.**

The function $g(x) = x^2$ is decreasing on $(-\infty, 0)$ and increasing on $(0, \infty)$. The two local inverses are $h_1(y) = -\sqrt{y}$ and $h_2(y) = \sqrt{y}$, each with derivative $|h_i'(y)| = \frac{1}{2\sqrt{y}}$.

$$f_Y(y) = \frac{f_X(-\sqrt{y}) + f_X(\sqrt{y})}{2\sqrt{y}}, \quad y > 0$$

When $f_X$ is symmetric about 0, this simplifies to $f_Y(y) = \frac{f_X(\sqrt{y})}{\sqrt{y}}$.

## Python Implementation

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

fig, axes = plt.subplots(1, 3, figsize=(16, 5))

x = np.linspace(-4, 4, 1000)

# --- Panel 1: Y = X^2 for X ~ N(0,1) ---
fX = stats.norm.pdf(x)
axes[0].plot(x, fX, 'b-', lw=2, label='$f_X$: N(0,1)')

y = np.linspace(0.01, 10, 500)
fY_theory = stats.chi2.pdf(y, df=1)

# Simulation
np.random.seed(42)
X_sim = np.random.normal(0, 1, 200000)
Y_sim = X_sim**2
axes[0].hist(Y_sim, bins=100, density=True, alpha=0.4, color='coral',
             range=(0, 10), label='Y = X² simulated')
axes[0].plot(y, fY_theory, 'r-', lw=2, label='χ²(1) PDF')
axes[0].set_xlim(-4, 10)
axes[0].set_title('Y = X², X ~ N(0,1) → χ²(1)')
axes[0].legend(fontsize=9)
axes[0].grid(True, alpha=0.3)

# --- Panel 2: Y = -ln(X), X ~ U(0,1) → Exp(1) ---
X_unif = np.random.uniform(0, 1, 200000)
Y_exp = -np.log(X_unif)

y2 = np.linspace(0.01, 6, 300)
axes[1].hist(Y_exp, bins=80, density=True, alpha=0.5, color='steelblue',
             label='Y = -ln(X) simulated')
axes[1].plot(y2, stats.expon.pdf(y2), 'r-', lw=2, label='Exp(1) PDF')
axes[1].set_title('Y = -ln(X), X ~ U(0,1) → Exp(1)')
axes[1].set_xlabel('y')
axes[1].legend()
axes[1].grid(True, alpha=0.3)

# --- Panel 3: Y = |X| for X ~ N(0,1) → Half-Normal ---
Y_abs = np.abs(X_sim)
y3 = np.linspace(0, 4, 300)
fY_half = 2 * stats.norm.pdf(y3)  # half-normal PDF

axes[2].hist(Y_abs, bins=80, density=True, alpha=0.5, color='steelblue',
             label='|X| simulated')
axes[2].plot(y3, fY_half, 'r-', lw=2, label='Half-Normal PDF')
axes[2].set_title('Y = |X|, X ~ N(0,1) → Half-Normal')
axes[2].set_xlabel('y')
axes[2].legend()
axes[2].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('functions_continuous.png', dpi=150, bbox_inches='tight')
plt.show()
```
