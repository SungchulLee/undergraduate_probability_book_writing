# Convolution for Continuous Random Variables

## Definition

!!! info "Convolution (Continuous)"
    If $X$ and $Y$ are **independent** continuous random variables, the **convolution** of their PDFs gives the PDF of $X + Y$:

    $$(f_X * f_Y)(a) = f_{X+Y}(a) = \int_{-\infty}^{\infty} f_X(b) \cdot f_Y(a - b) \, db$$

    The integral runs over all $b$ where both $f_X(b) > 0$ and $f_Y(a - b) > 0$.

### CDF Version

$$(F_X * F_Y)(a) = F_{X+Y}(a) = \int_{-\infty}^{\infty} F_Y(a - b) \, dF_X(b)$$

where $dF_X(b) = f_X(b) \, db$ represents "the probability that $X$ falls in $[b, b+db]$."

### Derivation

Conditioning on $X = b$:

$$f_{X+Y}(a) = \int_{-\infty}^{\infty} f_{Y}(a - b) \cdot \underbrace{f_X(b) \, db}_{P(b \leq X \leq b + db)}$$

This is the continuous analog of summing over all possible values of $X$ and computing the density of $Y = a - X$ at each.

## Practical Computation

The key challenge in computing convolutions is determining the **limits of integration**. The integrand is nonzero only where both:

- $f_X(b) > 0$: $b$ is in the support of $X$
- $f_Y(a - b) > 0$: $a - b$ is in the support of $Y$

These two constraints together determine the effective limits.

### Strategy

1. Write down the supports: $b \in [x_{\min}, x_{\max}]$ and $a - b \in [y_{\min}, y_{\max}]$
2. Solve for $b$: combine $x_{\min} \leq b \leq x_{\max}$ with $a - y_{\max} \leq b \leq a - y_{\min}$
3. Take the intersection to get the integration limits

## Properties

1. **Commutativity:** $f_X * f_Y = f_Y * f_X$
2. **Associativity:** $(f_X * f_Y) * f_Z = f_X * (f_Y * f_Z)$
3. **Linearity of Expectation:** $E[X + Y] = E[X] + E[Y]$ (always, even without independence)
4. **Variance Addition:** $\text{Var}(X + Y) = \text{Var}(X) + \text{Var}(Y)$ (requires independence)
5. **MGF Multiplication:** $M_{X+Y}(t) = M_X(t) \cdot M_Y(t)$ (requires independence)

## Connection to MGFs

Convolution in the "density domain" corresponds to **multiplication** in the "MGF domain":

$$f_{X+Y} = f_X * f_Y \quad \longleftrightarrow \quad M_{X+Y}(t) = M_X(t) \cdot M_Y(t)$$

This is analogous to the convolution theorem in signal processing, where convolution in the time domain becomes multiplication in the frequency domain. When MGFs are available, multiplying them is often easier than computing the convolution integral.

## Python Implementation

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

np.random.seed(42)
n_sim = 100000

# Continuous convolution via simulation and numerical computation
# Example: Sum of two independent Exp(1)
lam = 1.0
X = np.random.exponential(1/lam, n_sim)
Y = np.random.exponential(1/lam, n_sim)
S = X + Y

fig, ax = plt.subplots(1, 1, figsize=(8, 5))

# Simulation histogram
ax.hist(S, bins=80, density=True, alpha=0.5, color='steelblue',
        label='Simulation of X+Y')

# Theoretical: Exp(1) * Exp(1) = Gamma(2,1)
a_vals = np.linspace(0, 10, 200)
pdf_gamma = stats.gamma.pdf(a_vals, a=2, scale=1/lam)
ax.plot(a_vals, pdf_gamma, 'r-', lw=2, label='Γ(2,1) PDF (theory)')

# Numerical convolution
dx = 0.01
x_grid = np.arange(0, 10, dx)
f_exp = lam * np.exp(-lam * x_grid)
f_conv = np.convolve(f_exp, f_exp) * dx
a_conv = np.arange(0, len(f_conv)) * dx
ax.plot(a_conv[:len(a_vals)], f_conv[:len(a_vals)], 'g--', lw=2,
        label='Numerical convolution')

ax.set_title('Convolution: Exp(1) * Exp(1) = Γ(2,1)')
ax.set_xlabel('a')
ax.set_ylabel('f_{X+Y}(a)')
ax.set_xlim(0, 10)
ax.legend()
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('continuous_convolution.png', dpi=150, bbox_inches='tight')
plt.show()
```
