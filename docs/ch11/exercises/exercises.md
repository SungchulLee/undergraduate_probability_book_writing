# Chapter 11 Exercises: MGFs, PGFs, and Characteristic Functions

---

## Exercise 1: Computing an MGF

Let $X$ have PMF $P(X = -1) = \tfrac{1}{4}$, $P(X = 0) = \tfrac{1}{2}$, $P(X = 1) = \tfrac{1}{4}$.

**(a)** Find $M_X(t)$.

**(b)** Use the MGF to compute $E[X]$ and $\text{Var}(X)$.

??? solution "Solution"

    **(a)**

    $$M_X(t) = \tfrac{1}{4}e^{-t} + \tfrac{1}{2} + \tfrac{1}{4}e^{t} = \tfrac{1}{2} + \tfrac{1}{2}\cosh(t)$$

    **(b)** $M_X'(t) = \tfrac{1}{4}(-e^{-t} + e^{t}) = \tfrac{1}{2}\sinh(t)$, so $E[X] = M_X'(0) = 0$.

    $M_X''(t) = \tfrac{1}{2}\cosh(t)$, so $E[X^2] = M_X''(0) = \tfrac{1}{2}$.

    $\text{Var}(X) = \tfrac{1}{2} - 0 = \tfrac{1}{2}$.

---

## Exercise 2: Moments via Taylor Expansion

Suppose $M_X(t) = \frac{1}{1 - 2t}$ for $t < \tfrac{1}{2}$.

**(a)** Expand $M_X(t)$ as a power series and identify $E[X^n]$ for general $n$.

**(b)** What named distribution does $X$ follow?

??? solution "Solution"

    **(a)** $\frac{1}{1-2t} = \sum_{n=0}^{\infty}(2t)^n = \sum_{n=0}^{\infty} 2^n t^n$. Since $M_X(t) = \sum \frac{E[X^n]}{n!}t^n$, we get $E[X^n] = 2^n \cdot n!$.

    **(b)** This is the MGF of $\text{Exp}(\tfrac{1}{2})$, i.e., $\frac{\lambda}{\lambda - t} = \frac{1/2}{1/2 - t} = \frac{1}{1-2t}$ with $\lambda = \tfrac{1}{2}$.

---

## Exercise 3: Exponential Moments from MGF

Let $X \sim \text{Exp}(3)$.

**(a)** Write down $M_X(t)$ and its domain.

**(b)** Compute $E[X]$, $E[X^2]$, $E[X^3]$.

**(c)** Verify that $E[X^n] = \frac{n!}{\lambda^n}$ for general $n$.

??? solution "Solution"

    **(a)** $M_X(t) = \frac{3}{3 - t}$ for $t < 3$.

    **(b)** $M_X^{(n)}(t) = \frac{n! \cdot 3}{(3-t)^{n+1}}$, so $M_X^{(n)}(0) = \frac{n!}{3^n}$.

    $E[X] = \tfrac{1}{3}$, $E[X^2] = \tfrac{2}{9}$, $E[X^3] = \tfrac{6}{27} = \tfrac{2}{9}$.

    **(c)** $M_X(t) = \frac{\lambda}{\lambda - t} = \sum_{n=0}^{\infty}\frac{t^n}{\lambda^n}$, so $\frac{E[X^n]}{n!} = \frac{1}{\lambda^n}$, giving $E[X^n] = \frac{n!}{\lambda^n}$.

---

## Exercise 4: Uniqueness Application

Suppose $X$ has MGF $M_X(t) = e^{5(e^t - 1)}$.

**(a)** Identify the distribution of $X$.

**(b)** Find $P(X = 0)$, $E[X]$, and $\text{Var}(X)$ without computing any derivatives.

??? solution "Solution"

    **(a)** This is the MGF of $\text{Po}(5)$, since $M_{\text{Po}(\lambda)}(t) = e^{\lambda(e^t - 1)}$ with $\lambda = 5$.

    **(b)** By uniqueness, $X \sim \text{Po}(5)$, so $P(X = 0) = e^{-5} \approx 0.0067$, $E[X] = 5$, $\text{Var}(X) = 5$.

---

## Exercise 5: MGF of a Sum

Let $X \sim \text{Gamma}(2, 3)$ and $Y \sim \text{Gamma}(5, 3)$ be independent.

**(a)** Find $M_{X+Y}(t)$.

**(b)** Identify the distribution of $X + Y$.

