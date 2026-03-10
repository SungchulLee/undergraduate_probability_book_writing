# Poisson Distribution

The Poisson distribution counts rare events in a fixed domain — the natural model when many independent trials each have a small probability of success.

## Definition

$X \sim \text{Pois}(\lambda)$ if

$$
P(X = k) = \frac{e^{-\lambda}\lambda^k}{k!}, \qquad k = 0, 1, 2, \ldots
$$

where $\lambda > 0$ is the rate parameter.

**Moments:** $E[X] = \text{Var}(X) = \lambda$.

**MGF:** $M_X(t) = e^{\lambda(e^t - 1)}$.

## Explanation

### Normalization

$$
\sum_{k=0}^{\infty}\frac{e^{-\lambda}\lambda^k}{k!} = e^{-\lambda}\sum_{k=0}^{\infty}\frac{\lambda^k}{k!} = e^{-\lambda}\cdot e^{\lambda} = 1
$$

### Key Properties

- **Support:** $\{0, 1, 2, \ldots\}$
- **Mode:** $\lfloor\lambda\rfloor$ (when $\lambda \notin \mathbb{Z}$); both $\lambda - 1$ and $\lambda$ (when $\lambda \in \mathbb{Z}$)
- **Ratio of successive probabilities:** $P(X = k)/P(X = k-1) = \lambda/k$
- **Mean = Variance:** The hallmark property. The dispersion index $D = \text{Var}(X)/E[X] = 1$
- **Tail decay:** Faster than geometric since $k!$ grows faster than any exponential

### Where the Poisson Arises

The Poisson models counts of rare events: insurance claims per month, mutations in a DNA strand, defects per unit, calls per minute, accidents per year. It arises as the limit of $\text{Bin}(n, \lambda/n)$ as $n \to \infty$.

## Examples

**Example.** $X \sim \text{Pois}(10)$.

```python
from scipy.stats import poisson

la = 10
print(f"P(X=5)  = {poisson.pmf(5, la):.6f}")
print(f"P(X=10) = {poisson.pmf(10, la):.6f}")
print(f"P(X<=8) = {poisson.cdf(8, la):.6f}")
print(f"P(X>12) = {1 - poisson.cdf(12, la):.6f}")
print(f"Mean={poisson.mean(la)}, Var={poisson.var(la)}")
```
