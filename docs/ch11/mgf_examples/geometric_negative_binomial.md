# MGF of Geometric and Negative Binomial
<<<<<<< Updated upstream

## MGF of Geometric$(p)$

Let $X \sim \text{Geo}(p)$ count the number of trials until the first success, so $P(X = k) = (1-p)^{k-1}p$ for $k = 1, 2, 3, \ldots$

$$M_X(t) = E[e^{tX}] = \sum_{k=1}^{\infty} e^{tk}(1-p)^{k-1}p = pe^t \sum_{k=0}^{\infty} [(1-p)e^t]^k$$

The geometric series converges when $(1-p)e^t < 1$, i.e., $t < -\ln(1-p)$:

$$M_X(t) = \frac{pe^t}{1 - (1-p)e^t}$$

$$\boxed{M_{\text{Geo}(p)}(t) = \frac{pe^t}{1 - (1-p)e^t}, \quad t < -\ln(1-p)}$$

### Deriving Moments

Let $q = 1 - p$. Write $M(t) = pe^t(1 - qe^t)^{-1}$ and differentiate using the quotient rule:

$$M'(t) = \frac{pe^t(1 - qe^t) + pe^t \cdot qe^t}{(1 - qe^t)^2} = \frac{pe^t}{(1 - qe^t)^2}$$

$$E[X] = M'(0) = \frac{p}{(1 - q)^2} = \frac{p}{p^2} = \frac{1}{p}$$

For the second derivative:

$$M''(t) = \frac{pe^t(1 - qe^t)^2 + 2pe^t \cdot qe^t(1 - qe^t)}{(1 - qe^t)^4} = \frac{pe^t(1 + qe^t)}{(1 - qe^t)^3}$$

$$E[X^2] = M''(0) = \frac{p(1 + q)}{p^3} = \frac{1 + q}{p^2} = \frac{2 - p}{p^2}$$

$$\text{Var}(X) = \frac{2 - p}{p^2} - \frac{1}{p^2} = \frac{1 - p}{p^2} = \frac{q}{p^2}$$

## MGF of Negative Binomial$(r, p)$

The negative binomial $X \sim \text{NB}(r, p)$ counts the number of trials until the $r$-th success. It can be written as a sum of $r$ independent geometric random variables:

$$X = X_1 + X_2 + \cdots + X_r, \quad X_i \stackrel{\text{iid}}{\sim} \text{Geo}(p)$$

By independence, the MGF of a sum is the product of the MGFs:

$$M_X(t) = \prod_{i=1}^r M_{X_i}(t) = \left[\frac{pe^t}{1 - (1-p)e^t}\right]^r$$

$$\boxed{M_{\text{NB}(r,p)}(t) = \left[\frac{pe^t}{1 - (1-p)e^t}\right]^r, \quad t < -\ln(1-p)}$$

### Deriving Moments via the Geometric

Since $X = \sum_{i=1}^r X_i$ with $X_i$ iid Geo$(p)$:

$$E[X] = r \cdot E[X_1] = \frac{r}{p}$$

$$\text{Var}(X) = r \cdot \text{Var}(X_1) = \frac{r(1-p)}{p^2}$$

## Python Verification

```python
import numpy as np
from scipy.misc import derivative

def mgf_geo(t, p=0.3):
    q = 1 - p
    return p * np.exp(t) / (1 - q * np.exp(t))

def mgf_nb(t, r=5, p=0.3):
    return mgf_geo(t, p)**r

# Geo(0.3): E[X] = 10/3, Var(X) = 70/9
p = 0.3
EX = derivative(mgf_geo, 0, n=1, dx=1e-6)
EX2 = derivative(mgf_geo, 0, n=2, dx=1e-6)
print(f"Geo({p}):")
print(f"  E[X]   = {EX:.4f}  (exact: {1/p:.4f})")
print(f"  Var(X) = {EX2 - EX**2:.4f}  (exact: {(1-p)/p**2:.4f})")

# NB(5, 0.3): E[X] = 50/3, Var(X) = 350/9
r = 5
EX = derivative(mgf_nb, 0, n=1, dx=1e-6)
EX2 = derivative(mgf_nb, 0, n=2, dx=1e-6)
print(f"\nNB({r}, {p}):")
print(f"  E[X]   = {EX:.4f}  (exact: {r/p:.4f})")
print(f"  Var(X) = {EX2 - EX**2:.4f}  (exact: {r*(1-p)/p**2:.4f})")
```
=======
>>>>>>> Stashed changes
