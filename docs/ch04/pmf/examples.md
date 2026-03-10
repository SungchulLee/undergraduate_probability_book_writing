# Coin-Flip Distribution Family

The Bernoulli, Binomial, Geometric, and Negative Binomial distributions all arise from the same experiment — flipping a $p$-coin — but count different things.

## Definition

| Distribution | PMF | Support |
|:-------------|:----|:--------|
| $\text{Bern}(p)$ | $P(X = k) = p^k(1-p)^{1-k}$ | $k \in \{0, 1\}$ |
| $\text{Bin}(n, p)$ | $P(X = k) = \binom{n}{k}p^k(1-p)^{n-k}$ | $k = 0, 1, \ldots, n$ |
| $\text{Geo}(p)$ | $P(X = k) = p(1-p)^{k-1}$ | $k = 1, 2, 3, \ldots$ |
| $\text{NB}(r, p)$ | $P(X = k) = \binom{k-1}{r-1}p^r(1-p)^{k-r}$ | $k = r, r+1, \ldots$ |

## Explanation

### What Each Distribution Counts

| Distribution | Experiment | Random Variable |
|:-------------|:-----------|:----------------|
| $\text{Bern}(p)$ | Flip once | 1 if head, 0 if tail |
| $\text{Bin}(n,p)$ | Flip $n$ times | Number of heads |
| $\text{Geo}(p)$ | Flip until first head | Number of flips |
| $\text{NB}(r,p)$ | Flip until $r$-th head | Number of flips |

### Relationships

- $\text{Bern}(p) = \text{Bin}(1, p)$
- $\text{Geo}(p) = \text{NB}(1, p)$
- If $X_1, \ldots, X_n \stackrel{\text{iid}}{\sim} \text{Bern}(p)$, then $X_1 + \cdots + X_n \sim \text{Bin}(n, p)$
- If $Y_1, \ldots, Y_r \stackrel{\text{iid}}{\sim} \text{Geo}(p)$, then $Y_1 + \cdots + Y_r \sim \text{NB}(r, p)$

### Moment Summary

| Distribution | $E[X]$ | $\text{Var}(X)$ |
|:-------------|:-------|:-----------------|
| $\text{Bern}(p)$ | $p$ | $p(1-p)$ |
| $\text{Bin}(n,p)$ | $np$ | $np(1-p)$ |
| $\text{Geo}(p)$ | $1/p$ | $(1-p)/p^2$ |
| $\text{NB}(r,p)$ | $r/p$ | $r(1-p)/p^2$ |

### PMF Normalization Check

**Binomial:** The binomial theorem gives $\sum_{k=0}^n \binom{n}{k}p^k(1-p)^{n-k} = (p + (1-p))^n = 1$.

**Geometric:** A geometric series gives $\sum_{k=1}^{\infty} p(1-p)^{k-1} = p \cdot \frac{1}{1-(1-p)} = 1$.

## Examples

**Example 1.** $X \sim \text{Bin}(10, 0.3)$. Compute $P(X = 3)$ and $P(X \ge 2)$.

$$
P(X = 3) = \binom{10}{3}(0.3)^3(0.7)^7 = 120 \cdot 0.027 \cdot 0.0824 \approx 0.2668
$$

$$
P(X \ge 2) = 1 - P(X=0) - P(X=1) = 1 - 0.7^{10} - 10 \cdot 0.3 \cdot 0.7^9 \approx 0.8507
$$

**Example 2.** $Y \sim \text{Geo}(1/6)$ models the number of die rolls until the first six. The expected number of rolls is $E[Y] = 6$.

$$
P(Y > 10) = (5/6)^{10} \approx 0.1615
$$

```python
from math import comb

# Binomial(10, 0.3)
n, p = 10, 0.3
pmf_3 = comb(n, 3) * p**3 * (1-p)**7
p_ge_2 = 1 - (1-p)**n - n * p * (1-p)**(n-1)
print(f"Bin(10, 0.3): P(X=3) = {pmf_3:.4f}, P(X>=2) = {p_ge_2:.4f}")

# Geometric(1/6): rolls until first six
p_geo = 1/6
p_gt_10 = (1 - p_geo)**10
print(f"Geo(1/6): P(Y > 10) = {p_gt_10:.4f}, E[Y] = {1/p_geo:.1f}")

# Verify Binomial normalization
total = sum(comb(n, k) * p**k * (1-p)**(n-k) for k in range(n+1))
print(f"Bin PMF sum = {total:.6f}")
```
