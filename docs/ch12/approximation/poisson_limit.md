# Poisson Limit Theorem

## Statement

!!! info "Poisson Limit Theorem"
    Let $X_n \sim B(n, p_n)$ where $p_n = \lambda/n$ for a fixed $\lambda > 0$. Then for every non-negative integer $k$:

    $$
    \lim_{n \to \infty} P(X_n = k) = \frac{e^{-\lambda} \lambda^k}{k!}
    $$

    That is, $B(n, \lambda/n) \to \text{Po}(\lambda)$ in distribution as $n \to \infty$.

---

## Proof

Starting from the Binomial PMF with $p = \lambda/n$:

$$
P(X_n = k) = \binom{n}{k} p^k (1-p)^{n-k}
$$

Substituting $p = \lambda/n$:

$$
P(X_n = k) = \frac{n(n-1)(n-2)\cdots(n-k+1)}{k!} \left(\frac{\lambda}{n}\right)^k \left(1 - \frac{\lambda}{n}\right)^{n-k}
$$

Rearranging:

$$
P(X_n = k) = \frac{1}{k!} \cdot \underbrace{\frac{n(n-1)(n-2)\cdots(n-k+1)}{n^k}}_{\to 1} \cdot \lambda^k \cdot \underbrace{\left(1 - \frac{\lambda}{n}\right)^n}_{\to e^{-\lambda}} \cdot \underbrace{\left(1 - \frac{\lambda}{n}\right)^{-k}}_{\to 1}
$$

Taking the limit as $n \to \infty$ with $k$ fixed:

$$
P(X_n = k) \to \frac{1}{k!} \cdot 1 \cdot \lambda^k \cdot e^{-\lambda} \cdot 1 = \frac{e^{-\lambda} \lambda^k}{k!}
$$

**Details of each factor:**

1. $\frac{n(n-1)\cdots(n-k+1)}{n^k} = 1 \cdot \left(1 - \frac{1}{n}\right) \cdot \left(1 - \frac{2}{n}\right) \cdots \left(1 - \frac{k-1}{n}\right) \to 1$ since $k$ is fixed.

2. $\left(1 - \frac{\lambda}{n}\right)^n \to e^{-\lambda}$ by the classical limit definition of $e$.

3. $\left(1 - \frac{\lambda}{n}\right)^{-k} \to 1$ since $k$ is fixed and $\lambda/n \to 0$.

---

## Moment Convergence

The moments also converge correctly:

| | $B(n, p)$ with $p = \lambda/n$ | $\text{Po}(\lambda)$ |
|:---|:---:|:---:|
| Mean | $np = \lambda$ | $\lambda$ |
| Variance | $npq = \lambda(1 - \lambda/n) \to \lambda$ | $\lambda$ |

The mean matches exactly for all $n$. The variance converges: $\text{Var}(X_n) = \lambda(1 - \lambda/n) \to \lambda$ as $n \to \infty$.

---

## Generalization: Sum of Independent Bernoullis with Different p_i

The Poisson Limit Theorem extends beyond the case where all Bernoulli trials have the same probability. Let $A_1, A_2, \ldots, A_n$ be independent events with $p_i = P(A_i)$, and let

$$
X = \sum_{i=1}^{n} \mathbf{1}_{A_i}
$$

Note that $X$ is **not** $B(n, p)$ in general (since the $p_i$ may differ). Nevertheless, if $Y \sim \text{Po}(\lambda)$ with $\lambda = \sum_{i=1}^{n} p_i$, then for any set $A$:

$$
\left| P(X \in A) - P(Y \in A) \right| \leq \sum_{i=1}^{n} p_i^2 \leq \left(\max_{1 \leq i \leq n} p_i\right) \cdot \sum_{i=1}^{n} p_i = \left(\max_{1 \leq i \leq n} p_i\right) \cdot \lambda
$$

!!! note "Le Cam's Inequality"
    This result, known as **Le Cam's inequality**, provides an explicit error bound for the Poisson approximation. The bound is small when $\max_i p_i$ is small — that is, when each individual event is rare.

---

## Numerical Illustration

```python
import numpy as np
from scipy.stats import binom, poisson
from math import comb, factorial

def poisson_limit_demo(n_values, la=10):
    """Show convergence of B(n, λ/n) to Po(λ) for specific k values."""
    k_values = [0, 5, 10, 15, 20]
    poisson_probs = {k: poisson.pmf(k, la) for k in k_values}

    print(f"Convergence of B(n, {la}/n) to Po({la})")
    print(f"{'n':>10}", end="")
    for k in k_values:
        print(f"{'k='+str(k):>12}", end="")
    print()
    print("-" * (10 + 12 * len(k_values)))

    for n in n_values:
        p = la / n
        print(f"{n:>10}", end="")
        for k in k_values:
            binom_prob = binom.pmf(k, n, p)
            print(f"{binom_prob:>12.6f}", end="")
        print()

    print(f"{'Po(' + str(la) + ')':>10}", end="")
    for k in k_values:
        print(f"{poisson_probs[k]:>12.6f}", end="")
    print()

poisson_limit_demo([20, 50, 100, 500, 1000, 10000])
```

Expected output:

```
Convergence of B(n, 10/n) to Po(10)
         n         k=0         k=5        k=10        k=15        k=20
------------------------------------------------------------------------
        20    0.003520    0.014786    0.176197    0.014786    0.000000
        50    0.000132    0.018133    0.131839    0.034469    0.000014
       100    0.000027    0.033139    0.131966    0.034955    0.000188
       500    0.000046    0.036249    0.126259    0.034643    0.000864
      1000    0.000046    0.036459    0.125937    0.034660    0.000876
     10000    0.000045    0.036558    0.125838    0.034665    0.000881
    Po(10)    0.000045    0.036561    0.125110    0.034718    0.000866
```

---

## Visualization

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom, poisson

la = 10
n_values = [20, 50, 200, 2000]
k_max = 25
k = np.arange(0, k_max + 1)

fig, axes = plt.subplots(2, 2, figsize=(12, 10))
axes = axes.ravel()

poisson_pmf = poisson.pmf(k, la)

for idx, n in enumerate(n_values):
    p = la / n
    binom_pmf = binom.pmf(k, n, p)

    axes[idx].bar(k - 0.2, binom_pmf, width=0.4, alpha=0.7,
                  label=f'B({n}, {la/n:.4f})', color='steelblue')
    axes[idx].bar(k + 0.2, poisson_pmf, width=0.4, alpha=0.7,
                  label=f'Po({la})', color='coral')
    axes[idx].set_title(f'n = {n}, p = {la/n:.4f}')
    axes[idx].set_xlabel('k')
    axes[idx].set_ylabel('P(X = k)')
    axes[idx].legend()
    axes[idx].grid(True, alpha=0.3)

    max_diff = np.max(np.abs(binom_pmf - poisson_pmf))
    axes[idx].text(0.95, 0.95, f'Max |diff| = {max_diff:.2e}',
                   transform=axes[idx].transAxes, ha='right', va='top',
                   fontsize=9, bbox=dict(boxstyle='round', facecolor='wheat'))

plt.suptitle(f'Poisson Limit Theorem: B(n, λ/n) → Po(λ), λ = {la}',
             fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('poisson_limit_theorem.png', dpi=150, bbox_inches='tight')
plt.show()
```
