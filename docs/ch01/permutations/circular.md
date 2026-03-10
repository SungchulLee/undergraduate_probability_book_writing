# Circular Permutations

Circular permutations arrange objects around a circle, where rotations are considered identical. This is a clean application of the many-to-one principle.

## Definition

The number of ways to arrange $n$ distinct objects in a circle is

$$
(n-1)!
$$

## Explanation

**Approach 1 (Many-to-one).** Start with the $n!$ linear arrangements. Each circular arrangement corresponds to exactly $n$ linear ones (by choosing which element appears "first"). Dividing: $n!/n = (n-1)!$.

**Approach 2 (Fix one element).** A circle has no distinguished starting position. Fix one object to break the rotational symmetry, then arrange the remaining $n-1$ objects: $(n-1)!$ ways.

### With Reflections

If the circle can be flipped (e.g., a bracelet rather than a seated table), reflections also produce equivalent arrangements. Each circular arrangement and its mirror image are the same, giving

$$
\frac{(n-1)!}{2}
$$

distinct arrangements (for $n \ge 3$).

## Examples

**Example 1 (Dinner table).** Seat 6 people around a circular table: $(6-1)! = 120$.

For comparison, in a row: $6! = 720 = 6 \times 120$ — exactly 6 times as many, since each circular seating corresponds to 6 linear ones.

---

**Example 2 (Keychain).** Arrange 5 keys on a keychain (reflections equivalent): $(5-1)!/2 = 24/2 = 12$.

```python
from math import factorial

# Example 1
n = 6
circular = factorial(n - 1)
linear = factorial(n)
print(f"Circular permutations of {n}: {circular}")
print(f"Linear permutations: {linear}")
print(f"Ratio: {linear // circular}")
# Output: Circular: 120, Linear: 720, Ratio: 6

# Example 2
n = 5
bracelet = factorial(n - 1) // 2
print(f"Bracelet arrangements of {n}: {bracelet}")
# Output: Bracelet arrangements of 5: 12
```
