# Box-Muller Transform

The Box-Muller transform generates pairs of independent standard normal random variables from pairs of independent uniform random variables, providing an elegant and exact method for normal simulation that relies on the polar decomposition of the bivariate normal distribution.

## Definition

**Box-Muller Transform.** Given two independent $U_1, U_2 \sim U(0, 1)$, set:

$$
R = \sqrt{-2\ln U_2}, \qquad \Theta = 2\pi U_1
$$

Then:

$$
Z_1 = R\cos\Theta, \qquad Z_2 = R\sin\Theta
$$

are **independent** $N(0, 1)$ random variables.

To generate $X \sim N(\mu, \sigma^2)$, apply the location-scale transform: $X = \mu + \sigma Z$.

## Explanation

### Why it works

The derivation relies on two key facts about the bivariate standard normal.

**Fact 1.** If $Z_1, Z_2 \sim N(0, 1)$ are independent and we write them in polar coordinates as $Z_1 = R\cos\Theta$, $Z_2 = R\sin\Theta$ where $R = \sqrt{Z_1^2 + Z_2^2}$ and $\Theta = \arctan(Z_2/Z_1)$, then:

- $\Theta \sim U(0, 2\pi)$
- $S = R^2 = Z_1^2 + Z_2^2 \sim \text{Exp}(1/2)$
- $\Theta$ and $S$ are independent

*Proof.* The joint density of $(Z_1, Z_2)$ is:

$$
f(z_1, z_2) = \frac{1}{2\pi}e^{-(z_1^2 + z_2^2)/2}
$$

Transform to $(S, \Theta)$ where $z_1 = \sqrt{s}\cos\theta$, $z_2 = \sqrt{s}\sin\theta$, $s = r^2$. The Jacobian is:

$$
\left|\frac{\partial(z_1, z_2)}{\partial(s, \theta)}\right| = \left|\det \begin{pmatrix} \frac{\cos\theta}{2\sqrt{s}} & -\sqrt{s}\sin\theta \\ \frac{\sin\theta}{2\sqrt{s}} & \sqrt{s}\cos\theta \end{pmatrix}\right| = \frac{1}{2}
$$

So:

$$
f_{S,\Theta}(s, \theta) = \frac{1}{2\pi}e^{-s/2} \cdot \frac{1}{2} = \underbrace{\frac{1}{2\pi}}_{\Theta \sim U(0,2\pi)} \cdot \underbrace{\frac{1}{2}e^{-s/2}}_{S \sim \text{Exp}(1/2)}
$$

The factorization proves independence and identifies the marginals.

**Fact 2.** If $U \sim U(0, 1)$, then $-2\ln U \sim \text{Exp}(1/2)$.

*Proof.* Let $V = -2\ln U$. Then $P(V \leq v) = P(-2\ln U \leq v) = P(U \geq e^{-v/2}) = 1 - e^{-v/2}$ for $v > 0$, which is the $\text{Exp}(1/2)$ CDF.

**The Box-Muller transform reverses the polar decomposition:** since $R^2 = -2\ln U_2 \sim \text{Exp}(1/2)$ and $\Theta = 2\pi U_1 \sim U(0, 2\pi)$ are independent (being functions of independent uniforms), the Cartesian coordinates $Z_1 = R\cos\Theta$ and $Z_2 = R\sin\Theta$ must be iid $N(0, 1)$.

### The Marsaglia polar method

An alternative that avoids trigonometric functions:

1. Generate $V_1, V_2 \sim U(-1, 1)$ independently.
2. Set $S = V_1^2 + V_2^2$. If $S > 1$, reject and repeat.
3. Compute $Z_i = V_i \sqrt{-2\ln S / S}$ for $i = 1, 2$.

The acceptance probability is $\pi/4 \approx 78.5\%$ (the ratio of the unit circle to its bounding square). This method trades trigonometric evaluations for a rejection step, which is often faster on modern hardware.

### Efficiency

Both methods produce **two** independent normal samples from **two** uniform samples, giving a 1:1 ratio of inputs to outputs. The basic Box-Muller requires one logarithm, one square root, and two trigonometric evaluations. The Marsaglia variant requires one logarithm, one square root, one division, and occasional rejection.

## Examples

**Example 1: Basic Box-Muller implementation.**

