# Discrete vs Continuous Random Variables

The two fundamental types of random variable — discrete and continuous — differ in whether probability mass concentrates at individual points or spreads smoothly across intervals.

## Definition

A random variable $X$ is **discrete** if it takes values in a countable set $\{x_1, x_2, \ldots\}$. Its distribution is specified by the probability mass function (PMF):

$$
p_X(x_i) = P(X = x_i), \quad \sum_i p_X(x_i) = 1
$$

A random variable $X$ is **continuous** if its CDF $F(x) = P(X \le x)$ is continuous. Equivalently, $P(X = a) = 0$ for every $a \in \mathbb{R}$. Its distribution is specified by a probability density function (PDF):

$$
P(X \in A) = \int_A f_X(x)\,dx, \quad \int_{-\infty}^{\infty} f_X(x)\,dx = 1
$$

## Explanation

### Comparison Table

| Property | Discrete | Continuous |
|:---------|:---------|:-----------|
| Values | Countable set | Uncountable (interval) |
| Point probability | $P(X = a) > 0$ possible | $P(X = a) = 0$ always |
| Described by | PMF: $p_X(x)$ | PDF: $f_X(x)$ |
| Total probability | $\sum_x p_X(x) = 1$ | $\int f_X(x)\,dx = 1$ |
| CDF behavior | Step function | Continuous function |

### Why Point Probabilities Vanish for Continuous Variables

For a continuous random variable, $P(X = a) = 0$ for every $a$. This is not a failure of the model — it is a consequence of spreading probability over uncountably many values. If any single point had positive probability $\varepsilon > 0$, then uncountably many such points would give infinite total mass, contradicting $P(\Omega) = 1$.

Probability for continuous variables always requires an interval: $P(a \le X \le b) = \int_a^b f_X(x)\,dx$.

### Common Instances

**Discrete:** Bernoulli, Binomial, Geometric, Poisson, Hypergeometric.

**Continuous:** Uniform, Exponential, Normal, Gamma, Beta.

### Mixed Random Variables

Some random variables are neither purely discrete nor purely continuous. For example, an insurance claim $X$ might be 0 with probability 0.9 (no claim) and follow an exponential distribution given $X > 0$. These **mixed** distributions have both a point mass and a continuous component.

## Examples

**Example 1.** Let $X \sim \text{Binomial}(3, 1/2)$ count the number of heads in 3 fair coin flips.

| $k$ | 0 | 1 | 2 | 3 |
|:---:|:---:|:---:|:---:|:---:|
| $P(X=k)$ | $1/8$ | $3/8$ | $3/8$ | $1/8$ |

The CDF jumps at each integer: $F(1.5) = P(X \le 1) = 4/8 = 1/2$.

**Example 2.** Let $X \sim \text{Uniform}(0,1)$ with PDF $f(x) = 1$ for $0 \le x \le 1$.

$$
P(0.3 \le X \le 0.7) = \int_{0.3}^{0.7} 1\,dx = 0.4
$$

The CDF is $F(x) = x$ for $0 \le x \le 1$ — a straight line with no jumps.

```python
import numpy as np

# Discrete: Binomial(3, 0.5)
from math import comb
for k in range(4):
    p = comb(3, k) * 0.5**3
    print(f"P(X = {k}) = {p:.4f}")

# Continuous: Uniform(0, 1) — point probability is zero
samples = np.random.uniform(0, 1, size=100000)
print(f"\nP(X = 0.5) estimate: {np.mean(np.abs(samples - 0.5) < 1e-10)}")
print(f"P(0.3 <= X <= 0.7) estimate: {np.mean((samples >= 0.3) & (samples <= 0.7)):.4f}")
```
