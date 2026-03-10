# Expectation

The expected value is the probability-weighted average of a random variable — the single most important summary of a distribution.

## Definition

**Discrete case.** If $X$ has PMF $p(x)$:

$$
E[X] = \sum_{x} x\,p(x)
$$

**Continuous case.** If $X$ has PDF $f(x)$:

$$
E[X] = \int_{-\infty}^{\infty} x\,f(x)\,dx
$$

Both require absolute convergence ($\sum |x|\,p(x) < \infty$ or $\int |x|\,f(x)\,dx < \infty$). If this fails, $E[X]$ does not exist.

## Explanation

### Interpretation

- **Long-run average:** By the Law of Large Numbers, the sample mean $\bar{X}_n \to E[X]$ as $n \to \infty$
- **Center of mass:** $E[X]$ is the balance point of the probability distribution
- **Fair price:** $E[X]$ is the break-even price for a gamble with payoff $X$

### Basic Properties

1. $E[c] = c$ for any constant
2. $E[cX] = c\,E[X]$ (scaling)
3. $E[X + c] = E[X] + c$ (shift)
4. $X \ge 0 \implies E[X] \ge 0$ (non-negativity)
5. $X \le Y \implies E[X] \le E[Y]$ (monotonicity)

### When Expectation Does Not Exist

The Cauchy distribution $f(x) = 1/(\pi(1+x^2))$ has no expectation because $\int |x|/(\pi(1+x^2))\,dx = \infty$. The tails are too heavy for the integral to converge.

## Examples

**Example 1.** Fair die: $E[X] = (1+2+3+4+5+6)/6 = 3.5$. Note that 3.5 is not even a possible outcome.

**Example 2.** $X \sim \text{Bern}(p)$: $E[X] = 0(1-p) + 1 \cdot p = p$.

**Example 3.** $X \sim \text{Uniform}(a,b)$: $E[X] = \int_a^b x/(b-a)\,dx = (a+b)/2$.

**Example 4.** $Z \sim N(0,1)$: $E[Z] = 0$ by symmetry.

```python
import numpy as np

# Fair die
E_die = sum(k * (1/6) for k in range(1, 7))
print(f"E[fair die] = {E_die}")

# Uniform(2, 8)
a, b = 2, 8
print(f"E[Uniform({a},{b})] = {(a+b)/2}")

# Monte Carlo: verify E[N(5,4)] = 5
np.random.seed(42)
samples = np.random.normal(5, 2, 1_000_000)
print(f"MC E[N(5,4)] = {samples.mean():.4f}")
```
