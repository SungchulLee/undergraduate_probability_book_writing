# Chebyshev's Inequality

## Statement

For any random variable $X$ with mean $\mu$ and variance $\sigma^2$, and for any $k > 0$:

$$
P(|X - \mu| \geq k\sigma) \leq \frac{1}{k^2}
$$

Equivalently, for any $a > 0$:

$$
P(|X - \mu| \geq a) \leq \frac{\sigma^2}{a^2}
$$

---

## Proof

Apply Markov's inequality to the non-negative random variable $(X - \mu)^2$:

$$
P(|X - \mu| \geq a) = P((X - \mu)^2 \geq a^2) \leq \frac{E[(X-\mu)^2]}{a^2} = \frac{\sigma^2}{a^2}
$$

Setting $a = k\sigma$ gives $P(|X - \mu| \geq k\sigma) \leq 1/k^2$.

---

## Key Values

| $k$ | $P(\lvert X - \mu\rvert \geq k\sigma) \leq$ | At least this much probability within $k\sigma$ |
|:---:|:---:|:---:|
| 1 | 1 | 0% (trivial) |
| 2 | 0.25 | 75% |
| 3 | 0.111 | 88.9% |
| 4 | 0.0625 | 93.75% |
| 5 | 0.04 | 96% |

---

## Application: Weak Law of Large Numbers

Let $X_1, \ldots, X_n$ be iid with mean $\mu$ and variance $\sigma^2$. The sample mean $\bar{X}_n = \frac{1}{n}\sum_{i=1}^n X_i$ has $E[\bar{X}_n] = \mu$ and $\text{Var}(\bar{X}_n) = \sigma^2/n$. By Chebyshev:

$$
P(|\bar{X}_n - \mu| \geq \epsilon) \leq \frac{\sigma^2}{n\epsilon^2} \to 0 \text{ as } n \to \infty
$$

---

## Python Implementation

```python
import numpy as np

np.random.seed(42)
N = 1_000_000

# Normal(0,1): compare Chebyshev bounds to actual
X = np.random.normal(0, 1, N)

for k in [1, 2, 3, 4, 5]:
    chebyshev = 1 / k**2
    actual = np.mean(np.abs(X) >= k)
    print(f"k={k}: Chebyshev <= {chebyshev:.4f}, actual = {actual:.4f}")
```
