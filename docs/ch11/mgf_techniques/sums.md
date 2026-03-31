# MGF of Sums of Independent Random Variables
<<<<<<< Updated upstream

## The Product Rule

!!! info "MGF of a Sum of Independent Random Variables"
    If $X$ and $Y$ are **independent** random variables whose MGFs exist, then:

    $$M_{X+Y}(t) = M_X(t) \cdot M_Y(t)$$

**Proof.**

$$M_{X+Y}(t) = E[e^{t(X+Y)}] = E[e^{tX} e^{tY}]$$

Since $X$ and $Y$ are independent, $e^{tX}$ and $e^{tY}$ are independent, so the expectation factors:

$$= E[e^{tX}] \cdot E[e^{tY}] = M_X(t) \cdot M_Y(t) \qquad \square$$

!!! warning "Independence Is Essential"
    The product rule fails without independence. If $X$ and $Y$ are dependent, then $E[e^{tX}e^{tY}] \neq E[e^{tX}]\,E[e^{tY}]$ in general.

## Extension to $n$ Independent Random Variables

If $X_1, X_2, \ldots, X_n$ are independent, then by induction:

$$M_{X_1 + X_2 + \cdots + X_n}(t) = \prod_{i=1}^n M_{X_i}(t)$$

When the $X_i$ are iid with common MGF $M_X(t)$:

$$M_{S_n}(t) = [M_X(t)]^n \quad \text{where } S_n = X_1 + \cdots + X_n$$

## Example: Sum of Independent Exponentials

Let $X_1, \ldots, X_n \stackrel{\text{iid}}{\sim} \text{Exp}(\lambda)$. Each has MGF $M_{X_i}(t) = \frac{\lambda}{\lambda - t}$.

$$M_{S_n}(t) = \left(\frac{\lambda}{\lambda - t}\right)^n$$

This is the MGF of $\text{Gamma}(n, \lambda)$. By the uniqueness theorem:

$$X_1 + X_2 + \cdots + X_n \sim \text{Gamma}(n, \lambda)$$

This gives an MGF proof that the sum of $n$ iid exponentials is gamma-distributed.

## Example: Sum of Independent Poissons

Let $X \sim \text{Po}(\lambda)$ and $Y \sim \text{Po}(\mu)$ be independent. Their MGFs are $e^{\lambda(e^t - 1)}$ and $e^{\mu(e^t - 1)}$.

$$M_{X+Y}(t) = e^{\lambda(e^t - 1)} \cdot e^{\mu(e^t - 1)} = e^{(\lambda + \mu)(e^t - 1)}$$

This is the MGF of $\text{Po}(\lambda + \mu)$. By uniqueness:

$$X + Y \sim \text{Po}(\lambda + \mu)$$

## Linear Transformations

For $Y = aX + b$:

$$M_Y(t) = E[e^{t(aX+b)}] = e^{bt}\,M_X(at)$$

This combines with the product rule. For example, if $X_1, \ldots, X_n$ are iid with common MGF $M_X(t)$ and $\bar{X} = \frac{1}{n}\sum X_i$:

$$M_{\bar{X}}(t) = \left[M_X\!\left(\frac{t}{n}\right)\right]^n$$

## Python Verification

```python
import numpy as np
from scipy import stats

np.random.seed(42)
n_sim = 100000

# Sum of 5 iid Exp(2) should be Gamma(5, scale=0.5)
lam = 2.0
n = 5
samples = np.sum(np.random.exponential(1/lam, (n_sim, n)), axis=1)

print(f"Sum of {n} iid Exp({lam}):")
print(f"  Mean:  {samples.mean():.4f}  (exact: {n/lam})")
print(f"  Var:   {samples.var():.4f}  (exact: {n/lam**2})")

# Sum of independent Po(3) + Po(5) should be Po(8)
X = np.random.poisson(3, n_sim)
Y = np.random.poisson(5, n_sim)
S = X + Y

print(f"\nPo(3) + Po(5):")
print(f"  Mean:  {S.mean():.4f}  (exact: 8)")
print(f"  Var:   {S.var():.4f}  (exact: 8)")
```
=======
>>>>>>> Stashed changes
