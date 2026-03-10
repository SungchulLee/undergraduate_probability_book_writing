# Chapter 3 Exercises

!!! warning "Exercise page"
    This page collects practice problems for Chapter 3 and does not follow the five-section structure used by concept pages.

Exercises covering conditional probability, Bayes' theorem, independence, gambler's ruin, and Simpson's paradox.

## Section 3.1 — Conditional Probability and Chain Rule

**Exercise 3.1.** A box contains 5 red and 3 blue balls. Two balls are drawn without replacement. What is the probability that the second ball is red given that the first ball is red?

**Exercise 3.2.** Three cards are drawn sequentially without replacement from a standard 52-card deck. What is the probability that all three are hearts? Use the chain rule.

**Exercise 3.3.** We choose two cards from an ordinary 52-card deck. Let $A$ = "at least one ace is chosen," $A_1$ = "the spade ace is chosen," and $B$ = "both cards are aces." Verify that $P(B \mid A_1) > P(B \mid A)$ and explain intuitively why this is the case.

**Exercise 3.4.** In a class of 30 students, what is the probability that at least two share the same birthday? Compute both the exact value and the exponential approximation.

**Exercise 3.5.** Generalize the birthday problem: in a class of $n$ students where each birthday is equally likely to fall on any of $d$ days, find the minimum $n$ such that the probability of at least one match exceeds 50% when $d = 365$, $d = 100$, and $d = 1000$.

## Section 3.2 — Total Probability and Tree Diagrams

**Exercise 3.6.** An urn contains 3 red and 7 blue balls. A ball is drawn, its color noted, and then it is returned to the urn along with 2 additional balls of the same color. A second ball is then drawn. What is the probability that the second ball is red?

**Exercise 3.7.** A factory has three machines, $M_1$, $M_2$, $M_3$, producing 30%, 45%, and 25% of the total output, respectively. The defect rates are 2%, 3%, and 2% for $M_1$, $M_2$, $M_3$. If a randomly selected item is defective, what is the probability it was produced by $M_2$?

**Exercise 3.8.** In the Monty Hall problem, verify by simulation that the switching strategy wins approximately 2/3 of the time over 10,000 trials. Write a Python simulation.

**Exercise 3.9.** Draw a complete tree diagram for the false positive medical testing example. Label all branches with their probabilities and all leaves with their joint probabilities. Verify that the leaf probabilities sum to 1.

## Section 3.3 — Bayes' Theorem

**Exercise 3.10.** A disease affects 1 in 10,000 people. A test has 99% sensitivity and 99% specificity. Find $P(\text{Disease} \mid \text{Positive test})$. How does this change if the prevalence increases to 1 in 100?

**Exercise 3.11.** You are dealt two cards from a standard deck. Given that at least one card is an ace, what is the probability that both cards are aces? Compare this to the probability given that one of the cards is specifically the ace of spades.

**Exercise 3.12.** A student takes a multiple-choice exam with 4 options per question. The student either knows the answer (with probability $p$) or guesses randomly. If the student answered correctly, what is the probability they actually knew the answer? Express in terms of $p$.

## Section 3.4 — Independence

**Exercise 3.13.** Let $A$ and $B$ be independent events with $P(A) = 0.3$ and $P(B) = 0.4$. Compute $P(A \cup B)$, $P(A^c \cap B)$, and $P(A^c \cup B^c)$.

**Exercise 3.14.** A fair die is rolled. Let $A$ = "the number is even," $B$ = "the number is less than 4," and $C$ = "the number is 1 or 2." Determine which pairs are independent. Are $A$, $B$, $C$ mutually independent?

**Exercise 3.15.** Prove that if $A$ and $B$ are independent, then $A$ and $B^c$ are also independent.

**Exercise 3.16.** Give an example of three events $A$, $B$, $C$ that are pairwise independent but not mutually independent. Verify all conditions explicitly.

**Exercise 3.17.** Construct an example where $A$ and $B$ are conditionally independent given $C$, but not (unconditionally) independent. Verify the calculations.

## Section 3.5 — Gambler's Ruin

**Exercise 3.18.** A gambler starts with \$50 and bets \$1 on each round of a game with win probability $p = 0.49$. The gambler's goal is \$100. Compute the exact ruin probability using the formula

$$
Q(i) = \frac{(q/p)^N - (q/p)^i}{(q/p)^N - 1}
$$

with $i = 50$ and $N = 100$.

**Exercise 3.19.** For the fair game case ($p = q = 1/2$), show that the ruin probability starting with initial capital $i$ and goal $N$ is $Q(i) = (N - i)/N$. Derive this from the recurrence relation $Q(i) = \frac{1}{2}Q(i+1) + \frac{1}{2}Q(i-1)$ with boundary conditions $Q(0) = 1$ and $Q(N) = 0$.

**Exercise 3.20.** Write a Python simulation of the gambler's ruin problem. For $p = 0.49$, initial capital $i = 100$, and goal $N = 200$, run 1,000 simulations and compare the estimated ruin probability with the theoretical value.

**Exercise 3.21.** In the gambler's ruin problem with $p < 1/2$, explain why the ruin probability approaches 1 exponentially fast as the initial capital $i$ decreases from $N$. What is the rate of exponential convergence?

## Section 3.6 — Simpson's Paradox

**Exercise 3.22.** Construct a numerical example of Simpson's paradox using two treatments ($A$ and $B$) and two patient groups (mild and severe). Treatment $A$ should have a higher success rate in both groups, but Treatment $B$ should have a higher overall success rate.

**Exercise 3.23.** In the Berkeley admissions example, explain using conditional probability notation why the aggregate admission rate for women can be lower than for men even when each department's rate is higher for women.

## Section 3.7 — Comprehensive

**Exercise 3.24.** Prove the following identity using the chain rule:

$$
P(A_1 A_2 \cdots A_n) = P(A_1)\,P(A_2 \mid A_1)\,P(A_3 \mid A_1 A_2) \cdots P(A_n \mid A_1 A_2 \cdots A_{n-1})
$$

**Exercise 3.25.** Let $A$ and $B$ be events with $P(A) = 0.6$, $P(B) = 0.4$, and $P(A \mid B) = 0.5$. Find $P(B \mid A)$, $P(A \cup B)$, and determine whether $A$ and $B$ are independent.
