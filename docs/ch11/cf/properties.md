# Properties of Characteristic Functions


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

## Why Characteristic Functions?

The moment generating function $M_X(t) = E[e^{tX}]$ may not exist for all distributions (e.g., the Cauchy distribution has no MGF, and the log-normal has $M_X(t) = \infty$ for $t > 0$). The **characteristic function** always exists.

!!! info "Existence Guarantee"
    For **any** random variable $X$ (discrete, continuous, or mixed), the characteristic function $\varphi_X(t) = E[e^{itX}]$ exists for all $t \in \mathbb{R}$, because $|e^{itX}| = 1$.

## Basic Properties

!!! info "Properties of Characteristic Functions"
    For any random variable $X$ with CF $\varphi_X(t)$:

    1. $\varphi_X(0) = 1$
    2. $|\varphi_X(t)| \leq 1$ for all $t$
    3. $\varphi_X(-t) = \overline{\varphi_X(t)}$ (complex conjugate)
    4. $\varphi_X$ is **uniformly continuous** on $\mathbb{R}$
    5. If $Y = aX + b$, then $\varphi_Y(t) = e^{ibt}\,\varphi_X(at)$
    6. If $X$ and $Y$ are independent, then $\varphi_{X+Y}(t) = \varphi_X(t) \cdot \varphi_Y(t)$

Property (6) extends to $n$ independent random variables: $\varphi_{\sum X_i}(t) = \prod \varphi_{X_i}(t)$.

## Moments from the Characteristic Function

If $E[|X|^n] < \infty$, then $\varphi_X$ is $n$-times differentiable at $t = 0$ and:

$$E[X^n] = \frac{\varphi_X^{(n)}(0)}{i^n}$$

In particular:

$$E[X] = \frac{\varphi_X'(0)}{i}, \qquad E[X^2] = \frac{\varphi_X''(0)}{i^2} = -\varphi_X''(0)$$

## CFs of Common Distributions

| Distribution | CF $\varphi_X(t)$ |
|:---|:---:|
| $\text{Bernoulli}(p)$ | $1 - p + pe^{it}$ |
| $\text{Binomial}(n, p)$ | $(1 - p + pe^{it})^n$ |
| $\text{Poisson}(\lambda)$ | $\exp\!\left(\lambda(e^{it} - 1)\right)$ |
| $\text{Geometric}(p)$ | $\frac{pe^{it}}{1 - (1-p)e^{it}}$ |
| $N(\mu, \sigma^2)$ | $\exp\!\left(i\mu t - \frac{\sigma^2 t^2}{2}\right)$ |
| $\text{Exp}(\lambda)$ | $\frac{\lambda}{\lambda - it}$ |
| $\text{Gamma}(\alpha, \lambda)$ | $\left(\frac{\lambda}{\lambda - it}\right)^\alpha$ |
| $\text{Cauchy}(0,1)$ | $e^{-|t|}$ |
| $\text{Uniform}(a,b)$ | $\frac{e^{itb} - e^{ita}}{it(b-a)}$ |

## Uniqueness Theorem

!!! info "Uniqueness (Lévy)"
    Two random variables $X$ and $Y$ have the same distribution if and only if $\varphi_X(t) = \varphi_Y(t)$ for all $t \in \mathbb{R}$.

This is the characteristic function analogue of the MGF uniqueness theorem, but it is **stronger** because CFs always exist.

## Inversion Formula

The CF uniquely determines the distribution, and the relationship can be made explicit.

!!! info "Lévy Inversion Formula"
    If $X$ has CF $\varphi_X$ and CDF $F_X$, then at continuity points $a < b$ of $F_X$:

    $$F_X(b) - F_X(a) = \lim_{T \to \infty} \frac{1}{2\pi} \int_{-T}^{T} \frac{e^{-ita} - e^{-itb}}{it}\,\varphi_X(t)\,dt$$

For continuous distributions with $\varphi_X \in L^1(\mathbb{R})$ (i.e., $\int_{-\infty}^{\infty} |\varphi_X(t)|\,dt < \infty$), the PDF can be recovered directly:

$$f_X(x) = \frac{1}{2\pi} \int_{-\infty}^{\infty} e^{-itx}\,\varphi_X(t)\,dt$$

This is the **inverse Fourier transform** — the characteristic function is the Fourier transform of the density.

## Lévy Continuity Theorem

This theorem is the key tool for proving the Central Limit Theorem.

!!! info "Lévy Continuity Theorem"
    Let $X_1, X_2, \ldots$ be random variables with CFs $\varphi_{X_n}$.

    1. If $X_n \xrightarrow{d} X$, then $\varphi_{X_n}(t) \to \varphi_X(t)$ for all $t$.
    2. Conversely, if $\varphi_{X_n}(t) \to \varphi(t)$ for all $t$, where $\varphi$ is continuous at $t = 0$, then $\varphi$ is the CF of some random variable $X$, and $X_n \xrightarrow{d} X$.

**Significance.** To prove convergence in distribution, it suffices to show pointwise convergence of characteristic functions. This is often algebraically simpler than working with CDFs directly.

## CLT Proof Sketch via CFs

Let $X_1, X_2, \ldots$ be iid with $E[X_i] = 0$, $\text{Var}(X_i) = 1$. Let $Z_n = \frac{\sum_{i=1}^n X_i}{\sqrt{n}}$.

The CF of $Z_n$ is:

$$\varphi_{Z_n}(t) = \left[\varphi_X\!\left(\frac{t}{\sqrt{n}}\right)\right]^n$$

Taylor-expanding $\varphi_X(s)$ around $s = 0$:

$$\varphi_X(s) = 1 + is\,E[X] - \frac{s^2}{2}\,E[X^2] + o(s^2) = 1 - \frac{s^2}{2} + o(s^2)$$

Setting $s = t/\sqrt{n}$:

$$\varphi_{Z_n}(t) = \left[1 - \frac{t^2}{2n} + o(1/n)\right]^n \to e^{-t^2/2}$$

Since $e^{-t^2/2}$ is the CF of $N(0,1)$, by Lévy's continuity theorem, $Z_n \xrightarrow{d} N(0,1)$. $\square$

## Python Implementation

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

fig, axes = plt.subplots(1, 3, figsize=(16, 5))

t = np.linspace(-5, 5, 500)

# --- Panel 1: Real and imaginary parts of CFs ---
# N(0,1): φ(t) = exp(-t²/2)
cf_normal = np.exp(-t**2 / 2)

# Exp(1): φ(t) = 1/(1-it)
cf_exp_real = 1 / (1 + t**2)
cf_exp_imag = t / (1 + t**2)

# Cauchy: φ(t) = exp(-|t|)
cf_cauchy = np.exp(-np.abs(t))

axes[0].plot(t, cf_normal, 'b-', lw=2, label='N(0,1): real (imag=0)')
axes[0].plot(t, cf_exp_real, 'r-', lw=2, label='Exp(1): real part')
axes[0].plot(t, cf_exp_imag, 'r--', lw=1.5, label='Exp(1): imag part')
axes[0].plot(t, cf_cauchy, 'g-', lw=2, label='Cauchy: real (imag=0)')
axes[0].set_title('Characteristic Functions')
axes[0].set_xlabel('t')
axes[0].legend(fontsize=8)
axes[0].grid(True, alpha=0.3)

# --- Panel 2: Inversion - recovering PDF ---
x = np.linspace(-4, 4, 300)

# Numerical inversion for N(0,1)
dt = 0.01
t_grid = np.arange(-50, 50, dt)
f_recovered = np.zeros_like(x)
for i, xi in enumerate(x):
    integrand = np.exp(-1j * t_grid * xi) * np.exp(-t_grid**2 / 2)
    f_recovered[i] = np.real(np.sum(integrand) * dt / (2 * np.pi))

axes[1].plot(x, stats.norm.pdf(x), 'b-', lw=2, label='True N(0,1) PDF')
axes[1].plot(x, f_recovered, 'r--', lw=2, label='Recovered via inversion')
axes[1].set_title('PDF Recovery via Inversion Formula')
axes[1].set_xlabel('x')
axes[1].legend()
axes[1].grid(True, alpha=0.3)

# --- Panel 3: CLT via CFs ---
ns = [1, 2, 5, 20]
t_plot = np.linspace(-4, 4, 300)
colors = ['red', 'orange', 'green', 'blue']

# Exp(1) CF: 1/(1-it), standardized mean: φ((t/sqrt(n)))^n
for n, color in zip(ns, colors):
    cf_sum = (1 / (1 - 1j * t_plot / np.sqrt(n)))**n
    axes[2].plot(t_plot, np.abs(cf_sum), color=color, lw=2,
                 label=f'n={n}')

cf_target = np.exp(-t_plot**2 / 2)
axes[2].plot(t_plot, cf_target, 'k--', lw=2, label='N(0,1) CF')
axes[2].set_title('CF of Standardized Sum → N(0,1) CF')
axes[2].set_xlabel('t')
axes[2].set_ylabel('|φ(t)|')
axes[2].legend()
axes[2].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('characteristic_functions.png', dpi=150, bbox_inches='tight')
plt.show()
```
