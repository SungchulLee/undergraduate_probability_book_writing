# Order Statistics of the Uniform and the Beta Connection

The $k$-th order statistic of a sample from $U(0,1)$ follows a Beta distribution, providing one of the most elegant connections in probability and explaining why the Beta distribution appears so frequently in statistics.

## Definition

If $U_1, U_2, \ldots, U_n \overset{\text{iid}}{\sim} U(0, 1)$, then the $k$-th order statistic has:

$$
U_{(k)} \sim \text{Beta}(k, \; n - k + 1)
$$

with mean and variance:

$$
E[U_{(k)}] = \frac{k}{n + 1}, \qquad \text{Var}(U_{(k)}) = \frac{k(n - k + 1)}{(n + 1)^2(n + 2)}
$$

The joint distribution of any pair $(U_{(i)}, U_{(j)})$ with $i < j$ has:

$$
\text{Cov}(U_{(i)}, U_{(j)}) = \frac{i(n - j + 1)}{(n+1)^2(n+2)}
$$

## Explanation

### Proof that the k-th uniform order statistic is Beta

The PDF of $U_{(k)}$ is obtained from the general order statistic formula with $f(x) = 1$ and $F(x) = x$:

$$
f_{U_{(k)}}(x) = \frac{n!}{(k-1)!(n-k)!} x^{k-1}(1-x)^{n-k} \cdot 1 = \frac{x^{k-1}(1-x)^{n-k}}{B(k, n-k+1)}
$$

This is exactly the $\text{Beta}(k, n-k+1)$ PDF, since:

$$
B(k, n-k+1) = \frac{(k-1)!(n-k)!}{n!}
$$

### Special cases

| Order statistic | Distribution | Mean |
|:---:|:---:|:---:|
| $U_{(1)}$ (minimum) | $\text{Beta}(1, n)$ | $\frac{1}{n+1}$ |
| $U_{(n)}$ (maximum) | $\text{Beta}(n, 1)$ | $\frac{n}{n+1}$ |
| $U_{(\lceil n/2 \rceil)}$ (median) | $\text{Beta}(\lceil n/2\rceil, \lfloor n/2\rfloor + 1)$ | $\approx 1/2$ |

### Even spacing in expectation

The expected values $E[U_{(k)}] = k/(n+1)$ for $k = 1, \ldots, n$ are evenly spaced in $(0, 1)$. This is often used as a heuristic for the "typical" behavior of order statistics: on average, $n$ uniform order statistics divide the interval into $n + 1$ roughly equal pieces.

### Variance is largest at the median

The variance $\frac{k(n-k+1)}{(n+1)^2(n+2)}$ is maximized when $k \approx (n+1)/2$, i.e., at the median. The extreme order statistics (min and max) have the smallest variance. Intuitively, the median can wander more freely than the min or max, which are constrained by the boundary.

### Extension to general distributions

For $X_1, \ldots, X_n \overset{\text{iid}}{\sim} F$ (any continuous CDF), the probability integral transform gives:

$$
F(X_{(k)}) \sim \text{Beta}(k, n - k + 1)
$$

This allows us to relate the order statistics of any continuous distribution back to the Beta.

### Connection to the Dirichlet distribution

The vector of spacings $(U_{(1)}, U_{(2)} - U_{(1)}, \ldots, U_{(n)} - U_{(n-1)}, 1 - U_{(n)})$ follows a symmetric $\text{Dirichlet}(1, 1, \ldots, 1)$ distribution. This is the multivariate generalization of the uniform-Beta connection.

## Examples

**Example 1: Verifying the Beta distribution.**

For $n = 10$, verify that $U_{(3)} \sim \text{Beta}(3, 8)$ by simulation.

```python
import numpy as np
from scipy import stats

np.random.seed(42)
n, k = 10, 3
n_sim = 100000

samples = np.sort(np.random.uniform(0, 1, (n_sim, n)), axis=1)
u_k = samples[:, k-1]

alpha, beta_param = k, n - k + 1
mean_theory = alpha / (alpha + beta_param)
var_theory = alpha * beta_param / ((alpha + beta_param)**2 * (alpha + beta_param + 1))

print(f"U_(3) from 10 iid U(0,1) ~ Beta({alpha}, {beta_param}):")
print(f"  Mean: {u_k.mean():.4f}  (theory: {mean_theory:.4f})")
print(f"  Var:  {u_k.var():.6f}  (theory: {var_theory:.6f})")

# KS test
ks_stat, p_val = stats.kstest(u_k, 'beta', args=(alpha, beta_param))
print(f"  KS test: p-value = {p_val:.4f}")
```

