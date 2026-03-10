# Classical Probability

When all outcomes in a finite sample space are equally likely, computing probabilities reduces to counting. This is the classical model that motivated the entire field.

## Definition

If $\Omega$ is finite and all outcomes are equally likely, then for any event $A \subseteq \Omega$:

$$
P(A) = \frac{|A|}{|\Omega|}
$$

This assigns $P(\{\omega\}) = 1/|\Omega|$ to each outcome $\omega$.

!!! note "When does this apply?"
    The equally likely model requires a symmetry argument: fair coins, fair dice, well-shuffled decks, random selections. It does **not** apply when outcomes have different likelihoods (loaded dice, biased coins).

## Explanation

Under the classical model, every probability question becomes a counting question:

1. Define the sample space $\Omega$ and compute $|\Omega|$
2. Define the event $A$ and count $|A|$
3. Compute $P(A) = |A|/|\Omega|$

The entire toolkit of Chapter 1 (multiplication rule, combinations, permutations, inclusion-exclusion, complement counting) now becomes directly applicable to probability.

## Examples

**Example 1 (Three coin flips).** $\Omega = \{HHH, HHT, HTH, HTT, THH, THT, TTH, TTT\}$, $|\Omega| = 8$.

- $P(\text{all heads}) = 1/8$
- $P(\text{exactly 2 heads}) = |\{HHT, HTH, THH\}|/8 = 3/8$
- $P(\text{at least 1 head}) = 1 - P(\{TTT\}) = 7/8$

---

**Example 2 (Full house in poker).** A full house has three of one rank and two of another. Sample space: $|\Omega| = \binom{52}{5}$.

| Step | Count |
|:---|:---|
| Choose rank for triple | 13 |
| Choose 3 suits from 4 | $\binom{4}{3} = 4$ |
| Choose rank for pair | 12 |
| Choose 2 suits from 4 | $\binom{4}{2} = 6$ |

$$
P(\text{full house}) = \frac{13 \cdot 4 \cdot 12 \cdot 6}{\binom{52}{5}} = \frac{3744}{2{,}598{,}960} \approx 0.00144
$$

About 1 in 694 hands.

```python
from math import comb

# Example 1: three coins
omega = ['HHH','HHT','HTH','HTT','THH','THT','TTH','TTT']
print(f"P(exactly 2 heads) = {sum(w.count('H')==2 for w in omega)}/{len(omega)}")

# Example 2: full house
full_house = 13 * comb(4, 3) * 12 * comb(4, 2)
total = comb(52, 5)
print(f"P(full house) = {full_house}/{total} = {full_house/total:.6f}")
print(f"About 1 in {total/full_house:.0f}")
```
