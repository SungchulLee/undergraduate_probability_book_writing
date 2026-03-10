# Linear Combinations of Normals

A linear transformation of a normal random variable is again normal, with the mean and variance transforming according to simple rules.

## Definition

If $X \sim N(\mu, \sigma^2)$ and $a, b$ are constants with $a \neq 0$, then:

$$
aX + b \sim N(a\mu + b, \; a^2\sigma^2)
$$

That is, multiplying by $a$ scales the mean by $a$ and the variance by $a^2$, while adding $b$ shifts the mean by $b$ and leaves the variance unchanged.

## Explanation

### Proof via moment generating functions

The MGF of $X \sim N(\mu, \sigma^2)$ is $M_X(t) = e^{\mu t + \sigma^2 t^2/2}$. For $Y = aX + b$:

$$
M_Y(t) = E[e^{t(aX+b)}] = e^{bt} M_X(at) = e^{bt} \cdot e^{\mu(at) + \frac{1}{2}\sigma^2(at)^2} = e^{(a\mu + b)t + \frac{1}{2}a^2\sigma^2 t^2}
$$

This is the MGF of $N(a\mu + b, a^2\sigma^2)$. Since the MGF uniquely determines the distribution, $Y \sim N(a\mu + b, a^2\sigma^2)$.

### Special case: standardization

Taking $a = 1/\sigma$ and $b = -\mu/\sigma$ gives:

$$
Z = \frac{X - \mu}{\sigma} = \frac{1}{\sigma}X - \frac{\mu}{\sigma} \sim N\!\left(\frac{\mu}{\sigma} - \frac{\mu}{\sigma}, \; \frac{\sigma^2}{\sigma^2}\right) = N(0, 1)
$$

This confirms that standardization produces a standard normal.

### Special case: location-scale family

Every normal distribution can be obtained from the standard normal. If $Z \sim N(0, 1)$, then:

$$
X = \sigma Z + \mu \sim N(\mu, \sigma^2)
$$

This shows that the normal family is a **location-scale family** parameterized by $\mu$ (location) and $\sigma$ (scale).

### Why the variance scales by the square

The factor $a^2$ in the variance formula $\text{Var}(aX + b) = a^2 \text{Var}(X)$ is a general fact about variance, not specific to the normal. What is special about the normal is that the transformed variable remains normal -- this is not true for most distributions.

### Negation and reflection

Taking $a = -1$ and $b = 0$: if $X \sim N(\mu, \sigma^2)$, then $-X \sim N(-\mu, \sigma^2)$. In particular, if $Z \sim N(0, 1)$, then $-Z \sim N(0, 1)$, confirming the symmetry of the standard normal.

## Examples

**Example 1: Temperature conversion.**

Temperatures in a city follow $C \sim N(20, 5^2)$ in Celsius. Find the distribution in Fahrenheit, where $F = 1.8C + 32$.

$$
F = 1.8C + 32 \sim N(1.8 \times 20 + 32, \; 1.8^2 \times 25) = N(68, 81)
$$

So Fahrenheit temperatures follow $N(68, 9^2)$.

```python
from scipy import stats
import numpy as np

mu_C, sigma_C = 20, 5
a, b = 1.8, 32

mu_F = a * mu_C + b
sigma_F = abs(a) * sigma_C

print(f"Celsius:    N({mu_C}, {sigma_C}^2)")
print(f"Fahrenheit: N({mu_F}, {sigma_F}^2)")
print(f"            N({mu_F}, {sigma_F**2})")

# Verify by simulation
np.random.seed(42)
C_samples = np.random.normal(mu_C, sigma_C, 100000)
F_samples = a * C_samples + b
print(f"\nSimulated Fahrenheit: mean = {F_samples.mean():.2f}, std = {F_samples.std():.2f}")
print(f"Theoretical:          mean = {mu_F:.2f}, std = {sigma_F:.2f}")
```

**Output:**
```
Celsius:    N(20, 5^2)
Fahrenheit: N(68.0, 9.0^2)
            N(68.0, 81.0)

Simulated Fahrenheit: mean = 67.99, std = 9.00
Theoretical:          mean = 68.00, std = 9.00
```

**Example 2: Standardization.**

If $X \sim N(100, 15^2)$, verify that $Z = (X - 100)/15 \sim N(0, 1)$.

```python
import numpy as np
from scipy import stats

np.random.seed(42)
n = 100000
X = np.random.normal(100, 15, n)
Z = (X - 100) / 15

print("Z = (X - 100) / 15:")
print(f"  Mean: {Z.mean():.4f}  (expected: 0)")
print(f"  Std:  {Z.std():.4f}   (expected: 1)")

# Shapiro-Wilk test for normality
_, p_val = stats.shapiro(Z[:5000])
print(f"  Shapiro-Wilk p-value: {p_val:.4f}")
```

**Output:**
```
Z = (X - 100) / 15:
  Mean: -0.0001  (expected: 0)
  Std:  1.0004   (expected: 1)
  Shapiro-Wilk p-value: 0.3876
```

**Example 3: Profit from a random price.**

A commodity price follows $P \sim N(50, 6^2)$ dollars per unit. A trader's profit on 200 units is $\text{Profit} = 200P - 9000$. Find the probability the trader makes a positive profit.

$$
\text{Profit} = 200P - 9000 \sim N(200 \times 50 - 9000, \; 200^2 \times 36) = N(1000, 1440000)
$$

So $\text{Profit} \sim N(1000, 1200^2)$.

$$
P(\text{Profit} > 0) = P\!\left(Z > \frac{0 - 1000}{1200}\right) = P(Z > -0.833) = \Phi(0.833)
$$

```python
from scipy import stats

mu_P, sigma_P = 50, 6
a, b = 200, -9000

mu_profit = a * mu_P + b
sigma_profit = abs(a) * sigma_P

z = (0 - mu_profit) / sigma_profit
p = 1 - stats.norm.cdf(z)
print(f"Profit ~ N({mu_profit}, {sigma_profit}^2)")
print(f"P(Profit > 0) = P(Z > {z:.4f}) = {p:.4f}")
```

**Output:**
```
Profit ~ N(1000, 1200^2)
P(Profit > 0) = P(Z > -0.8333) = 0.7977
```
