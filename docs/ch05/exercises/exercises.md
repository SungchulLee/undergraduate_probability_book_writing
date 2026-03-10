# Chapter 5 Exercises

!!! warning "Exercise page"
    This page collects practice problems for Chapter 5 and does not follow the five-section structure used by concept pages.

Exercises on joint distributions, marginals, independence, and the multinomial distribution.

## Section 5.1 — Joint PMF

**Exercise 5.1.** Two fair dice are rolled. Let $X$ be the value on the first die and $Y$ the sum of the two dice. Write down the joint PMF of $(X, Y)$ in table form.

**Exercise 5.2.** Three fair coins are flipped. Let $X$ denote the number of heads in the first two flips and $Y$ the total number of heads. Construct the joint PMF table and verify the entries sum to 1.

**Exercise 5.3.** The joint PMF of $(X, Y)$ is given by $P(X = i, Y = j) = c(i + j)$ for $i \in \{1, 2\}$, $j \in \{1, 2, 3\}$. Find the constant $c$ and the marginal PMFs of $X$ and $Y$.

## Section 5.2 — Joint PDF and CDF

**Exercise 5.4.** Let $f(x, y) = cxy$ for $0 \le x \le 1$, $0 \le y \le 2$. Find $c$, the marginal PDFs, and $P(X + Y \le 1)$.

**Exercise 5.5.** Given the joint CDF $F(x, y) = (1 - e^{-x})(1 - e^{-2y})$ for $x, y \ge 0$, find the joint PDF and compute $P(X > 1, Y > 1)$.

## Section 5.3 — Independence

**Exercise 5.6.** Given the joint PMF table:

| | $x=0$ | $x=1$ |
|:---|:---:|:---:|
| $y=0$ | $0.12$ | $0.28$ |
| $y=1$ | $0.18$ | $0.42$ |

Determine whether $X$ and $Y$ are independent.

**Exercise 5.7.** Suppose $X$ and $Y$ are independent with $X \sim \text{Bin}(3, 0.5)$ and $Y \sim \text{Geo}(0.5)$. Compute $P(X = 2, Y = 1)$.

**Exercise 5.8.** A bin contains 3 red balls and 1 blue ball. Two balls are drawn without replacement. Let $X_1$ and $X_2$ be indicator variables for the first and second ball being blue. Are $X_1$ and $X_2$ independent? Justify by checking the factorization condition.

**Exercise 5.9.** Give an example of three random variables that are pairwise independent but not mutually independent.

## Section 5.4 — Multinomial

**Exercise 5.10.** A fair die is rolled 10 times. What is the probability that each of the six faces appears at least once?

**Exercise 5.11.** If $(X_1, X_2, X_3) \sim \text{Mult}(20, (0.5, 0.3, 0.2))$, compute $P(X_1 = 10, X_2 = 6, X_3 = 4)$ and verify that $X_1 \sim \text{Bin}(20, 0.5)$.
