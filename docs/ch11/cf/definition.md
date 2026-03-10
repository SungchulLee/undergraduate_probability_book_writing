# Characteristic Function Definition

The characteristic function replaces $t$ with $it$ in the MGF — it always exists and uniquely determines any distribution, even those without finite moments.

## Definition

The **characteristic function (CF)** of $X$ is

$$
\varphi_X(t) = E[e^{itX}] = E[\cos(tX)] + i\,E[\sin(tX)]
$$

for all $t \in \mathbb{R}$. The CF always exists because $|e^{itX}| = 1$.

If the MGF $M_X(t)$ exists, then $\varphi_X(t) = M_X(it)$.

## Explanation

### Existence Guarantee

Unlike the MGF, which may be infinite, $|e^{itx}| = |\cos(tx) + i\sin(tx)| = 1$, so $|E[e^{itX}]| \le 1$. The CF is finite and well-defined for **every** random variable.

### Relationship to Fourier Transform

For continuous $X$ with density $f$:

$$
\varphi_X(t) = \int_{-\infty}^{\infty}e^{itx}f(x)\,dx
$$

This is the **Fourier transform** of $f$. The density is recovered by the inverse transform:

$$
f(x) = \frac{1}{2\pi}\int_{-\infty}^{\infty}e^{-itx}\,\varphi_X(t)\,dt
$$

### Moments from the CF

If $E[|X|^n] < \infty$:

$$
E[X^n] = \frac{\varphi_X^{(n)}(0)}{i^n}
$$

## Examples

**Example.** $Z \sim N(0,1)$: $\varphi_Z(t) = e^{-t^2/2}$. The CF is real-valued and decays as a Gaussian — reflecting the symmetry and light tails of the normal distribution.

```python
import numpy as np

# Verify CF numerically for N(0,1)
np.random.seed(42)
n_sim = 500_000
Z = np.random.standard_normal(n_sim)

for t in [0.5, 1.0, 2.0]:
    cf_sim = np.mean(np.exp(1j * t * Z))
    cf_theory = np.exp(-t**2 / 2)
    print(f"t={t}: phi(t) = {cf_sim.real:.4f} + {cf_sim.imag:.4f}i  "
          f"(theory: {cf_theory:.4f})")
```
