# Continuous Uniform Distribution

The continuous uniform distribution models "pure randomness" on an interval, where every subinterval of a given length is equally likely.

## Definition

A continuous random variable $X$ has the **Uniform distribution** on the interval $(a, b)$, written $X \sim U(a, b)$, if its PDF is:

$$
f(x) = \frac{1}{b - a}, \quad a < x < b
$$

The CDF is:

$$
F(x) = \begin{cases} 0 & x \leq a \\ \dfrac{x - a}{b - a} & a < x < b \\ 1 & x \geq b \end{cases}
$$

The mean and variance are:

$$
E[X] = \frac{a + b}{2}, \qquad \text{Var}(X) = \frac{(b - a)^2}{12}
$$

The **standard uniform** $U(0, 1)$ has $f(x) = 1$ for $0 < x < 1$, $F(x) = x$ for $0 \leq x \leq 1$, mean $1/2$, and variance $1/12$.

## Explanation

### Derivation of the mean

$$
E[X] = \int_a^b x \cdot \frac{1}{b - a} \, dx = \frac{1}{b - a} \left[\frac{x^2}{2}\right]_a^b = \frac{b^2 - a^2}{2(b-a)} = \frac{(b+a)(b-a)}{2(b-a)} = \frac{a + b}{2}
$$

The mean is simply the midpoint of the interval, which makes geometric sense: the density is symmetric about the center.

### Derivation of the variance

First compute $E[X^2]$:

$$
E[X^2] = \frac{1}{b - a} \int_a^b x^2 \, dx = \frac{b^3 - a^3}{3(b-a)} = \frac{a^2 + ab + b^2}{3}
$$

using the identity $b^3 - a^3 = (b - a)(b^2 + ab + a^2)$. Then:

$$
\text{Var}(X) = E[X^2] - (E[X])^2 = \frac{a^2 + ab + b^2}{3} - \frac{(a+b)^2}{4} = \frac{4(a^2 + ab + b^2) - 3(a^2 + 2ab + b^2)}{12} = \frac{(b - a)^2}{12}
$$

### Connection to the Poisson process

If a Poisson process has exactly one arrival in the interval $[a, b]$, then the position of that arrival is uniformly distributed on $[a, b]$. More generally, given $N([a,b]) = n$ arrivals, the $n$ arrival positions (unordered) are iid $U(a, b)$.

### Linear transformation

If $U \sim U(0, 1)$, then $X = a + (b - a)U \sim U(a, b)$. Conversely, if $X \sim U(a, b)$, then $(X - a)/(b - a) \sim U(0, 1)$. More generally, if $X \sim U(a, b)$ and $Y = cX + d$ with $c > 0$, then:

$$
Y \sim U(ca + d, \; cb + d)
$$

### Symmetry

If $X \sim U(a, b)$, then $a + b - X \sim U(a, b)$. In particular, if $U \sim U(0, 1)$, then $1 - U \sim U(0, 1)$. This reflection symmetry about the midpoint is useful in simulation: replacing $U$ by $1 - U$ does not change the distribution.

## Examples

**Example 1: Basic probability calculations.**

Let $X \sim U(2, 8)$. Find $P(3 < X < 6)$ and $P(X > 5)$.

$$
P(3 < X < 6) = \frac{6 - 3}{8 - 2} = \frac{3}{6} = 0.5
$$

$$
P(X > 5) = \frac{8 - 5}{8 - 2} = \frac{3}{6} = 0.5
$$

```python
from scipy import stats

a, b = 2, 8
X = stats.uniform(loc=a, scale=b - a)

p1 = X.cdf(6) - X.cdf(3)
p2 = 1 - X.cdf(5)
print(f"U({a}, {b}):")
print(f"P(3 < X < 6) = (6 - 3) / (8 - 2) = {p1:.4f}")
print(f"P(X > 5) = (8 - 5) / (8 - 2) = {p2:.4f}")
print(f"E[X] = {X.mean():.4f}  (theory: {(a+b)/2})")
print(f"Var(X) = {X.var():.4f}  (theory: {(b-a)**2/12:.4f})")
```

**Output:**
```
U(2, 8):
P(3 < X < 6) = (6 - 3) / (8 - 2) = 0.5000
P(X > 5) = (8 - 5) / (8 - 2) = 0.5000
E[X] = 5.0000  (theory: 5.0)
Var(X) = 3.0000  (theory: 3.0000)
```

**Example 2: Bus arrival.**

A bus arrives every 15 minutes. You arrive at a random time. Let $W \sim U(0, 15)$ be your waiting time (in minutes). Find the probability you wait more than 10 minutes, and the expected waiting time.

```python
from scipy import stats

W = stats.uniform(loc=0, scale=15)

p = 1 - W.cdf(10)
print(f"P(wait > 10 min) = {p:.4f}")
print(f"E[W] = {W.mean():.2f} minutes")
print(f"SD(W) = {W.std():.2f} minutes")
```

**Output:**
```
P(wait > 10 min) = 0.3333
E[W] = 7.50 minutes
SD(W) = 4.33 minutes
```

**Example 3: Simulation verification.**

```python
import numpy as np

np.random.seed(42)
n_sim = 100000
a, b = 2, 8
X = np.random.uniform(a, b, n_sim)

print(f"U({a}, {b}) simulation (n = {n_sim}):")
print(f"  Mean:  {X.mean():.4f}  (theory: {(a+b)/2:.4f})")
print(f"  Var:   {X.var():.4f}  (theory: {(b-a)**2/12:.4f})")
print(f"  P(3<X<6): {np.mean((X > 3) & (X < 6)):.4f}  (theory: 0.5000)")
```

**Output:**
```
U(2, 8) simulation (n = 100000):
  Mean:  4.9978  (theory: 5.0000)
  Var:   2.9964  (theory: 3.0000)
  P(3<X<6): 0.4997  (theory: 0.5000)
```
