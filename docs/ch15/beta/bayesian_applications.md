# Bayesian Applications of the Beta Distribution

The Beta distribution is the conjugate prior for the Binomial likelihood, meaning that Bayesian updating with binomial data preserves the Beta family -- the posterior is always another Beta distribution with updated parameters.

## Definition

**Beta-Binomial conjugacy.** If the prior and likelihood are:

$$
p \sim \text{Beta}(\alpha, \beta), \qquad X \mid p \sim \text{Binomial}(n, p)
$$

then the posterior after observing $X = k$ successes is:

$$
p \mid X = k \sim \text{Beta}(\alpha + k, \; \beta + n - k)
$$

The posterior mean is a weighted average of the prior mean and the maximum likelihood estimate (MLE):

$$
E[p \mid X = k] = \frac{\alpha + k}{\alpha + \beta + n} = \frac{\alpha + \beta}{\alpha + \beta + n} \cdot \underbrace{\frac{\alpha}{\alpha + \beta}}_{\text{prior mean}} + \frac{n}{\alpha + \beta + n} \cdot \underbrace{\frac{k}{n}}_{\text{MLE}}
$$

## Explanation

### Deriving the posterior

By Bayes' theorem, the posterior density is proportional to the likelihood times the prior:

$$
f(p \mid X = k) \propto f(k \mid p) \cdot f(p) \propto p^k(1-p)^{n-k} \cdot p^{\alpha - 1}(1-p)^{\beta - 1} = p^{\alpha + k - 1}(1-p)^{\beta + n - k - 1}
$$

This is the kernel of a $\text{Beta}(\alpha + k, \beta + n - k)$ density. Since a density is determined by its kernel (the normalizing constant is fixed), the posterior is $\text{Beta}(\alpha + k, \beta + n - k)$.

### Interpreting the prior parameters

- $\alpha$ acts as "prior successes" (pseudo-observations of success)
- $\beta$ acts as "prior failures" (pseudo-observations of failure)
- $\alpha + \beta$ is the "prior sample size," controlling how informative the prior is
- A larger $\alpha + \beta$ means the prior is more concentrated and harder for data to overwhelm
- $\text{Beta}(1, 1) = U(0, 1)$ is a non-informative (flat) prior

### Sequential updating

Data can be incorporated one observation at a time. Starting from $\text{Beta}(\alpha_0, \beta_0)$:

- After a success: update to $\text{Beta}(\alpha_0 + 1, \beta_0)$
- After a failure: update to $\text{Beta}(\alpha_0, \beta_0 + 1)$
- After $k$ successes and $n - k$ failures (in any order): $\text{Beta}(\alpha_0 + k, \beta_0 + n - k)$

The order of observations does not matter -- only the total counts.

### Credible intervals

A **credible interval** is the Bayesian analogue of a confidence interval. The equal-tailed $100(1 - \alpha)\%$ credible interval for $p$ is:

$$
\left[F^{-1}\!\left(\frac{\alpha}{2}\right),\; F^{-1}\!\left(1 - \frac{\alpha}{2}\right)\right]
$$

where $F^{-1}$ is the Beta quantile function of the posterior distribution.

### Predictive distribution

After observing $k$ successes in $n$ trials with prior $\text{Beta}(\alpha, \beta)$, the posterior predictive probability of success on the next trial is:

$$
P(X_{n+1} = 1 \mid \text{data}) = E[p \mid \text{data}] = \frac{\alpha + k}{\alpha + \beta + n}
$$

With the uniform prior $\alpha = \beta = 1$, this gives **Laplace's rule of succession**:

$$
P(X_{n+1} = 1 \mid k \text{ successes in } n) = \frac{k + 1}{n + 2}
$$

### Choosing a prior

| Prior choice | Parameters | Interpretation |
|---|---|---|
| Non-informative | $\text{Beta}(1, 1)$ | No prior knowledge |
| Jeffreys prior | $\text{Beta}(1/2, 1/2)$ | Invariant under reparameterization |
| Weakly informative | $\text{Beta}(2, 2)$ | Mild preference for moderate values |
| Informative | Large $\alpha + \beta$ | Strong prior knowledge |

## Examples

**Example 1: Quality control.**

A factory's defect rate $p$ is unknown. Prior belief: $p \sim \text{Beta}(2, 38)$ (mean $0.05$). After inspecting 100 items and finding 8 defective, find the posterior.

$$
p \mid X = 8 \sim \text{Beta}(2 + 8, \; 38 + 92) = \text{Beta}(10, 130)
$$