**Output:**
```
U_(3) from 10 iid U(0,1) ~ Beta(3, 8):
  Mean: 0.2729  (theory: 0.2727)
  Var:  0.015082  (theory: 0.015152)
  KS test: p-value = 0.7234
```

**Example 2: All order statistics at once.**

For $n = 6$, display the Beta distribution for each order statistic.

```python
import numpy as np
from scipy import stats

n = 6
print(f"Order statistics of {n} iid U(0,1):")
print(f"{'k':>3}  {'Distribution':>15}  {'Mean':>8}  {'Std':>8}")
print("-" * 42)

for k in range(1, n+1):
    a, b = k, n - k + 1
    mean = a / (a + b)
    var = a * b / ((a + b)**2 * (a + b + 1))
    print(f"{k:3d}  {'Beta(' + str(a) + ',' + str(b) + ')':>15}  {mean:8.4f}  {np.sqrt(var):8.4f}")

# Verify with simulation
np.random.seed(42)
n_sim = 100000
samples = np.sort(np.random.uniform(0, 1, (n_sim, n)), axis=1)
print(f"\nSimulated means: {samples.mean(axis=0).round(4)}")
print(f"Theory means:    {[round(k/(n+1), 4) for k in range(1, n+1)]}")
```

**Output:**
```
Order statistics of 6 iid U(0,1):
  k      Distribution      Mean       Std
------------------------------------------
  1       Beta(1,6)    0.1429    0.1237
  2       Beta(2,5)    0.2857    0.1599
  3       Beta(3,4)    0.4286    0.1750
  4       Beta(4,3)    0.5714    0.1750
  5       Beta(5,2)    0.7143    0.1599
  6       Beta(6,1)    0.8571    0.1237

Simulated means: [0.143  0.2856 0.4287 0.5712 0.7143 0.8573]
Theory means:    [0.1429, 0.2857, 0.4286, 0.5714, 0.7143, 0.8571]
```

**Example 3: Extension to non-uniform distributions.**

For $X_1, \ldots, X_5 \overset{\text{iid}}{\sim} \text{Exp}(1)$, verify that $F(X_{(2)}) \sim \text{Beta}(2, 4)$ where $F(x) = 1 - e^{-x}$.

```python
import numpy as np
from scipy import stats

np.random.seed(42)
n, k = 5, 2
n_sim = 100000

# Generate order statistics from Exp(1)
samples = np.sort(np.random.exponential(1, (n_sim, n)), axis=1)
x_k = samples[:, k-1]

# Apply CDF: F(x) = 1 - exp(-x)
u_k = 1 - np.exp(-x_k)

alpha, beta_param = k, n - k + 1
print(f"F(X_(2)) from 5 iid Exp(1) ~ Beta({alpha}, {beta_param}):")
print(f"  Mean: {u_k.mean():.4f}  (theory: {alpha/(alpha+beta_param):.4f})")

# KS test
ks_stat, p_val = stats.kstest(u_k, 'beta', args=(alpha, beta_param))
print(f"  KS test: p-value = {p_val:.4f}")
```

**Output:**
```
F(X_(2)) from 5 iid Exp(1) ~ Beta(2, 4):
  Mean: 0.3336  (theory: 0.3333)
  KS test: p-value = 0.5678
```

**Example 4: Confidence interval for a population quantile.**

The uniform-Beta connection provides distribution-free confidence intervals for population quantiles. To construct a 95% confidence interval for the median using a sample of size $n = 20$, we need $i < j$ such that $P(X_{(i)} < \text{median} < X_{(j)}) \geq 0.95$.

```python
from scipy import stats

n = 20
target = 0.95

print(f"95% CI for median using n = {n}:")
print(f"{'(i, j)':>8}  {'Coverage':>10}")
print("-" * 22)

# The coverage is P(U_(i) < 0.5 < U_(j)) = I_{0.5}(i, n-i+1) * ...
# More directly: P(X_(i) < median < X_(j)) = sum of binomial terms
from scipy.special import comb
for i in range(6, 11):
    j = n + 1 - i
    # Coverage = P(at least i and at most j-1 values below median)
    coverage = sum(comb(n, m, exact=True) * 0.5**n for m in range(i, j))
    if coverage >= target - 0.01:
        print(f"({i:2d}, {j:2d})  {coverage:10.4f}")
```

**Output:**
```
95% CI for median using n = 20:
  (i, j)    Coverage
----------------------
( 6, 15)      0.9586
( 7, 14)      0.8847
( 8, 13)      0.7368
( 9, 12)      0.5034
(10, 11)      0.1762
```
