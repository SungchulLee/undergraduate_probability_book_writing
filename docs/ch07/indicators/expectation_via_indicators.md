# Expectation via Indicators


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

## The Indicator Method

Many random variables can be expressed as sums of indicator random variables:

$$
X = \sum_{i} \mathbf{1}_{A_i}
$$

By linearity of expectation:

$$
E[X] = \sum_{i} E[\mathbf{1}_{A_i}] = \sum_{i} P(A_i)
$$

This works **regardless of whether the indicators are independent**, making it one of the most versatile tools in probability.

---

## Variance via Indicators

When $X = \sum_{i=1}^m \mathbf{1}_{A_i}$, the variance requires more care:

$$
\text{Var}(X) = \sum_{i=1}^m \text{Var}(\mathbf{1}_{A_i}) + 2\sum_{1 \leq i < j \leq m} \text{Cov}(\mathbf{1}_{A_i}, \mathbf{1}_{A_j})
$$

where

$$
\text{Var}(\mathbf{1}_{A_i}) = P(A_i)(1 - P(A_i))
$$

$$
\text{Cov}(\mathbf{1}_{A_i}, \mathbf{1}_{A_j}) = P(A_i \cap A_j) - P(A_i)P(A_j)
$$

**If the indicators are independent**, the covariance terms vanish and $\text{Var}(X) = \sum_i \text{Var}(\mathbf{1}_{A_i})$.

---

## When Is the Sum Binomial?

A sum of indicators $X = \sum_{i=1}^m \mathbf{1}_{A_i}$ is $\text{Binomial}(m, p)$ **only if**:

1. Each $\mathbf{1}_{A_i} \sim \text{Bernoulli}(p)$ (same $p$)
2. The indicators are **mutually independent**

If either condition fails, $X$ is **not** binomial. We can still compute $E[X]$ and $\text{Var}(X)$ using the indicator method.

---

## Example: Binomial via Indicators

Flip a $p$-coin $n$ times independently. Let $S$ count the number of heads:

$$
S = \sum_{i=1}^n \mathbf{1}_{A_i}, \quad \mathbf{1}_{A_i} \stackrel{iid}{\sim} \text{Bernoulli}(p)
$$

Since the indicators are iid:

$$
E[S] = np, \quad \text{Var}(S) = npq
$$

---

## Example: Not Binomial — Birthday Pairs

There are $n$ people, each with a birthday chosen uniformly from 365 days. Let $S_n$ count the number of pairs sharing a birthday:

$$
S_n = \sum_{1 \leq i < j \leq n} \mathbf{1}_{A_{ij}}
$$

where $A_{ij}$ is the event that persons $i$ and $j$ share a birthday.

**Why not binomial**: There are $m = \binom{n}{2}$ indicators, each with $p = 1/365$, but they are **not independent**. (If $A_{12}$ and $A_{13}$ both occur, then persons 2 and 3 share a birthday with person 1, making $A_{23}$ more likely.)

However, the indicators are **pairwise independent**, so the covariance terms vanish:

$$
E[S_n] = \binom{n}{2} \cdot \frac{1}{365}
$$

$$
\text{Var}(S_n) = \binom{n}{2} \cdot \frac{1}{365} \cdot \frac{364}{365}
$$

---

## Example: Not Binomial — Empty Bins

There are $n$ balls and $M = 365$ bins. Each ball independently chooses a bin uniformly at random. Let $S_n$ count the number of empty bins:

$$
S_n = \sum_{i=1}^{365} \mathbf{1}_{A_i}
$$

where $A_i$ is the event that bin $i$ is empty. Each $\mathbf{1}_{A_i} \sim \text{Bernoulli}(p)$ with $p = \left(\frac{364}{365}\right)^n$, but the indicators are **not independent** (if one bin is empty, the remaining bins are slightly more likely to contain balls).

$$
E[S_n] = 365 \cdot p
$$

$$
\text{Var}(S_n) = 365 \cdot pq + 2\binom{365}{2} \left[\left(\frac{363}{365}\right)^n - p^2\right]
$$

---

## Python Implementation

```python
import numpy as np
from math import comb

# Birthday pairs: mean and variance
def birthday_pairs_stats(n_people):
    m = comb(n_people, 2)
    p = 1 / 365
    mean = m * p
    var = m * p * (1 - p)  # pairwise independent
    return mean, var

n = 30
mu, v = birthday_pairs_stats(n)
print(f"Birthday pairs (n={n}): E = {mu:.4f}, SD = {np.sqrt(v):.4f}")

# Empty bins: mean and variance
def empty_bins_stats(n_balls, M=365):
    p = ((M - 1) / M) ** n_balls
    p2 = ((M - 2) / M) ** n_balls
    mean = M * p
    var = M * p * (1 - p) + 2 * comb(M, 2) * (p2 - p**2)
    return mean, var

n_balls = 100
mu, v = empty_bins_stats(n_balls)
print(f"Empty bins (n={n_balls}): E = {mu:.4f}, SD = {np.sqrt(v):.4f}")

# Monte Carlo verification: birthday pairs
np.random.seed(42)
N_sim = 100_000
n_people = 30
pair_counts = []
for _ in range(N_sim):
    bdays = np.random.randint(0, 365, n_people)
    count = 0
    for i in range(n_people):
        for j in range(i+1, n_people):
            if bdays[i] == bdays[j]:
                count += 1
    pair_counts.append(count)

pair_counts = np.array(pair_counts)
mu_exact = comb(n_people, 2) / 365
print(f"\nBirthday pairs MC: E = {np.mean(pair_counts):.4f}, exact = {mu_exact:.4f}")
```
