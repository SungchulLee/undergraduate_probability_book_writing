# MGF of Geometric and Negative Binomial

The negative binomial MGF is a power of the geometric MGF, mirroring the sum-of-geometrics decomposition.

## Definition

**Geometric** ($X \sim \text{Geo}(p)$, trials until first success):

$$
M_X(t) = \frac{pe^t}{1 - qe^t}, \qquad t < -\ln q
$$

**Negative binomial** ($X \sim \text{NB}(r, p)$):

$$
M_X(t) = \left(\frac{pe^t}{1 - qe^t}\right)^r, \qquad t < -\ln q
$$

where $q = 1 - p$.

## Explanation

### Derivation

$$
M_X(t) = \sum_{k=1}^{\infty}e^{tk}q^{k-1}p = pe^t\sum_{k=0}^{\infty}(qe^t)^k = \frac{pe^t}{1 - qe^t}
$$

Convergence requires $qe^t < 1$, i.e., $t < -\ln q$.

### Moments

Geometric: $E[X] = 1/p$, $\text{Var}(X) = q/p^2$.

Negative binomial: $E[X] = r/p$, $\text{Var}(X) = rq/p^2$.

### Sum Property

$\text{NB}(r_1, p) + \text{NB}(r_2, p) \sim \text{NB}(r_1 + r_2, p)$ for independent summands with the same $p$.

## Examples

**Example.** $X \sim \text{Geo}(0.3)$: $E[X] \approx 3.33$, $\text{Var}(X) \approx 7.78$.

```python
import numpy as np

np.random.seed(42)
n_sim = 200_000
p = 0.3

X = np.random.geometric(p, n_sim)
print(f"Geo(0.3): E={X.mean():.3f} (theory: {1/p:.3f}), "
      f"Var={X.var():.3f} (theory: {(1-p)/p**2:.3f})")

r = 5
S = sum(np.random.geometric(p, n_sim) for _ in range(r))
print(f"NB(5,0.3): E={S.mean():.3f} (theory: {r/p:.3f}), "
      f"Var={S.var():.2f} (theory: {r*(1-p)/p**2:.2f})")
```
