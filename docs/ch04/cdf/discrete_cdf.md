# Discrete CDF

The CDF of a discrete random variable is a right-continuous step function whose jumps encode the PMF.

## Definition

For a discrete random variable $X$ with PMF $p_X(x_i) = P(X = x_i)$, the CDF is

$$
F_X(x) = P(X \le x) = \sum_{x_i \le x} p_X(x_i)
$$

This is a **step function** that jumps at each value $x_i$ by the amount $p_X(x_i)$.

## Explanation

### Shape

- Flat between consecutive support points: if $x_i < x_{i+1}$ and $x_i < x < x_{i+1}$, then $F(x)$ is constant
- Jumps upward at each $x_i$ by exactly $P(X = x_i)$
- Starts at 0 (below the smallest value) and reaches 1 (at or above the largest value)

### Recovering the PMF

Given the CDF, the PMF is recovered from the jump sizes:

$$
p_X(x_i) = F(x_i) - F(x_i^-)
$$

This means the CDF and PMF carry exactly the same information.

### Standard Discrete CDFs

**Bernoulli** $X \sim \text{Bern}(p)$:

$$
F(x) = \begin{cases} 0 & x < 0 \\ 1-p & 0 \le x < 1 \\ 1 & x \ge 1 \end{cases}
$$

Two jumps: size $1-p$ at $x = 0$, size $p$ at $x = 1$.

**Geometric** $X \sim \text{Geo}(p)$:

$$
F(k) = 1 - (1-p)^k, \quad k = 1, 2, 3, \ldots
$$

Infinitely many jumps, each smaller than the last: $P(X = k) = p(1-p)^{k-1}$.

## Examples

**Example.** $X \sim \text{Bin}(3, 0.5)$.

| $k$ | $P(X=k)$ | $F(k) = P(X \le k)$ |
|:---:|:---------:|:--------------------:|
| 0 | 1/8 | 1/8 |
| 1 | 3/8 | 4/8 |
| 2 | 3/8 | 7/8 |
| 3 | 1/8 | 8/8 |

Then $P(1 \le X \le 2) = F(2) - F(0) = 7/8 - 1/8 = 6/8 = 3/4$.

Equivalently: $P(X=1) + P(X=2) = 3/8 + 3/8 = 3/4$.

```python
from math import comb

# Binomial(3, 0.5) CDF
n, p = 3, 0.5
print("k  P(X=k)  F(k)")
cum = 0
for k in range(n + 1):
    pmf = comb(n, k) * p**k * (1-p)**(n-k)
    cum += pmf
    print(f"{k}  {pmf:.4f}  {cum:.4f}")

# P(1 <= X <= 2) two ways
F_2 = sum(comb(n,k) * p**k * (1-p)**(n-k) for k in range(3))
F_0 = (1-p)**n
print(f"\nP(1 <= X <= 2) = F(2) - F(0) = {F_2 - F_0:.4f}")
```