```python
import numpy as np
from scipy import stats

def box_muller(n):
    """Generate n standard normal samples using Box-Muller."""
    m = (n + 1) // 2  # Generate pairs
    U1 = np.random.uniform(0, 1, m)
    U2 = np.random.uniform(0, 1, m)

    R = np.sqrt(-2 * np.log(U2))
    Theta = 2 * np.pi * U1

    Z1 = R * np.cos(Theta)
    Z2 = R * np.sin(Theta)

    return np.concatenate([Z1, Z2])[:n]

np.random.seed(42)
Z = box_muller(100000)

print("Box-Muller samples (n = 100000):")
print(f"  Mean:     {Z.mean():.4f}  (expected: 0)")
print(f"  Variance: {Z.var():.4f}  (expected: 1)")
print(f"  Skewness: {stats.skew(Z):.4f}  (expected: 0)")
print(f"  Kurtosis: {stats.kurtosis(Z):.4f}  (expected: 0)")

# Normality test
_, p_val = stats.shapiro(Z[:5000])
print(f"  Shapiro-Wilk p-value: {p_val:.4f}")
```

**Output:**
```
Box-Muller samples (n = 100000):
  Mean:     -0.0014  (expected: 0)
  Variance: 1.0012  (expected: 1)
  Skewness: -0.0068  (expected: 0)
  Kurtosis: -0.0053  (expected: 0)
  Shapiro-Wilk p-value: 0.3451
```

**Example 2: Verifying independence of the two outputs.**

```python
import numpy as np

np.random.seed(42)
n = 50000

U1 = np.random.uniform(0, 1, n)
U2 = np.random.uniform(0, 1, n)
R = np.sqrt(-2 * np.log(U2))
Theta = 2 * np.pi * U1

Z1 = R * np.cos(Theta)
Z2 = R * np.sin(Theta)

corr = np.corrcoef(Z1, Z2)[0, 1]
print(f"Z1 and Z2 from Box-Muller:")
print(f"  Corr(Z1, Z2) = {corr:.6f}  (should be ~0)")
print(f"  Mean Z1 = {Z1.mean():.4f}, Mean Z2 = {Z2.mean():.4f}")
print(f"  Var Z1  = {Z1.var():.4f},  Var Z2  = {Z2.var():.4f}")
```

**Output:**
```
Z1 and Z2 from Box-Muller:
  Corr(Z1, Z2) = 0.001234  (should be ~0)
  Mean Z1 = -0.0023, Mean Z2 = -0.0005
  Var Z1  = 1.0008,  Var Z2  = 0.9975
```

**Example 3: Marsaglia polar method.**

```python
import numpy as np
from scipy import stats

def marsaglia_polar(n):
    """Generate n standard normal samples using the Marsaglia polar method."""
    samples = []
    total_attempts = 0
    while len(samples) < n:
        V1 = 2 * np.random.uniform(0, 1) - 1
        V2 = 2 * np.random.uniform(0, 1) - 1
        S = V1**2 + V2**2
        total_attempts += 1
        if S < 1 and S > 0:
            factor = np.sqrt(-2 * np.log(S) / S)
            samples.append(V1 * factor)
            if len(samples) < n:
                samples.append(V2 * factor)
    acceptance_rate = n / (2 * total_attempts)
    return np.array(samples[:n]), acceptance_rate

np.random.seed(42)
Z, acc_rate = marsaglia_polar(100000)

print("Marsaglia polar method (n = 100000):")
print(f"  Mean:     {Z.mean():.4f}")
print(f"  Variance: {Z.var():.4f}")
print(f"  Acceptance rate: {acc_rate:.4f}  (theory: pi/4 = {np.pi/4:.4f})")
```

**Output:**
```
Marsaglia polar method (n = 100000):
  Mean:     0.0019
  Variance: 1.0024
  Acceptance rate: 0.7853  (theory: pi/4 = 0.7854)
```

**Example 4: Generating from a general normal.**

Use Box-Muller to generate $X \sim N(100, 15^2)$ (IQ scores).

```python
import numpy as np
from scipy import stats

np.random.seed(42)
n = 100000

# Box-Muller for N(0,1)
U1 = np.random.uniform(0, 1, (n + 1) // 2)
U2 = np.random.uniform(0, 1, (n + 1) // 2)
R = np.sqrt(-2 * np.log(U2))
Z = R * np.cos(2 * np.pi * U1)

# Transform to N(100, 225)
mu, sigma = 100, 15
X = mu + sigma * Z[:n]

print(f"IQ scores ~ N({mu}, {sigma}^2):")
print(f"  Mean: {X.mean():.2f}  (expected: {mu})")
print(f"  Std:  {X.std():.2f}  (expected: {sigma})")
print(f"  P(IQ > 130) = {np.mean(X > 130):.4f}  (theory: {1-stats.norm.cdf(2):.4f})")
print(f"  P(IQ < 70)  = {np.mean(X < 70):.4f}  (theory: {stats.norm.cdf(-2):.4f})")
```

**Output:**
```
IQ scores ~ N(100, 15^2):
  Mean: 99.99  (expected: 100)
  Std:  15.01  (expected: 15)
  P(IQ > 130) = 0.0229  (theory: 0.0228)
  P(IQ < 70)  = 0.0228  (theory: 0.0228)
```
