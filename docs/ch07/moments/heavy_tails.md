# Heavy Tails and the Moment Problem

## Excess Kurtosis

The **excess kurtosis** is defined as $\gamma_2 = \kappa_4 - 3$, where $\kappa_4 = E[(X - \mu)^4] / \sigma^4$ is the (raw) kurtosis. The subtraction of 3 normalizes against the Normal distribution, which has $\kappa_4 = 3$.

!!! info "Interpretation of Excess Kurtosis"
    | $\gamma_2$ | Type | Tails | Examples |
    |:---:|:---:|:---:|:---:|
    | $\gamma_2 > 0$ | Leptokurtic | Heavier than Normal | $t$-distribution, Laplace |
    | $\gamma_2 = 0$ | Mesokurtic | Normal-like | Normal |
    | $\gamma_2 < 0$ | Platykurtic | Lighter than Normal | Uniform, Beta-symmetric |

**Common misconception:** Kurtosis is often described as measuring "peakedness," but it is more accurately a measure of **tail weight** — how much probability mass lies far from the center.

## Excess Kurtosis of Common Distributions

| Distribution | Excess Kurtosis $\gamma_2$ |
|:---|:---:|
| $\text{Uniform}(a, b)$ | $-6/5$ |
| $\text{Normal}$ | $0$ |
| $\text{Exponential}(\lambda)$ | $6$ |
| $\text{Laplace}(0, b)$ | $3$ |
| $t(\nu)$, $\nu > 4$ | $6/(\nu - 4)$ |
| $\text{Beta}(\alpha, \alpha)$ | $-6/(2\alpha + 3)$ |
| $\text{Bernoulli}(p)$ | $(1 - 6p(1-p))/(p(1-p))$ |

## The Moment Problem

!!! info "The Moment Problem"
    **Question:** Does the sequence of moments $\mu_k = E[X^k]$ for $k = 1, 2, 3, \ldots$ uniquely determine the distribution of $X$?

    **Answer:** Not always. A distribution is **moment-determinate** if its moments uniquely identify it, and **moment-indeterminate** otherwise.

**Sufficient conditions for uniqueness:**

1. **Carleman's condition.** If $\sum_{k=1}^{\infty} (E[|X|^{2k}])^{-1/(2k)} = \infty$, then the distribution is determined by its moments.
2. **MGF exists in a neighborhood of 0.** This implies Carleman's condition.

**The log-normal counterexample.** The Log-Normal distribution is the classic **moment-indeterminate** distribution. The family of densities:

$$f_a(x) = f_0(x)\left[1 + a\sin(2\pi\ln x)\right], \quad -1 \leq a \leq 1$$

where $f_0$ is the standard log-normal PDF, all share the **same moments** but are different distributions.

## Standardized Moments

The $k$-th **standardized moment** is:

$$\tilde{\mu}_k = E\!\left[\left(\frac{X - \mu}{\sigma}\right)^k\right]$$

- $\tilde{\mu}_1 = 0$, $\tilde{\mu}_2 = 1$, $\tilde{\mu}_3 = \gamma_1$ (skewness), $\tilde{\mu}_4 = \kappa_4$ (kurtosis)

For symmetric distributions, all odd standardized moments are zero.

## Python Implementation

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

fig, axes = plt.subplots(1, 3, figsize=(16, 5))

x = np.linspace(-6, 6, 1000)

# --- Panel 1: Kurtosis comparison ---
dists = [
    ('Uniform', stats.uniform(-np.sqrt(3), 2*np.sqrt(3)), -1.2),
    ('Normal', stats.norm(), 0),
    ('Laplace', stats.laplace(), 3),
    ('t(5)', stats.t(5), 6),
]
colors = ['green', 'blue', 'orange', 'red']

for (name, dist, kurt), color in zip(dists, colors):
    axes[0].plot(x, dist.pdf(x), color=color, lw=2,
                 label=f'{name} (γ₂={kurt})')

axes[0].set_title('Distributions with Different Kurtosis')
axes[0].set_xlabel('x')
axes[0].set_ylabel('f(x)')
axes[0].legend(fontsize=9)
axes[0].grid(True, alpha=0.3)

# --- Panel 2: Fourth power tail weighting ---
np.random.seed(42)
z = np.sort(np.abs(np.random.normal(0, 1, 10000)))
contrib = z**4
cum_frac = np.cumsum(contrib[::-1]) / contrib.sum()
pct = np.linspace(0, 100, len(z))

axes[1].plot(pct, cum_frac, 'b-', lw=2)
axes[1].axhline(0.5, color='red', ls='--', alpha=0.5)
axes[1].set_title('Cumulative 4th Moment from Largest |z|')
axes[1].set_xlabel('Top percentile of |z| values')
axes[1].set_ylabel('Fraction of total E[Z⁴]')
axes[1].grid(True, alpha=0.3)

# --- Panel 3: Log-normal moment indeterminacy ---
x_ln = np.linspace(0.01, 5, 500)
f0 = stats.lognorm.pdf(x_ln, s=1, scale=1)

for a in [-0.8, 0, 0.8]:
    f_a = f0 * (1 + a * np.sin(2 * np.pi * np.log(x_ln)))
    label = f'a={a}' if a != 0 else 'LogNormal (a=0)'
    axes[2].plot(x_ln, f_a, lw=2, label=label)

axes[2].set_title('Same Moments, Different Distributions')
axes[2].set_xlabel('x')
axes[2].set_ylabel('f(x)')
axes[2].legend()
axes[2].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('heavy_tails_moment_problem.png', dpi=150, bbox_inches='tight')
plt.show()
```
