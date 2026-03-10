# First Step Analysis


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

## Idea

**First step analysis** is a technique for solving problems about random processes by conditioning on the outcome of the first step. For the gambler's ruin, we decompose the ruin event $R$ according to whether the gambler wins or loses the first bet.

## Derivation of the Recurrence Relation

Let $W$ be the event that the gambler wins the first game. By the law of total probability:

$$
Q(i) = P(R \mid I = i)
$$

$$
= P(R \cap W \mid I = i) + P(R \cap W^c \mid I = i)
$$

$$
= P(W \mid I = i)\,P(R \mid I = i, W) + P(W^c \mid I = i)\,P(R \mid I = i, W^c)
$$

After winning the first bet, the gambler has $i + 1$ dollars and faces the same problem from that new starting point. After losing, the gambler has $i - 1$ dollars. Therefore:

$$
P(R \mid I = i, W) = Q(i + 1), \qquad P(R \mid I = i, W^c) = Q(i - 1)
$$

Substituting:

$$
Q(i) = p\,Q(i + 1) + q\,Q(i - 1)
$$

## The Complete Problem

**Recurrence relation:**

$$
Q(i) = p\,Q(i + 1) + q\,Q(i - 1), \quad i = 1, 2, \ldots, N - 1
$$

**Boundary conditions:**

$$
Q(0) = 1, \qquad Q(N) = 0
$$

This is a **second-order linear recurrence relation** with constant coefficients. It can be solved via the characteristic equation method (see subsequent sections) or numerically as a tridiagonal linear system.

## Characteristic Equation

To solve the recurrence, we guess a solution of the form $Q(i) = \lambda^i$. Substituting:

$$
p\lambda^{i+1} + q\lambda^{i-1} = \lambda^i
$$

Dividing by $\lambda^{i-1}$:

$$
p\lambda^2 - \lambda + q = 0
$$

This is the **characteristic equation**. Since $q = 1 - p$:

$$
p\lambda^2 - \lambda + (1 - p) = 0
$$

$$
p(\lambda + 1)(\lambda - 1) + 1 - \lambda = (\lambda - 1)[p(\lambda + 1) - 1] = 0
$$

The **characteristic roots** are:

$$
\lambda = 1 \qquad \text{and} \qquad \lambda = \frac{q}{p}
$$

## Linearity of Solutions

If $Q_1(i)$ and $Q_2(i)$ are both solutions to the recurrence, then any linear combination $Q(i) = \alpha\,Q_1(i) + \beta\,Q_2(i)$ is also a solution:

$$
p\,Q(i+1) + q\,Q(i-1) = \alpha\bigl[p\,Q_1(i+1) + q\,Q_1(i-1)\bigr] + \beta\bigl[p\,Q_2(i+1) + q\,Q_2(i-1)\bigr]
$$

$$
= \alpha\,Q_1(i) + \beta\,Q_2(i) = Q(i)
$$

This superposition principle allows us to construct the general solution from the two characteristic roots and then determine the constants $\alpha$ and $\beta$ using the boundary conditions.
