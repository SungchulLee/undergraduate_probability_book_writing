# Weak Law of Large Numbers — Examples and Extensions

## Review of the Statement

!!! info "Weak Law of Large Numbers (WLLN)"
    Let $X_1, X_2, \ldots$ be iid with $E[X_i] = \mu$ and $\text{Var}(X_i) = \sigma^2 < \infty$. Then for all $\varepsilon > 0$:

    $$P\!\left(\left|\bar{X}_n - \mu\right| \geq \varepsilon\right) \to 0 \quad \text{as } n \to \infty$$

    Equivalently, $\bar{X}_n \xrightarrow{p} \mu$.

The standard proof uses Chebyshev's inequality (see Section 20.3, Statement and Proof).

## Alternative Proof: Truncation (Without Finite Variance)

The WLLN holds even **without the finite variance assumption** — only $E[|X|] < \infty$ is needed.

!!! info "WLLN (Finite Mean Only)"
    If $X_1, X_2, \ldots$ are iid with $E[X_i] = \mu$ (no variance assumption), then $\bar{X}_n \xrightarrow{p} \mu$.

**Proof sketch (truncation method).** Define $Y_i = X_i \cdot \mathbf{1}(|X_i| \leq n)$ (truncated version). Then:

1. $E[Y_i] \to \mu$ as $n \to \infty$ (dominated convergence)
2. $\text{Var}(Y_i) \leq E[Y_i^2] \leq n \cdot E[|X|]$ (since $|Y_i| \leq n$)
3. Apply Chebyshev to $\bar{Y}_n$: $P(|\bar{Y}_n - E[Y_1]| > \varepsilon/2) \leq \frac{n E[|X|]}{n^2 (\varepsilon/2)^2} \to 0$
4. $P(\bar{X}_n \neq \bar{Y}_n) \leq \sum P(|X_i| > n) = n P(|X_1| > n) \to 0$

Combining steps 3 and 4 gives $P(|\bar{X}_n - \mu| > \varepsilon) \to 0$. $\square$

## Example: Sample Mean of Exponentials

Let $X_i \sim \text{Exp}(\lambda)$ with $\mu = 1/\lambda$. The WLLN says $\bar{X}_n \to 1/\lambda$ in probability.

The rate of convergence can be quantified via Chebyshev:

$$P\!\left(\left|\bar{X}_n - \frac{1}{\lambda}\right| \geq \varepsilon\right) \leq \frac{\text{Var}(\bar{X}_n)}{\varepsilon^2} = \frac{1}{n\lambda^2\varepsilon^2}$$

For example, with $\lambda = 1$ and $\varepsilon = 0.1$: the bound is $\frac{100}{n}$, so $n \geq 10000$ guarantees this probability is at most 1%.

## Example: Estimating $\pi$

Consider the **Monte Carlo estimation** of $\pi$. Generate $(U_i, V_i) \sim \text{Uniform}([0,1]^2)$ iid and let $X_i = \mathbf{1}(U_i^2 + V_i^2 \leq 1)$. Then $\mu = E[X_i] = \pi/4$ and:

$$\hat{\pi}_n = 4\bar{X}_n \xrightarrow{p} \pi$$

## Convergence Rate: Chebyshev vs CLT

Chebyshev gives a **polynomial** bound: $P(|\bar{X}_n - \mu| \geq \varepsilon) \leq \frac{\sigma^2}{n\varepsilon^2}$.

The CLT gives a **sharper asymptotic** characterization:

$$P\!\left(\left|\bar{X}_n - \mu\right| \geq \varepsilon\right) \approx 2\left(1 - \Phi\!\left(\frac{\varepsilon\sqrt{n}}{\sigma}\right)\right)$$

which decays **exponentially** in $n$, much faster than Chebyshev's polynomial bound.

## When WLLN Fails

!!! warning "No WLLN Without Finite Mean"
    If $E[|X|] = \infty$, the WLLN may fail. The standard example is the **Cauchy distribution**.

