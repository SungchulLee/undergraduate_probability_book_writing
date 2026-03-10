# LOTUS

The Law of the Unconscious Statistician computes $E[g(X)]$ directly from the distribution of $X$, without finding the distribution of $g(X)$ first.

## Definition

**Discrete:** If $X$ has PMF $p(x)$, then

$$
E[g(X)] = \sum_x g(x)\,p(x)
$$

**Continuous:** If $X$ has PDF $f(x)$, then

$$
E[g(X)] = \int_{-\infty}^{\infty} g(x)\,f(x)\,dx
$$

**Joint version:**

$$
E[g(X,Y)] = \sum_x \sum_y g(x,y)\,p(x,y) \quad \text{or} \quad \iint g(x,y)\,f(x,y)\,dx\,dy
$$

## Explanation

### Why It Works

The key insight: to average $g(X)$, weight each value $g(x)$ by the probability that $X = x$. You don't need the distribution of the transformed variable $g(X)$ — the original distribution of $X$ suffices.

### Why "Unconscious Statistician"

The formula looks like you "forgot" that $g(X)$ is a different random variable and naively plugged $g(x)$ into the expectation formula for $X$. Despite the joke, the result is rigorous.

### Key Application: Variance

The shortcut formula $\text{Var}(X) = E[X^2] - (E[X])^2$ requires $E[X^2]$, which is computed via LOTUS with $g(x) = x^2$.

## Examples

**Example 1.** Fair die, $g(x) = x^2$:

$$
E[X^2] = \sum_{k=1}^6 k^2 \cdot \frac{1}{6} = \frac{91}{6} \approx 15.17
$$

Note: $(E[X])^2 = 3.5^2 = 12.25 \ne E[X^2]$.

**Example 2.** $X \sim \text{Exp}(\lambda)$, moment generating function:

$$
E[e^{tX}] = \int_0^{\infty} e^{tx} \lambda e^{-\lambda x}\,dx = \frac{\lambda}{\lambda - t}, \quad t < \lambda
$$

```python
import numpy as np
from scipy import integrate

# E[X^2] for fair die
E_X2 = sum(k**2 / 6 for k in range(1, 7))
E_X = 3.5
print(f"E[X^2] = {E_X2:.4f}, (E[X])^2 = {E_X**2:.4f}")

# E[X^2] for Uniform(0,1)
result, _ = integrate.quad(lambda x: x**2, 0, 1)
print(f"E[X^2] for U(0,1) = {result:.4f}")

# MGF of Exp(2) at t=0.5
lam, t = 2.0, 0.5
exact = lam / (lam - t)
numerical, _ = integrate.quad(lambda x: np.exp(t*x) * lam * np.exp(-lam*x), 0, np.inf)
print(f"MGF: exact={exact:.4f}, numerical={numerical:.4f}")
```
