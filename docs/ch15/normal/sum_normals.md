# Sum of Independent Normals

The sum of independent normal random variables is again normal, with the means and variances adding. This closure property makes the normal family exceptionally tractable in applications.

## Definition

If $X \sim N(\mu_1, \sigma_1^2)$ and $Y \sim N(\mu_2, \sigma_2^2)$ are **independent**, then:

$$
X + Y \sim N(\mu_1 + \mu_2, \; \sigma_1^2 + \sigma_2^2)
$$

More generally, for independent $X_1, \ldots, X_n$ with $X_i \sim N(\mu_i, \sigma_i^2)$:

$$
\sum_{i=1}^n X_i \sim N\!\left(\sum_{i=1}^n \mu_i, \; \sum_{i=1}^n \sigma_i^2\right)
$$

For any constants $a_1, \ldots, a_n$ and independent normals:

$$
\sum_{i=1}^n a_i X_i \sim N\!\left(\sum_{i=1}^n a_i \mu_i, \; \sum_{i=1}^n a_i^2 \sigma_i^2\right)
$$

## Explanation

### Proof via MGF

The MGF of $N(\mu, \sigma^2)$ is $M(t) = e^{\mu t + \sigma^2 t^2 / 2}$. For independent $X$ and $Y$:

$$
M_{X+Y}(t) = M_X(t) \cdot M_Y(t) = e^{\mu_1 t + \frac{1}{2}\sigma_1^2 t^2} \cdot e^{\mu_2 t + \frac{1}{2}\sigma_2^2 t^2} = e^{(\mu_1 + \mu_2)t + \frac{1}{2}(\sigma_1^2 + \sigma_2^2)t^2}
$$

This is the MGF of $N(\mu_1 + \mu_2, \sigma_1^2 + \sigma_2^2)$. By the uniqueness of moment generating functions, $X + Y$ has this distribution.

The proof extends to $n$ variables by induction or by multiplying $n$ MGFs.

### The difference of normals

Since $X - Y = X + (-Y)$ and $-Y \sim N(-\mu_2, \sigma_2^2)$, we have:

$$
X - Y \sim N(\mu_1 - \mu_2, \; \sigma_1^2 + \sigma_2^2)
$$

The variances **add** even when subtracting, because $\text{Var}(-Y) = \text{Var}(Y)$.

!!! warning "Independence Required"
    The sum of two normal random variables is **not necessarily normal** unless they are independent (or more generally, jointly normal). Counterexamples exist: if $X \sim N(0,1)$ and $Y = X \cdot \text{sign}(W)$ where $W$ is an independent standard normal, then $Y \sim N(0,1)$ but $X + Y$ takes the value $0$ or $2X$, which is not normally distributed.

### Special cases for iid normals

For iid $X_1, \ldots, X_n \sim N(\mu, \sigma^2)$:

| Quantity | Distribution |
|----------|-------------|
| Sum $S_n = \sum_{i=1}^n X_i$ | $N(n\mu, \; n\sigma^2)$ |
| Sample mean $\bar{X}_n = S_n / n$ | $N(\mu, \; \sigma^2/n)$ |
| Standardized sum $\frac{S_n - n\mu}{\sigma\sqrt{n}}$ | $N(0, 1)$ exactly |

The sample mean $\bar{X}_n$ has the same mean as each individual $X_i$ but its variance shrinks by a factor of $n$. This is the foundation of statistical estimation: averaging reduces uncertainty.

### Connection to the Central Limit Theorem

For iid normals, the standardized sum is **exactly** $N(0, 1)$ for every $n$. The Central Limit Theorem says this is **approximately** true for sums of non-normal random variables as $n \to \infty$. The normal distribution is the unique fixed point of this standardization-and-summation operation.

## Examples

**Example 1: Sum of two normals.**

Let $X \sim N(3, 4)$ and $Y \sim N(-1, 9)$ be independent. Find the distribution of $X + Y$.

$$
X + Y \sim N(3 + (-1), \; 4 + 9) = N(2, 13)
$$

```python
import numpy as np
from scipy import stats

np.random.seed(42)
n = 100000

X = np.random.normal(3, 2, n)   # N(3, 4) since sigma=2
Y = np.random.normal(-1, 3, n)  # N(-1, 9) since sigma=3
S = X + Y

print("X + Y ~ N(2, 13):")
print(f"  Simulated mean: {S.mean():.4f}  (expected: 2)")
print(f"  Simulated var:  {S.var():.4f}  (expected: 13)")

# Normality test
_, p_value = stats.shapiro(S[:5000])
print(f"  Shapiro-Wilk p-value: {p_value:.4f}")
```

**Output:**
```
X + Y ~ N(2, 13):
  Simulated mean: 1.9856  (expected: 2)
  Simulated var:  12.9932  (expected: 13)
  Shapiro-Wilk p-value: 0.5234
```

