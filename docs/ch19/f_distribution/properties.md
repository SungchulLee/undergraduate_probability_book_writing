# F Distribution: Properties


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

## Mean and Variance

| Property | Value | Condition |
|----------|-------|-----------|
| Mean | $\frac{d_2}{d_2 - 2}$ | $d_2 > 2$ |
| Variance | $\frac{2d_2^2(d_1 + d_2 - 2)}{d_1(d_2 - 2)^2(d_2 - 4)}$ | $d_2 > 4$ |
| Mode | $\frac{d_1 - 2}{d_1} \cdot \frac{d_2}{d_2 + 2}$ | $d_1 > 2$ |

!!! note
    The mean depends **only** on $d_2$, not on $d_1$. For small $d_2$, the mean can be substantially greater than 1.

## Key Properties

### Support and Shape

The $F$ distribution is supported on $(0, \infty)$ and is **right-skewed**. The skewness decreases as both $d_1$ and $d_2$ increase.

### Reciprocal Property

If $F \sim F_{d_1, d_2}$, then:

$$\frac{1}{F} \sim F_{d_2, d_1}$$

This follows directly from the definition: swapping numerator and denominator swaps the degrees of freedom.

## Relationship to the t Distribution

If $T \sim t_d$, then:

$$T^2 \sim F_{1, d}$$

**Proof.** Write $T = Z / \sqrt{V/d}$ where $Z \sim N(0,1)$ and $V \sim \chi^2_d$ are independent. Then:

$$T^2 = \frac{Z^2}{V/d} = \frac{Z^2 / 1}{V / d} = \frac{\chi^2_1 / 1}{\chi^2_d / d} \sim F_{1, d}$$

This connection means that a two-sided $t$-test with $d$ degrees of freedom is equivalent to an $F$-test with $(1, d)$ degrees of freedom.

## Relationship to the Beta Distribution

If $F \sim F_{d_1, d_2}$, then:

$$\frac{d_1 F / d_2}{1 + d_1 F / d_2} \sim \text{Beta}\!\left(\frac{d_1}{2}, \frac{d_2}{2}\right)$$

## Python Exploration

```python
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

x = np.linspace(0.01, 5, 500)

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Varying d1
ax = axes[0]
d2 = 10
for d1 in [1, 2, 5, 10, 30]:
    ax.plot(x, stats.f.pdf(x, d1, d2), label=f'$F_{{{d1},{d2}}}$')
ax.set_title(f'Varying $d_1$ (fixed $d_2 = {d2}$)')
ax.set_xlabel('$x$'); ax.set_ylabel('Density')
ax.legend()

# Varying d2
ax = axes[1]
d1 = 5
for d2 in [3, 5, 10, 30, 100]:
    ax.plot(x, stats.f.pdf(x, d1, d2), label=f'$F_{{{d1},{d2}}}$')
ax.set_title(f'Varying $d_2$ (fixed $d_1 = {d1}$)')
ax.set_xlabel('$x$'); ax.set_ylabel('Density')
ax.legend()

plt.tight_layout()
plt.show()
```
