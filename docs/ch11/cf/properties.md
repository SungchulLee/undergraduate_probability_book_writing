# Properties of Characteristic Functions

The CF inherits all useful properties of the MGF — uniqueness, product rule for sums, convergence characterization — while always existing.

## Definition

For any random variable $X$ with CF $\varphi_X(t)$:

| Property | Statement |
|:---------|:----------|
| Normalization | $\varphi_X(0) = 1$ |
| Boundedness | $|\varphi_X(t)| \le 1$ |
| Conjugate symmetry | $\varphi_X(-t) = \overline{\varphi_X(t)}$ |
| Scaling | $\varphi_{aX+b}(t) = e^{ibt}\,\varphi_X(at)$ |
| Independence | $\varphi_{X+Y}(t) = \varphi_X(t)\,\varphi_Y(t)$ |
| Uniqueness | $\varphi_X = \varphi_Y \Leftrightarrow X \stackrel{d}{=} Y$ |

## Explanation

### CFs of Common Distributions

| Distribution | $\varphi_X(t)$ |
|:-------------|:---------------|
| $\text{Bern}(p)$ | $q + pe^{it}$ |
| $\text{Bin}(n, p)$ | $(q + pe^{it})^n$ |
| $\text{Pois}(\lambda)$ | $e^{\lambda(e^{it}-1)}$ |
| $N(\mu, \sigma^2)$ | $e^{i\mu t - \sigma^2 t^2/2}$ |
| $\text{Exp}(\lambda)$ | $\lambda/(\lambda - it)$ |
| $\text{Cauchy}(0,1)$ | $e^{-|t|}$ |

### Levy Continuity Theorem

If $\varphi_{X_n}(t) \to \varphi(t)$ for all $t$ and $\varphi$ is continuous at 0, then $\varphi$ is a CF and $X_n \xrightarrow{d} X$ where $\varphi_X = \varphi$.

### CLT Proof Sketch

For iid $X_i$ with $E[X_i] = 0$, $\text{Var}(X_i) = 1$, and $Z_n = \sum X_i / \sqrt{n}$:

$$
\varphi_{Z_n}(t) = \left[\varphi_X(t/\sqrt{n})\right]^n
$$

Taylor expanding: $\varphi_X(s) = 1 - s^2/2 + o(s^2)$, so:

$$
\varphi_{Z_n}(t) = \left[1 - \frac{t^2}{2n} + o(1/n)\right]^n \to e^{-t^2/2}
$$

By Levy's theorem, $Z_n \xrightarrow{d} N(0,1)$.

## Examples

**Example.** Verify the Cauchy CF $\varphi(t) = e^{-|t|}$. The Cauchy has no MGF and no finite moments, but its CF is perfectly well-defined.

```python
import numpy as np

np.random.seed(42)
n_sim = 500_000

# Cauchy samples (heavy-tailed, no mean)
X = np.random.standard_cauchy(n_sim)

for t in [0.5, 1.0, 2.0]:
    cf_sim = np.mean(np.exp(1j * t * X))
    cf_theory = np.exp(-abs(t))
    print(f"t={t}: |phi| = {abs(cf_sim):.4f}  (theory: {cf_theory:.4f})")
```
