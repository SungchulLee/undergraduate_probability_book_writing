# Strong Law of Large Numbers — Intuition and Connections

## SLLN vs WLLN

!!! info "Strong Law of Large Numbers"
    Let $X_1, X_2, \ldots$ be iid with $E[X_i] = \mu$. Then:

    $$P\!\left(\lim_{n \to \infty} \bar{X}_n = \mu\right) = 1$$

    That is, $\bar{X}_n \xrightarrow{\text{a.s.}} \mu$.

The key distinction from the WLLN:

| | WLLN | SLLN |
|:---|:---:|:---:|
| **Mode** | Convergence in probability | Almost sure convergence |
| **Meaning** | $P(\|\bar{X}_n - \mu\| > \varepsilon) \to 0$ for each $\varepsilon$ | $P(\bar{X}_n \to \mu) = 1$ |
| **Requirement** | Finite mean (or finite variance for easy proof) | Finite mean |
| **Allows** | Occasional large deviations | Only finitely many large deviations |

## Intuitive Difference

The WLLN says: "for any fixed tolerance $\varepsilon$, the probability that $\bar{X}_n$ deviates from $\mu$ by more than $\varepsilon$ goes to zero."

The SLLN says: "with probability 1, $\bar{X}_n$ **eventually stays** within $\varepsilon$ of $\mu$ and **never leaves again** (except finitely many times)."

**Analogy.** Consider a dart thrower:

- WLLN: "For any ring around the bullseye, the fraction of darts landing outside it goes to 0" — but there could be occasional wild throws.
- SLLN: "Eventually, after some dart $N$, **all subsequent darts** land within $\varepsilon$ of the bullseye" (with probability 1).

## Proof Strategy via Borel-Cantelli

The proof of the SLLN relies heavily on the **Borel-Cantelli lemmas**.

!!! info "First Borel-Cantelli Lemma"
    If $\sum_{n=1}^{\infty} P(A_n) < \infty$, then $P(A_n \text{ occurs infinitely often}) = 0$.

    That is, with probability 1, only **finitely many** of the events $A_n$ occur.

**Application to SLLN.** Let $A_n = \{|\bar{X}_n - \mu| > \varepsilon\}$. If we can show $\sum_n P(A_n) < \infty$, then by Borel-Cantelli, $\bar{X}_n$ deviates from $\mu$ by more than $\varepsilon$ only finitely many times, i.e., $\bar{X}_n \to \mu$ almost surely.

**Why doesn't Chebyshev work directly?** Chebyshev gives $P(A_n) \leq \frac{\sigma^2}{n\varepsilon^2}$, and $\sum \frac{1}{n} = \infty$. So the bound isn't summable.

**The trick: use subsequences.** Along $n_k = k^2$:

$$P(|\bar{X}_{k^2} - \mu| > \varepsilon) \leq \frac{\sigma^2}{k^2\varepsilon^2}$$

and $\sum \frac{1}{k^2} < \infty$. So $\bar{X}_{k^2} \to \mu$ a.s. Then one shows that $\bar{X}_n$ between successive squares $k^2$ and $(k+1)^2$ cannot deviate much from $\bar{X}_{k^2}$, completing the proof.

## Does WLLN Imply SLLN?

**No.** There exist sequences that converge in probability but not almost surely.

**Counterexample (typewriter sequence).** Let $\Omega = [0, 1]$ with Lebesgue measure. Define:

$$X_n = \mathbf{1}\!\left[\frac{n - 2^k}{2^k}, \frac{n - 2^k + 1}{2^k}\right) \quad \text{where } 2^k \leq n < 2^{k+1}$$

The intervals cycle through $[0, 1]$ with decreasing width. Then $X_n \xrightarrow{p} 0$ (since the interval lengths $\to 0$), but for **every** $\omega \in [0,1]$, $X_n(\omega) = 1$ infinitely often. So $X_n$ does **not** converge a.s. to 0.

## SLLN for Specific Distributions

### Bernoulli SLLN (Borel's Theorem)

If $X_i \sim \text{Bernoulli}(p)$ are iid, then:

$$\frac{X_1 + \cdots + X_n}{n} \xrightarrow{\text{a.s.}} p$$

This was historically the first version of the SLLN (Borel, 1909). It formalizes the frequentist interpretation: the long-run relative frequency of success converges to $p$ with probability 1.

### Normal SLLN

If $X_i \sim N(\mu, \sigma^2)$ are iid, then $\bar{X}_n \xrightarrow{\text{a.s.}} \mu$. Moreover, the rate can be quantified using the **law of the iterated logarithm**:

