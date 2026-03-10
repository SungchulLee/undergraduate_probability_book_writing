# Beta Distribution Properties


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

## Special Cases

The Beta distribution encompasses several familiar distributions as special cases.

!!! info "Special Cases of Beta(α, β)"
    | Parameters | Distribution | PDF |
    |:---:|:---:|:---:|
    | $\alpha = 1, \beta = 1$ | $\text{Uniform}(0,1)$ | $f(x) = 1$ |
    | $\alpha = n, \beta = 1$ | Power distribution | $f(x) = nx^{n-1}$ |
    | $\alpha = 1, \beta = n$ | Reflected power | $f(x) = n(1-x)^{n-1}$ |
    | $\alpha = \tfrac{1}{2}, \beta = \tfrac{1}{2}$ | Arcsine distribution | $f(x) = \frac{1}{\pi\sqrt{x(1-x)}}$ |

The $\text{Beta}(1,1) = \text{Uniform}(0,1)$ case is immediate: when $\alpha = \beta = 1$, the PDF is $f(x) = \frac{x^0(1-x)^0}{B(1,1)} = \frac{1}{1} = 1$.

## Shape Analysis

The shape of the Beta PDF depends on the parameter values relative to 1.

**Mode.** For $\alpha, \beta > 1$, the Beta distribution is unimodal with mode:

$$\text{Mode} = \frac{\alpha - 1}{\alpha + \beta - 2}$$

This follows from setting $f'(x) = 0$, yielding $(\alpha - 1)(1 - x) = (\beta - 1)x$.

**Shape regimes:**

- $\alpha > 1, \beta > 1$: unimodal, bell-shaped on $(0, 1)$
- $\alpha < 1, \beta < 1$: U-shaped (bimodal at boundaries)
- $\alpha = \beta$: symmetric about $x = 1/2$
- $\alpha > \beta$: skewed left (mass concentrated toward 1)
- $\alpha < \beta$: skewed right (mass concentrated toward 0)

## Higher Moments

!!! info "Raw Moments"
    For $X \sim \text{Beta}(\alpha, \beta)$:

    $$E[X^k] = \frac{B(\alpha + k, \beta)}{B(\alpha, \beta)} = \prod_{j=0}^{k-1} \frac{\alpha + j}{\alpha + \beta + j}$$

In particular:

$$E[X] = \frac{\alpha}{\alpha + \beta}, \qquad E[X^2] = \frac{\alpha(\alpha+1)}{(\alpha+\beta)(\alpha+\beta+1)}$$

**Skewness:**

$$\gamma_1 = \frac{2(\beta - \alpha)\sqrt{\alpha + \beta + 1}}{(\alpha + \beta + 2)\sqrt{\alpha\beta}}$$

When $\alpha = \beta$, the skewness is zero (the distribution is symmetric).

**Kurtosis (excess):**

$$\gamma_2 = \frac{6(\alpha^3 - \alpha^2(2\beta - 1) + \beta^2(\beta + 1) - 2\alpha\beta(\beta + 2))}{\alpha\beta(\alpha + \beta + 2)(\alpha + \beta + 3)}$$

## Bayesian Conjugacy

The Beta distribution is the **conjugate prior** for the Binomial likelihood. This means that if we start with a Beta prior and observe Binomial data, the posterior is also Beta.

!!! info "Beta-Binomial Conjugacy"
    **Prior:** $p \sim \text{Beta}(\alpha, \beta)$

    **Likelihood:** $X \mid p \sim \text{Binomial}(n, p)$

    **Posterior:** $p \mid X = k \sim \text{Beta}(\alpha + k, \beta + n - k)$

**Derivation.** By Bayes' theorem:

$$f(p \mid X = k) \propto f(k \mid p) \cdot f(p) \propto p^k(1-p)^{n-k} \cdot p^{\alpha - 1}(1-p)^{\beta - 1} = p^{\alpha + k - 1}(1-p)^{\beta + n - k - 1}$$

This is the kernel of a $\text{Beta}(\alpha + k, \beta + n - k)$ density.

**Interpretation:**

- $\alpha$ acts as "prior successes" and $\beta$ as "prior failures"
- $\alpha + \beta$ controls how informative the prior is
- The posterior mean is a weighted average of the prior mean and the data:

$$E[p \mid X = k] = \frac{\alpha + k}{\alpha + \beta + n} = \frac{\alpha + \beta}{\alpha + \beta + n} \cdot \underbrace{\frac{\alpha}{\alpha + \beta}}_{\text{prior mean}} + \frac{n}{\alpha + \beta + n} \cdot \underbrace{\frac{k}{n}}_{\text{MLE}}$$

## Symmetry and Reflection

!!! info "Reflection Property"
    If $X \sim \text{Beta}(\alpha, \beta)$, then $1 - X \sim \text{Beta}(\beta, \alpha)$.

**Proof.** Let $Y = 1 - X$. For $0 < y < 1$:

$$P(Y \leq y) = P(X \geq 1 - y) = \int_{1-y}^{1} \frac{x^{\alpha-1}(1-x)^{\beta-1}}{B(\alpha,\beta)}\,dx$$

Substituting $u = 1 - x$:

$$= \int_0^{y} \frac{(1-u)^{\alpha-1}u^{\beta-1}}{B(\alpha,\beta)}\,du$$

which is the CDF of $\text{Beta}(\beta, \alpha)$. $\square$

## Connection to Order Statistics

The Beta distribution arises naturally as the distribution of order statistics from the Uniform distribution.

!!! info "Order Statistic Connection"
    If $U_1, U_2, \ldots, U_n \overset{\text{iid}}{\sim} \text{Uniform}(0,1)$ and $U_{(k)}$ is the $k$-th smallest value, then:

    $$U_{(k)} \sim \text{Beta}(k, n - k + 1)$$

This is proven in detail in Section 15.5 (Order Statistics).

## Python Implementation

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

fig, axes = plt.subplots(1, 3, figsize=(18, 5))

# --- Panel 1: Shape regimes ---
x = np.linspace(0.001, 0.999, 500)
cases = [
    ((0.5, 0.5), 'U-shaped', 'red'),
    ((1, 1), 'Uniform', 'black'),
    ((2, 5), 'Right-skewed', 'blue'),
    ((5, 2), 'Left-skewed', 'green'),
    ((5, 5), 'Symmetric bell', 'purple'),
    ((10, 10), 'Concentrated', 'orange'),
]
for (a, b), label, color in cases:
    pdf = stats.beta.pdf(x, a, b)
    pdf = np.clip(pdf, 0, 8)
    axes[0].plot(x, pdf, color=color, lw=2, label=f'({a},{b}) {label}')
axes[0].set_title('Beta PDF Shape Regimes')
axes[0].set_xlabel('x')
axes[0].set_ylabel('f(x)')
axes[0].set_ylim(0, 5)
axes[0].legend(fontsize=8)
axes[0].grid(True, alpha=0.3)

# --- Panel 2: Bayesian updating ---
alpha_prior, beta_prior = 2, 2
n_obs, k_obs = 10, 7

alpha_post = alpha_prior + k_obs
beta_post = beta_prior + n_obs - k_obs

axes[1].plot(x, stats.beta.pdf(x, alpha_prior, beta_prior),
             'b-', lw=2, label=f'Prior: Beta({alpha_prior},{beta_prior})')
axes[1].plot(x, stats.beta.pdf(x, alpha_post, beta_post),
             'r-', lw=2, label=f'Posterior: Beta({alpha_post},{beta_post})')
axes[1].axvline(k_obs / n_obs, color='green', ls='--', lw=1.5,
                label=f'MLE = {k_obs}/{n_obs}')
axes[1].set_title(f'Bayesian Updating (observed {k_obs}/{n_obs})')
axes[1].set_xlabel('p')
axes[1].legend()
axes[1].grid(True, alpha=0.3)

# --- Panel 3: Order statistics ---
np.random.seed(42)
n, k = 10, 3
n_sim = 100000
samples = np.sort(np.random.uniform(size=(n_sim, n)), axis=1)
order_stat = samples[:, k - 1]

axes[2].hist(order_stat, bins=60, density=True, alpha=0.5,
             color='steelblue', label=f'$U_{{({k})}}$ simulated')
theory = stats.beta.pdf(x, k, n - k + 1)
axes[2].plot(x, theory, 'r-', lw=2,
             label=f'Beta({k},{n-k+1}) PDF')
axes[2].set_title(f'Order Statistic $U_{{({k})}}$ from Uniform(0,1), n={n}')
axes[2].set_xlabel('x')
axes[2].legend()
axes[2].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('beta_properties.png', dpi=150, bbox_inches='tight')
plt.show()
```
