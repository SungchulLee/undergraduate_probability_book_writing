# Sum of Independent Binomials

The sum of independent Binomial random variables with the same success probability is again Binomial — a closure property that fails without independence.

## Definition

If $X \sim \text{Bin}(n, p)$ and $Y \sim \text{Bin}(m, p)$ are **independent**, then

$$
X + Y \sim \text{Bin}(n + m, p)
$$

!!! warning "Independence is essential"
    Without independence, $X + Y$ need not be Binomial even if both $X$ and $Y$ are individually Binomial with the same $p$.

## Explanation

### Proof by Story

Flip a $p$-coin $n$ times: $X$ counts heads. Flip it $m$ more times: $Y$ counts heads. Since the two groups of flips are independent, $X \perp Y$. The total $X + Y$ counts heads in $n + m$ independent flips, so $X + Y \sim \text{Bin}(n+m, p)$.

### Proof by Convolution

Using the law of total probability and independence:

$$
P(X + Y = k) = \sum_{l} P(X = l)\,P(Y = k - l) = \sum_{l}\binom{n}{l}\binom{m}{k-l}p^k q^{n+m-k}
$$

By Vandermonde's identity, $\sum_l \binom{n}{l}\binom{m}{k-l} = \binom{n+m}{k}$, confirming $X+Y \sim \text{Bin}(n+m, p)$.

### When Independence Fails

Consider $n$ people, each with an independently uniform birthday out of 365 days. For each pair $(i,j)$, let $I_{ij} = \mathbf{1}(\text{same birthday})$. Each $I_{ij} \sim \text{Bern}(1/365)$, but the total

$$
X = \sum_{i < j} I_{ij}
$$

is **not** Binomial because the indicators are dependent: if persons 1,2 share a birthday and persons 1,3 share a birthday, then 2,3 must also share a birthday.

## Examples

**Example.** $X \sim \text{Bin}(10, 0.3)$, $Y \sim \text{Bin}(15, 0.3)$, independent. Then $X + Y \sim \text{Bin}(25, 0.3)$.

$$
P(X + Y = 8) = \binom{25}{8}(0.3)^8(0.7)^{17}
$$

```python
from math import comb
from scipy.stats import binom

# X ~ Bin(10, 0.3), Y ~ Bin(15, 0.3), independent
n1, n2, p = 10, 15, 0.3
k = 8

# Direct from Bin(25, 0.3)
direct = binom.pmf(k, n1 + n2, p)

# Convolution
conv = sum(binom.pmf(l, n1, p) * binom.pmf(k - l, n2, p)
           for l in range(min(k, n1) + 1) if k - l <= n2)

print(f"P(X+Y = {k}):")
print(f"  Bin({n1+n2}, {p}): {direct:.6f}")
print(f"  Convolution:    {conv:.6f}")
print(f"  Match: {abs(direct - conv) < 1e-10}")
```
