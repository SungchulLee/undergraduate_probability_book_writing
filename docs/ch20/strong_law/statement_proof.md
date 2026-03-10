# Strong Law of Large Numbers

The sample mean converges almost surely to the population mean — with probability one, the running average eventually settles at $\mu$ and stays there.

## Definition

Let $X_1, X_2, \ldots$ be iid with $E[\lvert X_i \rvert] < \infty$. Then:

$$
P\!\left(\lim_{n \to \infty} \bar{X}_n = \mu\right) = 1
$$

More generally, $\frac{1}{n}\sum_{i=1}^n g(X_i) \xrightarrow{a.s.} E[g(X)]$ whenever $E[\lvert g(X) \rvert] < \infty$.

## Explanation

### Proof Sketch (Finite Fourth Moment)

Assume $E[X_i^4] < \infty$. Let $S_n = \sum X_i$.

**Step 1.** Show $\sum_{n=1}^\infty E[(\bar{X}_n - \mu)^4] < \infty$. Cross-terms vanish by independence, leaving $E[(S_n - n\mu)^4] = O(n^2)$, so $E[(\bar{X}_n - \mu)^4] = O(n^{-2})$.

**Step 2.** Since expectations sum to a finite value, the sum $\sum (\bar{X}_n - \mu)^4 < \infty$ a.s.

**Step 3.** Terms of a convergent series go to zero: $(\bar{X}_n - \mu)^4 \to 0$ a.s.

**Step 4.** Take fourth roots: $\bar{X}_n \to \mu$ a.s. $\square$

The full SLLN (Kolmogorov) requires only $E[\lvert X \rvert] < \infty$ but uses more advanced tools.

### WLLN vs SLLN

| | Weak Law | Strong Law |
|:---|:---|:---|
| Mode | In probability | Almost surely |
| Simple proof needs | $\sigma^2 < \infty$ | $E[X^4] < \infty$ |
| General version needs | $E[\lvert X \rvert] < \infty$ | $E[\lvert X \rvert] < \infty$ |
| Technique | Chebyshev | Fourth moment + series |

## Examples

**Example.** Verify SLLN for $\operatorname{Exp}(1)$: all paths converge to $\mu = 1$.

```python
import numpy as np

np.random.seed(42)
n = 50_000

for trial in range(5):
    X = np.random.exponential(1.0, n)
    X_bar = np.cumsum(X) / np.arange(1, n + 1)
    print(f"Trial {trial+1}: X̄_{n} = {X_bar[-1]:.6f}")
```
