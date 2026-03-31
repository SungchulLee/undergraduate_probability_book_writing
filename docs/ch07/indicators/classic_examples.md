# Classic Examples Using Indicators

## Example 1: Matching Problem (Derangements)

A hat-check person returns $n$ hats to $n$ people at random. Let $X$ be the number of people who get their own hat.

$$
X = \sum_{i=1}^n \mathbf{1}_{A_i}
$$

where $A_i$ is the event that person $i$ gets their own hat.

**Mean**: By symmetry, $P(A_i) = \frac{1}{n}$ for each $i$, so

$$
E[X] = \sum_{i=1}^n \frac{1}{n} = 1
$$

Remarkably, the expected number of matches is exactly 1, regardless of $n$.

**Variance**: We need $P(A_i \cap A_j)$ for $i \neq j$:

$$
P(A_i \cap A_j) = \frac{(n-2)!}{n!} = \frac{1}{n(n-1)}
$$

$$
\text{Cov}(\mathbf{1}_{A_i}, \mathbf{1}_{A_j}) = \frac{1}{n(n-1)} - \frac{1}{n^2} = \frac{1}{n^2(n-1)}
$$

$$
\text{Var}(X) = n \cdot \frac{1}{n}\left(1 - \frac{1}{n}\right) + 2\binom{n}{2} \cdot \frac{1}{n^2(n-1)} = \frac{n-1}{n} + \frac{1}{n} = 1
$$

So $\text{Var}(X) = 1$ for all $n$, and $\text{SD}(X) = 1$.

---

## Example 2: Number of Pairs with Same Birthday

There are $n$ people in a class, each choosing a birthday independently and uniformly from 365 days. Let $S_n$ count the number of pairs sharing a birthday.

$$
S_n = \sum_{1 \leq i < j \leq n} \mathbf{1}_{A_{ij}}
$$

where $A_{ij}$ is the event that persons $i$ and $j$ share a birthday.

!!! warning "Not Binomial"
    Although there are $m = \binom{n}{2}$ Bernoulli indicators each with $p = 1/365$, $S_n$ is **not** $\text{Binomial}(m, p)$ because the indicators are not independent.

**Mean**:

$$
E[S_n] = \binom{n}{2} \cdot \frac{1}{365}
$$

**Variance**: The indicators are pairwise independent (knowing whether $i,j$ share a birthday doesn't change the probability for a disjoint pair $k,l$). More precisely, for pairs $(i,j)$ and $(k,l)$ with no common person:

$$
P(A_{ij} \cap A_{kl}) = P(A_{ij})P(A_{kl}) = \frac{1}{365^2}
$$

So the covariance terms vanish and:

$$
\text{Var}(S_n) = \binom{n}{2} \cdot \frac{1}{365} \cdot \frac{364}{365}
$$

---

## Example 3: Number of Empty Bins

There are $n$ balls and $M = 365$ bins. Each ball independently and uniformly chooses a bin. Let $S_n$ count the empty bins.

$$
S_n = \sum_{i=1}^{M} \mathbf{1}_{A_i}
$$

where $A_i$ = {bin $i$ is empty}. Then $P(A_i) = \left(\frac{M-1}{M}\right)^n$.

**Mean**:

$$
E[S_n] = M \left(\frac{M-1}{M}\right)^n
$$

**Variance**: Here the indicators are **not** independent and the covariance is nonzero:

$$
P(A_i \cap A_j) = \left(\frac{M-2}{M}\right)^n
$$

$$
\text{Cov}(\mathbf{1}_{A_i}, \mathbf{1}_{A_j}) = \left(\frac{M-2}{M}\right)^n - \left(\frac{M-1}{M}\right)^{2n}
$$

$$
\text{Var}(S_n) = M \cdot p(1-p) + 2\binom{M}{2}\left[\left(\frac{M-2}{M}\right)^n - p^2\right]
$$

where $p = \left(\frac{M-1}{M}\right)^n$.

---

## Example 4: Number of Stops (Elevator Problem)

There are $n$ people in an elevator at the basement. Each independently chooses a floor uniformly from $M = 365$ floors. Let $X_n$ be the total number of stops.

The number of stops equals the number of non-empty bins:

$$
X_n = M - S_n
$$

where $S_n$ is the number of empty bins (floors no one chose).

**Mean**:

$$
E[X_n] = M - E[S_n] = M - M\left(\frac{M-1}{M}\right)^n = M\left[1 - \left(\frac{M-1}{M}\right)^n\right]
$$

**Variance**:

$$
\text{Var}(X_n) = \text{Var}(M - S_n) = \text{Var}(S_n)
$$

---

## Python Implementation

```python
import numpy as np
import matplotlib.pyplot as plt
from math import comb

# ============================================================
# Birthday pairs: mean and standard deviation vs n
# ============================================================
n_people = np.arange(1, 367)
mu_pairs = np.array([comb(n, 2) for n in n_people]) / 365
sd_pairs = np.sqrt(mu_pairs * 364 / 365)

fig, axes = plt.subplots(1, 2, figsize=(12, 5))
axes[0].plot(n_people, mu_pairs)
axes[0].set_xlabel('Number of people in class')
axes[0].set_title('Mean of number of common birthday pairs')
axes[0].grid(True)

axes[1].plot(n_people, sd_pairs)
axes[1].set_xlabel('Number of people in class')
axes[1].set_title('Standard deviation of number of common birthday pairs')
axes[1].grid(True)
plt.tight_layout()
plt.savefig('birthday_pairs.png', dpi=150, bbox_inches='tight')
plt.show()

# ============================================================
# Empty bins: mean and standard deviation vs n
# ============================================================
M = 365
n_balls = np.arange(1, 2001)
p1 = ((M - 1) / M) ** n_balls
p2 = ((M - 2) / M) ** n_balls
mu_empty = M * p1
var_empty = M * p1 * (1 - p1) + 2 * comb(M, 2) * (p2 - p1**2)
sd_empty = np.sqrt(np.maximum(var_empty, 0))

fig, axes = plt.subplots(1, 2, figsize=(12, 5))
axes[0].plot(n_balls, mu_empty)
axes[0].set_xlabel('Number of balls thrown')
axes[0].set_title('Mean of number of empty bins')
axes[0].grid(True)

axes[1].plot(n_balls, sd_empty)
axes[1].set_xlabel('Number of balls thrown')
axes[1].set_title('Standard deviation of number of empty bins')
axes[1].grid(True)
plt.tight_layout()
plt.savefig('empty_bins.png', dpi=150, bbox_inches='tight')
plt.show()

# ============================================================
# Number of stops: mean and standard deviation vs n
# ============================================================
mu_stops = M - mu_empty
sd_stops = sd_empty  # Var(M - S) = Var(S)

fig, axes = plt.subplots(1, 2, figsize=(12, 5))
axes[0].plot(n_balls, mu_stops)
axes[0].set_xlabel('Number of people in elevator')
axes[0].set_title('Mean of number of overall stops')
axes[0].grid(True)

axes[1].plot(n_balls, sd_stops)
axes[1].set_xlabel('Number of people in elevator')
axes[1].set_title('Standard deviation of number of overall stops')
axes[1].grid(True)
plt.tight_layout()
plt.savefig('elevator_stops.png', dpi=150, bbox_inches='tight')
plt.show()
```
