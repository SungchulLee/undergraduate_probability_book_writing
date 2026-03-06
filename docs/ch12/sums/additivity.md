# Additivity of Independent Poisson Random Variables

## Statement

!!! info "Additivity of Poisson"
    If $X \sim \text{Po}(\lambda_1)$ and $Y \sim \text{Po}(\lambda_2)$ are **independent**, then

    $$

    X + Y \sim \text{Po}(\lambda_1 + \lambda_2)

    $$

    More generally, if $X_1, X_2, \ldots, X_n$ are independent with $X_i \sim \text{Po}(\lambda_i)$, then

    $$

    \sum_{i=1}^{n} X_i \sim \text{Po}\!\left(\sum_{i=1}^{n} \lambda_i\right)

    $$

This is a fundamental property that makes the Poisson distribution particularly convenient for modeling and computation.

---

## Proof via Convolution

For independent $X \sim \text{Po}(\lambda_1)$ and $Y \sim \text{Po}(\lambda_2)$, we compute the PMF of $Z = X + Y$ using the convolution formula:

$$

P(Z = k) = \sum_{j=0}^{k} P(X = j) \, P(Y = k - j)

$$

Substituting the Poisson PMFs:

$$

P(Z = k) = \sum_{j=0}^{k} \frac{e^{-\lambda_1} \lambda_1^j}{j!} \cdot \frac{e^{-\lambda_2} \lambda_2^{k-j}}{(k-j)!}

$$

$$

= e^{-(\lambda_1 + \lambda_2)} \sum_{j=0}^{k} \frac{\lambda_1^j \lambda_2^{k-j}}{j!(k-j)!}

$$

$$

= \frac{e^{-(\lambda_1 + \lambda_2)}}{k!} \sum_{j=0}^{k} \binom{k}{j} \lambda_1^j \lambda_2^{k-j}

$$

By the Binomial Theorem, $\sum_{j=0}^{k} \binom{k}{j} \lambda_1^j \lambda_2^{k-j} = (\lambda_1 + \lambda_2)^k$, so:

$$

P(Z = k) = \frac{e^{-(\lambda_1 + \lambda_2)} (\lambda_1 + \lambda_2)^k}{k!}

$$

which is the PMF of $\text{Po}(\lambda_1 + \lambda_2)$.

---

## Proof via MGF

The moment generating function of $X \sim \text{Po}(\lambda)$ is:

$$

M_X(t) = E[e^{tX}] = e^{\lambda(e^t - 1)}

$$

For independent $X \sim \text{Po}(\lambda_1)$ and $Y \sim \text{Po}(\lambda_2)$:

$$

M_{X+Y}(t) = M_X(t) \cdot M_Y(t) = e^{\lambda_1(e^t - 1)} \cdot e^{\lambda_2(e^t - 1)} = e^{(\lambda_1 + \lambda_2)(e^t - 1)}

$$

By the uniqueness theorem for MGFs, $X + Y \sim \text{Po}(\lambda_1 + \lambda_2)$.

---

## Connection to Poisson Process: Merger

The additivity property has a natural interpretation via **Poisson processes** (covered in Chapter 13).

If we have two independent Poisson processes with intensities $\lambda_1$ and $\lambda_2$, merging them produces a Poisson process with intensity $\lambda_1 + \lambda_2$. The count of events in any interval is the sum of counts from each process — exactly the additivity property.

---

## Important: Independence Is Required

Additivity requires independence. If $X$ and $Y$ are dependent Poisson random variables, their sum is generally **not** Poisson.

```python
import numpy as np
from scipy.stats import poisson, kstest

np.random.seed(42)
n = 100_000
la1, la2 = 3, 5

# Independent case: sum IS Poisson
X_ind = np.random.poisson(la1, n)
Y_ind = np.random.poisson(la2, n)
Z_ind = X_ind + Y_ind

# Dependent case: sum is NOT Poisson
# (e.g., Y = X + Poisson(2) makes them dependent)
X_dep = np.random.poisson(la1, n)
Y_dep = X_dep + np.random.poisson(la2 - la1, n)  # Y depends on X
Z_dep = X_dep + Y_dep

print("Independent case:")
print(f"  Z mean = {Z_ind.mean():.3f}, var = {Z_ind.var():.3f}")
print(f"  Expected: mean = {la1+la2}, var = {la1+la2}")

print("\nDependent case:")
print(f"  Z mean = {Z_dep.mean():.3f}, var = {Z_dep.var():.3f}")
print(f"  Note: var ≠ mean, so Z is NOT Poisson")
```

---

## Numerical Verification

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson

np.random.seed(42)
la1, la2 = 3, 7
la_sum = la1 + la2
n_samples = 100_000

# Simulate sum of independent Poissons
X = np.random.poisson(la1, n_samples)
Y = np.random.poisson(la2, n_samples)
Z = X + Y

# Compare empirical distribution with Po(λ1 + λ2)
k = np.arange(0, 30)
empirical_pmf = np.array([(Z == ki).mean() for ki in k])
theoretical_pmf = poisson.pmf(k, la_sum)

fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# PMF comparison
axes[0].bar(k - 0.2, empirical_pmf, width=0.4, alpha=0.7,
            label=f'Empirical X+Y', color='steelblue')
axes[0].bar(k + 0.2, theoretical_pmf, width=0.4, alpha=0.7,
            label=f'Po({la_sum})', color='coral')
axes[0].set_title(f'Po({la1}) + Po({la2}) = Po({la_sum})')
axes[0].set_xlabel('k')
axes[0].set_ylabel('P(Z = k)')
axes[0].legend()
axes[0].grid(True, alpha=0.3)

# Difference plot
axes[1].bar(k, empirical_pmf - theoretical_pmf, color='gray', alpha=0.7)
axes[1].axhline(y=0, color='black', linewidth=0.5)
axes[1].set_title('Difference (Empirical − Theoretical)')
axes[1].set_xlabel('k')
axes[1].set_ylabel('PMF difference')
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('poisson_additivity.png', dpi=150, bbox_inches='tight')
plt.show()

print(f"Sample mean:  {Z.mean():.3f}  (theoretical: {la_sum})")
print(f"Sample var:   {Z.var(ddof=1):.3f}  (theoretical: {la_sum})")
```

---

## Application: Combining Counts from Multiple Sources

In practice, if events from different independent sources follow Poisson distributions, the total count is also Poisson. For example:

- **Call center**: Calls from region A arrive at rate $\lambda_1 = 5$/hr and from region B at rate $\lambda_2 = 3$/hr. Total calls per hour follow $\text{Po}(8)$.

- **Insurance**: Claims from auto policies ($\lambda_1$) and home policies ($\lambda_2$), if independent, have a total claim count following $\text{Po}(\lambda_1 + \lambda_2)$.

- **Finance**: Default events in independent credit portfolios with rates $\lambda_1, \lambda_2, \ldots, \lambda_n$ produce a total default count following $\text{Po}(\sum \lambda_i)$.