**Example 2: Difference of normals.**

Heights of men follow $M \sim N(178, 7^2)$ cm and heights of women follow $W \sim N(164, 6^2)$ cm. For a random independent couple, find $P(M > W)$.

$$
M - W \sim N(178 - 164, \; 49 + 36) = N(14, 85)
$$

$$
P(M > W) = P(M - W > 0) = P\!\left(Z > \frac{0 - 14}{\sqrt{85}}\right) = \Phi\!\left(\frac{14}{\sqrt{85}}\right)
$$

```python
from scipy import stats
import numpy as np

mu_diff = 178 - 164
var_diff = 49 + 36
sigma_diff = np.sqrt(var_diff)

z = mu_diff / sigma_diff
p = stats.norm.cdf(z)
print(f"M - W ~ N({mu_diff}, {var_diff})")
print(f"P(M > W) = Phi({mu_diff}/{sigma_diff:.2f}) = Phi({z:.4f}) = {p:.4f}")
```

**Output:**
```
M - W ~ N(14, 85)
P(M > W) = Phi(14/9.22) = Phi(1.5185) = 0.9356
```

**Example 3: Sample mean.**

A factory produces bolts with weights $X_i \sim N(10, 0.04)$ grams (iid). A sample of $n = 25$ bolts is taken. Find the probability the sample mean is within 0.05 grams of the true mean.

$$
\bar{X}_{25} \sim N\!\left(10, \; \frac{0.04}{25}\right) = N(10, 0.0016)
$$

$$
P(\lvert \bar{X} - 10 \rvert < 0.05) = P\!\left(\left\lvert Z \right\rvert < \frac{0.05}{0.04}\right) = P(\lvert Z \rvert < 1.25) = 2\Phi(1.25) - 1
$$

```python
from scipy import stats
import numpy as np

mu = 10
sigma_x = np.sqrt(0.04)  # sigma of individual bolts
n = 25
sigma_xbar = sigma_x / np.sqrt(n)

z = 0.05 / sigma_xbar
p = 2 * stats.norm.cdf(z) - 1
print(f"X_bar ~ N({mu}, {sigma_xbar**2:.4f})")
print(f"SD(X_bar) = {sigma_xbar:.4f}")
print(f"P(|X_bar - 10| < 0.05) = P(|Z| < {z:.2f}) = {p:.4f}")

# Verify by simulation
np.random.seed(42)
n_sim = 100000
means = np.array([np.random.normal(mu, sigma_x, n).mean() for _ in range(n_sim)])
p_sim = np.mean(np.abs(means - mu) < 0.05)
print(f"Simulated probability: {p_sim:.4f}")
```

**Output:**
```
X_bar ~ N(10, 0.0016)
SD(X_bar) = 0.0400
P(|X_bar - 10| < 0.05) = P(|Z| < 1.25) = 0.7887
Simulated probability: 0.7887
```

**Example 4: Weighted sum.**

Portfolio value: $V = 3X_1 + 2X_2 - X_3$ where $X_1 \sim N(10, 4)$, $X_2 \sim N(5, 1)$, $X_3 \sim N(8, 9)$ are independent.

$$
V \sim N(3(10) + 2(5) - 8, \; 9(4) + 4(1) + 1(9)) = N(32, 49)
$$

```python
from scipy import stats
import numpy as np

mu_V = 3*10 + 2*5 - 8
var_V = 9*4 + 4*1 + 1*9
sigma_V = np.sqrt(var_V)

print(f"V = 3*X1 + 2*X2 - X3 ~ N({mu_V}, {var_V})")
print(f"E[V] = {mu_V}, SD(V) = {sigma_V}")

# P(V > 40)
z = (40 - mu_V) / sigma_V
p = 1 - stats.norm.cdf(z)
print(f"P(V > 40) = 1 - Phi({z:.4f}) = {p:.4f}")

# Simulate
np.random.seed(42)
n_sim = 100000
X1 = np.random.normal(10, 2, n_sim)
X2 = np.random.normal(5, 1, n_sim)
X3 = np.random.normal(8, 3, n_sim)
V_sim = 3*X1 + 2*X2 - X3
print(f"\nSimulated: mean = {V_sim.mean():.2f}, var = {V_sim.var():.2f}")
print(f"P(V > 40) simulated = {np.mean(V_sim > 40):.4f}")
```

**Output:**
```
V = 3*X1 + 2*X2 - X3 ~ N(32, 49)
E[V] = 32, SD(V) = 7.0
P(V > 40) = 1 - Phi(1.1429) = 0.1265

Simulated: mean = 32.02, var = 49.17
P(V > 40) simulated = 0.1268
```
