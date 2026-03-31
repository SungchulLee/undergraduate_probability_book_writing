<<<<<<< Updated upstream
# Exercises: Convolutions and Distributions of Sums

## Discrete Convolution

**Exercise 16.1.** Let $X$ and $Y$ be independent, each uniform on $\{0, 1, 2\}$. Compute the PMF of $X + Y$ using the convolution formula and verify that the probabilities sum to 1.

**Exercise 16.2.** Let $X \sim \text{Bin}(3, 1/2)$ and $Y \sim \text{Bin}(2, 1/2)$ be independent. Use the convolution formula to compute $P(X + Y = 3)$.

*Hint: Sum over all valid values of $X$.*

**Exercise 16.3.** If $X \sim \text{Po}(2)$ and $Y \sim \text{Po}(3)$ are independent, find $P(X + Y = 4)$ in two ways: (a) by direct convolution of the Poisson PMFs, and (b) by recognizing $X + Y \sim \text{Po}(5)$.

## Continuous Convolution

**Exercise 16.4.** Let $X$ and $Y$ be independent $\text{Exp}(1)$ random variables. Compute the PDF of $X + Y$ using the convolution integral and verify that the result matches $\Gamma(2, 1)$.

**Exercise 16.5.** Let $X \sim U(0, 1)$ and $Y \sim U(0, 2)$ be independent. Compute $f_{X+Y}(a)$ for all $a \geq 0$.

*Hint: Determine the integration limits by intersecting the supports $0 \leq b \leq 1$ and $0 \leq a - b \leq 2$. Consider the cases $0 \leq a \leq 1$, $1 < a \leq 2$, and $2 < a \leq 3$ separately.*

## Identifying Distributions via Convolution

**Exercise 16.6.** A random variable $W$ has MGF $M_W(t) = (1 - 2t)^{-5}$ for $t < 1/2$. Identify the distribution of $W$. If $W = V_1 + V_2$ where $V_1 \sim \chi^2_3$ and $V_2 \sim \chi^2_7$, explain why this contradicts the MGF.

**Exercise 16.7.** Let $X_1, \ldots, X_n$ be iid $\text{Exp}(\lambda)$. Use the MGF of $S_n = \sum_{i=1}^n X_i$ to show that $S_n \sim \Gamma(n, \lambda)$. Compute $E[S_n]$ and $\text{Var}(S_n)$.

## Sum of Normals

**Exercise 16.8.** Let $X_1, \ldots, X_4$ be independent with $X_i \sim N(i, i^2)$. Find the exact distribution of $S = X_1 + X_2 + X_3 + X_4$.

**Exercise 16.9.** Suppose $X \sim N(3, 4)$ and $Y \sim N(-1, 9)$ are independent. Find $P(X + Y > 5)$.

*Hint: First identify the distribution of $X + Y$, then standardize.*

## Conceptual

**Exercise 16.10.** Give an example showing that convolution does **not** give the correct distribution of $X + Y$ when $X$ and $Y$ are dependent. Specifically, let $X \sim U(0, 1)$ and $Y = X$. Find the distribution of $X + Y$ and show it differs from the triangular distribution obtained by convolving $U(0,1)$ with itself.
=======
# Exercises
>>>>>>> Stashed changes
