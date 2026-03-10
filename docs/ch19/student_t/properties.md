# Student's t Properties

The $t$ distribution is symmetric with heavier tails than the normal. Its variance exceeds 1 for all finite degrees of freedom, and when $d = 1$ it becomes the Cauchy distribution, which has no finite moments at all.

## Definition

For $T \sim t_d$, the key properties are:

$$
E[T] = 0 \;\;(d > 1), \qquad \operatorname{Var}(T) = \frac{d}{d-2} \;\;(d > 2)
$$

## Explanation

### Mean

By symmetry of the PDF, $E[T] = 0$ whenever the mean exists ($d > 1$).

### Variance

The variance $d/(d-2)$ is always greater than 1 and approaches 1 as $d \to \infty$, consistent with convergence to $N(0,1)$. The extra variance reflects the additional randomness from estimating $\sigma$ with $S$.

### Heavy tails

The $t_d$ density decays as $|t|^{-(d+1)}$ (polynomial), while the normal decays as $e^{-t^2/2}$ (exponential). This means extreme values are more likely under $t_d$ than under $N(0,1)$.

### Cauchy distribution (d = 1)

When $d = 1$, the PDF simplifies to $f(t) = 1/[\pi(1 + t^2)]$. The Cauchy distribution has no finite mean, no finite variance, and the sample mean of iid Cauchy variables has the same Cauchy distribution (the CLT does not apply).

## Examples

**Example 1.** Compare tail probabilities of $t_d$ and $N(0,1)$.

```python
from scipy import stats

print(f"{'d':>5}  {'Var(t_d)':>10}  {'P(|T|>1.96)':>14}")
for d in [1, 5, 10, 30, 100]:
    var_str = "inf" if d <= 2 else f"{d/(d-2):.4f}"
    tail = 2 * stats.t(d).sf(1.96)
    print(f"{d:5d}  {var_str:>10}  {tail:14.4f}")

tail_norm = 2 * stats.norm.sf(1.96)
print(f"{'inf':>5}  {'1.0000':>10}  {tail_norm:14.4f}")
```
