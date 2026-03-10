# Convergence of t to Normal

As the degrees of freedom increase, the $t$ distribution converges to the standard normal. This explains why $z$-tests and $t$-tests give nearly identical results for large samples.

## Definition

As $d \to \infty$:

$$
t_d \xrightarrow{d} N(0,1)
$$

## Explanation

### Proof via Slutsky's theorem

Write $T = Z/\sqrt{V/d}$ where $V = \sum_{i=1}^d W_i^2$ with $W_i$ iid $N(0,1)$. By the law of large numbers:

$$
\frac{V}{d} = \frac{1}{d}\sum_{i=1}^d W_i^2 \xrightarrow{p} E[W^2] = 1
$$

So $\sqrt{V/d} \xrightarrow{p} 1$, and by Slutsky's theorem $T \xrightarrow{d} Z \sim N(0,1)$.

### Pointwise PDF convergence

At each point $t$, using $(1 + a/d)^d \to e^a$:

$$
\left(1 + \frac{t^2}{d}\right)^{-(d+1)/2} \to e^{-t^2/2} \quad \text{as } d \to \infty
$$

### Practical rule of thumb

For $d \ge 30$, the $t$ and normal critical values differ by less than a few percent. Using $z$-values in place of $t$-values introduces only minor error for large degrees of freedom.

## Examples

**Example 1.** Show how the tail probability $P(|T| > 1.96)$ approaches 0.05 as $d$ grows.

```python
from scipy import stats

print(f"{'d':>5}  {'P(|T|>1.96)':>14}  {'Var(t_d)':>10}")
for d in [1, 3, 5, 10, 30, 100, 1000]:
    tail = 2 * stats.t(d).sf(1.96)
    var_str = "inf" if d <= 2 else f"{d/(d-2):.4f}"
    print(f"{d:5d}  {tail:14.4f}  {var_str:>10}")

print(f"{'inf':>5}  {2*stats.norm.sf(1.96):14.4f}  {'1.0000':>10}")
```
