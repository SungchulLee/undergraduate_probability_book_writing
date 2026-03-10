# Multiplication Rule

The multiplication rule is the most fundamental counting principle. It converts a multi-stage procedure into a single product, and underpins nearly every formula in combinatorics.

## Definition

If a procedure consists of $k$ sequential stages with $n_1, n_2, \ldots, n_k$ possible outcomes at each stage (where the count at each stage does not depend on the choices made at earlier stages), then the total number of outcomes is

$$
n_1 \times n_2 \times \cdots \times n_k
$$

The key requirement is **independence of stage counts**: the number of choices available at stage $i$ must be the same regardless of which outcomes occurred at stages $1, \ldots, i-1$. When this condition fails (e.g., "choose a letter, then choose a digit different from the letter" — which makes no sense), the multiplication rule does not directly apply.

## Explanation

### Tree Diagram Interpretation

The multiplication rule is most naturally visualized as a **tree diagram**. Each stage of the experiment corresponds to a level of branching. Every path from the root to a leaf represents one outcome, and the total number of leaves equals the product of the branching factors at each level.

For a two-stage experiment with $m$ choices at Stage 1 and $n$ choices at Stage 2, the tree has $m$ branches at the first level, each splitting into $n$ branches at the second level, for $m \times n$ leaves total.

### When Stage Counts Vary

Sometimes the number of choices at a later stage depends on earlier choices — for instance, "choose two distinct elements from $\{1, \ldots, n\}$." Here Stage 2 always has $n-1$ choices regardless of which element was chosen first, so the multiplication rule still applies: the count is $n(n-1)$.

But if different first-stage choices led to *different* numbers of second-stage options, you would need to use a tree diagram with unequal branching and sum the leaf counts (the addition rule), rather than multiply.

## Examples

**Example 1 (Paths through a network).** Count the paths from $A$ to $C$ via $B$, where there are 2 paths from $A$ to $B$ and 3 paths from $B$ to $C$.

| $A \to B$ | $B \to C$ | Combined |
|:---:|:---:|:---:|
| 1 | $a$ | $1a$ |
| 1 | $b$ | $1b$ |
| 1 | $c$ | $1c$ |
| 2 | $a$ | $2a$ |
| 2 | $b$ | $2b$ |
| 2 | $c$ | $2c$ |

Total: $2 \times 3 = 6$ paths.

---

**Example 2 (Choosing officers).** From $n$ people, choose a president, vice-president, and secretary (all distinct).

- President: $n$ choices
- Vice-president: $n - 1$ choices (anyone except the president)
- Secretary: $n - 2$ choices

Total: $n(n-1)(n-2)$. For $n = 10$: $10 \times 9 \times 8 = 720$.

This is a **permutation** — an ordered selection without repetition — and leads directly to the general permutation formula.

---

**Example 3 (License plates).** A license plate consists of 3 letters followed by 4 digits. How many plates are possible if repetition is allowed?

$$
26 \times 26 \times 26 \times 10 \times 10 \times 10 \times 10 = 26^3 \times 10^4 = 175{,}760{,}000
$$

```python
from math import prod
from itertools import permutations

# Example 2: Officers from 10 people
n = 10
officers = n * (n - 1) * (n - 2)
verification = len(list(permutations(range(1, n + 1), 3)))
print(f"Officers from {n} people: {officers} (verified: {verification})")
# Output: Officers from 10 people: 720 (verified: 720)

# Example 3: License plates
plates = 26**3 * 10**4
print(f"License plates: {plates:,}")
# Output: License plates: 175,760,000
```
