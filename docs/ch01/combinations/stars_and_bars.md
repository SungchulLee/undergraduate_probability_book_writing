# Combinations with Repetition (Stars and Bars)

Stars and bars is the standard technique for counting selections where repetition is allowed. It converts a distribution problem into a simple binomial coefficient.

## Definition

The number of ways to choose $k$ items from $n$ types (with repetition, order irrelevant) is

$$
\binom{k + n - 1}{n - 1} = \binom{k + n - 1}{k}
$$

Equivalently, this counts non-negative integer solutions to $x_1 + x_2 + \cdots + x_n = k$.

**With at least 1 per type:** the number of positive integer solutions to $x_1 + \cdots + x_n = k$ (each $x_i \ge 1$) is

$$
\binom{k - 1}{n - 1}
$$

## Explanation

Represent the $k$ items as **stars** ($\star$) and separate $n$ types using $n-1$ **bars** ($|$). Every arrangement of $k$ stars and $n-1$ bars corresponds to exactly one valid selection: the stars between the $(i-1)$-th and $i$-th bar represent items of type $i$.

The total number of symbols is $k + n - 1$. Choosing which $n-1$ positions are bars (the rest are stars) gives $\binom{k+n-1}{n-1}$.

**Positive solutions.** If each type must appear at least once, first give 1 item to each type (using $n$ of the $k$ items), then distribute the remaining $k - n$ freely:

$$
\binom{(k-n)+n-1}{n-1} = \binom{k-1}{n-1}
$$

## Examples

**Example 1.** Choose 3 items from 4 types: $\binom{6}{3} = 20$.

One arrangement: $\star\star\,|\,\star\,|\,|\,$ means $(x_1,x_2,x_3,x_4) = (2,1,0,0)$.

---

**Example 2 (Distributing money).** Split \$10 among 3 people so each gets at least \$1.

Positive solutions to $x_1 + x_2 + x_3 = 10$: $\binom{9}{2} = 36$.

Without the "at least \$1" constraint: $\binom{12}{2} = 66$.

---

**Example 3 (Upper bounds).** How many non-negative integer solutions to $x_1 + x_2 + x_3 \le 8$?

Introduce a slack variable $x_4 \ge 0$ so $x_1 + x_2 + x_3 + x_4 = 8$: $\binom{11}{3} = 165$.

```python
from math import comb

# Example 1
print(f"Choose 3 from 4 types: {comb(6, 3)}")
# Output: Choose 3 from 4 types: 20

# Verify by enumeration
k, n = 3, 4
solutions = [
    (x1, x2, x3, k - x1 - x2 - x3)
    for x1 in range(k + 1)
    for x2 in range(k - x1 + 1)
    for x3 in range(k - x1 - x2 + 1)
]
print(f"Enumeration: {len(solutions)}")
# Output: Enumeration: 20

# Example 2
print(f"$10 among 3, each ≥ $1: {comb(9, 2)}")
print(f"$10 among 3, each ≥ $0: {comb(12, 2)}")

# Example 3
print(f"x1+x2+x3 ≤ 8 (non-neg): {comb(11, 3)}")
```
