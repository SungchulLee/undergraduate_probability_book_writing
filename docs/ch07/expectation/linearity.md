# Linearity of Expectation

## Statement

For any random variables $X_1, X_2, \ldots, X_n$ (not necessarily independent) and constants $a_1, a_2, \ldots, a_n, b$:

$$

E\left[\sum_{i=1}^n a_i X_i + b\right] = \sum_{i=1}^n a_i E[X_i] + b

$$

In its simplest form, for two random variables:

$$

E[aX + bY + c] = aE[X] + bE[Y] + c

$$

!!! note "Key Insight"
    Linearity of expectation holds **regardless of whether the random variables are independent or dependent**. This makes it an extraordinarily powerful tool.

---

## Proof Sketch (Discrete Case)

For two random variables $X$ and $Y$:

$$

E[X + Y] = \sum_x \sum_y (x + y) \, p(x, y) = \sum_x \sum_y x \, p(x, y) + \sum_x \sum_y y \, p(x, y)

$$

The first sum equals $\sum_x x \, p_X(x) = E[X]$ and the second equals $\sum_y y \, p_Y(y) = E[Y]$.

---

## Applications

### Example 1: Expected Sum of Dice

Roll $n$ fair dice. Let $S = X_1 + X_2 + \cdots + X_n$ where each $X_i$ is the face value of the $i$-th die.

$$

E[S] = \sum_{i=1}^n E[X_i] = n \cdot 3.5

$$

For $n = 2$: $E[S] = 7$.

### Example 2: Binomial Mean via Linearity

If $S \sim \text{Binomial}(n, p)$, write $S = \sum_{i=1}^n X_i$ where $X_i \sim \text{Bernoulli}(p)$ are independent. Then:

$$

E[S] = \sum_{i=1}^n E[X_i] = np

$$

This is much simpler than computing $E[S] = \sum_{k=0}^n k \binom{n}{k} p^k (1-p)^{n-k}$ directly.

### Example 3: Negative Binomial Mean

If $S \sim \text{NB}(r, p)$, write $S = \sum_{i=1}^r X_i$ where $X_i \sim \text{Geo}(p)$ are independent. Then:

$$

E[S] = \sum_{i=1}^r E[X_i] = \frac{r}{p}

$$

### Example 4: Coupon Collector Mean

To collect all $n$ types of coupons, let $T_n = \sum_{i=1}^n \tau_i$ where $\tau_i \sim \text{Geo}\left(\frac{n-(i-1)}{n}\right)$. Then:

$$

E[T_n] = \sum_{i=1}^n E[\tau_i] = \sum_{i=1}^n \frac{n}{n-(i-1)} = n\sum_{k=1}^n \frac{1}{k} = nH_n \sim n \log n

$$

where $H_n = 1 + \frac{1}{2} + \frac{1}{3} + \cdots + \frac{1}{n}$ is the $n$-th harmonic number.

---

## Linearity with Dependent Random Variables

### Example: Birthday Pairs

There are $n$ people in a class, each choosing a birthday uniformly at random from 365 days. Let $S_n$ be the number of pairs sharing a birthday.

Let $\mathbf{1}_{A_{ij}}$ be the indicator that persons $i$ and $j$ share a birthday. Then:

$$

S_n = \sum_{1 \leq i < j \leq n} \mathbf{1}_{A_{ij}}

$$

The indicators are **not independent** (if $i$ shares a birthday with $j$ and $k$, then $j$ and $k$ are more likely to share a birthday). But by linearity:

$$

E[S_n] = \sum_{1 \leq i < j \leq n} E[\mathbf{1}_{A_{ij}}] = \binom{n}{2} \cdot \frac{1}{365}

$$

---

## Python Implementation

```python
import numpy as np
from math import comb

# Binomial mean via linearity
n, p = 20, 0.3
E_binomial = n * p
print(f"E[Binomial({n},{p})] = {E_binomial}")  # 6.0

# Negative binomial mean via linearity
r, p = 5, 0.4
E_negbin = r / p
print(f"E[NB({r},{p})] = {E_negbin}")  # 12.5

# Coupon collector mean
n = 50
harmonic_n = sum(1/k for k in range(1, n+1))
E_coupon = n * harmonic_n
print(f"E[coupon collector, n={n}] = {E_coupon:.2f}")
print(f"n*ln(n) approximation = {n * np.log(n):.2f}")

# Birthday pairs mean
n_people = 30
E_birthday_pairs = comb(n_people, 2) / 365
print(f"E[birthday pairs, {n_people} people] = {E_birthday_pairs:.4f}")

# Monte Carlo: verify linearity with dependent variables
np.random.seed(42)
N_sim = 100_000
count = 0
for _ in range(N_sim):
    birthdays = np.random.randint(0, 365, n_people)
    pairs = 0
    for i in range(n_people):
        for j in range(i+1, n_people):
            if birthdays[i] == birthdays[j]:
                pairs += 1
    count += pairs
mc_estimate = count / N_sim
print(f"Monte Carlo E[birthday pairs] = {mc_estimate:.4f}")
print(f"Exact E[birthday pairs] = {E_birthday_pairs:.4f}")
```
