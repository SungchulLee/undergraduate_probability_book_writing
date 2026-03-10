# Permutations with Repetition

When some objects are identical, swapping them produces no new arrangement. The many-to-one principle corrects for this overcounting, yielding the multinomial coefficient.

## Definition

Given $n$ objects where $n_i$ are identical copies of type $i$ ($i = 1, \ldots, m$, with $n_1 + \cdots + n_m = n$), the number of distinct arrangements is

$$
\frac{n!}{n_1!\, n_2! \cdots n_m!}
$$

## Explanation

### The Many-to-One Principle

**Setup.** Temporarily label every object as distinct (attach subscripts to identical copies). There are $n!$ arrangements.

**Overcounting.** For each distinct arrangement, the $n_i$ copies of type $i$ can be internally permuted in $n_i!$ ways without changing the visible result. The total overcounting factor is $n_1! \cdot n_2! \cdots n_m!$.

**Result.** This is an $(n_1! \cdots n_m!)$-to-1 mapping from labeled to unlabeled arrangements, giving $n! / (n_1! \cdots n_m!)$.

### Worked Derivation — BOB

**Step 1.** Attach indices: $B_1, O, B_2$. Arrangements: $3! = 6$.

**Step 2.** List all and remove indices:

| Indexed | Unindexed |
|:---:|:---:|
| $B_1 B_2 O$ | BBO |
| $B_1 O B_2$ | BOB |
| $B_2 B_1 O$ | BBO |
| $B_2 O B_1$ | BOB |
| $O B_1 B_2$ | OBB |
| $O B_2 B_1$ | OBB |

**Step 3.** Each distinct word appears $2! = 2$ times. By many-to-one: $3!/2! = 3$.

## Examples

**Example 1 (BBOOO).** $n=5$: two B's, three O's.

$$
\frac{5!}{2!\cdot 3!} = \frac{120}{12} = 10
$$

---

**Example 2 (MISSISSIPPI).** $n=11$: M(1), I(4), S(4), P(2).

$$
\frac{11!}{1!\cdot 4!\cdot 4!\cdot 2!} = 34{,}650
$$

```python
from math import factorial
from collections import Counter
from itertools import permutations

def distinct_permutations(word):
    """Count distinct permutations via the multinomial coefficient."""
    n = len(word)
    denom = 1
    for c in Counter(word).values():
        denom *= factorial(c)
    return factorial(n) // denom

# Example 1
word = "BBOOO"
formula = distinct_permutations(word)
brute = len(set(permutations(word)))
print(f"'{word}': formula={formula}, brute force={brute}")
# Output: 'BBOOO': formula=10, brute force=10

# Example 2
word = "MISSISSIPPI"
print(f"'{word}': {distinct_permutations(word)}")
# Output: 'MISSISSIPPI': 34650
```
