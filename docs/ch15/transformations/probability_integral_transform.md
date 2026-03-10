# Probability Integral Transform

The probability integral transform states that applying a continuous CDF to its own random variable always produces a standard uniform, and conversely, the inverse CDF applied to a uniform produces any desired distribution -- providing a universal simulation method.

## Definition

**Probability Integral Transform.** If $X$ is a continuous random variable with CDF $F$, then:

$$
F(X) \sim U(0, 1)
$$

**Inverse Transform Method.** Conversely, if $U \sim U(0, 1)$ and $F$ is any continuous CDF, then:

$$
X = F^{-1}(U) \sim F
$$

That is, $X$ has CDF $F$. For non-continuous distributions, the generalized inverse $F^{-1}(u) = \inf\{x : F(x) \geq u\}$ is used.

## Explanation

### Proof of the probability integral transform

Let $U = F(X)$. Since $F$ is continuous and strictly increasing on the support of $X$:

$$
P(U \leq u) = P(F(X) \leq u) = P(X \leq F^{-1}(u)) = F(F^{-1}(u)) = u
$$

for $0 < u < 1$. This is the CDF of $U(0, 1)$.

### Proof of the inverse transform method

Let $X = F^{-1}(U)$ where $U \sim U(0, 1)$. Then:

$$
P(X \leq x) = P(F^{-1}(U) \leq x) = P(U \leq F(x)) = F(x)
$$

So $X$ has CDF $F$.

### Geometric interpretation

The inverse transform method works by:

1. Draw a horizontal line at a random height $U$ between 0 and 1.
2. Find where this line intersects the CDF curve $F$.
3. Read off the corresponding $x$-value.

Where the CDF is steep (high density), many $U$-values map to a narrow range of $x$-values, naturally producing more samples in high-density regions. Where the CDF is flat (low density), $U$-values are spread over a wide range.

### Practical implementation

The inverse transform method requires an explicit formula for $F^{-1}$. This is available for:

- **Exponential:** $F^{-1}(u) = -\frac{1}{\lambda}\ln(1 - u)$
- **Uniform:** $F^{-1}(u) = a + (b - a)u$
- **Pareto:** $F^{-1}(u) = x_m(1 - u)^{-1/\alpha}$
- **Cauchy:** $F^{-1}(u) = \tan(\pi(u - 1/2))$

### When no closed form exists

For distributions where $F^{-1}$ has no closed form (Normal, Gamma, Beta), alternative approaches include:

- **Numerical inversion:** Solve $F(x) = u$ using root-finding algorithms.
- **Accept-reject methods:** Generate candidates and filter.
- **Specialized transforms:** The Box-Muller transform for Normal, ratio-of-uniforms for Gamma.
- **Composition:** Decompose into simpler distributions.

### Applications beyond simulation

The probability integral transform has applications beyond simulation:

- **Goodness-of-fit testing:** If data come from distribution $F$, then $F(X_1), \ldots, F(X_n)$ should look uniform.
- **Copulas:** The transform separates marginal distributions from dependence structure.
- **Quantile-quantile plots:** Comparing $F^{-1}(i/(n+1))$ to the ordered data.

## Examples

**Example 1: Simulating Exponential from Uniform.**

Generate $X \sim \text{Exp}(\lambda)$ where $\lambda = 0.5$.

The CDF is $F(x) = 1 - e^{-\lambda x}$. Setting $u = F(x)$ and solving:

$$
X = F^{-1}(U) = -\frac{1}{\lambda}\ln(1 - U) = -2\ln(1 - U)
$$

Since $1 - U \sim U(0,1)$, we can simplify to $X = -2\ln(U)$.

```python
import numpy as np
from scipy import stats

np.random.seed(42)
n = 100000
lam = 0.5

U = np.random.uniform(0, 1, n)
X = -np.log(U) / lam  # Inverse CDF method

print(f"Inverse CDF: X = -ln(U)/{lam}")
print(f"  Mean: {X.mean():.4f}  (theory: {1/lam:.4f})")
print(f"  Var:  {X.var():.4f}  (theory: {1/lam**2:.4f})")

# Compare with direct scipy sampling
X_direct = np.random.exponential(1/lam, n)
print(f"\nDirect sampling:")
print(f"  Mean: {X_direct.mean():.4f}")
print(f"  Var:  {X_direct.var():.4f}")
```

