# $F$ Distribution: Definition as Ratio of Chi-Squareds

## Definition

If $V_1 \sim \chi^2_{d_1}$ and $V_2 \sim \chi^2_{d_2}$ are **independent**, then:

$$F = \frac{V_1 / d_1}{V_2 / d_2} \sim F_{d_1, d_2}$$

where $d_1$ and $d_2$ are the **numerator** and **denominator degrees of freedom**, respectively.

## PDF Derivation via Jacobian

### Setup

Let $F = \frac{X/d_1}{Y/d_2}$ and $Z = Y$, where $X \sim \chi^2_{d_1}$ and $Y \sim \chi^2_{d_2}$ are independent.

The inverse transformation: $x = f \cdot d_1 \cdot z / d_2$ and $y = z$.

### Jacobian

$$\left|\frac{\partial(x, y)}{\partial(f, z)}\right| = \left|\frac{\partial(f, z)}{\partial(x, y)}\right|^{-1} = \left|\det \begin{pmatrix} \frac{1/d_1}{z/d_2} & * \\ 0 & 1 \end{pmatrix}\right|^{-1} = \frac{z/d_2}{1/d_1} = \frac{d_1 z}{d_2}$$

### Joint Density

$$f_{F,Z}(f, z) = f_{X,Y}(x, y) \left|\frac{\partial(x,y)}{\partial(f,z)}\right|$$

$$= \frac{(1/2)^{d_1/2}}{\Gamma(d_1/2)} x^{d_1/2-1} e^{-x/2} \cdot \frac{(1/2)^{d_2/2}}{\Gamma(d_2/2)} y^{d_2/2-1} e^{-y/2} \cdot \frac{d_1 z}{d_2}$$

Substituting $x = f \cdot d_1 z / d_2$ and $y = z$, and setting $\lambda = \frac{1}{2}\!\left(1 + \frac{d_1}{d_2}f\right)$:

$$f_{F,Z}(f, z) = \frac{1}{B(d_1/2, \, d_2/2) \cdot f} \sqrt{\frac{(d_1 f)^{d_1} \cdot d_2^{d_2}}{(d_1 f + d_2)^{d_1+d_2}}} \cdot \underbrace{\frac{\lambda\,(\lambda z)^{(d_1+d_2)/2 - 1} e^{-\lambda z}}{\Gamma\!\left(\frac{d_1+d_2}{2}\right)}}_{\text{Gamma}\!\left(\frac{d_1+d_2}{2}, \, \lambda\right) \text{ density in } z}$$

### Marginal PDF of $F$

Integrating out $z$ (the Gamma density integrates to 1):

$$\boxed{f_F(f) = \frac{1}{B\!\left(\frac{d_1}{2}, \frac{d_2}{2}\right) \cdot f} \sqrt{\frac{(d_1 f)^{d_1} \cdot d_2^{d_2}}{(d_1 f + d_2)^{d_1 + d_2}}}, \quad f > 0}$$

## Python Verification

```python
import numpy as np
from scipy import stats, special
import matplotlib.pyplot as plt

d1, d2 = 5, 10
x = np.linspace(0.01, 5, 500)

# Formula
B = special.beta(d1/2, d2/2)
pdf_formula = (1 / (B * x)) * np.sqrt((d1*x)**d1 * d2**d2 / (d1*x + d2)**(d1+d2))

# scipy
pdf_scipy = stats.f.pdf(x, d1, d2)

print(f"Max difference: {np.max(np.abs(pdf_formula - pdf_scipy)):.2e}")

# Simulation
np.random.seed(42)
v1 = np.random.chisquare(d1, 100_000)
v2 = np.random.chisquare(d2, 100_000)
f_samples = (v1 / d1) / (v2 / d2)

fig, ax = plt.subplots(figsize=(8, 5))
ax.hist(f_samples, bins=100, density=True, alpha=0.5, range=(0, 6), label='Simulation')
ax.plot(x, pdf_scipy, 'r-', lw=2, label=f'$F_{{{d1},{d2}}}$ PDF')
ax.set_xlabel('$f$')
ax.set_ylabel('Density')
ax.set_title(f'$F$ Distribution ($d_1={d1}, d_2={d2}$)')
ax.legend()
plt.tight_layout()
plt.show()
```
