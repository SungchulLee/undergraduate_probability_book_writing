# Student's $t$ Distribution: Properties and Comparison to Normal

## Summary of Properties

| Property | Value |
|----------|-------|
| PDF | $\frac{1}{\sqrt{d}\,B(1/2, d/2)}\left(1 + \frac{t^2}{d}\right)^{-(d+1)/2}$ |
| Mean | $0$ for $d > 1$ |
| Variance | $\frac{d}{d - 2}$ for $d > 2$ |
| Symmetry | Symmetric about $0$ |
| Support | $(-\infty, \infty)$ |

## Mean and Variance

**Mean.** By the symmetry of the PDF ($f_T(t) = f_T(-t)$), $E[T] = 0$ for $d > 1$.

!!! warning "Mean Does Not Exist for $d = 1$"
    When $d = 1$, the $t$ distribution is the **Cauchy distribution**, which has no finite mean. The integral $\int_{-\infty}^{\infty} t \cdot f_T(t)\,dt$ diverges.

**Variance.** For $d > 2$:

$$\text{Var}(T) = \frac{d}{d - 2}$$

The variance is always greater than 1 (the variance of the standard normal), reflecting the heavier tails. As $d \to \infty$, $\text{Var}(T) \to 1$.

## Comparison to the Standard Normal

The $t$ distribution has **heavier tails** than the standard normal:

$$f_T(t) \propto \left(1 + \frac{t^2}{d}\right)^{-(d+1)/2} \quad \text{vs.} \quad \phi(t) \propto e^{-t^2/2}$$

The $t$ density decays **polynomially** (like $|t|^{-(d+1)}$), while the normal density decays **exponentially** (like $e^{-t^2/2}$). This means:

- More probability in the tails for $t_d$ compared to $N(0,1)$
- More probability near the center for $N(0,1)$ (to compensate, since both integrate to 1)
- Extreme values are more likely under $t_d$ than under $N(0,1)$

## Special Case: Cauchy Distribution ($d = 1$)

When $d = 1$:

$$f_T(t) \propto \frac{1}{1 + t^2} \quad \Rightarrow \quad f_T(t) = \frac{1}{\pi} \cdot \frac{1}{1 + t^2}$$

The Cauchy distribution has:

- No finite mean (the integral diverges)
- No finite variance
- No MGF
- The sample mean of $n$ iid Cauchy random variables has the **same** distribution as a single Cauchy — the CLT does not apply

## Python Comparison

```python
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

x = np.linspace(-4, 4, 500)

fig, ax = plt.subplots(figsize=(8, 5))
ax.plot(x, stats.norm.pdf(x), 'r-', lw=2, label='$N(0,1)$')
for d in [1, 2, 5, 10, 30]:
    ax.plot(x, stats.t.pdf(x, d), '--', label=f'$t_{{{d}}}$')

ax.set_xlabel('$x$')
ax.set_ylabel('Density')
ax.set_title("Student's $t$ vs. Standard Normal")
ax.legend()
plt.tight_layout()
plt.show()
```
