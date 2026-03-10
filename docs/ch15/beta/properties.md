# Beta Distribution Properties

The Beta distribution encompasses a rich variety of shapes depending on its parameters, and its moments, mode, and symmetry properties all have clean closed-form expressions.

## Definition

For $X \sim \text{Beta}(\alpha, \beta)$, the key properties are:

$$
E[X] = \frac{\alpha}{\alpha + \beta}, \qquad \text{Var}(X) = \frac{\alpha\beta}{(\alpha + \beta)^2(\alpha + \beta + 1)}
$$

$$
\text{Mode} = \frac{\alpha - 1}{\alpha + \beta - 2} \quad (\text{for } \alpha, \beta > 1)
$$

$$
E[X^k] = \prod_{j=0}^{k-1} \frac{\alpha + j}{\alpha + \beta + j}
$$

The **reflection property** states: if $X \sim \text{Beta}(\alpha, \beta)$, then $1 - X \sim \text{Beta}(\beta, \alpha)$.

## Explanation

### Special cases

| Parameters | Distribution | PDF |
|:---:|:---:|:---:|
| $\alpha = 1, \beta = 1$ | $\text{Uniform}(0,1)$ | $f(x) = 1$ |
| $\alpha = n, \beta = 1$ | Power distribution | $f(x) = nx^{n-1}$ |
| $\alpha = 1, \beta = n$ | Reflected power | $f(x) = n(1-x)^{n-1}$ |
| $\alpha = \tfrac{1}{2}, \beta = \tfrac{1}{2}$ | Arcsine distribution | $f(x) = \frac{1}{\pi\sqrt{x(1-x)}}$ |

The $\text{Beta}(1,1) = \text{Uniform}(0,1)$ case is immediate: when $\alpha = \beta = 1$, the PDF is $f(x) = x^0(1-x)^0 / B(1,1) = 1$.

### Shape analysis

The shape of the Beta PDF depends on the parameter values relative to 1.

**Shape regimes:**

- $\alpha > 1, \beta > 1$: unimodal, bell-shaped on $(0, 1)$
- $\alpha < 1, \beta < 1$: U-shaped (bimodal at the boundaries)
- $\alpha = \beta$: symmetric about $x = 1/2$
- $\alpha > \beta$: skewed left (mass concentrated toward 1)
- $\alpha < \beta$: skewed right (mass concentrated toward 0)

**Mode.** For $\alpha, \beta > 1$, setting $f'(x) = 0$ yields $(\alpha - 1)(1 - x) = (\beta - 1)x$, so:

$$
\text{Mode} = \frac{\alpha - 1}{\alpha + \beta - 2}
$$

When $\alpha \leq 1$ or $\beta \leq 1$ the mode occurs at the boundary (0 or 1), and for $\alpha = \beta = 1$ every point is a mode.

### Higher moments

The $k$-th raw moment has a product formula that follows from the Beta function identity:

$$
E[X^k] = \frac{B(\alpha + k, \beta)}{B(\alpha, \beta)} = \prod_{j=0}^{k-1} \frac{\alpha + j}{\alpha + \beta + j}
$$

In particular:

$$
E[X] = \frac{\alpha}{\alpha + \beta}, \qquad E[X^2] = \frac{\alpha(\alpha+1)}{(\alpha+\beta)(\alpha+\beta+1)}
$$

### Skewness and kurtosis

$$
\gamma_1 = \frac{2(\beta - \alpha)\sqrt{\alpha + \beta + 1}}{(\alpha + \beta + 2)\sqrt{\alpha\beta}}
$$

When $\alpha = \beta$, the skewness is zero (the distribution is symmetric). The sign of $\beta - \alpha$ determines the direction of skew.

### Reflection property

If $X \sim \text{Beta}(\alpha, \beta)$, then $1 - X \sim \text{Beta}(\beta, \alpha)$.

*Proof.* Let $Y = 1 - X$. For $0 < y < 1$:

$$
P(Y \leq y) = P(X \geq 1 - y) = \int_{1-y}^{1} \frac{x^{\alpha-1}(1-x)^{\beta-1}}{B(\alpha,\beta)}\,dx
$$

Substituting $u = 1 - x$:

$$
= \int_0^{y} \frac{(1-u)^{\alpha-1}u^{\beta-1}}{B(\alpha,\beta)}\,du
$$

which is the CDF of $\text{Beta}(\beta, \alpha)$.

### Connection to order statistics

If $U_1, U_2, \ldots, U_n \overset{\text{iid}}{\sim} U(0,1)$ and $U_{(k)}$ is the $k$-th smallest value, then:

$$
U_{(k)} \sim \text{Beta}(k, n - k + 1)
$$

This deep connection is proved in the order statistics section.

### Bayesian conjugacy preview

