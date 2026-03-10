# Categorical and Multinomial Distributions

The Categorical and Multinomial distributions generalize the Bernoulli and Binomial from two outcomes to $K$ outcomes — from coin flips to die rolls.

## Definition

**Categorical** $\text{Cat}(\mathbf{p})$: Roll a $K$-sided die once with probability vector $\mathbf{p} = (p_1, \ldots, p_K)$, $\sum p_j = 1$. Record the outcome as a one-hot vector $(X_1, \ldots, X_K)$:

$$
P(X_j = 1, X_k = 0 \text{ for } k \ne j) = p_j
$$

**Multinomial** $\text{Mult}(n, \mathbf{p})$: Roll the die $n$ times independently. Let $X_j$ count face $j$. Then

$$
P(X_1 = n_1, \ldots, X_K = n_K) = \frac{n!}{n_1!\cdots n_K!}\,p_1^{n_1}\cdots p_K^{n_K}
$$

where $n_1 + \cdots + n_K = n$.

## Explanation

### Relationship to Coin-Flip Distributions

| Coin (2 outcomes) | Die ($K$ outcomes) |
|:-------------------|:-------------------|
| $\text{Bern}(p)$ | $\text{Cat}(\mathbf{p})$ |
| $\text{Bin}(n, p)$ | $\text{Mult}(n, \mathbf{p})$ |

Setting $K = 2$ with $\mathbf{p} = (p, 1-p)$ recovers the Bernoulli and Binomial.

### Marginals are Binomial

Each component $X_j$ of a Multinomial is marginally Binomial:

$$
X_j \sim \text{Bin}(n, p_j)
$$

However, the components are **not independent** because $X_1 + \cdots + X_K = n$. Knowing that face 1 appeared often means less room for the others.

### Multinomial Coefficient

The factor $\frac{n!}{n_1!\cdots n_K!}$ counts the number of sequences of length $n$ with exactly $n_j$ copies of symbol $j$. Each such sequence has probability $p_1^{n_1}\cdots p_K^{n_K}$.

## Examples

**Example.** A fair six-sided die is rolled $n = 12$ times. What is the probability that each face appears exactly twice?

$$
P(X_1 = \cdots = X_6 = 2) = \frac{12!}{(2!)^6}\left(\frac{1}{6}\right)^{12} \approx 0.00344
$$

```python
from math import factorial, comb

# Each face appears exactly twice in 12 rolls of a fair die
n, K = 12, 6
p = 1 / K
numer = factorial(n)
denom = factorial(2)**K
multinomial_coeff = numer // denom
prob = multinomial_coeff * p**n
print(f"Multinomial coefficient: {multinomial_coeff}")
print(f"P(each face twice) = {prob:.6f}")

# Marginal: X_1 ~ Bin(12, 1/6)
from math import comb
p_x1_2 = comb(12, 2) * (1/6)**2 * (5/6)**10
print(f"\nMarginal: P(X_1 = 2) = {p_x1_2:.4f}")
print(f"E[X_1] = {n * p:.2f}, Var(X_1) = {n * p * (1-p):.2f}")
```
