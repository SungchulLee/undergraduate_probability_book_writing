# Definition, Existence, and Relationship to MGF

## Definition

The **characteristic function (CF)** of a random variable $X$ is:

$$\varphi_X(t) = E[e^{itX}]$$

where $i = \sqrt{-1}$ and $t \in \mathbb{R}$. Using Euler's formula $e^{itX} = \cos(tX) + i\sin(tX)$:

$$\varphi_X(t) = E[\cos(tX)] + i\,E[\sin(tX)]$$

For continuous $X$ with PDF $f$:

$$\varphi_X(t) = \int_{-\infty}^{\infty} e^{itx}\,f(x)\,dx$$

This is precisely the **Fourier transform** of the density $f$.

## Existence

!!! info "Universal Existence"
    The characteristic function $\varphi_X(t) = E[e^{itX}]$ exists for **every** random variable $X$ and for **all** $t \in \mathbb{R}$.

**Proof.** Since $|e^{itX}| = |\cos(tX) + i\sin(tX)| = 1$, we have:

$$|\varphi_X(t)| = |E[e^{itX}]| \leq E[|e^{itX}|] = E[1] = 1$$

The expectation of a bounded random variable always exists. $\square$

This is the key advantage over the MGF. The MGF $M_X(t) = E[e^{tX}]$ involves $e^{tX}$, which can be unbounded, causing the expectation to diverge. The CF replaces $t$ with $it$, converting exponential growth into bounded oscillation.

## Relationship to the MGF

When the MGF $M_X(t)$ exists in a neighborhood of $0$, the CF is obtained by the formal substitution $t \mapsto it$:

$$\varphi_X(t) = M_X(it)$$

Conversely, $M_X(t) = \varphi_X(-it)$ when the MGF exists.

???+ example "Normal distribution"
    For $X \sim N(\mu, \sigma^2)$, the MGF is $M_X(t) = e^{\mu t + \frac{1}{2}\sigma^2 t^2}$.

    Substituting $t \mapsto it$:

    $$\varphi_X(t) = e^{\mu(it) + \frac{1}{2}\sigma^2(it)^2} = e^{i\mu t - \frac{1}{2}\sigma^2 t^2}$$

???+ example "Exponential distribution"
    For $X \sim \text{Exp}(\lambda)$, the MGF is $M_X(t) = \frac{\lambda}{\lambda - t}$ for $t < \lambda$.

    Substituting $t \mapsto it$:

    $$\varphi_X(t) = \frac{\lambda}{\lambda - it}$$

    The CF is defined for all $t \in \mathbb{R}$, even though the MGF only exists for $t < \lambda$.

## When the MGF Does Not Exist

Some distributions have no MGF but always have a CF.

???+ example "Cauchy distribution"
    The standard Cauchy has PDF $f(x) = \frac{1}{\pi(1+x^2)}$. Its MGF does not exist ($E[e^{tX}] = \infty$ for $t \neq 0$), but its CF is:

    $$\varphi_X(t) = e^{-|t|}$$

    The CF is well-defined, smooth, and encodes the full distribution.

## Why CFs Matter

The characteristic function serves three main roles in probability theory:

1. **Universality.** It exists for every distribution, making it the default tool when the MGF is unavailable.

2. **Uniqueness.** Two random variables have the same distribution if and only if they have the same CF. The density can be recovered via the inversion formula (see the properties page).

3. **Proving limit theorems.** The Levy continuity theorem states that $X_n \xrightarrow{d} X$ if and only if $\varphi_{X_n}(t) \to \varphi_X(t)$ for all $t$. This is the cleanest route to the Central Limit Theorem.

## Comparison of Transform Methods

| Property | MGF $M_X(t)$ | PGF $G_X(s)$ | CF $\varphi_X(t)$ |
|:---|:---:|:---:|:---:|
| Definition | $E[e^{tX}]$ | $E[s^X]$ | $E[e^{itX}]$ |
| Exists for all RVs? | No | Only $X \in \{0,1,2,\ldots\}$ | **Yes** |
| Determines distribution? | Yes (when exists) | Yes (for its domain) | **Yes (always)** |
| Real-valued? | Yes | Yes | **Complex** |
| Moment extraction | $M^{(n)}(0)$ | Factorial moments | $\varphi^{(n)}(0)/i^n$ |
| Product rule (indep.) | Yes | Yes | Yes |

## Python Verification

```python
import numpy as np
from scipy import stats

# Verify CF of N(2, 9) at t = 1
mu, sigma2 = 2, 9
t = 1.0

# Exact CF
cf_exact = np.exp(1j * mu * t - 0.5 * sigma2 * t**2)

# Monte Carlo estimate
np.random.seed(42)
X = np.random.normal(mu, np.sqrt(sigma2), 200000)
cf_mc = np.mean(np.exp(1j * t * X))

print("CF of N(2, 9) at t=1:")
print(f"  Exact: {cf_exact:.6f}")
print(f"  MC:    {cf_mc:.6f}")

# Verify Cauchy CF: exp(-|t|)
t_vals = [0.5, 1.0, 2.0]
X_cauchy = np.random.standard_cauchy(500000)
print("\nCauchy CF (no MGF exists):")
for t in t_vals:
    cf_exact = np.exp(-abs(t))
    cf_mc = np.mean(np.exp(1j * t * X_cauchy))
    print(f"  t={t}: exact={cf_exact:.4f}, MC real={cf_mc.real:.4f}")
```
