# Chapter 5 Exercises

## Joint PMF Problems

**Exercise 5.1.** Two fair dice are rolled. Let $X$ be the value on the first die and $Y$ the sum of the two dice. Write down the joint PMF of $(X, Y)$ in table form.

**Exercise 5.2.** Three fair coins are flipped. Let $X$ denote the number of heads in the first two flips and $Y$ the total number of heads. Construct the joint PMF table and verify the entries sum to 1.

**Exercise 5.3.** The joint PMF of $(X, Y)$ is given by $P(X = i, Y = j) = c(i + j)$ for $i \in \{1, 2\}$, $j \in \{1, 2, 3\}$. Find the constant $c$ and compute $P(X + Y \le 3)$.

## Joint PDF Problems

**Exercise 5.4.** Let $(X, Y)$ have joint PDF $f(x, y) = c \, x \, y$ for $0 \le x \le 1$, $0 \le y \le 2$, and $f(x, y) = 0$ otherwise. Find the constant $c$ and compute $P(X \le 1/2, \, Y \le 1)$.

**Exercise 5.5.** The joint PDF of $(X, Y)$ is $f(x, y) = 6(1 - y)$ for $0 \le x \le y \le 1$, and $0$ otherwise. Verify that $f$ integrates to 1 and compute $P(X \le 1/4)$.

## Joint CDF Problems

**Exercise 5.6.** Given the joint CDF $F(x, y) = (1 - e^{-x})(1 - e^{-2y})$ for $x \ge 0$, $y \ge 0$, find:

(a) $P(X > 1, \, Y > 1)$

(b) the joint PDF $f(x, y)$

## Independence Problems

**Exercise 5.7.** Given the joint PMF table:

| | $x=0$ | $x=1$ |
|---|---|---|
| $y=0$ | $0.12$ | $0.28$ |
| $y=1$ | $0.18$ | $0.42$ |

Determine whether $X$ and $Y$ are independent by checking the factorization condition at every cell.

**Exercise 5.8.** Suppose $X$ and $Y$ are independent with $X \sim \text{B}(3, 0.5)$ and $Y \sim \text{Geo}(0.5)$. Compute $P(X = 2, Y = 1)$.

**Exercise 5.9.** A bin contains 3 red balls and 1 blue ball. Two balls are drawn without replacement. Let $X_1$ and $X_2$ be indicator variables for the first and second ball being blue. Are $X_1$ and $X_2$ independent? Justify your answer by computing the joint PMF and checking the factorization condition.

**Exercise 5.10.** Let $(X, Y)$ have joint PDF $f(x, y) = 4xy$ for $0 \le x \le 1$, $0 \le y \le 1$, and $0$ otherwise. Show that $X$ and $Y$ are independent by verifying that the joint PDF factors into the product of the marginal PDFs.

**Exercise 5.11.** If $X$ and $Y$ are independent and each is uniformly distributed on $\{1, 2, 3, 4, 5, 6\}$, find the PMF of $Z = \min(X, Y)$.

## Multinomial Problems

**Exercise 5.12.** A fair six-sided die is rolled 12 times. Let $X_1$ be the number of ones and $X_6$ the number of sixes. Using the multinomial distribution, compute $P(X_1 = 2, X_6 = 3)$.

**Exercise 5.13.** In a multinomial distribution $\text{Mul}(n, \mathbf{p})$ with $K$ categories, show that each marginal $X_j$ follows a $\text{B}(n, p_j)$ distribution. Are $X_1$ and $X_2$ independent? Why or why not?

## Conceptual and Proof Problems

**Exercise 5.14.** Give an example of three random variables that are pairwise independent but not mutually independent. Verify both claims explicitly.

**Exercise 5.15.** Explain why conditional independence given $Y$ does not imply unconditional independence. Provide a concrete example with a joint PMF table.

**Exercise 5.16.** Prove that if $X$ and $Y$ are independent discrete random variables, then $g(X)$ and $h(Y)$ are also independent for any functions $g$ and $h$.
