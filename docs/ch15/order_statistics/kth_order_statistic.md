# PDF of the k-th Order Statistic

The PDF of any order statistic $X_{(k)}$ can be derived by a counting argument that tracks how the $n$ observations split around the value $x$.

## Definition

Let $X_1, \ldots, X_n$ be iid with CDF $F$ and PDF $f$. The PDF of the $k$-th order statistic $X_{(k)}$ is:

$$
f_{X_{(k)}}(x) = \frac{n!}{(k-1)!(n-k)!} [F(x)]^{k-1} [1 - F(x)]^{n-k} f(x)
$$

This can also be written using the Beta function:

$$
f_{X_{(k)}}(x) = \frac{1}{B(k, n-k+1)} [F(x)]^{k-1} [1 - F(x)]^{n-k} f(x)
$$

The CDF is:

$$
F_{X_{(k)}}(x) = \sum_{j=k}^{n} \binom{n}{j} [F(x)]^j [1 - F(x)]^{n-j}
$$

## Explanation

### Derivation of the PDF

Consider the event $\{x < X_{(k)} \leq x + dx\}$ for infinitesimal $dx$. For this to happen, we need:

- Exactly $k - 1$ of the $n$ values fall below $x$ (each with probability $F(x)$)
- Exactly 1 value falls in $[x, x + dx]$ (probability $f(x)\,dx$)
- Exactly $n - k$ values fall above $x + dx$ (each with probability $1 - F(x)$)

The number of ways to assign these roles among the $n$ variables is:

$$
\frac{n!}{(k-1)! \cdot 1! \cdot (n-k)!}
$$

Therefore:

$$
f_{X_{(k)}}(x)\,dx = \frac{n!}{(k-1)!(n-k)!} [F(x)]^{k-1} \cdot f(x)\,dx \cdot [1 - F(x)]^{n-k}
$$

### Verification of special cases

**Minimum ($k = 1$):**

$$
f_{X_{(1)}}(x) = n[1 - F(x)]^{n-1} f(x)
$$

**Maximum ($k = n$):**

$$
f_{X_{(n)}}(x) = n[F(x)]^{n-1} f(x)
$$

Both match the formulas from the min/max section.

### Mean of the k-th order statistic

For a general distribution, the mean is:

$$
E[X_{(k)}] = \int_{-\infty}^{\infty} x \, f_{X_{(k)}}(x)\,dx
$$

For the uniform distribution on $(0, 1)$, this simplifies beautifully:

$$
E[U_{(k)}] = \frac{k}{n + 1}
$$

The order statistics of $U(0, 1)$ are evenly spaced in expectation.

### Variance of the k-th order statistic

For $U(0, 1)$:

$$
\text{Var}(U_{(k)}) = \frac{k(n - k + 1)}{(n + 1)^2(n + 2)}
$$

The variance is largest for the median (middle order statistic) and smallest for the extremes.

### The beta connection

Setting $p = F(x)$ in the CDF of $X_{(k)}$:

$$
F_{X_{(k)}}(x) = I_{F(x)}(k, n - k + 1)
$$

where $I_p(a, b)$ is the regularized incomplete beta function. This reveals the deep connection between order statistics and the Beta distribution, explored further in the uniform-beta page.

## Examples

**Example 1: PDF of the median.**

For $n = 5$ iid $U(0, 1)$, find the PDF of $X_{(3)}$ (the median).

$$
f_{X_{(3)}}(x) = \frac{5!}{2! \cdot 2!} x^2(1-x)^2 \cdot 1 = 30x^2(1-x)^2, \quad 0 < x < 1
$$

This is the $\text{Beta}(3, 3)$ PDF.

```python
import numpy as np
from scipy import stats

n, k = 5, 3

# Theory: Beta(k, n-k+1) = Beta(3, 3)
alpha, beta_param = k, n - k + 1
mean_theory = alpha / (alpha + beta_param)
var_theory = alpha * beta_param / ((alpha + beta_param)**2 * (alpha + beta_param + 1))

print(f"X_(3) from {n} iid U(0,1) ~ Beta({alpha}, {beta_param}):")
print(f"  E[X_(3)] = {mean_theory:.4f}")
print(f"  Var[X_(3)] = {var_theory:.4f}")

# Verify by simulation
np.random.seed(42)
n_sim = 100000
samples = np.sort(np.random.uniform(0, 1, (n_sim, n)), axis=1)
medians = samples[:, k-1]

print(f"  Simulated mean = {medians.mean():.4f}")
print(f"  Simulated var  = {medians.var():.4f}")
```

**Output:**
```
X_(3) from 5 iid U(0,1) ~ Beta(3, 3):
  E[X_(3)] = 0.5000
  Var[X_(3)] = 0.0357
  Simulated mean = 0.5000
  Simulated var  = 0.0357
```

**Example 2: Third-smallest of 7 exponentials.**

Let $X_1, \ldots, X_7 \sim \text{Exp}(1)$ iid. Find $E[X_{(3)}]$ by simulation and compare with the known formula.

For iid $\text{Exp}(1)$, $E[X_{(k)}] = \sum_{j=1}^{k} \frac{1}{n - j + 1} = H_n - H_{n-k}$ where $H_m = \sum_{i=1}^m 1/i$ is the harmonic number.

```python
import numpy as np

np.random.seed(42)
n, k = 7, 3
n_sim = 100000

samples = np.sort(np.random.exponential(1, (n_sim, n)), axis=1)
x_k = samples[:, k-1]

# Theory for Exp(1): E[X_(k)] = sum_{j=1}^{k} 1/(n-j+1)
E_theory = sum(1/(n - j + 1) for j in range(1, k+1))

print(f"X_(3) from 7 iid Exp(1):")
print(f"  E[X_(3)] = 1/{n} + 1/{n-1} + 1/{n-2}")
print(f"           = {1/7:.4f} + {1/6:.4f} + {1/5:.4f} = {E_theory:.4f}")
print(f"  Simulated mean = {x_k.mean():.4f}")
```

**Output:**
```
X_(3) from 7 iid Exp(1):
  E[X_(3)] = 1/7 + 1/6 + 1/5
           = 0.1429 + 0.1667 + 0.2000 = 0.5095
  Simulated mean = 0.5092
```

**Example 3: Comparing order statistic distributions.**

For $n = 10$ iid $U(0,1)$, plot the means and standard deviations of all order statistics.

```python
import numpy as np

n = 10
print(f"Order statistics of {n} iid U(0,1):")
print(f"{'k':>3}  {'E[X_(k)]':>10}  {'SD[X_(k)]':>10}")
print("-" * 28)

for k in range(1, n+1):
    mean = k / (n + 1)
    var = k * (n - k + 1) / ((n + 1)**2 * (n + 2))
    sd = np.sqrt(var)
    print(f"{k:3d}  {mean:10.4f}  {sd:10.4f}")
```

**Output:**
```
Order statistics of 10 iid U(0,1):
  k    E[X_(k)]   SD[X_(k)]
----------------------------
  1      0.0909      0.0830
  2      0.1818      0.1114
  3      0.2727      0.1286
  4      0.3636      0.1388
  5      0.4545      0.1437
  6      0.5455      0.1437
  7      0.6364      0.1388
  8      0.7273      0.1286
  9      0.8182      0.1114
 10      0.9091      0.0830
```
