# Definition of Expectation (Discrete and Continuous)


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

## Motivation

The **expectation** (or **expected value**, **mean**) of a random variable is the long-run average value it takes over many independent repetitions. It is the single most important summary of a probability distribution.

---

## Definition: Discrete Case

If $X$ is a discrete random variable with PMF $p(x) = P(X = x)$, the **expected value** of $X$ is

$$
E[X] = \sum_{x} x \, p(x)
$$

where the sum is over all possible values of $X$, provided the sum converges absolutely:

$$
\sum_{x} |x| \, p(x) < \infty
$$

If the sum does not converge absolutely, we say $E[X]$ **does not exist**.

---

## Definition: Continuous Case

If $X$ is a continuous random variable with PDF $f(x)$, the **expected value** of $X$ is

$$
E[X] = \int_{-\infty}^{\infty} x \, f(x) \, dx
$$

provided the integral converges absolutely:

$$
\int_{-\infty}^{\infty} |x| \, f(x) \, dx < \infty
$$

---

## Basic Examples

### Example 1: Fair Die

Let $X$ be the face value of a fair die. Then

$$
E[X] = \sum_{k=1}^{6} k \cdot \frac{1}{6} = \frac{1+2+3+4+5+6}{6} = \frac{21}{6} = 3.5
$$

Note that $E[X] = 3.5$ is not even a possible outcome — the expectation need not be a value the random variable can take.

### Example 2: Bernoulli Random Variable

If $X \sim \text{Bernoulli}(p)$, then

$$
E[X] = 0 \cdot (1-p) + 1 \cdot p = p
$$

### Example 3: Continuous Uniform

If $X \sim \text{Uniform}(a, b)$ with PDF $f(x) = \frac{1}{b-a}$ for $a \leq x \leq b$, then

$$
E[X] = \int_a^b x \cdot \frac{1}{b-a} \, dx = \frac{a+b}{2}
$$

### Example 4: Standard Normal

If $Z \sim N(0,1)$, then by symmetry of the PDF about zero,

$$
E[Z] = \int_{-\infty}^{\infty} z \cdot \frac{1}{\sqrt{2\pi}} e^{-z^2/2} \, dz = 0
$$

---

## Properties of Expectation

1. **Constants**: $E[c] = c$ for any constant $c$

2. **Scaling**: $E[cX] = cE[X]$

3. **Shift**: $E[X + c] = E[X] + c$

4. **Non-negativity**: If $X \geq 0$, then $E[X] \geq 0$

5. **Monotonicity**: If $X \leq Y$, then $E[X] \leq E[Y]$

---

## When Expectation Does Not Exist

### Example: Cauchy Distribution

The Cauchy distribution with PDF

$$
f(x) = \frac{1}{\pi(1 + x^2)}, \quad -\infty < x < \infty
$$

has no expectation because $\int_{-\infty}^{\infty} |x| \cdot \frac{1}{\pi(1+x^2)} dx = \infty$.

---

## Interpretation

The expected value $E[X]$ can be interpreted as:

- **Long-run average**: By the Law of Large Numbers, $\bar{X}_n \to E[X]$ as $n \to \infty$
- **Center of mass**: $E[X]$ is the balance point (center of gravity) of the probability distribution
- **Fair price**: In a gambling context, $E[X]$ is the fair price to pay for a game with random payoff $X$

---

## Python Implementation

```python
import numpy as np
from scipy import stats

# Discrete: Fair die
die_values = np.arange(1, 7)
die_probs = np.ones(6) / 6
E_die = np.sum(die_values * die_probs)
print(f"E[fair die] = {E_die}")  # 3.5

# Bernoulli
p = 0.3
E_bernoulli = p
print(f"E[Bernoulli({p})] = {E_bernoulli}")  # 0.3

# Continuous Uniform
a, b = 2, 8
E_uniform = (a + b) / 2
print(f"E[Uniform({a},{b})] = {E_uniform}")  # 5.0

# Verify with scipy
print(f"Scipy Uniform mean = {stats.uniform(loc=a, scale=b-a).mean()}")  # 5.0

# Normal
mu, sigma = 5, 2
E_normal = mu
print(f"E[N({mu},{sigma}²)] = {E_normal}")  # 5

# Monte Carlo verification
np.random.seed(42)
N = 1_000_000
samples = np.random.normal(mu, sigma, N)
print(f"Monte Carlo estimate = {np.mean(samples):.4f}")
```
