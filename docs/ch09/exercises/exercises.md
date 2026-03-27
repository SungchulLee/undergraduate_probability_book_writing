# Chapter 9 Exercises

## Section 9.1: Covariance and Correlation

**Exercise 9.1.1** Let $(X, Y)$ have joint PMF:

|  | $Y = 0$ | $Y = 1$ | $Y = 2$ |
|:---:|:---:|:---:|:---:|
| $X = 0$ | 0.1 | 0.2 | 0.1 |
| $X = 1$ | 0.15 | 0.25 | 0.2 |

Compute $\text{Cov}(X, Y)$ and $\rho(X, Y)$.

**Exercise 9.1.2** Prove that $\text{Cov}(X + Y, X - Y) = \text{Var}(X) - \text{Var}(Y)$ for any random variables $X$ and $Y$.

**Exercise 9.1.3** Let $X$ be uniform on $\{-2, -1, 0, 1, 2\}$ and $Y = X^2$. Show that $\text{Cov}(X, Y) = 0$ but $X$ and $Y$ are not independent.

**Exercise 9.1.4** If $\text{Var}(X) = 5$, $\text{Var}(Y) = 3$, and $\text{Var}(X + Y) = 12$, find $\text{Cov}(X, Y)$ and $\rho(X, Y)$.

**Exercise 9.1.5** Use the Cauchy--Schwarz inequality to show that for any random variable $X$ with $E[X^2] < \infty$:

$$
\bigl(E[|X|]\bigr)^2 \leq E[X^2]
$$

---

## Section 9.2: Expectation of Sums and Products

**Exercise 9.2.1** A class of $n = 25$ students each independently choose a favorite day of the week (uniformly among 7 days). Let $S$ be the number of pairs of students who share the same favorite day. Use linearity of expectation to compute $E[S]$.

**Exercise 9.2.2** Let $X$ and $Y$ be independent with $E[X] = 3$, $E[Y] = -2$, $E[X^2] = 13$, and $E[Y^2] = 8$. Compute $E[XY]$, $E[(X+Y)^2]$, and $\text{Cov}(X, Y)$.

**Exercise 9.2.3** Prove that if $X$ and $Y$ are independent, then $\text{Var}(XY) = \text{Var}(X)\,\text{Var}(Y) + \text{Var}(X)(E[Y])^2 + (E[X])^2\,\text{Var}(Y)$.

---

## Section 9.3: Variance of Sums

**Exercise 9.3.1** Let $X_1, X_2, X_3$ be random variables with $\text{Var}(X_i) = 2$ for all $i$, $\text{Cov}(X_1, X_2) = 0.5$, $\text{Cov}(X_1, X_3) = -0.3$, and $\text{Cov}(X_2, X_3) = 0.8$. Compute $\text{Var}(X_1 + X_2 + X_3)$.

**Exercise 9.3.2** Let $X_1, \ldots, X_{50}$ be iid with $E[X_i] = 10$ and $\text{Var}(X_i) = 16$. Compute $E[\bar{X}_{50}]$, $\text{Var}(\bar{X}_{50})$, and $\text{SD}(\bar{X}_{50})$.

**Exercise 9.3.3** A portfolio has weights $\mathbf{a} = (0.4, 0.4, 0.2)^T$ and the asset covariance matrix is

$$
\boldsymbol{\Sigma} = \begin{pmatrix} 0.04 & 0.02 & -0.01 \\ 0.02 & 0.09 & 0.03 \\ -0.01 & 0.03 & 0.16 \end{pmatrix}
$$

Compute the portfolio variance $\mathbf{a}^T \boldsymbol{\Sigma}\, \mathbf{a}$ and verify that $\boldsymbol{\Sigma}$ is positive semi-definite.

**Exercise 9.3.4** Show that for any $n$ random variables with the same variance $\sigma^2$ and the same pairwise correlation $\rho \geq 0$:

$$
\text{Var}\!\left(\frac{1}{n}\sum_{i=1}^n X_i\right) = \frac{\sigma^2}{n}\bigl(1 + (n-1)\rho\bigr)
$$

What happens as $n \to \infty$? Interpret the result.

**Exercise 9.3.5** Let $X$ and $Y$ be random variables with $\text{Var}(X) = \text{Var}(Y) = \sigma^2$ and correlation $\rho$. Find the value of $c$ that minimizes $\text{Var}(X - cY)$.
