# Linearity of Expectation

Linearity of expectation holds regardless of dependence — this makes it one of the most powerful tools in probability.

## Definition

For any random variables $X_1, \ldots, X_n$ and constants $a_1, \ldots, a_n, b$:

$$
E\!\left[\sum_{i=1}^n a_i X_i + b\right] = \sum_{i=1}^n a_i\,E[X_i] + b
$$

!!! note "No independence required"
    Linearity holds whether the variables are independent, dependent, or anything in between.

## Explanation

### Proof Sketch

$$
E[X + Y] = \sum_x \sum_y (x+y)\,p(x,y) = \sum_x x\,p_X(x) + \sum_y y\,p_Y(y) = E[X] + E[Y]
$$

The joint distribution is needed for the first step, but it cancels when we split and marginalize.

### Strategy

Linearity turns hard expectations into easy ones. Express a complicated random variable as a sum of simple pieces, then take expectations term by term. The pieces can be dependent — linearity doesn't care.

## Examples

**Example 1 (Binomial mean).** $S \sim \text{Bin}(n, p)$. Write $S = \sum_{i=1}^n X_i$ where $X_i \sim \text{Bern}(p)$. Then $E[S] = np$.

**Example 2 (Coupon collector).** To collect all $n$ coupon types: $T = \sum_{i=1}^n \tau_i$ where $\tau_i \sim \text{Geo}((n-i+1)/n)$.

$$
E[T] = \sum_{i=1}^n \frac{n}{n-i+1} = n\sum_{k=1}^n \frac{1}{k} = nH_n \approx n\ln n
$$

**Example 3 (Birthday pairs).** Among $n$ people with uniform random birthdays, the number of pairs sharing a birthday is $S = \sum_{i<j} \mathbf{1}_{A_{ij}}$. The indicators are **dependent**, but:

$$
E[S] = \binom{n}{2}\frac{1}{365}
$$

```python
import numpy as np
from math import comb

# Binomial mean
n, p = 20, 0.3
print(f"E[Bin({n},{p})] = {n*p}")

# Coupon collector
n = 50
E_coupon = sum(n / k for k in range(1, n+1))
print(f"E[coupon collector, n={n}] = {E_coupon:.2f}")
print(f"n*ln(n) = {n * np.log(n):.2f}")

# Birthday pairs
n_people = 30
E_pairs = comb(n_people, 2) / 365
print(f"E[birthday pairs, {n_people} people] = {E_pairs:.4f}")
```
