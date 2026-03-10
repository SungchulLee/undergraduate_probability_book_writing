# Order Statistics: Definition and Notation

Order statistics are the values of a random sample rearranged in increasing order, providing the natural framework for studying the minimum, maximum, median, range, and quantiles of a sample.

## Definition

Let $X_1, X_2, \ldots, X_n$ be iid continuous random variables with common CDF $F$ and PDF $f$. The **order statistics** are the values sorted in non-decreasing order:

$$
X_{(1)} \leq X_{(2)} \leq \cdots \leq X_{(n)}
$$

where $X_{(k)}$ denotes the $k$-th smallest value. In particular:

- $X_{(1)} = \min(X_1, \ldots, X_n)$ is the **sample minimum**
- $X_{(n)} = \max(X_1, \ldots, X_n)$ is the **sample maximum**
- $X_{(\lceil n/2 \rceil)}$ is the **sample median** (for odd $n$)

The **range** is $X_{(n)} - X_{(1)}$ and the **midrange** is $(X_{(1)} + X_{(n)})/2$.

## Explanation

### Distinction between the sample and the order statistics

The original sample $X_1, \ldots, X_n$ is an unordered collection of iid random variables. The order statistics $X_{(1)}, \ldots, X_{(n)}$ are the same values rearranged. The order statistics are **not independent** -- knowing $X_{(1)} = 3$ constrains $X_{(2)} \geq 3$, for instance.

### CDF of a general order statistic

The CDF of $X_{(k)}$ can be expressed using the binomial distribution. The event $\{X_{(k)} \leq x\}$ occurs when at least $k$ of the $n$ values fall at or below $x$. Each value falls below $x$ independently with probability $F(x)$, so:

$$
F_{X_{(k)}}(x) = P(X_{(k)} \leq x) = \sum_{j=k}^{n} \binom{n}{j} [F(x)]^j [1 - F(x)]^{n-j}
$$

This is the tail of a Binomial$(n, F(x))$ distribution.

### Connection to empirical CDF

The **empirical CDF** of the sample is $\hat{F}_n(x) = \frac{1}{n}\sum_{i=1}^n \mathbf{1}(X_i \leq x)$. The order statistics are the jump points of $\hat{F}_n$: the function increases by $1/n$ at each $X_{(k)}$.

### Spacings

The **spacings** between consecutive order statistics are:

$$
D_k = X_{(k)} - X_{(k-1)}, \quad k = 2, \ldots, n
$$

with $D_1 = X_{(1)} - a$ if the support starts at $a$. For Uniform$(0,1)$ order statistics, the spacings have a particularly elegant joint distribution (related to the Dirichlet distribution).

### Why continuous distributions are assumed

For continuous distributions, $P(X_i = X_j) = 0$ for $i \neq j$, so with probability 1 all values are distinct and the ordering is strict: $X_{(1)} < X_{(2)} < \cdots < X_{(n)}$. This simplifies the theory considerably.

## Examples

**Example 1: Order statistics of a small sample.**

Draw $n = 5$ values from $\text{Exp}(1)$ and display the original sample and order statistics.

```python
import numpy as np

np.random.seed(42)
n = 5
X = np.random.exponential(1, n)

print("Original sample:", [f"{x:.4f}" for x in X])
print("Order statistics:", [f"{x:.4f}" for x in np.sort(X)])
print(f"Minimum X_(1) = {np.min(X):.4f}")
print(f"Maximum X_(5) = {np.max(X):.4f}")
print(f"Median  X_(3) = {np.sort(X)[2]:.4f}")
print(f"Range = {np.max(X) - np.min(X):.4f}")
```

**Output:**
```
Original sample: ['0.3745', '1.2592', '0.0319', '0.4012', '2.2029']
Order statistics: ['0.0319', '0.3745', '0.4012', '1.2592', '2.2029']
Minimum X_(1) = 0.0319
Maximum X_(5) = 2.2029
Median  X_(3) = 0.4012
Range = 2.1710
```

**Example 2: CDF of an order statistic via the binomial formula.**

For $n = 4$ iid $U(0,1)$ variables, compute $P(X_{(2)} \leq 0.5)$.

$$
P(X_{(2)} \leq 0.5) = \sum_{j=2}^{4} \binom{4}{j} (0.5)^j (0.5)^{4-j} = \sum_{j=2}^{4} \binom{4}{j} (0.5)^4
$$

```python
import numpy as np
from scipy.special import comb

n, k, x = 4, 2, 0.5
F_x = x  # CDF of U(0,1) at 0.5

# Binomial CDF formula
prob = sum(comb(n, j, exact=True) * F_x**j * (1-F_x)**(n-j) for j in range(k, n+1))
print(f"P(X_(2) <= 0.5) = {prob:.4f}")

# Verify by simulation
np.random.seed(42)
n_sim = 100000
samples = np.sort(np.random.uniform(0, 1, (n_sim, n)), axis=1)
p_sim = np.mean(samples[:, k-1] <= x)
print(f"Simulated:        {p_sim:.4f}")
```

**Output:**
```
P(X_(2) <= 0.5) = 0.6875
Simulated:        0.6882
```

**Example 3: Distribution of the sample median.**

For $n = 5$ iid $\text{Exp}(1)$ variables, simulate the distribution of $X_{(3)}$ (the median).

```python
import numpy as np
from scipy import stats

np.random.seed(42)
n, k = 5, 3
n_sim = 100000

samples = np.sort(np.random.exponential(1, (n_sim, n)), axis=1)
medians = samples[:, k-1]

print(f"Sample median X_(3) from Exp(1), n = {n}:")
print(f"  Mean:   {medians.mean():.4f}")
print(f"  Median: {np.median(medians):.4f}")
print(f"  Std:    {medians.std():.4f}")

# True median of Exp(1) is ln(2) = 0.693
print(f"  Population median = ln(2) = {np.log(2):.4f}")
```

**Output:**
```
Sample median X_(3) from Exp(1), n = 5:
  Mean:   0.7862
  Median: 0.7058
  Std:    0.4023
  Population median = ln(2) = 0.6931
```
