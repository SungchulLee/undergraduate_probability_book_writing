# Student's t Distribution: Definition and Derivation


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

## Definition

If $Z \sim N(0, 1)$ and $V \sim \chi^2_d$ are **independent**, then:

$$T = \frac{Z}{\sqrt{V/d}} \sim t_d$$

The parameter $d$ is the **degrees of freedom**.

## PDF Derivation via Jacobian

### Setup

Let $T = Z / \sqrt{V/d}$ and $U = V$, where $Z \sim N(0,1)$ and $V \sim \chi^2_d$ are independent.

The inverse transformation is $z = t\sqrt{u/d}$ and $v = u$.

### Jacobian

$$\left|\frac{\partial(z, v)}{\partial(t, u)}\right| = \left|\frac{\partial(t, u)}{\partial(z, v)}\right|^{-1} = \left|\det \begin{pmatrix} 1/\sqrt{v/d} & * \\ 0 & 1 \end{pmatrix}\right|^{-1} = \sqrt{\frac{v}{d}} = \sqrt{\frac{u}{d}}$$

### Joint Density

Since $Z$ and $V$ are independent, $f_{Z,V}(z,v) = f_Z(z) \cdot f_V(v)$:

$$f_{T,U}(t, u) = f_{Z,V}(z, v) \left|\frac{\partial(z,v)}{\partial(t,u)}\right|$$

$$= \frac{1}{\sqrt{2\pi}} e^{-z^2/2} \cdot \frac{(1/2)^{d/2}}{\Gamma(d/2)} v^{d/2-1} e^{-v/2} \cdot \sqrt{\frac{u}{d}}$$

Substituting $z = t\sqrt{u/d}$ and $v = u$:

$$= \frac{(1/2)(1/2 \cdot u)^{d/2-1}}{\sqrt{2\pi}\,\Gamma(d/2)} \, e^{-\frac{1+t^2/d}{2}u} \cdot \sqrt{\frac{u}{d}}$$

### Recognizing the Conditional Distribution

With $\lambda = \frac{1 + t^2/d}{2}$, the joint density factors as:

$$f_{T,U}(t, u) = \underbrace{\frac{1}{\sqrt{d}\, B(1/2, \, d/2)} \left(1 + \frac{t^2}{d}\right)^{-(d+1)/2}}_{f_T(t)} \cdot \underbrace{\frac{\lambda\, (\lambda u)^{(d+1)/2 - 1} e^{-\lambda u}}{\Gamma\!\left(\frac{d+1}{2}\right)}}_{f_{U|T=t}(u) \;=\; \Gamma\!\left(\frac{d+1}{2}, \, \lambda\right)}$$

### Marginal PDF of T

Integrating out $u$ (the Gamma density integrates to 1):

$$\boxed{f_T(t) = \frac{1}{\sqrt{d}\, B\!\left(\frac{1}{2}, \frac{d}{2}\right)} \left(1 + \frac{t^2}{d}\right)^{-(d+1)/2}, \quad -\infty < t < \infty}$$

where $B(a, b) = \frac{\Gamma(a)\Gamma(b)}{\Gamma(a+b)}$ is the Beta function.

## Python Verification

```python
import numpy as np
from scipy import stats, special
import matplotlib.pyplot as plt

d = 5
x = np.linspace(-5, 5, 500)

# Theoretical PDF
B = special.beta(0.5, d / 2)
pdf_formula = (1 + x**2 / d)**(-(d + 1) / 2) / (np.sqrt(d) * B)

# scipy PDF
pdf_scipy = stats.t.pdf(x, d)

print(f"Max difference: {np.max(np.abs(pdf_formula - pdf_scipy)):.2e}")

# Simulation verification
np.random.seed(42)
z = np.random.standard_normal(100_000)
v = np.random.chisquare(d, 100_000)
t_samples = z / np.sqrt(v / d)

fig, ax = plt.subplots(figsize=(8, 5))
ax.hist(t_samples, bins=100, density=True, alpha=0.5, label='Simulation')
ax.plot(x, pdf_scipy, 'r-', lw=2, label=f'$t_{{{d}}}$ PDF')
ax.set_xlabel('$t$')
ax.set_ylabel('Density')
ax.set_title(f"Student's $t$ Distribution ($d = {d}$)")
ax.legend()
plt.tight_layout()
plt.show()
```
