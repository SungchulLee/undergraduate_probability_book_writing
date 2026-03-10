# Negative Binomial Distribution

The negative binomial counts the number of trials until $r$ successes — a sum of $r$ independent geometric random variables.

## Definition

$X \sim \text{NB}(r, p)$ if $X$ is the number of trials until the $r$-th success in independent Bernoulli($p$) trials.

**PMF:**

$$
P(X = k) = \binom{k-1}{r-1}p^r(1-p)^{k-r}, \qquad k = r, r+1, r+2, \ldots
$$

**Moments:**

$$
E[X] = \frac{r}{p}, \qquad \text{Var}(X) = \frac{r(1-p)}{p^2}
$$

Note: $\text{NB}(1, p) = \text{Geo}(p)$.

## Explanation

### Why the PMF Works

To have the $r$-th success on trial $k$: the first $k-1$ trials must contain exactly $r-1$ successes ($\binom{k-1}{r-1}$ arrangements), and trial $k$ must be a success ($p$). The total probability of any such arrangement is $p^r(1-p)^{k-r}$.

### Decomposition

$X = T_1 + T_2 + \cdots + T_r$ where $T_i \sim \text{Geo}(p)$ are independent (each $T_i$ is the waiting time between the $(i-1)$-th and $i$-th success). By independence:

$$
E[X] = r \cdot \frac{1}{p}, \qquad \text{Var}(X) = r \cdot \frac{1-p}{p^2}
$$

### Alternative Parameterization

Some texts define $Y$ = number of failures before $r$ successes, giving $Y = X - r$ and $P(Y = k) = \binom{k+r-1}{k}p^r(1-p)^k$ for $k = 0, 1, 2, \ldots$

## Examples

**Example.** Roll a die until the third 6. $X \sim \text{NB}(3, 1/6)$: $E[X] = 18$, $\text{SD}(X) = \sqrt{3 \cdot 5/36 \cdot 36} = \sqrt{90} \approx 9.49$.

```python
import numpy as np
from math import comb

np.random.seed(42)
n_sim = 200_000
r, p = 3, 1/6

# Simulate as sum of geometrics
samples = sum(np.random.geometric(p, n_sim) for _ in range(r))

E_theory = r / p
Var_theory = r * (1 - p) / p**2

print(f"E[X] = {samples.mean():.2f}  (theory: {E_theory:.1f})")
print(f"Var(X) = {samples.var():.1f}  (theory: {Var_theory:.1f})")

# Check PMF at k=18
k = 18
pmf_theory = comb(k-1, r-1) * p**r * (1-p)**(k-r)
pmf_sim = np.mean(samples == k)
print(f"P(X=18) = {pmf_sim:.4f}  (theory: {pmf_theory:.4f})")
```
