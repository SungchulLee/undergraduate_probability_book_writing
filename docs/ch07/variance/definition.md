# Variance: Definition and Computation

## Definition

The **variance** of a random variable $X$ is

$$

\text{Var}(X) = E\left[(X - E[X])^2\right] = E\left[(X - \mu)^2\right]

$$

where $\mu = E[X]$.

Variance measures the **spread** or **dispersion** of the distribution around its mean. It is always non-negative: $\text{Var}(X) \geq 0$.

---

## Computing Variance

### Discrete Case

$$

\text{Var}(X) = \sum_x (x - \mu)^2 \, p(x)

$$

### Continuous Case

$$

\text{Var}(X) = \int_{-\infty}^{\infty} (x - \mu)^2 \, f(x) \, dx

$$

---

## Examples

### Bernoulli Distribution

If $X \sim \text{Bernoulli}(p)$, then $\mu = p$ and

$$

\text{Var}(X) = (0-p)^2(1-p) + (1-p)^2 p = p^2(1-p) + (1-p)^2 p = p(1-p) = pq

$$

### Fair Die

If $X$ is a fair die roll, $\mu = 3.5$ and

$$

\text{Var}(X) = \frac{1}{6}\sum_{k=1}^6 (k - 3.5)^2 = \frac{(2.5)^2 + (1.5)^2 + (0.5)^2 + (0.5)^2 + (1.5)^2 + (2.5)^2}{6} = \frac{17.5}{6} \approx 2.917

$$

### Continuous Uniform

If $X \sim \text{Uniform}(a,b)$, then

$$

\text{Var}(X) = \frac{(b-a)^2}{12}

$$

---

## Properties

1. $\text{Var}(X) \geq 0$, with equality iff $X$ is constant with probability 1

2. $\text{Var}(c) = 0$ for any constant $c$

3. $\text{Var}(X)$ exists iff $E[X^2] < \infty$

---

## Python Implementation

```python
import numpy as np

# Bernoulli variance
p = 0.3
var_bernoulli = p * (1 - p)
print(f"Var(Bernoulli({p})) = {var_bernoulli}")

# Fair die variance
values = np.arange(1, 7)
probs = np.ones(6) / 6
mu = np.sum(values * probs)
var_die = np.sum((values - mu)**2 * probs)
print(f"Var(fair die) = {var_die:.4f}")  # 2.9167

# Uniform variance
a, b = 0, 1
var_uniform = (b - a)**2 / 12
print(f"Var(Uniform({a},{b})) = {var_uniform:.4f}")

# Monte Carlo
np.random.seed(42)
N = 1_000_000
samples = np.random.randint(1, 7, N)
print(f"MC Var(die) = {np.var(samples):.4f}")
```
