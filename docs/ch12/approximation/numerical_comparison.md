# Numerical Comparison: Binomial vs Poisson

## Side-by-Side PMF Comparison

When the Poisson approximation conditions are met ($n$ large, $p$ small, $\lambda = np$ moderate), the PMFs of $B(n, p)$ and $\text{Po}(\lambda)$ are nearly indistinguishable.

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom, poisson

n = 2000
p = 0.005
la = n * p  # λ = 10

k_max = int(la + 6 * np.sqrt(la))
k = np.arange(0, k_max + 1)

binom_pmf = binom.pmf(k, n, p)
poisson_pmf = poisson.pmf(k, la)

fig, axes = plt.subplots(1, 2, figsize=(14, 5))

axes[0].bar(k, binom_pmf, color='steelblue', alpha=0.7, edgecolor='black')
axes[0].set_title(f'PMF of B({n}, {p})')
axes[0].set_xlabel('k')
axes[0].set_ylabel('P(X = k)')
axes[0].set_xlim(-0.5, k_max + 0.5)
axes[0].set_ylim(0, 0.13)
axes[0].grid(True, alpha=0.3)

axes[1].bar(k, poisson_pmf, color='coral', alpha=0.7, edgecolor='black')
axes[1].set_title(f'PMF of Po({int(la)})')
axes[1].set_xlabel('k')
axes[1].set_ylabel('P(X = k)')
axes[1].set_xlim(-0.5, k_max + 0.5)
axes[1].set_ylim(0, 0.13)
axes[1].grid(True, alpha=0.3)

plt.suptitle(f'Poisson Approximation: B({n}, {p}) ≈ Po({int(la)})',
             fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('binomial_vs_poisson.png', dpi=150, bbox_inches='tight')
plt.show()

max_diff = np.max(np.abs(binom_pmf - poisson_pmf))
print(f"Maximum difference between PMFs: {max_diff:.4e}")
```

For $n = 2000$, $p = 0.005$, $\lambda = 10$: the maximum difference between the two PMFs is approximately $3.14 \times 10^{-4}$.

---

## Point-by-Point Comparison Table

```python
import numpy as np
from scipy.stats import binom, poisson

n = 2000
p = 0.005
la = n * p

print(f"{'k':>4} {'B(2000,0.005)':>15} {'Po(10)':>15} {'Difference':>15}")
print("-" * 52)
for k in range(21):
    b = binom.pmf(k, n, p)
    po = poisson.pmf(k, la)
    print(f"{k:>4} {b:>15.8f} {po:>15.8f} {b - po:>15.2e}")
```

---

## Example: Number of Couples with the Same Birthday

Approximately 80,000 marriages took place in New York in a given year. We wish to estimate the probability that more than 250 couples share a birthday (both partners born on the same day of the year).

**Setup**: Let $n = 80{,}000$ be the number of couples. For each couple $i$, let $A_i$ be the event that couple $i$ shares a birthday. Assuming birthdays are uniform over 365 days:

$$
p = P(A_i) = \frac{1}{365}
$$

Let $S_n = \sum_{i=1}^{n} \mathbf{1}_{A_i}$ count the number of couples with the same birthday. Then:

$$
S_n \sim B(n, p) \approx \text{Po}(\lambda), \quad \lambda = np = \frac{80{,}000}{365} \approx 219.18
$$

**Target**: $P(S_n > 250)$.

```python
import numpy as np
from scipy.stats import binom, poisson
import time

n = 80_000
p = 1 / 365
la = n * p
m = 250

# --- Exact Binomial ---
t0 = time.time()
# Use log-space computation to avoid overflow
binom_prob = 1 - binom.cdf(m, n, p)
binom_time = time.time() - t0

# --- Poisson Approximation ---
t0 = time.time()
poisson_prob = 1 - poisson.cdf(m, la)
poisson_time = time.time() - t0

print(f"λ = np = {la:.4f}")
print()
print(f"Exact (Binomial):       P(S_n > 250) = {binom_prob:.6f}")
print(f"Approximate (Poisson):  P(X  > 250) = {poisson_prob:.6f}")
print()
print(f"Absolute difference: {abs(binom_prob - poisson_prob):.6e}")
print(f"Binomial time:  {binom_time:.6f} s")
print(f"Poisson time:   {poisson_time:.6f} s")
```

**Results**:

| Method | $P(\cdot > 250)$ |
|:---|:---:|
| Exact: $S_n \sim B(80000, 1/365)$ | 0.0187 |
| Approximate: $X \sim \text{Po}(219.18)$ | 0.0188 |

The Poisson approximation is accurate to four decimal places.

---

## Iterative Computation (Avoiding Large Factorials)

When $n$ is very large, computing $\binom{n}{k}$ directly can cause overflow. Both the Binomial and Poisson PMFs can be computed iteratively using recurrence relations.

**Binomial recurrence**: Starting from $P(X = 0) = q^n$:

$$
P(X = k) = P(X = k-1) \cdot \frac{n - k + 1}{k} \cdot \frac{p}{q}
$$

**Poisson recurrence**: Starting from $P(X = 0) = e^{-\lambda}$:

$$
P(X = k) = P(X = k-1) \cdot \frac{\lambda}{k}
$$

```python
import numpy as np
import time

n = 80_000
p = 1 / 365
q = 1 - p
la = n * p
m = 250

# --- Iterative Binomial ---
t0 = time.time()
prob = q ** n
cum_prob = prob
for i in range(1, m + 1):
    prob = prob * (n - i + 1) / i * p / q
    cum_prob += prob
binom_exact = 1 - cum_prob
binom_time = time.time() - t0

# --- Iterative Poisson ---
t0 = time.time()
prob = np.exp(-la)
cum_prob = prob
for i in range(1, m + 1):
    prob = prob * la / i
    cum_prob += prob
poisson_approx = 1 - cum_prob
poisson_time = time.time() - t0

print(f"Binomial (iterative):  P(S > {m}) = {binom_exact:.6f}  ({binom_time:.6f} s)")
print(f"Poisson (iterative):   P(X > {m}) = {poisson_approx:.6f}  ({poisson_time:.6f} s)")
```

---

## Convergence as $n$ Increases

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom, poisson

la = 10
n_values = [20, 50, 100, 200, 500, 1000, 5000, 10000]
k_max = 25
k = np.arange(0, k_max + 1)

poisson_pmf = poisson.pmf(k, la)

max_diffs = []
for n in n_values:
    p = la / n
    binom_pmf = binom.pmf(k, n, p)
    max_diffs.append(np.max(np.abs(binom_pmf - poisson_pmf)))

plt.figure(figsize=(8, 5))
plt.loglog(n_values, max_diffs, 'o-', color='steelblue', linewidth=2, markersize=8)
plt.xlabel('n', fontsize=12)
plt.ylabel('Max |PMF difference|', fontsize=12)
plt.title(f'Convergence Rate: B(n, {la}/n) → Po({la})', fontsize=14)
plt.grid(True, alpha=0.3, which='both')

# Add reference line for O(1/n)
n_arr = np.array(n_values, dtype=float)
plt.loglog(n_arr, max_diffs[0] * n_values[0] / n_arr, '--', color='gray',
           alpha=0.5, label='O(1/n) reference')
plt.legend()
plt.tight_layout()
plt.savefig('poisson_convergence_rate.png', dpi=150, bbox_inches='tight')
plt.show()
```

The maximum PMF difference decreases as $O(1/n)$, consistent with the Le Cam bound $p \cdot \lambda = \lambda^2/n$.