The Beta distribution is the conjugate prior for the Binomial likelihood. If $p \sim \text{Beta}(\alpha, \beta)$ and $X \mid p \sim \text{Binomial}(n, p)$, then $p \mid X = k \sim \text{Beta}(\alpha + k, \beta + n - k)$. This is explored in detail in the Bayesian applications page.

## Examples

**Example 1: Shape regimes.**

Compare the PDF shapes for different parameter combinations.

```python
import numpy as np
from scipy import stats

x = np.linspace(0.001, 0.999, 500)
cases = [
    (0.5, 0.5, "U-shaped"),
    (1, 1, "Uniform"),
    (2, 5, "Right-skewed"),
    (5, 2, "Left-skewed"),
    (5, 5, "Symmetric bell"),
]

for a, b, desc in cases:
    mean = a / (a + b)
    var = a * b / ((a + b)**2 * (a + b + 1))
    print(f"Beta({a}, {b}) [{desc}]: mean = {mean:.3f}, var = {var:.4f}")
```

**Output:**
```
Beta(0.5, 0.5) [U-shaped]: mean = 0.500, var = 0.1250
Beta(1, 1) [Uniform]: mean = 0.500, var = 0.0833
Beta(2, 5) [Right-skewed]: mean = 0.286, var = 0.0255
Beta(5, 2) [Left-skewed]: mean = 0.714, var = 0.0255
Beta(5, 5) [Symmetric bell]: mean = 0.500, var = 0.0227
```

**Example 2: Mode calculation.**

For $X \sim \text{Beta}(5, 3)$, find the mean, mode, and verify by simulation.

$$
E[X] = \frac{5}{8} = 0.625, \qquad \text{Mode} = \frac{5 - 1}{5 + 3 - 2} = \frac{4}{6} = 0.667
$$

```python
import numpy as np
from scipy import stats

a, b = 5, 3
mean = a / (a + b)
mode = (a - 1) / (a + b - 2)
var = a * b / ((a + b)**2 * (a + b + 1))

print(f"Beta({a}, {b}):")
print(f"  Mean = {mean:.4f}")
print(f"  Mode = {mode:.4f}")
print(f"  Var  = {var:.4f}")

# Verify by simulation
np.random.seed(42)
samples = np.random.beta(a, b, 100000)
print(f"\nSimulated: mean = {samples.mean():.4f}, var = {samples.var():.4f}")
```

**Output:**
```
Beta(5, 3):
  Mean = 0.6250
  Mode = 0.6667
  Var  = 0.0260

Simulated: mean = 0.6253, var = 0.0261
```

**Example 3: Reflection property.**

Verify that if $X \sim \text{Beta}(2, 5)$, then $1 - X \sim \text{Beta}(5, 2)$.

```python
import numpy as np
from scipy import stats

np.random.seed(42)
n = 100000

X = np.random.beta(2, 5, n)
Y = 1 - X  # Should be Beta(5, 2)

print("X ~ Beta(2, 5):")
print(f"  Mean: {X.mean():.4f}  (theory: {2/7:.4f})")

print("1 - X ~ Beta(5, 2):")
print(f"  Mean: {Y.mean():.4f}  (theory: {5/7:.4f})")

# KS test comparing 1-X to Beta(5, 2)
ks_stat, p_val = stats.kstest(Y, 'beta', args=(5, 2))
print(f"  KS test p-value: {p_val:.4f}  (large p => good fit)")
```

**Output:**
```
X ~ Beta(2, 5):
  Mean: 0.2861  (theory: 0.2857)
1 - X ~ Beta(5, 2):
  Mean: 0.7139  (theory: 0.7143)
  KS test p-value: 0.8234  (large p => good fit)
```

**Example 4: Raw moments via the product formula.**

Compute $E[X^3]$ for $X \sim \text{Beta}(3, 2)$.

$$
E[X^3] = \frac{3}{5} \cdot \frac{4}{6} \cdot \frac{5}{7} = \frac{60}{210} = \frac{2}{7}
$$

```python
import numpy as np
from scipy import stats

a, b = 3, 2
# Product formula
E_X3 = (a/(a+b)) * ((a+1)/(a+b+1)) * ((a+2)/(a+b+2))
print(f"E[X^3] = {a}/{a+b} * {a+1}/{a+b+1} * {a+2}/{a+b+2} = {E_X3:.6f}")
print(f"       = {E_X3} = 2/7 = {2/7:.6f}")

# Verify by simulation
np.random.seed(42)
samples = np.random.beta(a, b, 100000)
print(f"Simulated E[X^3] = {np.mean(samples**3):.6f}")
```

**Output:**
```
E[X^3] = 3/5 * 4/6 * 5/7 = 0.285714
       = 0.2857142857142857 = 2/7 = 0.285714
Simulated E[X^3] = 0.285921
```
