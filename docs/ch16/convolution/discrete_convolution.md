# Discrete Convolution

The PMF of a sum of independent discrete random variables is obtained by convolving their individual PMFs — summing over all ways the parts can add up.

## Definition

If $X$ and $Y$ are **independent** discrete random variables, the **convolution** of their PMFs gives the PMF of $X + Y$:

$$
p_{X+Y}(a) = (p_X * p_Y)(a) = \sum_{b} p_X(b) \cdot p_Y(a - b)
$$

The sum ranges over all $b$ where both $p_X(b) > 0$ and $p_Y(a - b) > 0$.

| Notation | Meaning |
|:---:|:---|
| $p_X * p_Y$ | PMF of $X + Y$ (discrete) |
| $f_X * f_Y$ | PDF of $X + Y$ (continuous) |
| $F_X * F_Y$ | CDF of $X + Y$ |

## Explanation

### Derivation

By the law of total probability, conditioning on $X = b$:

$$
P(X + Y = a) = \sum_b P(Y = a - b \mid X = b) \cdot P(X = b) = \sum_b p_Y(a - b) \cdot p_X(b)
$$

The last step uses independence: $P(Y = a - b \mid X = b) = P(Y = a - b)$.

### CDF Version

$$
F_{X+Y}(a) = \sum_b F_Y(a - b) \cdot p_X(b)
$$

where the sum runs over all values $b$ in the support of $X$.

### Properties

| Property | Statement |
|:---|:---|
| Commutativity | $p_X * p_Y = p_Y * p_X$ |
| Associativity | $(p_X * p_Y) * p_Z = p_X * (p_Y * p_Z)$ |
| Requires independence | Convolution gives $P(X+Y=a)$ only when $X \perp Y$ |
| MGF domain | $p_X * p_Y \leftrightarrow M_X(t) \cdot M_Y(t)$ |

Associativity means we can find the distribution of $X_1 + \cdots + X_n$ by convolving one pair at a time.

### Connection to MGFs

Convolution in the PMF domain corresponds to multiplication in the MGF domain:

$$
M_{X+Y}(t) = M_X(t) \cdot M_Y(t)
$$

When the MGF is available, multiplying is often simpler than computing the convolution sum directly.

## Examples

**Example.** Sum of two fair dice. Each die has PMF $p(k) = 1/6$ for $k = 1, \ldots, 6$.

For the sum $S = X + Y$, the convolution gives $P(S = 7) = 6/36 = 1/6$ (the most likely outcome), since there are 6 pairs $(b, 7-b)$ with both values in $\{1,\ldots,6\}$.

```python
import numpy as np

np.random.seed(42)

# PMF of a single fair die (values 1-6)
p = np.ones(6) / 6

# Convolve to get PMF of X + Y (values 2-12)
p_sum = np.convolve(p, p)
values = np.arange(2, 13)

# Verify via simulation
n_sim = 100_000
X = np.random.randint(1, 7, n_sim)
Y = np.random.randint(1, 7, n_sim)
S = X + Y
counts = np.bincount(S, minlength=13)[2:13]
probs_sim = counts / n_sim

print("Sum | Convolution | Simulation")
print("-" * 35)
for v, pc, ps in zip(values, p_sum, probs_sim):
    print(f"  {v:2d} |    {pc:.4f}    |   {ps:.4f}")
```
