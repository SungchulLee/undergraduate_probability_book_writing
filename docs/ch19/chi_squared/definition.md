# Chi-Squared Distribution: Definition as Sum of Squared Standard Normals


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

## Recall: Gamma Distribution

The chi-squared distribution is a special case of the Gamma distribution. Recall the key properties of $\Gamma(\alpha, \lambda)$:

1. $\text{Exp}(\lambda) \stackrel{d}{=} \Gamma(1, \lambda)$
2. $\text{Exp}(\lambda) * \text{Exp}(\lambda) \stackrel{d}{=} \Gamma(2, \lambda)$
3. $\underbrace{\text{Exp}(\lambda) * \cdots * \text{Exp}(\lambda)}_{n} \stackrel{d}{=} \Gamma(n, \lambda)$
4. $\Gamma(\alpha, \lambda) * \Gamma(\beta, \lambda) \stackrel{d}{=} \Gamma(\alpha + \beta, \lambda)$ (additivity)

where $*$ denotes convolution (distribution of a sum of independent random variables).

## Definition

If $Z_1, Z_2, \ldots, Z_d$ are **iid** $N(0, 1)$, then:

$$\sum_{i=1}^d Z_i^2 \sim \chi^2_d$$

The parameter $d$ is the **degrees of freedom**.

## Connection to Gamma

### Step 1: Chi-squared(1) = Z^2 ~ Gamma(1/2, 1/2)

For $x > 0$:

$$P(Z^2 \leq x) = P(-\sqrt{x} \leq Z \leq \sqrt{x}) = \int_{-\sqrt{x}}^{\sqrt{x}} \frac{1}{\sqrt{2\pi}} e^{-s^2/2}\, ds = 2\int_0^{\sqrt{x}} \frac{1}{\sqrt{2\pi}} e^{-s^2/2}\, ds$$

Differentiating with respect to $x$:

$$f_{Z^2}(x) = 2 \cdot \frac{1}{\sqrt{2\pi}} e^{-x/2} \cdot \frac{1}{2} x^{-1/2} = \frac{\frac{1}{2} \left(\frac{1}{2} x\right)^{1/2 - 1} e^{-x/2}}{\Gamma(1/2)} = f_{\Gamma(1/2, \, 1/2)}(x)$$

Therefore:

$$\chi^2_1 \stackrel{d}{=} Z^2 \stackrel{d}{=} \Gamma\!\left(\frac{1}{2}, \frac{1}{2}\right)$$

### Step 2: Chi-squared(d) ~ Gamma(d/2, 1/2)

By the additivity property of the Gamma distribution:

$$\chi^2_d \stackrel{d}{=} Z_1^2 + \cdots + Z_d^2 \stackrel{d}{=} \underbrace{\Gamma\!\left(\frac{1}{2}, \frac{1}{2}\right) * \cdots * \Gamma\!\left(\frac{1}{2}, \frac{1}{2}\right)}_{d} \stackrel{d}{=} \Gamma\!\left(\frac{d}{2}, \frac{1}{2}\right)$$

## PDF

From the Gamma PDF with $\alpha = d/2$ and $\lambda = 1/2$:

$$f_{\chi^2_d}(x) = \frac{(1/2)^{d/2}}{\Gamma(d/2)} x^{d/2 - 1} e^{-x/2}, \quad x > 0$$

## Python Verification

```python
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

x = np.linspace(0.01, 30, 500)

fig, ax = plt.subplots(figsize=(8, 5))
for d in [1, 2, 3, 5, 10, 15]:
    ax.plot(x, stats.chi2.pdf(x, d), label=f'$d = {d}$')

ax.set_xlabel('$x$')
ax.set_ylabel('$f(x)$')
ax.set_title('Chi-Squared PDF for Various Degrees of Freedom')
ax.legend()
ax.set_ylim(0, 0.5)
plt.tight_layout()
plt.show()
```
