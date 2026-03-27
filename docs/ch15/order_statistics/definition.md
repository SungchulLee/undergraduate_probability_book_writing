# Definition and Notation

## Order Statistics

!!! info "Order Statistics"
    Let $X_1, X_2, \ldots, X_n$ be a random sample (iid) from a continuous distribution with CDF $F$ and PDF $f$. The **order statistics** are the sample values arranged in increasing order:

    $$X_{(1)} \leq X_{(2)} \leq \cdots \leq X_{(n)}$$

    where $X_{(k)}$ denotes the $k$-th smallest value.

The parentheses in the subscript distinguish order statistics from the original sample: $X_3$ is the third observation drawn, while $X_{(3)}$ is the third smallest observation.

## Key Terminology

| Symbol | Name | Definition |
|:---:|:---|:---|
| $X_{(1)}$ | Minimum | Smallest observation |
| $X_{(n)}$ | Maximum | Largest observation |
| $X_{(k)}$ | $k$-th order statistic | $k$-th smallest value |
| $R = X_{(n)} - X_{(1)}$ | Range | Spread of the sample |
| $X_{(\lceil n/2 \rceil)}$ | Sample median | Middle value (odd $n$) |

For even $n$, the sample median is typically defined as $\frac{1}{2}\bigl(X_{(n/2)} + X_{(n/2+1)}\bigr)$.

## Intuition

Sorting a sample destroys the information about **which** observation took which value, but preserves information about the **distribution** of values. Order statistics capture the shape of the sample: where the smallest values lie, where the largest lie, and how spread out the data are.

## Simple Example

??? example "Example: Sorting Five Observations"
    Suppose $n = 5$ observations drawn from $U(0, 1)$ yield:

    $$X_1 = 0.73, \; X_2 = 0.15, \; X_3 = 0.91, \; X_4 = 0.42, \; X_5 = 0.58$$

    The order statistics are:

    $$X_{(1)} = 0.15, \; X_{(2)} = 0.42, \; X_{(3)} = 0.58, \; X_{(4)} = 0.73, \; X_{(5)} = 0.91$$

    - Minimum: $X_{(1)} = 0.15$
    - Maximum: $X_{(5)} = 0.91$
    - Median: $X_{(3)} = 0.58$
    - Range: $R = 0.91 - 0.15 = 0.76$

## Continuity Assumption

We assume the underlying distribution is **continuous**, which guarantees $P(X_i = X_j) = 0$ for $i \neq j$. This means ties occur with probability zero, and the strict inequalities $X_{(1)} < X_{(2)} < \cdots < X_{(n)}$ hold almost surely.

## Relationship to Quantiles

The $k$-th order statistic from a sample of size $n$ estimates the $\frac{k}{n+1}$-quantile of the underlying distribution. As $n \to \infty$, the order statistics trace out the CDF:

$$X_{(k)} \approx F^{-1}\!\left(\frac{k}{n+1}\right)$$

This connection motivates **Q-Q plots**, which compare sample order statistics against theoretical quantiles to assess goodness of fit.

## Python Implementation

```python
import numpy as np

np.random.seed(42)
n = 5
X = np.random.uniform(0, 1, n)

print(f"Original sample: {X.round(4)}")
order_stats = np.sort(X)
print(f"Order statistics: {order_stats.round(4)}")
print(f"  Minimum X_(1) = {order_stats[0]:.4f}")
print(f"  Maximum X_(5) = {order_stats[-1]:.4f}")
print(f"  Median  X_(3) = {order_stats[2]:.4f}")
print(f"  Range         = {order_stats[-1] - order_stats[0]:.4f}")
```

**Output:**
```
Original sample: [0.3745 0.9507 0.7320 0.5987 0.1560]
Order statistics: [0.1560 0.3745 0.5987 0.7320 0.9507]
  Minimum X_(1) = 0.1560
  Maximum X_(5) = 0.9507
  Median  X_(3) = 0.5987
  Range         = 0.7947
```
