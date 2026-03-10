# Probability Mass Function

The PMF is the complete description of a discrete random variable's distribution — it assigns a probability to each possible value.

## Definition

The **probability mass function (PMF)** of a discrete random variable $X$ with values in $\{x_1, x_2, \ldots\}$ is

$$
p_X(x_i) = P(X = x_i)
$$

A valid PMF satisfies two properties:

1. **Non-negativity:** $p_X(x) \ge 0$ for all $x$.
2. **Normalization:** $\displaystyle\sum_i p_X(x_i) = 1$.

Any function satisfying these two properties defines a valid discrete distribution.

## Explanation

### Computing Probabilities from the PMF

For any set $A \subseteq \mathbb{R}$:

$$
P(X \in A) = \sum_{x_i \in A} p_X(x_i)
$$

The PMF contains all probabilistic information about $X$. Every probability question about $X$ reduces to summing the appropriate PMF values.

### PMF as a Weight Distribution

Return to the brick analogy: the PMF tells you the weight of the brick sitting at each point on the real line. The total weight is 1, and the weight at points not in the support is 0.

### Visualization

The PMF is displayed as a spike plot (or bar chart), where the height of each spike at $x_i$ equals $P(X = x_i)$. Unlike a histogram, spikes sit at isolated points — the probability between spikes is zero.

### PMF vs PDF

A common early confusion: the PMF gives actual probabilities ($p_X(x) = P(X = x)$), while the PDF for continuous variables gives probability *density* ($f_X(x) \ne P(X = x)$). Only the PMF can be read directly as a probability.

## Examples

**Example 1.** Let $X$ be the result of rolling a fair die.

$$
p_X(k) = \frac{1}{6}, \quad k = 1, 2, 3, 4, 5, 6
$$

Verification: $\sum_{k=1}^{6} 1/6 = 1$.

Then $P(X \ge 5) = p_X(5) + p_X(6) = 1/6 + 1/6 = 1/3$.

**Example 2.** A loaded coin has $P(H) = 0.7$. Flip it twice and let $X$ = number of heads. The PMF:

| $k$ | 0 | 1 | 2 |
|:---:|:---:|:---:|:---:|
| $p_X(k)$ | $0.09$ | $0.42$ | $0.49$ |

```python
# Loaded coin: P(H) = 0.7, two flips, X = number of heads
p = 0.7
pmf = {0: (1-p)**2, 1: 2*p*(1-p), 2: p**2}

for k, prob in pmf.items():
    print(f"P(X = {k}) = {prob:.2f}")
print(f"Sum = {sum(pmf.values()):.2f}")

# P(X >= 1)
print(f"P(X >= 1) = {pmf[1] + pmf[2]:.2f}")
```