**(c)** What goes wrong if $Y \sim \text{Gamma}(5, 4)$ instead?

??? solution "Solution"

    **(a)** $M_{X+Y}(t) = \left(\frac{3}{3-t}\right)^2 \cdot \left(\frac{3}{3-t}\right)^5 = \left(\frac{3}{3-t}\right)^7$

    **(b)** By uniqueness, $X + Y \sim \text{Gamma}(7, 3)$.

    **(c)** $M_{X+Y}(t) = \left(\frac{3}{3-t}\right)^2\left(\frac{4}{4-t}\right)^5$, which does not match any standard gamma MGF. The sum of gammas with different rate parameters is not gamma.

---

## Exercise 6: Identifying a Distribution

Let $X_1, \ldots, X_{20}$ be iid $\text{Bernoulli}(0.3)$, and let $S = \sum_{i=1}^{20} X_i$.

**(a)** Compute $M_S(t)$ using the product rule.

**(b)** Identify the distribution of $S$.

**(c)** Use the Poisson approximation MGF to approximate $P(S = 0)$.

??? solution "Solution"

    **(a)** $M_S(t) = [1 + 0.3(e^t - 1)]^{20} = [0.7 + 0.3e^t]^{20}$

    **(b)** This is the MGF of $B(20, 0.3)$, so $S \sim B(20, 0.3)$.

    **(c)** With $\lambda = np = 6$, $P(S = 0) \approx e^{-6} \approx 0.0025$. Exact: $0.7^{20} \approx 0.0008$.

---

## Exercise 7: PGF Basics

Let $X \sim \text{Po}(\lambda)$ with PGF $G_X(s) = e^{\lambda(s-1)}$.

**(a)** Verify that $G_X(0) = P(X = 0)$ and $G_X(1) = 1$.

**(b)** Compute $E[X]$ and $\text{Var}(X)$ using $G'(1)$ and $G''(1)$.

**(c)** Recover $P(X = 2)$ from the PGF by computing $G''(0)/2!$.

??? solution "Solution"

    **(a)** $G(0) = e^{-\lambda} = P(X=0)$. $G(1) = e^0 = 1$. Both check out.

    **(b)** $G'(s) = \lambda e^{\lambda(s-1)}$, so $E[X] = G'(1) = \lambda$. $G''(s) = \lambda^2 e^{\lambda(s-1)}$, so $G''(1) = \lambda^2$.

    $\text{Var}(X) = \lambda^2 + \lambda - \lambda^2 = \lambda$.

    **(c)** $G''(0) = \lambda^2 e^{-\lambda}$, so $P(X=2) = \frac{\lambda^2 e^{-\lambda}}{2}$, which matches $\frac{e^{-\lambda}\lambda^2}{2!}$.

---

## Exercise 8: Random Sum

Let $N \sim \text{Po}(4)$ and $X_i \stackrel{\text{iid}}{\sim} \text{Bernoulli}(0.5)$, independent of $N$. Let $S = X_1 + \cdots + X_N$.

**(a)** Find $G_S(s)$ using the composition formula.

**(b)** Identify the distribution of $S$.

**(c)** Compute $E[S]$ and $\text{Var}(S)$.

??? solution "Solution"

    **(a)** $G_X(s) = 0.5 + 0.5s$ and $G_N(s) = e^{4(s-1)}$.

    $G_S(s) = G_N(G_X(s)) = e^{4(0.5 + 0.5s - 1)} = e^{2(s-1)}$

    **(b)** This is the PGF of $\text{Po}(2)$. So $S \sim \text{Po}(2)$.

    **(c)** $E[S] = E[N] \cdot E[X] = 4 \cdot 0.5 = 2$. $\text{Var}(S) = 4 \cdot 0.25 + 4 \cdot 0.25 = 2$. Both consistent with $\text{Po}(2)$.

---

## Exercise 9: Characteristic Function Basics

Let $X \sim \text{Exp}(1)$.

**(a)** Compute $\varphi_X(t) = E[e^{itX}]$ directly by integration.

**(b)** Verify your answer agrees with $M_X(it) = \frac{1}{1 - it}$.

**(c)** Check that $|\varphi_X(t)| \leq 1$ and $\varphi_X(0) = 1$.

