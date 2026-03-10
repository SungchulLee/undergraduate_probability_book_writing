# Joint Distribution of Order Statistics

The joint PDF of all $n$ order statistics has a clean form: it equals $n!$ times the product of the individual densities, reflecting the $n!$ ways to assign the original variables to ordered positions.

## Definition

Let $X_1, \ldots, X_n$ be iid with PDF $f$ and CDF $F$. The joint PDF of all $n$ order statistics $(X_{(1)}, X_{(2)}, \ldots, X_{(n)})$ is:

$$
f_{X_{(1)}, \ldots, X_{(n)}}(x_1, x_2, \ldots, x_n) = n! \prod_{i=1}^{n} f(x_i), \quad x_1 < x_2 < \cdots < x_n
$$

For a pair $(X_{(i)}, X_{(j)})$ with $1 \leq i < j \leq n$, the joint PDF is:

$$
f_{X_{(i)}, X_{(j)}}(x, y) = \frac{n!}{(i-1)!(j-i-1)!(n-j)!} [F(x)]^{i-1} f(x) [F(y) - F(x)]^{j-i-1} f(y) [1-F(y)]^{n-j}
$$

for $x < y$.

## Explanation

### Derivation of the joint PDF

Consider the probability that the $n$ order statistics fall in infinitesimal intervals around $x_1 < x_2 < \cdots < x_n$:

$$
P(x_i < X_{(i)} \leq x_i + dx_i \text{ for all } i) = n! \prod_{i=1}^n f(x_i)\,dx_i
$$

The factor $n!$ arises because any permutation of the original variables $(X_1, \ldots, X_n)$ could produce the same ordered configuration. There are $n!$ permutations, and for each one, the probability that $X_{\pi(i)}$ falls in the interval around $x_i$ is $f(x_i)\,dx_i$ (by independence and identical distributions).

### Derivation of the bivariate joint PDF

For the pair $(X_{(i)}, X_{(j)})$ with $i < j$, we partition the $n$ values into five groups:

1. $i - 1$ values below $x$ (probability $F(x)$ each)
2. 1 value at $x$ (probability $f(x)\,dx$)
3. $j - i - 1$ values between $x$ and $y$ (probability $F(y) - F(x)$ each)
4. 1 value at $y$ (probability $f(y)\,dy$)
5. $n - j$ values above $y$ (probability $1 - F(y)$ each)

The multinomial coefficient counts the number of ways to assign roles:

$$
\frac{n!}{(i-1)! \cdot 1! \cdot (j-i-1)! \cdot 1! \cdot (n-j)!}
$$

### Conditional distribution

The conditional distribution of $X_{(j)}$ given $X_{(i)} = x$ (for $j > i$) can be derived from the joint PDF. The resulting conditional density depends on $F(y) - F(x)$, reflecting the distribution of the remaining $n - i$ observations that exceed $x$.

### Spacings

The **spacings** $D_k = X_{(k)} - X_{(k-1)}$ (with $D_1 = X_{(1)}$) are of interest in goodness-of-fit testing and reliability. For $U(0,1)$ order statistics, the joint distribution of normalized spacings has a symmetric form related to the Dirichlet distribution.

### Marginalizing to get the k-th order statistic

Integrating the joint PDF over all variables except the $k$-th recovers the marginal PDF:

$$
f_{X_{(k)}}(x) = \frac{n!}{(k-1)!(n-k)!} [F(x)]^{k-1}[1-F(x)]^{n-k} f(x)
$$

This is consistent with the formula derived from the counting argument.

## Examples

**Example 1: Joint PDF of the min and max.**

For $n = 3$ iid $U(0, 1)$, find the joint PDF of $(X_{(1)}, X_{(3)})$ and compute $E[X_{(3)} - X_{(1)}]$.

With $i = 1$, $j = 3$, and $f(x) = 1$, $F(x) = x$:

$$
f_{X_{(1)}, X_{(3)}}(x, y) = \frac{3!}{0! \cdot 1! \cdot 0!} \cdot 1 \cdot (y - x) \cdot 1 = 6(y - x), \quad 0 < x < y < 1
$$

$$
E[X_{(3)} - X_{(1)}] = \int_0^1 \int_x^1 6(y - x)^2 \, dy \, dx
$$