**Output:**
```
Inverse CDF: X = -ln(U)/0.5
  Mean: 2.0045  (theory: 2.0000)
  Var:  4.0008  (theory: 4.0000)

Direct sampling:
  Mean: 2.0018
  Var:  3.9928
```

**Example 2: Verifying the probability integral transform.**

Take $X \sim \text{Exp}(2)$ and verify that $F(X) \sim U(0, 1)$.

```python
import numpy as np
from scipy import stats

np.random.seed(42)
n = 100000
lam = 2.0

X = np.random.exponential(1/lam, n)
U_transform = 1 - np.exp(-lam * X)  # F(X) = 1 - exp(-lambda*x)

print("F(X) where X ~ Exp(2):")
print(f"  Mean: {U_transform.mean():.4f}  (U(0,1) mean = 0.5000)")
print(f"  Var:  {U_transform.var():.4f}  (U(0,1) var = {1/12:.4f})")

# KS test against U(0,1)
ks_stat, p_val = stats.kstest(U_transform, 'uniform')
print(f"  KS test vs U(0,1): p-value = {p_val:.4f}")
```

**Output:**
```
F(X) where X ~ Exp(2):
  Mean: 0.4998  (U(0,1) mean = 0.5000)
  Var:  0.0833  (U(0,1) var = 0.0833)
  KS test vs U(0,1): p-value = 0.5467
```

**Example 3: Simulating Cauchy from Uniform.**

The Cauchy distribution has CDF $F(x) = \frac{1}{2} + \frac{1}{\pi}\arctan(x)$, so $F^{-1}(u) = \tan(\pi(u - 1/2))$.

```python
import numpy as np
from scipy import stats

np.random.seed(42)
n = 100000

U = np.random.uniform(0, 1, n)
X = np.tan(np.pi * (U - 0.5))  # Cauchy via inverse CDF

# Cauchy has no finite mean or variance, so check median and IQR
print("X = tan(pi*(U - 0.5)) should be Cauchy(0,1):")
print(f"  Median: {np.median(X):.4f}  (theory: 0)")
print(f"  IQR:    {np.percentile(X, 75) - np.percentile(X, 25):.4f}  (theory: 2.0000)")

ks_stat, p_val = stats.kstest(X, 'cauchy')
print(f"  KS test vs Cauchy: p-value = {p_val:.4f}")
```

**Output:**
```
X = tan(pi*(U - 0.5)) should be Cauchy(0,1):
  Median: 0.0016  (theory: 0)
  IQR:    2.0024  (theory: 2.0000)
  KS test vs Cauchy: p-value = 0.7123
```

**Example 4: Goodness-of-fit via the PIT.**

Test whether data come from a $N(5, 2^2)$ distribution by checking if $F(X_i)$ looks uniform.

```python
import numpy as np
from scipy import stats

np.random.seed(42)

# Generate data from N(5, 4)
data = np.random.normal(5, 2, 500)

# Apply the hypothesized CDF
U_transformed = stats.norm.cdf(data, loc=5, scale=2)

# KS test against U(0,1)
ks_stat, p_val = stats.kstest(U_transformed, 'uniform')
print(f"Test H0: data ~ N(5, 4)")
print(f"KS statistic: {ks_stat:.4f}, p-value: {p_val:.4f}")
print(f"Conclusion: {'Fail to reject H0' if p_val > 0.05 else 'Reject H0'}")

# Now test with wrong distribution
U_wrong = stats.norm.cdf(data, loc=3, scale=2)  # Wrong mean
ks_stat2, p_val2 = stats.kstest(U_wrong, 'uniform')
print(f"\nTest H0: data ~ N(3, 4) (wrong!)")
print(f"KS statistic: {ks_stat2:.4f}, p-value: {p_val2:.4f}")
print(f"Conclusion: {'Fail to reject H0' if p_val2 > 0.05 else 'Reject H0'}")
```

**Output:**
```
Test H0: data ~ N(5, 4)
KS statistic: 0.0298, p-value: 0.7612
Conclusion: Fail to reject H0

Test H0: data ~ N(3, 4) (wrong!)
KS statistic: 0.3845, p-value: 0.0000
Conclusion: Reject H0
```
