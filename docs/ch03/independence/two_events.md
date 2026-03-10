# Independence of Two Events

Independence is the probabilistic formalization of "no information": knowing one event occurred tells you nothing about whether the other occurred.

## Definition

Events $A$ and $B$ are **independent** if

$$
P(A \cap B) = P(A)\,P(B)
$$

Equivalently (when $P(A), P(B) > 0$): $P(B \mid A) = P(B)$ and $P(A \mid B) = P(A)$.

## Explanation

### Independence vs Disjointness

These are fundamentally different:

- **Disjoint** events ($A \cap B = \emptyset$) are *maximally dependent*: knowing $A$ occurred tells you $B$ did not.
- **Independent** events with positive probability must overlap: $P(A \cap B) = P(A)P(B) > 0$.

### Complements

If $A$ and $B$ are independent, then so are $A$ and $B^c$, $A^c$ and $B$, and $A^c$ and $B^c$.

*Proof:* $P(AB^c) = P(A) - P(AB) = P(A) - P(A)P(B) = P(A)(1 - P(B)) = P(A)P(B^c)$. $\square$

### Computing Unions and Intersections

For **independent** events: $P(A_1 \cdots A_n) = \prod P(A_i)$.

The complement method for unions is especially clean:

$$
P\left(\bigcup_{i=1}^n A_i\right) = 1 - \prod_{i=1}^n (1 - P(A_i))
$$

## Examples

**Example.** Flip a fair coin and roll a fair die. $A$ = "heads", $B$ = "even roll."

$P(A) = 1/2$, $P(B) = 1/2$, $P(AB) = P(\text{heads and even}) = 1/4 = P(A)P(B)$. Independent. ✓

---

**Example (At least one 6).** Roll a die 4 times. $P(\text{at least one 6}) = 1 - (5/6)^4 \approx 0.518$.

```python
# Independence verification
P_A = 1/2  # heads
P_B = 1/2  # even die
P_AB = 1/4  # heads AND even
print(f"P(AB) = {P_AB}, P(A)*P(B) = {P_A * P_B}, Independent: {P_AB == P_A * P_B}")

# At least one 6 in 4 rolls
print(f"P(at least one 6) = {1 - (5/6)**4:.4f}")
```
