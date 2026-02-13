# Bayesian Applications of the Beta Distribution

## Beta as a Distribution on Probabilities

The Beta distribution is defined on $(0, 1)$, making it a natural model for **probabilities**, **proportions**, and **rates**. In Bayesian inference, we treat an unknown probability $p$ as a random variable and assign it a Beta prior.

## Example: Quality Control

A factory produces items that are either defective or non-defective. The true defect rate $p$ is unknown.

**Setup:**

- **Prior belief:** Before observing any data, we believe $p$ is around 5% but are not very certain. We choose $p \sim \text{Beta}(2, 38)$, which has mean $\frac{2}{40} = 0.05$ and is moderately concentrated.
- **Data:** We inspect $n = 100$ items and find $k = 8$ defectives.
- **Posterior:** $p \mid X = 8 \sim \text{Beta}(2 + 8, 38 + 92) = \text{Beta}(10, 130)$

The posterior mean is $\frac{10}{140} \approx 0.071$, which lies between the prior mean (0.05) and the MLE ($\frac{8}{100} = 0.08$).

## Example: A/B Testing

An online platform tests two versions of a webpage. For version A:

- **Prior:** $p_A \sim \text{Beta}(1, 1) = \text{Uniform}(0, 1)$ (non-informative)
- **Data:** 50 out of 200 visitors convert
- **Posterior:** $p_A \mid \text{data} \sim \text{Beta}(51, 151)$

For version B:

- **Prior:** $p_B \sim \text{Beta}(1, 1)$
- **Data:** 65 out of 200 visitors convert
- **Posterior:** $p_B \mid \text{data} \sim \text{Beta}(66, 136)$

The probability that B is better than A can be estimated by simulation:

$$P(p_B > p_A \mid \text{data}) \approx \frac{1}{N}\sum_{i=1}^{N} \mathbf{1}(p_B^{(i)} > p_A^{(i)})$$

where $p_A^{(i)}$ and $p_B^{(i)}$ are independent draws from the respective posteriors.

## Credible Intervals

A **credible interval** is the Bayesian analogue of a confidence interval. The **highest posterior density (HPD)** interval is the shortest interval containing a given probability mass.

For the Beta distribution, the **equal-tailed credible interval** at level $1 - \alpha$ is:

$$\left[F^{-1}\!\left(\frac{\alpha}{2}\right),\; F^{-1}\!\left(1 - \frac{\alpha}{2}\right)\right]$$

where $F^{-1}$ is the Beta quantile function.

## Sequential Updating

A key advantage of the Beta-Binomial conjugate model is that data can be incorporated **sequentially**. Processing observations one at a time or in batches yields the same posterior.

!!! info "Sequential Updating"
    Starting from $\text{Beta}(\alpha_0, \beta_0)$:

    - After observing a success: $\text{Beta}(\alpha_0 + 1, \beta_0)$
    - After observing a failure: $\text{Beta}(\alpha_0, \beta_0 + 1)$

    After $k$ successes and $n - k$ failures (in any order):

    $$\text{Beta}(\alpha_0 + k,\; \beta_0 + n - k)$$

The order of observations does not matter — only the total counts.

## Predictive Distribution

After observing $k$ successes in $n$ trials with prior $\text{Beta}(\alpha, \beta)$, the **posterior predictive probability** of success on the next trial is:

$$P(X_{n+1} = 1 \mid \text{data}) = E[p \mid \text{data}] = \frac{\alpha + k}{\alpha + \beta + n}$$

When $\alpha = \beta = 1$ (uniform prior), this gives **Laplace's rule of succession**:

$$P(X_{n+1} = 1 \mid k \text{ successes in } n) = \frac{k + 1}{n + 2}$$

## Python Implementation

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

fig, axes = plt.subplots(1, 3, figsize=(18, 5))

# --- Panel 1: Sequential Bayesian updating ---
x = np.linspace(0, 1, 500)
alpha0, beta0 = 1, 1
np.random.seed(42)
true_p = 0.35
observations = np.random.binomial(1, true_p, 20)

steps = [0, 1, 3, 5, 10, 20]
colors = plt.cm.viridis(np.linspace(0, 0.9, len(steps)))

for i, n in enumerate(steps):
    k = observations[:n].sum()
    a, b = alpha0 + k, beta0 + n - k
    axes[0].plot(x, stats.beta.pdf(x, a, b), color=colors[i], lw=2,
                 label=f'n={n}, k={k}: Beta({a},{b})')

axes[0].axvline(true_p, color='red', ls='--', lw=1.5, label=f'True p={true_p}')
axes[0].set_title('Sequential Bayesian Updating')
axes[0].set_xlabel('p')
axes[0].set_ylabel('Density')
axes[0].legend(fontsize=8)
axes[0].grid(True, alpha=0.3)

# --- Panel 2: A/B Testing ---
n_sim = 100000
pA = np.random.beta(51, 151, n_sim)
pB = np.random.beta(66, 136, n_sim)

axes[1].hist(pA, bins=80, density=True, alpha=0.5, color='blue', label='Version A')
axes[1].hist(pB, bins=80, density=True, alpha=0.5, color='red', label='Version B')
prob_b_better = np.mean(pB > pA)
axes[1].set_title(f'A/B Test: P(B > A) = {prob_b_better:.3f}')
axes[1].set_xlabel('Conversion rate p')
axes[1].legend()
axes[1].grid(True, alpha=0.3)

# --- Panel 3: Credible interval shrinkage ---
sample_sizes = np.arange(1, 201)
ci_widths = []
alpha_p, beta_p = 1, 1
true_rate = 0.3

for n in sample_sizes:
    k = int(n * true_rate)
    a, b = alpha_p + k, beta_p + n - k
    lo = stats.beta.ppf(0.025, a, b)
    hi = stats.beta.ppf(0.975, a, b)
    ci_widths.append(hi - lo)

axes[2].plot(sample_sizes, ci_widths, 'b-', lw=2)
axes[2].set_title('95% Credible Interval Width vs Sample Size')
axes[2].set_xlabel('Number of observations')
axes[2].set_ylabel('CI Width')
axes[2].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('beta_bayesian_applications.png', dpi=150, bbox_inches='tight')
plt.show()
```
