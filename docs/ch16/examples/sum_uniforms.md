# Sum of Independent Uniforms

## Convolution of Two Uniforms

!!! info "Sum of Two iid U(-1/2, 1/2)"
    If $X$ and $Y$ are independent $U(-1/2, 1/2)$, then $X + Y$ has the **triangular distribution**:

    $$f_{X+Y}(a) = (1 - |a|)^+, \quad -1 \leq a \leq 1$$

    where $(x)^+ = \max(x, 0)$.

### Derivation (for 0 <= a <= 1)

By symmetry, it suffices to compute the convolution for $0 \leq a \leq 1$:

$$f_{X+Y}(a) = \int_{-\infty}^{\infty} f_X(b) \, f_Y(a - b) \, db$$

**Determining the limits:** Both densities equal 1 on $(-1/2, 1/2)$ and 0 elsewhere. So we need:

$$-\frac{1}{2} \leq b \leq \frac{1}{2} \quad \text{and} \quad -\frac{1}{2} \leq a - b \leq \frac{1}{2}$$

The second constraint gives $a - \frac{1}{2} \leq b \leq a + \frac{1}{2}$.

For $0 \leq a \leq 1$: the intersection is $a - \frac{1}{2} \leq b \leq \frac{1}{2}$.

$$f_{X+Y}(a) = \int_{a - 1/2}^{1/2} 1 \, db = \frac{1}{2} - \left(a - \frac{1}{2}\right) = 1 - a$$

By symmetry, $f_{X+Y}(a) = 1 + a$ for $-1 \leq a \leq 0$. Combining: $f_{X+Y}(a) = 1 - |a|$.

## General Case: Sum of Two iid U(0, 1)

If $X, Y$ are iid $U(0, 1)$, then $X + Y$ has the **triangular distribution** on $(0, 2)$:

$$f_{X+Y}(a) = \begin{cases} a & 0 \leq a \leq 1 \\ 2 - a & 1 < a \leq 2 \end{cases}$$

This is a shift of the $U(-1/2, 1/2)$ result: if $X' = X - 1/2 \sim U(-1/2, 1/2)$, then $X + Y = (X' + Y') + 1$.

## Sum of n iid Uniforms

As $n$ increases, the distribution of $S_n = X_1 + \cdots + X_n$ approaches a Normal distribution by the Central Limit Theorem. The convolution $U * U$ gives a triangle, $U * U * U$ gives a piecewise quadratic, and so on. In general, the $n$-fold convolution of $U(0,1)$ is called the **Irwin-Hall distribution** and consists of piecewise polynomials of degree $n-1$.

## Python Implementation

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

np.random.seed(42)
n_sim = 100000

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Sum of two iid U(-1/2, 1/2)
X = np.random.uniform(-0.5, 0.5, n_sim)
Y = np.random.uniform(-0.5, 0.5, n_sim)
S = X + Y

a_vals = np.linspace(-1, 1, 200)
pdf_theory = np.maximum(1 - np.abs(a_vals), 0)

axes[0].hist(S, bins=100, density=True, alpha=0.5, color='steelblue',
             label='Simulated X+Y')
axes[0].plot(a_vals, pdf_theory, 'r-', lw=2, label='(1-|a|)⁺')
axes[0].set_title('X + Y where X, Y iid U(-1/2, 1/2)')
axes[0].set_xlabel('a')
axes[0].set_ylabel('Density')
axes[0].legend()
axes[0].grid(True, alpha=0.3)

# Sum of n iid U(-1/2, 1/2) for increasing n
colors = ['blue', 'red', 'green', 'orange', 'purple']
for i, n in enumerate([2, 3, 5, 10, 30]):
    samples = np.random.uniform(-0.5, 0.5, (n_sim, n))
    sums = samples.sum(axis=1)
    axes[1].hist(sums, bins=80, density=True, alpha=0.3,
                 color=colors[i % len(colors)], label=f'n={n}')

# Overlay Normal for n=30
x_norm = np.linspace(-4, 4, 200)
axes[1].plot(x_norm, stats.norm.pdf(x_norm, loc=0, scale=np.sqrt(30/12)),
             'k-', lw=2, label='Normal approx (n=30)')
axes[1].set_title('Sum of n iid U(-1/2, 1/2) → Normal')
axes[1].set_xlabel('Sum')
axes[1].legend(fontsize=9)
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('sum_uniforms.png', dpi=150, bbox_inches='tight')
plt.show()
```