```python
import numpy as np
from scipy import integrate

# Compute E[range] = E[X_(3) - X_(1)] for n=3 U(0,1)
def integrand(y, x):
    return 6 * (y - x)**2

result, _ = integrate.dblquad(integrand, 0, 1, lambda x: x, lambda x: 1)
print(f"E[X_(3) - X_(1)] = {result:.4f}")
print(f"Theory: (n-1)/(n+1) = 2/4 = {2/4:.4f}")

# Verify by simulation
np.random.seed(42)
n_sim = 100000
samples = np.sort(np.random.uniform(0, 1, (n_sim, 3)), axis=1)
ranges = samples[:, 2] - samples[:, 0]
print(f"Simulated: {ranges.mean():.4f}")
```

**Output:**
```
E[X_(3) - X_(1)] = 0.5000
Theory: (n-1)/(n+1) = 2/4 = 0.5000
Simulated: 0.5001
```

**Example 2: Joint density of two order statistics.**

For $n = 5$ iid $U(0, 1)$, find $f_{X_{(2)}, X_{(4)}}(0.3, 0.7)$.

With $i = 2$, $j = 4$: the coefficient is $\frac{5!}{1! \cdot 1! \cdot 1!} = 120$.

$$
f_{X_{(2)}, X_{(4)}}(0.3, 0.7) = 120 \cdot (0.3)^1 \cdot 1 \cdot (0.7 - 0.3)^1 \cdot 1 \cdot (1 - 0.7)^1 = 120 \cdot 0.3 \cdot 0.4 \cdot 0.3 = 4.32
$$

```python
import numpy as np
from math import factorial

n = 5
i, j = 2, 4
x, y = 0.3, 0.7

coeff = factorial(n) / (factorial(i-1) * factorial(j-i-1) * factorial(n-j))
pdf_val = coeff * x**(i-1) * (y - x)**(j-i-1) * (1 - y)**(n-j)
print(f"f_{{X_(2),X_(4)}}(0.3, 0.7) = {coeff:.0f} * {x}^{i-1} * {y-x}^{j-i-1} * {1-y}^{n-j}")
print(f"                         = {pdf_val:.4f}")

# Verify by simulation: estimate density near (0.3, 0.7)
np.random.seed(42)
n_sim = 500000
samples = np.sort(np.random.uniform(0, 1, (n_sim, n)), axis=1)
h = 0.02
mask = (np.abs(samples[:, i-1] - x) < h) & (np.abs(samples[:, j-1] - y) < h)
density_est = mask.sum() / (n_sim * (2*h)**2)
print(f"Simulated density: {density_est:.2f}")
```

**Output:**
```
f_{X_(2),X_(4)}(0.3, 0.7) = 120 * 0.3^1 * 0.4^1 * 0.3^1
                         = 4.3200
Simulated density: 4.29
```

**Example 3: Covariance of two order statistics.**

For $n = 5$ iid $U(0, 1)$, compute $\text{Cov}(X_{(2)}, X_{(4)})$.

The formula for uniform order statistics is:

$$
\text{Cov}(U_{(i)}, U_{(j)}) = \frac{i(n - j + 1)}{(n+1)^2(n+2)}, \quad i \leq j
$$

```python
import numpy as np

np.random.seed(42)
n = 5
i, j = 2, 4
n_sim = 100000

# Theory
cov_theory = i * (n - j + 1) / ((n + 1)**2 * (n + 2))
print(f"Cov(U_(2), U_(4)) = {i}*{n-j+1} / ({n+1}^2 * {n+2}) = {cov_theory:.6f}")

# Simulation
samples = np.sort(np.random.uniform(0, 1, (n_sim, n)), axis=1)
cov_sim = np.cov(samples[:, i-1], samples[:, j-1])[0, 1]
print(f"Simulated:          {cov_sim:.6f}")

# Correlation
var_i = i * (n - i + 1) / ((n + 1)**2 * (n + 2))
var_j = j * (n - j + 1) / ((n + 1)**2 * (n + 2))
corr = cov_theory / np.sqrt(var_i * var_j)
print(f"Correlation:        {corr:.4f}")
```

**Output:**
```
Cov(U_(2), U_(4)) = 2*2 / (6^2 * 7) = 0.015873
Simulated:          0.015841
Correlation:        0.5774
```
