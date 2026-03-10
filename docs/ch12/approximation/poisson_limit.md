# Poisson Limit Theorem

The Poisson distribution is the limit of the binomial when $n \to \infty$, $p \to 0$, and $np = \lambda$ stays fixed — justifying the Poisson as the model for rare events.

## Definition

If $X_n \sim \text{Bin}(n, \lambda/n)$, then for every $k \ge 0$:

$$
\lim_{n \to \infty}P(X_n = k) = \frac{e^{-\lambda}\lambda^k}{k!}
$$

That is, $\text{Bin}(n, \lambda/n) \xrightarrow{d} \text{Pois}(\lambda)$.

## Explanation

### Proof

Starting from the binomial PMF with $p = \lambda/n$:

$$
P(X_n = k) = \binom{n}{k}\left(\frac{\lambda}{n}\right)^k\left(1 - \frac{\lambda}{n}\right)^{n-k}
$$

Rearranging into three factors:

$$
P(X_n = k) = \frac{\lambda^k}{k!}\cdot\underbrace{\frac{n(n-1)\cdots(n-k+1)}{n^k}}_{\to 1}\cdot\underbrace{\left(1-\frac{\lambda}{n}\right)^n}_{\to e^{-\lambda}}\cdot\underbrace{\left(1-\frac{\lambda}{n}\right)^{-k}}_{\to 1}
$$

The limit is $e^{-\lambda}\lambda^k/k!$.

### Le Cam's Inequality

For independent indicators $X = \sum_{i=1}^n \mathbf{1}_{A_i}$ with $p_i = P(A_i)$ and $\lambda = \sum p_i$:

$$
\bigl|P(X \in A) - P(Y \in A)\bigr| \le \sum_{i=1}^n p_i^2 \le \left(\max_i p_i\right)\lambda
$$

where $Y \sim \text{Pois}(\lambda)$. The error is small when each $p_i$ is small.

### Moment Convergence

The mean matches exactly ($np = \lambda$). The variance converges: $npq = \lambda(1 - \lambda/n) \to \lambda$.

## Examples

**Example.** Convergence of $\text{Bin}(n, 10/n) \to \text{Pois}(10)$.

```python
from scipy.stats import binom, poisson

la = 10
print(f"{'n':>8} {'Max PMF diff':>14} {'Le Cam bound':>14}")
for n in [20, 50, 100, 500, 1000, 10000]:
    import numpy as np
    k = np.arange(0, 30)
    diff = np.max(np.abs(binom.pmf(k, n, la/n) - poisson.pmf(k, la)))
    bound = la**2 / n
    print(f"{n:>8} {diff:>14.6e} {bound:>14.6e}")
```
