# Numerical Comparison: Binomial vs Poisson

Side-by-side PMF comparisons reveal how the approximation quality depends on $n$, $p$, and $\lambda$.

## Definition

For $X_n \sim \text{Bin}(n, \lambda/n)$ and $Y \sim \text{Pois}(\lambda)$, the **total variation distance** is

$$
d_{TV}(X_n, Y) = \frac{1}{2}\sum_{k=0}^{\infty}\bigl|P(X_n = k) - P(Y = k)\bigr|
$$

This decreases as $O(1/n)$, matching the Le Cam bound $\lambda^2/n$.

## Explanation

### Convergence Rate

The maximum PMF difference $\max_k |P(X_n = k) - P(Y = k)|$ also decreases as $O(1/n)$. Doubling $n$ roughly halves the error.

### Iterative Computation

For very large $n$, computing $\binom{n}{k}$ directly overflows. Use recurrences instead:

**Poisson:** $P(X = k) = P(X = k-1)\cdot\lambda/k$, starting from $P(X = 0) = e^{-\lambda}$.

**Binomial:** $P(X = k) = P(X = k-1)\cdot\frac{n-k+1}{k}\cdot\frac{p}{1-p}$, starting from $P(X = 0) = (1-p)^n$.

## Examples

**Example (Birthday couples).** 80,000 marriages, probability $1/365$ of shared birthday. $\lambda = 80000/365 \approx 219.18$.

$$
P(S > 250) \approx 0.019 \text{ (both methods agree to 4 decimal places)}
$$

```python
from scipy.stats import binom, poisson

n = 80_000
p = 1 / 365
la = n * p

binom_prob = 1 - binom.cdf(250, n, p)
poisson_prob = 1 - poisson.cdf(250, la)

print(f"lambda = {la:.2f}")
print(f"Binomial: P(S > 250) = {binom_prob:.6f}")
print(f"Poisson:  P(X > 250) = {poisson_prob:.6f}")
print(f"Difference: {abs(binom_prob - poisson_prob):.2e}")
```
