# Classical Probability

## Equally Likely Probability Measure

When all outcomes in a finite sample space are **equally likely**, the probability measure takes a particularly simple form:

$$
P(\omega) = \frac{1}{|\Omega|}
$$

For any event $A \subseteq \Omega$:

$$
P(A) = \frac{|A|}{|\Omega|}
$$

This is the **classical** or **equally likely** probability model. Computing probabilities reduces to counting: count the favorable outcomes $|A|$ and divide by the total number of outcomes $|\Omega|$.

!!! note "When Does This Apply?"
    The equally likely model is appropriate when:

    - The sample space is finite
    - There is a symmetry argument justifying equal weights (e.g., fair coins, fair dice, well-shuffled decks)

    It is **not** appropriate when outcomes have different likelihoods (e.g., loaded dice, biased coins).

## Example: Flip a Fair Coin Three Times

The sample space has $|\Omega| = 2^3 = 8$ equally likely outcomes:

$$
\Omega = \{HHH, HHT, HTH, HTT, THH, THT, TTH, TTT\}
$$

Each outcome has probability:

$$
P(\omega) = \frac{1}{8}
$$

!!! example "Computing Event Probabilities"
    - $P(\text{all heads}) = P(\{HHH\}) = \frac{1}{8}$
    - $P(\text{exactly 2 heads}) = P(\{HHT, HTH, THH\}) = \frac{3}{8}$
    - $P(\text{at least 1 head}) = 1 - P(\{TTT\}) = 1 - \frac{1}{8} = \frac{7}{8}$

## Example: Probability of a Full House

A **full house** in poker is a hand with three cards of one rank and two cards of another rank.

**Sample space:** The number of ways to choose 5 cards from a standard 52-card deck:

$$
|\Omega| = \binom{52}{5}
$$

**Counting favorable outcomes:**

| Step | Count |
|------|-------|
| Choose the rank for the three-of-a-kind | 13 choices |
| Choose 3 suits from 4 for that rank | $\binom{4}{3}$ choices |
| Choose the rank for the pair | 12 remaining choices |
| Choose 2 suits from 4 for the pair | $\binom{4}{2}$ choices |

Therefore:

$$
|A| = 13 \cdot \binom{4}{3} \cdot 12 \cdot \binom{4}{2}
$$

The probability of a full house:

$$
P(\text{full house}) = \frac{|A|}{|\Omega|} = \frac{13 \cdot \binom{4}{3} \cdot 12 \cdot \binom{4}{2}}{\binom{52}{5}}
$$

## Python Example

```python
from math import comb

# Coin flipping example
omega_coins = ['HHH', 'HHT', 'HTH', 'HTT', 'THH', 'THT', 'TTH', 'TTT']

# Count events
exactly_2H = [w for w in omega_coins if w.count('H') == 2]
at_least_1H = [w for w in omega_coins if w.count('H') >= 1]

print("=== Fair Coin (3 flips) ===")
print(f"P(all heads) = 1/{len(omega_coins)} = {1/len(omega_coins):.4f}")
print(f"P(exactly 2 heads) = {len(exactly_2H)}/{len(omega_coins)} = {len(exactly_2H)/len(omega_coins):.4f}")
print(f"P(at least 1 head) = {len(at_least_1H)}/{len(omega_coins)} = {len(at_least_1H)/len(omega_coins):.4f}")

# Full house probability
print("\n=== Full House ===")
omega_size = comb(52, 5)
full_house = 13 * comb(4, 3) * 12 * comb(4, 2)

print(f"|Ω| = C(52,5) = {omega_size}")
print(f"|A| = 13 × C(4,3) × 12 × C(4,2) = 13 × {comb(4,3)} × 12 × {comb(4,2)} = {full_house}")
print(f"P(full house) = {full_house}/{omega_size} = {full_house/omega_size:.6f}")
print(f"P(full house) ≈ 1 in {omega_size/full_house:.0f}")
```

**Output:**
```
=== Fair Coin (3 flips) ===
P(all heads) = 1/8 = 0.1250
P(exactly 2 heads) = 3/8 = 0.3750
P(at least 1 head) = 7/8 = 0.8750

=== Full House ===
|Ω| = C(52,5) = 2598960
|A| = 13 × C(4,3) × 12 × C(4,2) = 13 × 4 × 12 × 6 = 3744
P(full house) = 3744/2598960 = 0.001441
P(full house) ≈ 1 in 694
```