??? solution "Solution"

    **(a)** $\varphi_X(t) = \int_0^{\infty} e^{itx} e^{-x}\,dx = \int_0^{\infty} e^{-(1-it)x}\,dx = \frac{1}{1-it}$

    The integral converges because $\text{Re}(1 - it) = 1 > 0$.

    **(b)** $M_X(t) = \frac{1}{1-t}$, so $M_X(it) = \frac{1}{1-it}$. Confirmed.

    **(c)** $|\varphi_X(t)| = \frac{1}{\sqrt{1+t^2}} \leq 1$ for all $t$. $\varphi_X(0) = 1$.

---

## Exercise 10: CF and the CLT

Let $X_1, \ldots, X_n$ be iid with $E[X_i] = \mu$ and $\text{Var}(X_i) = \sigma^2$. Define $Z_n = \frac{\sum X_i - n\mu}{\sigma\sqrt{n}}$.

**(a)** Show that $\varphi_{Z_n}(t) = \left[\varphi_X\!\left(\frac{t}{\sigma\sqrt{n}}\right) \cdot e^{-i\mu t / (\sigma\sqrt{n})}\right]^n$.

**(b)** Use the Taylor expansion $\varphi_X(s) \approx 1 + i\mu s - \tfrac{1}{2}(\sigma^2 + \mu^2)s^2$ to show that $\varphi_{Z_n}(t) \to e^{-t^2/2}$ as $n \to \infty$.

??? solution "Solution"

    **(a)** $Z_n = \frac{1}{\sigma\sqrt{n}}\sum(X_i - \mu)$, so $\varphi_{Z_n}(t) = \prod_{i=1}^n \varphi_{X_i - \mu}\!\left(\frac{t}{\sigma\sqrt{n}}\right) = \left[e^{-i\mu t/(\sigma\sqrt{n})}\varphi_X\!\left(\frac{t}{\sigma\sqrt{n}}\right)\right]^n$.

    **(b)** Let $s = t/(\sigma\sqrt{n})$. Then:

    $$e^{-i\mu s}\varphi_X(s) \approx e^{-i\mu s}\left(1 + i\mu s - \tfrac{1}{2}(\sigma^2+\mu^2)s^2\right) \approx 1 - \tfrac{1}{2}\sigma^2 s^2 = 1 - \frac{t^2}{2n}$$

    So $\varphi_{Z_n}(t) \approx \left(1 - \frac{t^2}{2n}\right)^n \to e^{-t^2/2}$, the CF of $N(0,1)$.

---

## Exercise 11: MGF Does Not Determine All Distributions

**(a)** Explain why the Cauchy distribution has no MGF.

**(b)** The log-normal distribution $X \sim \text{Lognormal}(0,1)$ has moments $E[X^n] = e^{n^2/2}$. Show that the moment series $\sum \frac{E[X^n]}{n!}t^n$ diverges for all $t \neq 0$.

**(c)** Does this mean the log-normal distribution is not uniquely determined? Explain.

??? solution "Solution"

    **(a)** The Cauchy PDF $f(x) = \frac{1}{\pi(1+x^2)}$ has tails so heavy that $E[|X|] = \infty$. Since $e^{tx} \geq |tx|$ for large $x$, $E[e^{tX}] = \infty$ for all $t \neq 0$.

    **(b)** $\frac{E[X^n]}{n!}|t|^n = \frac{e^{n^2/2}}{n!}|t|^n$. By the ratio test, $\frac{a_{n+1}}{a_n} = \frac{e^{(n+1)^2/2}}{e^{n^2/2}} \cdot \frac{1}{n+1}|t| = \frac{e^{n+1/2}}{n+1}|t| \to \infty$. The series diverges.

    **(c)** The log-normal is determined by its CF (which always exists), but it is an example where the moment sequence alone does not uniquely determine the distribution. This is the Hamburger moment problem.

---

## Exercise 12: PGF Product Rule

Let $X \sim \text{Po}(3)$ and $Y \sim \text{Po}(7)$ be independent.

**(a)** Compute $G_{X+Y}(s)$ using the PGF product rule.

**(b)** Identify the distribution of $X + Y$.

**(c)** Verify that $E[X + Y]$ and $\text{Var}(X + Y)$ are consistent with your answer.

??? solution "Solution"

    **(a)** $G_{X+Y}(s) = e^{3(s-1)} \cdot e^{7(s-1)} = e^{10(s-1)}$

    **(b)** This is the PGF of $\text{Po}(10)$, so $X + Y \sim \text{Po}(10)$.

    **(c)** $E[X+Y] = 3 + 7 = 10$ and $\text{Var}(X+Y) = 3 + 7 = 10$, both matching $\text{Po}(10)$.
