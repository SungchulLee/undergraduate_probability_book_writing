# Exercises

## Section 2.1: Sample Spaces and Events

**Exercise 2.1.** An experiment consists of rolling two distinguishable fair dice. 

(a) Write out the sample space $\Omega$ and determine $|\Omega|$.

(b) Let $A$ be the event that the sum is 7. Find $|A|$ and $P(A)$.

(c) Let $B$ be the event that both dice show the same number. Find $P(B)$.

(d) Are $A$ and $B$ mutually exclusive? Justify your answer.

---

**Exercise 2.2.** Three cards are drawn from a standard 52-card deck **without replacement**. Find the probability that:

(a) All three are hearts.

(b) All three are the same suit.

(c) No two cards share the same suit.

---

**Exercise 2.3.** Verify De Morgan's Laws for the events $A = \{1, 2, 3, 4\}$ and $B = \{3, 4, 5, 6\}$ with $\Omega = \{1, 2, 3, 4, 5, 6, 7, 8\}$.

---

## Section 2.2: Axioms and Properties

**Exercise 2.4.** Let $P(A) = 0.6$, $P(B) = 0.4$, and $P(A \cap B) = 0.2$. Find:

(a) $P(A \cup B)$

(b) $P(A^c)$

(c) $P(A \cap B^c)$

(d) $P(A^c \cap B^c)$

---

**Exercise 2.5.** Prove that for any events $A$ and $B$:

$$
P(A \cup B) = P(A) + P(B) - P(A \cap B)
$$

using only the Kolmogorov axioms and the fact that $P(A) = P(A \cap B) + P(A \cap B^c)$.

---

**Exercise 2.6.** Suppose $P(A) = 0.5$, $P(B) = 0.4$, and $P(C) = 0.3$. If $A$, $B$, and $C$ are pairwise disjoint, find $P(A \cup B \cup C)$ and $P((A \cup B \cup C)^c)$.

---

**Exercise 2.7 (Boole's Inequality).** Let $A_1, A_2, \ldots, A_n$ be arbitrary events. Prove by induction that:

$$
P\left(\bigcup_{i=1}^{n} A_i\right) \leq \sum_{i=1}^{n} P(A_i)
$$

---

## Section 2.3: Equally Likely Outcomes

**Exercise 2.8 (Poker Hands).** From a standard 52-card deck, 5 cards are dealt. Compute the probability of:

(a) Four of a kind

(b) A flush (all 5 cards of the same suit, but not a straight flush)

(c) Two pair (but not a full house)

---

**Exercise 2.9 (Newton–Pepys Variant).** Compute:

(a) $P(\text{at least 2 sixes in 12 dice rolls})$ using the complement and verify the formula from the Newton–Pepys problem.

(b) Generalize: for $6k$ dice, find a formula for $P(\text{at least } k \text{ sixes})$ and compute it for $k = 1, 2, 3, 4, 5$. Do you see a trend?

---

**Exercise 2.10 (Birthday Problem Variant).** 

(a) In a class of 30 students, what is the probability that at least two students share a birthday? (Assume 365 equally likely days.)

(b) How large must the class be for the probability to exceed 0.99?

(c) Suppose there are only 100 possible birthdays. How many people are needed for a 50% chance of a match?

---

**Exercise 2.11 (Bertrand's Ballot Theorem).** In an election, candidate A receives 8 votes and candidate B receives 3 votes.

(a) Using Bertrand's ballot theorem, find the probability that A is strictly ahead throughout the entire count.

(b) Verify your answer by computing $\binom{11}{3}$ and the number of "good" count sequences.

---

**Exercise 2.12 (Matching Problem Preview).** Suppose $n$ people each place their hat into a common bin, and each person randomly selects a hat. Find the probability that at least one person gets their own hat back, using the inclusion-exclusion principle.

*Hint:* Let $A_i$ be the event that person $i$ gets their own hat. Compute $P(A_i)$, $P(A_i \cap A_j)$, etc., then apply inclusion-exclusion.

---

## Solutions

??? solution "Solution to Exercise 2.1"
    (a) $\Omega = \{(i,j) : 1 \leq i, j \leq 6\}$, so $|\Omega| = 36$.

    (b) $A = \{(1,6),(2,5),(3,4),(4,3),(5,2),(6,1)\}$, so $|A| = 6$ and $P(A) = 6/36 = 1/6$.

    (c) $B = \{(1,1),(2,2),(3,3),(4,4),(5,5),(6,6)\}$, so $P(B) = 6/36 = 1/6$.

    (d) Yes, $A \cap B = \emptyset$ since no pair $(i,i)$ sums to 7 (that would require $2i = 7$).

??? solution "Solution to Exercise 2.4"
    (a) $P(A \cup B) = 0.6 + 0.4 - 0.2 = 0.8$

    (b) $P(A^c) = 1 - 0.6 = 0.4$

    (c) $P(A \cap B^c) = P(A) - P(A \cap B) = 0.6 - 0.2 = 0.4$

    (d) $P(A^c \cap B^c) = P((A \cup B)^c) = 1 - P(A \cup B) = 1 - 0.8 = 0.2$

??? solution "Solution to Exercise 2.8 (Poker Hands)"
    $|\Omega| = \binom{52}{5} = 2{,}598{,}960$

    (a) **Four of a kind:** Choose rank (13), choose 4 suits $\binom{4}{4}=1$, choose kicker from remaining 48 cards: $|A| = 13 \times 1 \times 48 = 624$. $P = 624/2{,}598{,}960 \approx 0.000240$.

    (b) **Flush (not straight flush):** Choose suit (4), choose 5 from 13 of that suit $\binom{13}{5}$, subtract 10 straight flushes per suit: $|A| = 4 \times (\binom{13}{5} - 10) = 4 \times 1277 = 5108$. $P = 5108/2{,}598{,}960 \approx 0.001965$.

    (c) **Two pair:** Choose 2 ranks from 13 for pairs $\binom{13}{2}$, choose 2 suits each $\binom{4}{2}^2$, choose kicker rank from remaining 11, choose 1 suit $\binom{4}{1}$: $|A| = \binom{13}{2} \times \binom{4}{2}^2 \times 11 \times 4 = 78 \times 36 \times 44 = 123{,}552$. $P = 123{,}552/2{,}598{,}960 \approx 0.04754$.

??? solution "Solution to Exercise 2.11"
    (a) $P = \frac{a-b}{a+b} = \frac{8-3}{8+3} = \frac{5}{11} \approx 0.4545$

    (b) Total paths $= \binom{11}{3} = 165$. Bad paths $= 2\binom{10}{2} = 2 \times 45 = 90$. Good paths $= 165 - 90 = 75$. $P = 75/165 = 5/11$. ✓
