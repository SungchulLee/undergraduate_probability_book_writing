# Discrete Uniform Distribution

The discrete uniform distribution assigns equal probability to each value in a finite set — the mathematical model for "equally likely outcomes."

## Definition

$X \sim \text{DUnif}(a, a+1, \ldots, b)$ if

$$
P(X = k) = \frac{1}{n}, \qquad k = a, a+1, \ldots, b
$$

where $n = b - a + 1$. The CDF is a staircase: $F(x) = \lfloor x - a + 1 \rfloor / n$ for $a \le x \le b$.

**Moments:**

$$
E[X] = \frac{a + b}{2}, \qquad \text{Var}(X) = \frac{n^2 - 1}{12}
$$

**MGF:**

$$
M_X(t) = \frac{e^{at}(1 - e^{nt})}{n(1 - e^t)}, \qquad t \ne 0
$$

## Explanation

### Mean by Symmetry

The PMF is symmetric about $(a + b)/2$, so the mean is the midpoint. For a fair die ($a = 1, b = 6$): $E[X] = 3.5$.

### Variance Derivation

For $X \sim \text{DUnif}(1, \ldots, n)$:

$$
E[X^2] = \frac{1}{n}\sum_{k=1}^n k^2 = \frac{(n+1)(2n+1)}{6}
$$

$$
\text{Var}(X) = \frac{(n+1)(2n+1)}{6} - \left(\frac{n+1}{2}\right)^2 = \frac{n^2 - 1}{12}
$$

The general case $\text{DUnif}(a, \ldots, b)$ has the same variance since shifting does not change spread.

### Connection to Continuous Uniform

As $n \to \infty$ with the range $[a, b]$ fixed, the discrete uniform converges to the continuous $\text{Uniform}(a, b)$.

## Examples

**Example.** Fair die: $X \sim \text{DUnif}(1, 6)$, $E[X] = 3.5$, $\text{Var}(X) = 35/12 \approx 2.917$.

```python
import numpy as np

np.random.seed(42)
n_sim = 200_000

# Fair die
X = np.random.randint(1, 7, n_sim)
print(f"Die: E[X] = {X.mean():.4f}  (theory: 3.5)")
print(f"Die: Var(X) = {X.var():.4f}  (theory: {35/12:.4f})")

# DUnif(1,...,20)
n = 20
Y = np.random.randint(1, n + 1, n_sim)
print(f"\nDUnif(1,20): E[Y] = {Y.mean():.3f}  (theory: {(1+n)/2:.1f})")
print(f"DUnif(1,20): Var(Y) = {Y.var():.2f}  (theory: {(n**2-1)/12:.2f})")
```
