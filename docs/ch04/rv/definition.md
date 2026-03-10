# Random Variable

A random variable is a function from the sample space to the real line, translating abstract outcomes into numbers that can be analyzed with calculus and algebra.

## Definition

A **random variable** is a function $X : \Omega \to \mathbb{R}$ that assigns a real number $X(\omega)$ to each outcome $\omega$ in a sample space $\Omega$.

The **distribution** of $X$ describes how probability mass is distributed over $\mathbb{R}$:

$$
P(X \in A) = P(\{\omega \in \Omega : X(\omega) \in A\})
$$

## Explanation

### The Brick Analogy

Attach a brick to each outcome $\omega \in \Omega$, with weight $P(\{\omega\})$. The function $X$ moves each brick from $\omega$ to the point $X(\omega)$ on the real line. After all bricks are placed, the total weight on $\mathbb{R}$ is 1, and the resulting weight distribution is the distribution of $X$.

- $P(X = a)$ is the total weight of bricks at point $a$
- $P(X \in A)$ is the total weight of bricks in the set $A$

### Why Random Variables Matter

Without random variables, probability lives in abstract sample spaces where outcomes might be strings like "HHT" or "defective." By mapping outcomes to numbers, we can compute averages, variances, and apply the machinery of calculus — tools that do not operate on abstract labels.

### Measurability (Technical Note)

The formal requirement is that $\{X \le a\} = \{\omega : X(\omega) \le a\}$ must be an event (i.e., belong to the $\sigma$-algebra) for every $a \in \mathbb{R}$. For finite and countable sample spaces with the power set $\sigma$-algebra, every function $X : \Omega \to \mathbb{R}$ is automatically a random variable.

## Examples

**Example 1.** Roll a fair die once and let $X$ be the number shown. Then $X : \Omega \to \{1,2,3,4,5,6\}$ with $P(X = k) = 1/6$ for each $k$.

**Example 2.** Flip a fair coin three times. Let $X$ = number of heads in the first two flips, and $Y$ = total number of heads. The sample space is $\Omega = \{HHH, HHT, HTH, HTT, THH, THT, TTH, TTT\}$.

| $\omega$ | $X(\omega)$ | $Y(\omega)$ |
|:---------:|:-----------:|:------------:|
| HHH | 2 | 3 |
| HHT | 2 | 2 |
| HTH | 1 | 2 |
| HTT | 1 | 1 |
| THH | 1 | 2 |
| THT | 1 | 1 |
| TTH | 0 | 1 |
| TTT | 0 | 0 |

From the table: $P(X = 0) = 2/8$, $P(X = 1) = 4/8$, $P(X = 2) = 2/8$.

```python
from itertools import product

# All outcomes of 3 fair coin flips
outcomes = list(product('HT', repeat=3))
X = lambda w: w[:2].count('H')
Y = lambda w: w.count('H')

for x_val in [0, 1, 2]:
    count = sum(1 for w in outcomes if X(w) == x_val)
    print(f"P(X = {x_val}) = {count}/{len(outcomes)} = {count/len(outcomes):.4f}")
```
