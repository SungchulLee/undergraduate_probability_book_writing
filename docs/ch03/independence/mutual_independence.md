# Mutual Independence

Mutual independence requires the product rule to hold for every subcollection of events, not just pairs. This is strictly stronger than pairwise independence.

## Definition

Events $A_1, \ldots, A_n$ are **mutually independent** if for every subcollection of size $2 \le m \le n$:

$$
P(A_{i_1} \cap \cdots \cap A_{i_m}) = P(A_{i_1}) \cdots P(A_{i_m})
$$

This requires $2^n - n - 1$ conditions. Events are **pairwise independent** if only the $\binom{n}{2}$ pairwise conditions hold.

Mutual independence $\implies$ pairwise independence, but the converse is **false**.

## Explanation

### Why Pairwise Is Not Enough

Consider $n$ people with independent uniform birthdays. Let $A_{ij}$ = "persons $i$ and $j$ share a birthday."

**Pairwise independent:** $P(A_{13} \mid A_{12}) = P(A_{13}) = 1/365$, because knowing persons 1 and 2 match tells you nothing about whether persons 1 and 3 match (they picked independently).

**Not mutually independent:** $P(A_{23} \mid A_{12} \cap A_{13}) = 1$. If persons 1,2 match and persons 1,3 match, then persons 2,3 must match. The three-way condition fails.

### Consequences

- Variance of a sum: $\text{Var}(\sum X_i) = \sum \text{Var}(X_i)$ requires only pairwise independence (uncorrelatedness suffices).
- MGF of a sum factoring: $M_{\sum X_i}(t) = \prod M_{X_i}(t)$ requires mutual independence.
- Most limit theorems (CLT, LLN) require mutual independence.

## Examples

**Example (Three coins).** Flip a fair coin twice. Let $A$ = "first is H", $B$ = "second is H", $C$ = "both same."

- $P(A) = P(B) = P(C) = 1/2$
- $P(AB) = 1/4 = P(A)P(B)$ ✓
- $P(AC) = P(\text{HH}) = 1/4 = P(A)P(C)$ ✓
- $P(BC) = P(\text{HH}) = 1/4 = P(B)P(C)$ ✓
- $P(ABC) = P(\text{HH}) = 1/4 \ne 1/8 = P(A)P(B)P(C)$ ✗

Pairwise independent but not mutually independent.

```python
# Verify the three-coin example
omega = ['HH', 'HT', 'TH', 'TT']
A = {'HH', 'HT'}  # first H
B = {'HH', 'TH'}  # second H
C = {'HH', 'TT'}  # both same

P = lambda E: len(E) / 4
print(f"P(AB) = {P(A & B)} vs P(A)P(B) = {P(A)*P(B)}")
print(f"P(AC) = {P(A & C)} vs P(A)P(C) = {P(A)*P(C)}")
print(f"P(BC) = {P(B & C)} vs P(B)P(C) = {P(B)*P(C)}")
print(f"P(ABC) = {P(A & B & C)} vs P(A)P(B)P(C) = {P(A)*P(B)*P(C)}")
```