If $X_1, X_2, \ldots$ are iid $\text{Cauchy}(0, 1)$, then $\bar{X}_n$ has the **same** Cauchy(0,1) distribution for every $n$. The sample mean does not converge to any value.

## Python Implementation

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

fig, axes = plt.subplots(1, 3, figsize=(16, 5))
np.random.seed(42)

# --- Panel 1: WLLN convergence for different distributions ---
n_max = 5000
ns = np.arange(1, n_max + 1)

# Exponential
exp_samples = np.random.exponential(1, n_max)
exp_means = np.cumsum(exp_samples) / ns

# Bernoulli
bern_samples = np.random.binomial(1, 0.3, n_max)
bern_means = np.cumsum(bern_samples) / ns

# Uniform
unif_samples = np.random.uniform(0, 1, n_max)
unif_means = np.cumsum(unif_samples) / ns

axes[0].plot(ns, exp_means, alpha=0.7, lw=0.8, label='Exp(1), μ=1')
axes[0].plot(ns, bern_means, alpha=0.7, lw=0.8, label='Bern(0.3), μ=0.3')
axes[0].plot(ns, unif_means, alpha=0.7, lw=0.8, label='U(0,1), μ=0.5')
axes[0].axhline(1, color='blue', ls='--', alpha=0.3)
axes[0].axhline(0.3, color='orange', ls='--', alpha=0.3)
axes[0].axhline(0.5, color='green', ls='--', alpha=0.3)
axes[0].set_title('WLLN: Sample Mean Convergence')
axes[0].set_xlabel('n')
axes[0].set_ylabel('$\\bar{X}_n$')
axes[0].legend()
axes[0].grid(True, alpha=0.3)

# --- Panel 2: Chebyshev bound vs actual probability ---
sigma = 1.0  # Exp(1)
mu = 1.0
eps_values = [0.1, 0.2, 0.5]
n_range = np.arange(10, 2001, 10)
n_sim = 10000

for eps in eps_values:
    chebyshev_bound = sigma**2 / (n_range * eps**2)
    chebyshev_bound = np.minimum(chebyshev_bound, 1)

    actual_probs = []
    for n in n_range:
        samples = np.random.exponential(1, (n_sim, n))
        means = samples.mean(axis=1)
        actual_probs.append(np.mean(np.abs(means - mu) >= eps))

    axes[1].plot(n_range, chebyshev_bound, '--', lw=2,
                 label=f'Chebyshev ε={eps}')
    axes[1].plot(n_range, actual_probs, '-', lw=1, alpha=0.7,
                 label=f'Actual ε={eps}')

axes[1].set_title('Chebyshev Bound vs Actual P(|X̄-μ|≥ε)')
axes[1].set_xlabel('n')
axes[1].set_ylabel('Probability')
axes[1].set_yscale('log')
axes[1].legend(fontsize=7, ncol=2)
axes[1].grid(True, alpha=0.3)

# --- Panel 3: Cauchy — WLLN fails ---
cauchy_samples = np.random.standard_cauchy(n_max)
cauchy_means = np.cumsum(cauchy_samples) / ns

normal_samples = np.random.normal(0, 1, n_max)
normal_means = np.cumsum(normal_samples) / ns

axes[2].plot(ns, cauchy_means, alpha=0.7, lw=0.8, color='red',
             label='Cauchy (no convergence)')
axes[2].plot(ns, normal_means, alpha=0.7, lw=0.8, color='blue',
             label='N(0,1) → 0')
axes[2].axhline(0, color='black', ls='--', alpha=0.3)
axes[2].set_title('WLLN Fails for Cauchy')
axes[2].set_xlabel('n')
axes[2].set_ylabel('$\\bar{X}_n$')
axes[2].set_ylim(-5, 5)
axes[2].legend()
axes[2].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('wlln_examples.png', dpi=150, bbox_inches='tight')
plt.show()
```
