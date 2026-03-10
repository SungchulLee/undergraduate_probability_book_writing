# Properties and Applications of the Uniform Distribution

The uniform distribution has remarkable structural properties, most notably the universality of $U(0,1)$: every continuous distribution can be generated from it, and applying any continuous CDF to its own random variable produces it.

## Definition

The key properties of $X \sim U(a, b)$ are collected here:

**Symmetry:** $a + b - X \sim U(a, b)$, so $X$ and its reflection about the midpoint have the same distribution.

**Linear transformation:** If $Y = cX + d$ with $c > 0$, then $Y \sim U(ca + d, \; cb + d)$.

**Universality (forward):** If $X$ has continuous CDF $F$, then $F(X) \sim U(0, 1)$.

**Universality (inverse):** If $U \sim U(0, 1)$, then $F^{-1}(U)$ has CDF $F$.

**CDF of the standard uniform:**

$$
F(x) = x, \quad 0 \leq x \leq 1
$$

## Explanation

### Universality of the uniform

The $U(0, 1)$ distribution is universal in two senses.

**Probability Integral Transform.** If $X$ is a continuous random variable with CDF $F$, then:

$$
F(X) \sim U(0, 1)
$$

*Proof.* Let $U = F(X)$. Since $F$ is continuous and non-decreasing:

$$
P(U \leq u) = P(F(X) \leq u) = P(X \leq F^{-1}(u)) = F(F^{-1}(u)) = u
$$

for $0 < u < 1$. This is the CDF of $U(0,1)$.

**Inverse Transform Method.** Conversely, if $U \sim U(0, 1)$, then $X = F^{-1}(U)$ has CDF $F$:

$$
P(F^{-1}(U) \leq x) = P(U \leq F(x)) = F(x)
$$

This provides a universal recipe for simulating any distribution from uniform random numbers.

### Decomposition technique

A powerful technique for uniform problems is to **decompose** the random variable into a known constant plus a simpler uniform component.

??? example "Example: Breaking the Stick"
    We break a stick of length $L$ at a uniformly random point. Let $X$ be the length of the **longer** piece. Find its mean and variance.

    The longer piece always has length at least $L/2$. Write $X = L/2 + Y$ where $Y$ is the excess beyond the midpoint. Since the break point is uniform on $[0, L]$, the excess $Y \sim U(0, L/2)$.

    **Mean:**

    $$
    E[X] = \frac{L}{2} + E[Y] = \frac{L}{2} + \frac{L}{4} = \frac{3L}{4}
    $$

    **Variance:** Since shifting by a constant does not change variance:

    $$
    \text{Var}(X) = \text{Var}(Y) = \frac{(L/2)^2}{12} = \frac{L^2}{48}
    $$

### Sum of uniforms is not uniform

The sum of independent uniforms is **not** uniform (unless the variables are degenerate). The sum of two iid $U(0, 1)$ variables has a triangular distribution on $(0, 2)$ with PDF $f(s) = s$ for $0 < s < 1$ and $f(s) = 2 - s$ for $1 \leq s < 2$. As more uniforms are summed, the distribution approaches normal by the Central Limit Theorem.

### Memorylessness -- or lack thereof

Unlike the exponential distribution, the uniform distribution is **not** memoryless. If $X \sim U(0, 1)$ and we learn that $X > 0.5$, the conditional distribution $X \mid X > 0.5$ is $U(0.5, 1)$, not $U(0, 0.5)$. The conditional distribution shifts, reflecting the information gained.

### Higher moments

For $X \sim U(a, b)$, the $k$-th raw moment is:

$$
E[X^k] = \frac{1}{b - a} \int_a^b x^k \, dx = \frac{b^{k+1} - a^{k+1}}{(k+1)(b-a)}
$$

For the standard uniform $U(0, 1)$: $E[U^k] = 1/(k+1)$.

## Examples

**Example 1: Probability integral transform.**

Generate $X \sim \text{Exp}(2)$ from $U \sim U(0, 1)$ and verify that $F(X) \sim U(0, 1)$.

The CDF of $\text{Exp}(2)$ is $F(x) = 1 - e^{-2x}$. The inverse is $F^{-1}(u) = -\frac{1}{2}\ln(1 - u)$.

```python
import numpy as np
from scipy import stats

np.random.seed(42)
n = 100000

# Generate Exp(2) from uniform via inverse CDF
U = np.random.uniform(0, 1, n)
X = -0.5 * np.log(1 - U)  # Exp(2) via inverse CDF

# Verify X ~ Exp(2)
print("X = F^{-1}(U) should be Exp(2):")
print(f"  Mean: {X.mean():.4f}  (expected: {1/2:.4f})")
print(f"  Var:  {X.var():.4f}  (expected: {1/4:.4f})")

# Apply CDF to X: should get U(0,1)
U_back = 1 - np.exp(-2 * X)
print(f"\nF(X) should be U(0,1):")
print(f"  Mean: {U_back.mean():.4f}  (expected: 0.5000)")
print(f"  Var:  {U_back.var():.4f}  (expected: {1/12:.4f})")
```

**Output:**
```
X = F^{-1}(U) should be Exp(2):
  Mean: 0.5011  (expected: 0.5000)
  Var:  0.2500  (expected: 0.2500)

F(X) should be U(0,1):
  Mean: 0.4998  (expected: 0.5000)
  Var:  0.0833  (expected: 0.0833)
```

**Example 2: Breaking the stick.**

Verify the decomposition result: for a stick of length $L = 10$, the longer piece has mean $3L/4 = 7.5$ and variance $L^2/48 \approx 2.083$.

```python
import numpy as np

np.random.seed(42)
n = 100000
L = 10.0

break_point = np.random.uniform(0, L, n)
longer = np.maximum(break_point, L - break_point)

print(f"Stick of length L = {L}:")
print(f"  E[longer piece] = {longer.mean():.4f}  (theory: {3*L/4:.4f})")
print(f"  Var[longer piece] = {longer.var():.4f}  (theory: {L**2/48:.4f})")
```

**Output:**
```
Stick of length L = 10.0:
  E[longer piece] = 7.5013  (theory: 7.5000)
  Var[longer piece] = 2.0851  (theory: 2.0833)
```

**Example 3: Sum of two uniforms is triangular.**

```python
import numpy as np
from scipy import stats

np.random.seed(42)
n = 100000

U1 = np.random.uniform(0, 1, n)
U2 = np.random.uniform(0, 1, n)
S = U1 + U2

print("S = U1 + U2 where U1, U2 ~ iid U(0,1):")
print(f"  Mean: {S.mean():.4f}  (expected: 1.0000)")
print(f"  Var:  {S.var():.4f}  (expected: {2/12:.4f})")

# Compare with triangular distribution
triang = stats.triang(c=0.5, loc=0, scale=2)  # symmetric triangular on [0, 2]
print(f"  Triangular mean: {triang.mean():.4f}, var: {triang.var():.4f}")
```

**Output:**
```
S = U1 + U2 where U1, U2 ~ iid U(0,1):
  Mean: 1.0017  (expected: 1.0000)
  Var:  0.1666  (expected: 0.1667)
  Triangular mean: 1.0000, var: 0.1667
```