$$\limsup_{n \to \infty} \frac{\bar{X}_n - \mu}{\sigma\sqrt{2\ln\ln n / n}} = 1 \quad \text{a.s.}$$

This gives the **exact fluctuation envelope** of $\bar{X}_n$ around $\mu$.

## The Law of the Iterated Logarithm

!!! info "Law of the Iterated Logarithm (LIL)"
    If $X_i$ are iid with $E[X_i] = 0$ and $\text{Var}(X_i) = \sigma^2$, then:

    $$\limsup_{n \to \infty} \frac{S_n}{\sigma\sqrt{2n\ln\ln n}} = 1 \quad \text{a.s.}$$

    $$\liminf_{n \to \infty} \frac{S_n}{\sigma\sqrt{2n\ln\ln n}} = -1 \quad \text{a.s.}$$

The LIL sits between the CLT (which says $S_n / \sqrt{n}$ has approximate standard normal distribution) and the SLLN (which says $S_n / n \to 0$). It tells us the **exact boundary** of the random walk $S_n$: it grows like $\pm\sqrt{2n\ln\ln n}$ infinitely often, but never faster.

## Python Implementation

```python
import numpy as np
import matplotlib.pyplot as plt

fig, axes = plt.subplots(1, 3, figsize=(16, 5))
np.random.seed(42)

# --- Panel 1: SLLN vs WLLN visualization ---
n_max = 10000
ns = np.arange(1, n_max + 1)
eps = 0.05

# Multiple paths
n_paths = 20
for i in range(n_paths):
    samples = np.random.exponential(1, n_max)
    means = np.cumsum(samples) / ns
    axes[0].plot(ns, means, alpha=0.3, lw=0.5, color='steelblue')

axes[0].axhline(1, color='red', ls='-', lw=2, label='μ = 1')
axes[0].axhline(1 + eps, color='red', ls='--', alpha=0.5)
axes[0].axhline(1 - eps, color='red', ls='--', alpha=0.5)
axes[0].set_title('SLLN: All paths converge to μ')
axes[0].set_xlabel('n')
axes[0].set_ylabel('$\\bar{X}_n$')
axes[0].set_ylim(0.8, 1.2)
axes[0].legend()
axes[0].grid(True, alpha=0.3)

# --- Panel 2: Law of the Iterated Logarithm ---
n_lil = 100000
samples = np.random.normal(0, 1, n_lil)
S_n = np.cumsum(samples)
ns_lil = np.arange(1, n_lil + 1)

# LIL envelope
with np.errstate(divide='ignore', invalid='ignore'):
    envelope = np.sqrt(2 * ns_lil * np.log(np.log(ns_lil)))
    envelope[:3] = np.nan  # avoid log(log(1)) issues

axes[1].plot(ns_lil, S_n, alpha=0.5, lw=0.3, color='steelblue',
             label='$S_n$')
axes[1].plot(ns_lil, envelope, 'r-', lw=1.5, alpha=0.7,
             label='$\\sqrt{2n\\ln\\ln n}$')
axes[1].plot(ns_lil, -envelope, 'r-', lw=1.5, alpha=0.7)
axes[1].fill_between(ns_lil, -envelope, envelope, alpha=0.1, color='red')
axes[1].set_title('Law of the Iterated Logarithm')
axes[1].set_xlabel('n')
axes[1].set_ylabel('$S_n$')
axes[1].legend(fontsize=9)
axes[1].grid(True, alpha=0.3)

# --- Panel 3: Borel-Cantelli demonstration ---
# Count how many times |X̄_n - μ| > ε for increasing ε
n_bc = 5000
samples = np.random.normal(0, 1, n_bc)
means = np.cumsum(samples) / np.arange(1, n_bc + 1)

epsilons = [0.5, 0.2, 0.1, 0.05]
for eps in epsilons:
    violations = np.abs(means) > eps
    cum_violations = np.cumsum(violations)
    axes[2].plot(np.arange(1, n_bc + 1), cum_violations, lw=1.5,
                 label=f'ε={eps}: {int(cum_violations[-1])} violations')

axes[2].set_title('Cumulative Violations |X̄ₙ - μ| > ε')
axes[2].set_xlabel('n')
axes[2].set_ylabel('Count of violations so far')
axes[2].legend(fontsize=8)
axes[2].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('slln_intuition.png', dpi=150, bbox_inches='tight')
plt.show()
```
