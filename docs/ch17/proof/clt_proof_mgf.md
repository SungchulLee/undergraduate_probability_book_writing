# CLT Proof via MGFs

The MGF of the standardized sum converges pointwise to $e^{t^2/2}$, the MGF of $N(0,1)$, establishing the CLT through the continuity theorem.

## Definition

**Theorem (CLT).** If $X_1, X_2, \ldots$ are iid with mean $\mu$, variance $\sigma^2$, and MGF $M_X(t)$ existing in a neighborhood of $0$, then:

$$
\frac{S_n - n\mu}{\sigma\sqrt{n}} \xrightarrow{d} N(0,1)
$$

## Explanation

### Setup

Define standardized variables $Y_k = (X_k - \mu)/\sigma$, so $E[Y_k] = 0$, $E[Y_k^2] = 1$. The standardized sum is:

$$
Z_n = \frac{S_n - n\mu}{\sigma\sqrt{n}} = \sum_{k=1}^n \frac{Y_k}{\sqrt{n}}
$$

### Proof

**Step 1.** Factor the MGF using independence:

$$
M_{Z_n}(t) = \left[M_{Y_1}\!\left(\frac{t}{\sqrt{n}}\right)\right]^n
$$

**Step 2.** Taylor expand around $0$:

$$
M_{Y_1}(s) = 1 + s \cdot E[Y_1] + \frac{s^2}{2} E[Y_1^2] + O(s^3) = 1 + \frac{s^2}{2} + O(s^3)
$$

**Step 3.** Substitute $s = t/\sqrt{n}$:

$$
M_{Y_1}\!\left(\frac{t}{\sqrt{n}}\right) = 1 + \frac{t^2}{2n} + O(n^{-3/2})
$$

**Step 4.** Take the $n$-th power and the limit:

$$
M_{Z_n}(t) = \left(1 + \frac{t^2}{2n} + O(n^{-3/2})\right)^n \to e^{t^2/2}
$$

using $\lim_{n\to\infty}(1 + a/n)^n = e^a$.

**Step 5.** By the continuity theorem for MGFs, $Z_n \xrightarrow{d} N(0,1)$. $\square$

### Key Ingredients

| Ingredient | Role |
|:---|:---|
| Independence | Factors $M_{Z_n}(t) = [M_{Y_1}(t/\sqrt{n})]^n$ |
| Finite variance | Validates the Taylor expansion to second order |
| Continuity theorem | Converts MGF convergence to distributional convergence |

??? note "Why finite variance is essential"
    The Taylor expansion requires $E[Y_1^2] = 1 < \infty$. For the Cauchy distribution, the variance is infinite, the MGF does not exist, and the CLT fails: the standardized sum of iid Cauchy random variables remains Cauchy.

## Examples

**Example.** Verify the MGF convergence numerically for $X_i \sim \operatorname{Exp}(1)$.

```python
import numpy as np

# MGF of standardized Exp(1): Y = (X-1)/1, M_Y(t) = e^{-t}/(1-t) for t<1
def mgf_Zn(t, n):
    """MGF of standardized sum of n iid Exp(1)."""
    s = t / np.sqrt(n)
    if s >= 1:
        return float('inf')
    return (np.exp(-s) / (1 - s)) ** n

# Compare with N(0,1) MGF = exp(t^2/2)
for t in [0.5, 1.0]:
    print(f"t = {t}")
    for n in [10, 100, 1000]:
        ratio = mgf_Zn(t, n) / np.exp(t**2 / 2)
        print(f"  n={n:5d}: M_Zn({t}) / exp(t²/2) = {ratio:.6f}")
```