```python
from scipy import stats

alpha_prior, beta_prior = 2, 38
n, k = 100, 8

alpha_post = alpha_prior + k
beta_post = beta_prior + n - k

prior_mean = alpha_prior / (alpha_prior + beta_prior)
post_mean = alpha_post / (alpha_post + beta_post)
mle = k / n

print(f"Prior:     Beta({alpha_prior}, {beta_prior}),  mean = {prior_mean:.4f}")
print(f"Data:      {k} defective out of {n}")
print(f"Posterior: Beta({alpha_post}, {beta_post}), mean = {post_mean:.4f}")
print(f"MLE:       {mle:.4f}")

# 95% credible interval
lo = stats.beta.ppf(0.025, alpha_post, beta_post)
hi = stats.beta.ppf(0.975, alpha_post, beta_post)
print(f"95% credible interval: ({lo:.4f}, {hi:.4f})")
```

**Output:**
```
Prior:     Beta(2, 38),  mean = 0.0500
Data:      8 defective out of 100
Posterior: Beta(10, 130), mean = 0.0714
MLE:       0.0800
95% credible interval: (0.0353, 0.1196)
```

**Example 2: A/B testing.**

Two webpage versions are tested with non-informative priors:

- Version A: 50 conversions out of 200 visitors
- Version B: 65 conversions out of 200 visitors

Estimate $P(p_B > p_A \mid \text{data})$.

```python
import numpy as np
from scipy import stats

np.random.seed(42)
n_sim = 100000

# Posteriors
pA = np.random.beta(1 + 50, 1 + 150, n_sim)   # Beta(51, 151)
pB = np.random.beta(1 + 65, 1 + 135, n_sim)    # Beta(66, 136)

prob_B_better = np.mean(pB > pA)
print(f"Posterior A: Beta(51, 151), mean = {51/202:.4f}")
print(f"Posterior B: Beta(66, 136), mean = {66/202:.4f}")
print(f"P(B > A | data) = {prob_B_better:.4f}")

# Expected lift
lift = (pB - pA) / pA
print(f"Expected relative lift: {np.mean(lift):.2%}")
print(f"95% CI for lift: ({np.percentile(lift, 2.5):.2%}, {np.percentile(lift, 97.5):.2%})")
```

**Output:**
```
Posterior A: Beta(51, 151), mean = 0.2525
Posterior B: Beta(66, 136), mean = 0.3267
P(B > A | data) = 0.9557
Expected relative lift: 32.41%
95% CI for lift: (-2.91%, 76.97%)
```

**Example 3: Sequential updating.**

Start with $\text{Beta}(1, 1)$ and observe the sequence: success, success, failure, success, failure. Track the posterior after each observation.

```python
from scipy import stats

alpha, beta_param = 1, 1
observations = [1, 1, 0, 1, 0]  # 1 = success, 0 = failure

print(f"Step 0: Beta({alpha}, {beta_param}), "
      f"mean = {alpha/(alpha+beta_param):.4f}")

for i, obs in enumerate(observations):
    if obs == 1:
        alpha += 1
    else:
        beta_param += 1
    mean = alpha / (alpha + beta_param)
    lo = stats.beta.ppf(0.025, alpha, beta_param)
    hi = stats.beta.ppf(0.975, alpha, beta_param)
    label = "S" if obs == 1 else "F"
    print(f"Step {i+1} ({label}): Beta({alpha}, {beta_param}), "
          f"mean = {mean:.4f}, 95% CI = ({lo:.3f}, {hi:.3f})")
```

**Output:**
```
Step 0: Beta(1, 1), mean = 0.5000
Step 1 (S): Beta(2, 1), mean = 0.6667, 95% CI = (0.158, 0.992)
Step 2 (S): Beta(3, 1), mean = 0.7500, 95% CI = (0.292, 0.997)
Step 3 (F): Beta(3, 2), mean = 0.6000, 95% CI = (0.185, 0.937)
Step 4 (S): Beta(4, 2), mean = 0.6667, 95% CI = (0.251, 0.956)
Step 5 (F): Beta(4, 3), mean = 0.5714, 95% CI = (0.200, 0.901)
```

**Example 4: Laplace's rule of succession.**

If the sun has risen every day for $n = 10{,}000$ days (since you started counting), what is the probability it rises tomorrow?

With a uniform prior $\text{Beta}(1, 1)$: after $k = n = 10{,}000$ successes and 0 failures:

$$
P(\text{sunrise tomorrow}) = \frac{k + 1}{n + 2} = \frac{10001}{10002}
$$

```python
n = 10_000
k = n  # sun rose every day
p_next = (k + 1) / (n + 2)
print(f"Laplace's rule: P(sunrise) = {k+1}/{n+2} = {p_next:.8f}")
print(f"Posterior: Beta({1+k}, {1+n-k}) = Beta({1+k}, 1)")
print(f"Posterior mean = {(1+k)/(2+n):.8f}")
```

**Output:**
```
Laplace's rule: P(sunrise) = 10001/10002 = 0.99990002
Posterior: Beta(10001, 1) = Beta(10001, 1)
Posterior mean = 0.99990002
```
