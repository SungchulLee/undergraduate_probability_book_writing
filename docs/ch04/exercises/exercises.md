# Chapter 4 Exercises

<<<<<<< Updated upstream
## Section 4.1 — Random Variables

**Exercise 4.1.** Explain in your own words why $P(X = a) = 0$ for every value $a$ when $X$ is a continuous random variable, even though $X$ must take some value.

**Exercise 4.2.** A random variable $X$ has a discrete CDF with jumps of size 0.1, 0.2, 0.3, 0.15, 0.25 at $x = 1, 3, 5, 7, 10$ respectively. Determine $P(X = 5)$, $P(X \ge 7)$, $P(3 < X \le 7)$, and $P(X < 5)$.

**Exercise 4.3.** Flip a fair coin four times. Let $X$ be the length of the longest run of consecutive heads. List all 16 outcomes, find $X(\omega)$ for each, and write down the PMF of $X$.
=======
## Conceptual Questions

**Exercise 4.1.** Explain in your own words why $P(X = a) = 0$ for every value $a$ when $X$ is a continuous random variable, even though $X$ must take some value.

**Exercise 4.2.** A random variable $X$ has the CDF shown below (step function with jumps at $x = 5, 10, 20, 25$). Determine $P(X = 5)$, $P(X \ge 20)$, and $P(10 < X \le 25)$ from the CDF.

## PMF Problems
>>>>>>> Stashed changes

## Section 4.2 — Probability Mass Function

**Exercise 4.4.** Let $X$ be the number of heads in 3 flips of a fair coin. Write down the PMF of $X$ and verify it sums to 1.

<<<<<<< Updated upstream
**Exercise 4.5.** A random variable $X$ has PMF $P(X = k) = c \cdot k$ for $k = 1, 2, 3, 4, 5$. Find the constant $c$ and compute $P(X \ge 3)$.

**Exercise 4.6.** A random variable $X$ has PMF $P(X = k) = c \cdot 2^{-k}$ for $k = 1, 2, 3, \ldots$ Find the constant $c$ and compute $P(X \le 3)$.

**Exercise 4.7.** Prove that if $p_X(x) \ge 0$ for all $x$ and $\sum_x p_X(x) = 1$, then $0 \le P(X \in A) \le 1$ for every set $A \subseteq \mathbb{R}$.

## Section 4.3 — Cumulative Distribution Function

**Exercise 4.8.** Given the PMF from Exercise 4.4, write the CDF $F(x)$ as a piecewise function and sketch it.

**Exercise 4.9.** The CDF of a random variable is

$$
F(x) = \begin{cases} 0 & x < 0 \\ x/2 & 0 \le x < 1 \\ 1/2 & 1 \le x < 2 \\ 1 & x \ge 2 \end{cases}
$$

Is $X$ discrete, continuous, or mixed? Find $P(X = 1)$, $P(X = 2)$, and $P(0.5 < X \le 2)$.

**Exercise 4.10.** Show that for any CDF $F$, the probability $P(a < X \le b) = F(b) - F(a)$ follows directly from the axioms of probability and the definition $F(x) = P(X \le x)$.

## Section 4.4 — Probability Density Function

**Exercise 4.11.** A continuous random variable has PDF $f(x) = 3x^2$ for $0 \le x \le 1$. Find the CDF, and compute $P(0.5 \le X \le 0.8)$.

**Exercise 4.12.** Determine the value of $c$ that makes $f(x) = c(1 - x^2)$ a valid PDF on $[-1, 1]$. Then compute $P(X > 0)$.

**Exercise 4.13.** A random variable has PDF $f(x) = \lambda e^{-\lambda x}$ for $x \ge 0$ where $\lambda > 0$. Verify that $\int_0^\infty f(x)\,dx = 1$ and find $P(X > 1/\lambda)$.

**Exercise 4.14.** Explain why the PDF $f(x) = 5$ for $0 \le x \le 1/5$ is a valid density even though $f(x) > 1$, and compute $P(0.1 \le X \le 0.15)$.

## Section 4.5 — Functions of a Random Variable

**Exercise 4.15.** If $X \sim \text{B}(0.3)$ (Bernoulli with $p = 0.3$), find the PMF of $Y = 5X + 2$.

**Exercise 4.16.** Let $X$ be a random variable taking values $\{-2, -1, 0, 1, 2\}$ each with probability $1/5$. Find the PMF of $Y = X^2$.

**Exercise 4.17.** Let $X \sim \text{Uniform}(0, 1)$ (continuous). Use the CDF method to find the PDF of $Y = X^2$.

**Exercise 4.18.** Let $X$ be a discrete random variable with PMF $P(X = k) = 1/4$ for $k = -1, 0, 1, 2$. Find the PMF of $Y = |X|$ and the PMF of $Z = \max(X, 0)$.

## Section 4.6 — Comprehensive

**Exercise 4.19.** Write a Python program that simulates rolling two fair dice and plots the PMF of their sum $S = X_1 + X_2$. Compare the simulated PMF with the exact PMF computed by enumeration.

**Exercise 4.20.** A continuous random variable $X$ has CDF

$$
F(x) = \begin{cases} 0 & x < 0 \\ 1 - e^{-2x} & x \ge 0 \end{cases}
$$

(a) Find the PDF $f(x)$.
(b) Compute $P(1 \le X \le 3)$.
(c) Find the value $m$ such that $P(X \le m) = 0.5$ (the median).

**Exercise 4.21.** Let $X$ have PMF $P(X = k) = (1-p)^{k-1} p$ for $k = 1, 2, 3, \ldots$ (Geometric). Show that the CDF is $F(k) = 1 - (1-p)^k$ for positive integers $k$, and use this to compute $P(X > n)$ for any positive integer $n$.

**Exercise 4.22.** A sensor reports temperature readings that are uniformly distributed on $[20, 30]$ (in Celsius). The reading is converted to Fahrenheit via $Y = 1.8X + 32$. Find the PDF of $Y$ using the change-of-variables formula and verify that $\int f_Y(y)\,dy = 1$.
=======
## CDF Problems

**Exercise 4.5.** Given the PMF from Exercise 4.3, write the CDF $F(x)$ as a piecewise function and sketch it.

**Exercise 4.6.** A continuous random variable has PDF $f(x) = 3x^2$ for $0 \le x \le 1$. Find the CDF and compute $P(0.5 \le X \le 0.8)$.

## Transformation Problems

**Exercise 4.7.** If $X \sim \text{B}(0.3)$ (Bernoulli with $p = 0.3$), find the PMF of $Y = 5X + 2$.

**Exercise 4.8.** Let $X$ be a random variable taking values $\{-2, -1, 0, 1, 2\}$ each with probability $1/5$. Find the PMF of $Y = X^2$.
>>>>>>> Stashed changes
