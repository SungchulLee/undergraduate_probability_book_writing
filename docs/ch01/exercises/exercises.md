# Chapter 1 Exercises — Counting


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

## Exercise 1: Multiplication Rule

A license plate consists of 3 letters followed by 4 digits. How many different license plates are possible if:

**(a)** Repetition is allowed?

**(b)** No repetition of letters or digits is allowed?

??? note "Solution"
    **(a)** $26^3 \times 10^4 = 175{,}760{,}000$

    **(b)** $26 \times 25 \times 24 \times 10 \times 9 \times 8 \times 7 = 78{,}624{,}000$

---

## Exercise 2: Poker Hands

A standard deck has 52 cards (13 ranks, 4 suits). A poker hand consists of 5 cards.

**(a)** How many possible poker hands are there?

**(b)** How many hands contain exactly one pair (two cards of one rank, and three cards of three other distinct ranks)?

**(c)** How many hands are a full house (three of one rank, two of another)?

??? note "Solution"
    **(a)** $\binom{52}{5} = 2{,}598{,}960$

    **(b)** Choose the pair rank: $\binom{13}{1}$. Choose 2 suits for the pair: $\binom{4}{2}$. Choose 3 other ranks: $\binom{12}{3}$. Choose 1 suit each: $4^3$.
    Total: $13 \times 6 \times 220 \times 64 = 1{,}098{,}240$

    **(c)** Choose the triple rank: $13$. Choose 3 suits: $\binom{4}{3} = 4$. Choose the pair rank: $12$. Choose 2 suits: $\binom{4}{2} = 6$.
    Total: $13 \times 4 \times 12 \times 6 = 3{,}744$

---

## Exercise 3: Permutations with Repetition

How many distinct arrangements can be made from the letters of the word MISSISSIPPI?

??? note "Solution"
    MISSISSIPPI has 11 letters: M(1), I(4), S(4), P(2).

    $$\frac{11!}{1! \cdot 4! \cdot 4! \cdot 2!} = \frac{39{,}916{,}800}{1 \cdot 24 \cdot 24 \cdot 2} = 34{,}650$$

---

## Exercise 4: Vandermonde's Identity

Verify Vandermonde's identity for $m = 4$, $n = 6$, $k = 5$:

$$\binom{10}{5} = \sum_{\ell=0}^{4} \binom{4}{\ell}\binom{6}{5-\ell}$$

??? note "Solution"

    $$\binom{4}{0}\binom{6}{5} + \binom{4}{1}\binom{6}{4} + \binom{4}{2}\binom{6}{3} + \binom{4}{3}\binom{6}{2} + \binom{4}{4}\binom{6}{1}$$

    $$= 1 \cdot 6 + 4 \cdot 15 + 6 \cdot 20 + 4 \cdot 15 + 1 \cdot 6 = 6 + 60 + 120 + 60 + 6 = 252$$

    And $\binom{10}{5} = 252$. ✓

---

## Exercise 5: Inclusion-Exclusion

Among 100 students: 60 study mathematics, 45 study physics, 30 study chemistry, 20 study both math and physics, 15 study both math and chemistry, 10 study both physics and chemistry, and 5 study all three subjects.

**(a)** How many study at least one of the three subjects?

**(b)** How many study none of the three subjects?

??? note "Solution"
    **(a)** By inclusion-exclusion:
    $|M \cup P \cup C| = 60 + 45 + 30 - 20 - 15 - 10 + 5 = 95$

    **(b)** $100 - 95 = 5$ students study none.

---

## Exercise 6: Derangements

**(a)** Compute $D_5$, the number of derangements of $\{1, 2, 3, 4, 5\}$.

**(b)** What is the probability that a random permutation of $\{1, 2, 3, 4, 5\}$ is a derangement?

??? note "Solution"
    **(a)** $D_5 = 5!\left(1 - 1 + \frac{1}{2} - \frac{1}{6} + \frac{1}{24} - \frac{1}{120}\right) = 120 \times \frac{11}{30} = 44$

    **(b)** $P = \frac{D_5}{5!} = \frac{44}{120} = \frac{11}{30} \approx 0.3667$

---

## Exercise 7: Double Counting (Football / Soccer Ball)

A standard soccer ball (truncated icosahedron) has 12 pentagons and 20 hexagons.

**(a)** Each pentagon has 5 edges and each hexagon has 6 edges. Using double counting, find the total number of edges.

**(b)** Find the number of vertices using the fact that exactly 3 faces meet at each vertex.

??? note "Solution"
    **(a)** Each edge borders exactly 2 faces. Total face-edges: $12 \times 5 + 20 \times 6 = 60 + 120 = 180$. By double counting: $E = 180 / 2 = 90$ edges.

    **(b)** Each vertex is shared by exactly 3 faces. Total face-vertices: $12 \times 5 + 20 \times 6 = 180$. Each vertex counted 3 times: $V = 180 / 3 = 60$ vertices.

    Verification by Euler's formula: $V - E + F = 60 - 90 + 32 = 2$. ✓

---

## Exercise 8: Stars and Bars

How many ways can you distribute 10 identical cookies among 4 children if each child must receive at least one cookie?

??? note "Solution"
    Give each child 1 cookie first. Remaining: $10 - 4 = 6$ cookies to distribute among 4 children (0 or more each).

    $$\binom{6 + 4 - 1}{4 - 1} = \binom{9}{3} = 84$$

---

## Python: Verification Script

```python
from math import comb, factorial

# Exercise 1
print("Exercise 1:")
print(f"  (a) {26**3 * 10**4}")
print(f"  (b) {26*25*24 * 10*9*8*7}")

# Exercise 2
print("\nExercise 2:")
print(f"  (a) C(52,5) = {comb(52, 5)}")
print(f"  (b) One pair: {13 * comb(4,2) * comb(12,3) * 4**3}")
print(f"  (c) Full house: {13 * comb(4,3) * 12 * comb(4,2)}")

# Exercise 3
print(f"\nExercise 3: MISSISSIPPI = {factorial(11)//(1*factorial(4)*factorial(4)*factorial(2))}")

# Exercise 5
print(f"\nExercise 5: |M∪P∪C| = {60+45+30-20-15-10+5}")

# Exercise 6
D5 = sum((-1)**k * factorial(5) // factorial(k) for k in range(6))
print(f"\nExercise 6: D_5 = {D5}, P = {D5}/{factorial(5)} = {D5/factorial(5):.4f}")

# Exercise 8
print(f"\nExercise 8: C(9,3) = {comb(9, 3)}")
```
