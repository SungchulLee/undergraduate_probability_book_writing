# Partitions and Total Probability


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

## Total Probability Law — Divide and Conquer

The **law of total probability** provides a systematic way to compute $P(A)$ by breaking the problem into simpler conditional pieces.

### Setup

Suppose $\Omega$ can be divided into $n$ disjoint events $B_1, B_2, \ldots, B_n$ such that

$$
\Omega = \bigcup_{k=1}^{n} B_k \quad \text{(disjointly)}
$$

This is called a **partition** of the sample space. Equivalently, event $A$ can be divided into $n$ disjoint pieces:

$$
A = \bigcup_{k=1}^{n} (A \cap B_k) \quad \text{(disjointly)}
$$

### The Algorithm

**Step 1 (Divide):** Divide $A$ into $n$ disjoint events $AB_1, AB_2, \ldots, AB_n$.

**Step 2 (Conquer):** Compute each $P(AB_k)$ using the chain rule: $P(AB_k) = P(B_k)\,P(A \mid B_k)$.

### Statement

$$
P(A) = \sum_{k=1}^{n} P(AB_k) = \sum_{k=1}^{n} P(B_k)\,P(A \mid B_k)
$$

The law of total probability decomposes a potentially complicated probability into a weighted sum of conditional probabilities, where the weights are the prior probabilities $P(B_k)$.

## Bayes' Rule Combined with Total Probability

When the partition $\Omega = \bigcup_{k=1}^{n} B_k$ is used, Bayes' rule becomes:

$$
P(B_1 \mid A) \;\stackrel{\text{Bayes}}{=}\; \frac{P(A \mid B_1)\,P(B_1)}{P(A)} \;\stackrel{\text{TPL}}{=}\; \frac{P(B_1)\,P(A \mid B_1)}{\displaystyle\sum_{k=1}^{n} P(B_k)\,P(A \mid B_k)}
$$

This combined formula is one of the most widely used results in probability and statistics.

## Example — Monty Hall Problem

**Problem:** You are on a game show with three doors. Behind one door is a car; behind the others are goats. You pick door \#1, and the host (who knows what's behind the doors) opens door \#3, revealing a goat. He asks: "Do you want to switch to door \#2?" Is it to your advantage to switch?

### Analysis Using Total Probability (Change Strategy)

Define:

| Event | Description |
|-------|-------------|
| $C$ | Car door is chosen in the first round |
| $G$ | Goat door is chosen in the first round |
| $W$ | Win the prize (under the **change** strategy) |

Under the **change strategy**, you always switch after the host reveals a goat.

**Step 1 (Divide):** Using the first-round choice, divide $W$ into disjoint events:

$$
W = (W \cap C) \cup (W \cap G) \quad \text{(disjointly)}
$$

**Step 2 (Conquer):** Compute each piece using the chain rule:

$$
P(WC) = P(C)\,P(W \mid C) = \frac{1}{3} \times 0 = 0
$$

If you initially chose the car door and then switch, you lose.

$$
P(WG) = P(G)\,P(W \mid G) = \frac{2}{3} \times 1 = \frac{2}{3}
$$

If you initially chose a goat door and then switch, the host reveals the other goat, so you must switch to the car.

**Conclusion:**

$$
P(W) = P(WC) + P(WG) = 0 + \frac{2}{3} = \frac{2}{3}
$$

| Strategy | Winning Probability |
|----------|-------------------|
| No change (stay) | $1/3$ |
| Change (switch) | $2/3$ |

**Switching doubles your chance of winning.**
