# Chapter 15 Exercises

Practice problems covering the normal distribution, continuous uniform, Beta, log-normal, transformations, and order statistics.

!!! warning "Exercise page"
    This page contains exercises for Chapter 15.

## Normal Distribution

**Exercise 15.1.** Let $Z \sim N(0, 1)$. Compute:

(a) $P(Z > 1.5)$

(b) $P(-2 < Z < 1)$

(c) The value $c$ such that $P(|Z| < c) = 0.90$

??? solution
    (a) $P(Z > 1.5) = 1 - \Phi(1.5) = 1 - 0.9332 = 0.0668$

    (b) $P(-2 < Z < 1) = \Phi(1) - \Phi(-2) = 0.8413 - 0.0228 = 0.8186$

    (c) $P(|Z| < c) = 2\Phi(c) - 1 = 0.90$, so $\Phi(c) = 0.95$, giving $c = 1.645$

---

**Exercise 15.2.** The weight of cereal boxes follows $X \sim N(500, 10^2)$ grams. Find:

(a) The probability a box weighs between 485 and 515 grams.

(b) The weight exceeded by only 1% of boxes.

(c) If a sample of 16 boxes is taken, find $P(\bar{X} > 505)$.

??? solution
    (a) $P(485 < X < 515) = \Phi(1.5) - \Phi(-1.5) = 2(0.9332) - 1 = 0.8664$

    (b) $P(X > x) = 0.01$ means $x = 500 + 10 \cdot \Phi^{-1}(0.99) = 500 + 10(2.326) = 523.26$ grams

    (c) $\bar{X} \sim N(500, 100/16) = N(500, 6.25)$. $P(\bar{X} > 505) = 1 - \Phi(5/2.5) = 1 - \Phi(2) = 0.0228$

---

**Exercise 15.3 (Linear Combination).** Let $X \sim N(10, 4)$ and $Y \sim N(20, 9)$ be independent. Find:

(a) The distribution of $3X - 2Y + 5$.

(b) $P(3X - 2Y + 5 > 0)$.

??? solution
    (a) $3X - 2Y + 5 \sim N(3(10) - 2(20) + 5, \; 9(4) + 4(9)) = N(-5, 72)$

    (b) $P(3X - 2Y + 5 > 0) = P\left(Z > \frac{0 - (-5)}{\sqrt{72}}\right) = P(Z > 0.589) = 1 - \Phi(0.589) \approx 0.278$

---

**Exercise 15.4 (Sum of Normals).** Scores on two tests are independent: $X_1 \sim N(70, 8^2)$ and $X_2 \sim N(75, 6^2)$. A student's total score is $T = X_1 + X_2$.

(a) Find the distribution of $T$.

(b) Find $P(T > 160)$.

(c) Find $P(X_2 > X_1)$.

??? solution
    (a) $T \sim N(70 + 75, \; 64 + 36) = N(145, 100)$

    (b) $P(T > 160) = P(Z > (160 - 145)/10) = P(Z > 1.5) = 0.0668$

    (c) $X_2 - X_1 \sim N(5, 100)$. $P(X_2 > X_1) = P(X_2 - X_1 > 0) = \Phi(5/10) = \Phi(0.5) = 0.6915$

---

## Continuous Uniform Distribution

**Exercise 15.5.** A bus arrives every 20 minutes. You arrive at a random time. Let $W \sim U(0, 20)$.

(a) Find $P(W > 15)$.

(b) Find $E[W]$ and $\text{Var}(W)$.

(c) Given that $W > 10$, find $E[W \mid W > 10]$.

??? solution
    (a) $P(W > 15) = 5/20 = 0.25$

    (b) $E[W] = 10$, $\text{Var}(W) = 400/12 = 100/3 \approx 33.33$

    (c) $W \mid W > 10 \sim U(10, 20)$, so $E[W \mid W > 10] = 15$

---

**Exercise 15.6 (Longer Piece).** A rod of length 1 is broken at a uniformly random point. Let $L$ be the length of the longer piece.

(a) Find the PDF of $L$.

(b) Find $E[L]$ and $\text{Var}(L)$.

??? solution
    (a) The break point $U \sim U(0, 1)$. $L = \max(U, 1-U)$. For $1/2 \leq l \leq 1$: $P(L \leq l) = P(l \geq U \geq 1 - l) = 2l - 1$. So $f_L(l) = 2$ for $1/2 < l < 1$.

    (b) $E[L] = \int_{1/2}^{1} 2l\,dl = [l^2]_{1/2}^1 = 1 - 1/4 = 3/4$. $E[L^2] = \int_{1/2}^1 2l^2\,dl = [2l^3/3]_{1/2}^1 = 2/3 - 1/12 = 7/12$. $\text{Var}(L) = 7/12 - 9/16 = 1/48$.

---

## Beta Distribution

**Exercise 15.7.** Let $X \sim \text{Beta}(3, 2)$.

(a) Find $E[X]$, $\text{Var}(X)$, and the mode.

(b) Find $E[X^2]$.

(c) Find the distribution of $1 - X$.

??? solution
    (a) $E[X] = 3/5 = 0.6$. $\text{Var}(X) = \frac{3 \cdot 2}{25 \cdot 6} = 1/25 = 0.04$. Mode $= (3-1)/(3+2-2) = 2/3$.

    (b) $E[X^2] = \frac{3 \cdot 4}{5 \cdot 6} = 12/30 = 2/5 = 0.4$

    (c) $1 - X \sim \text{Beta}(2, 3)$

---

**Exercise 15.8 (Bayesian Updating).** A coin has unknown probability $p$ of heads. Your prior is $p \sim \text{Beta}(2, 2)$. You flip the coin 10 times and observe 7 heads.

(a) Find the posterior distribution of $p$.

(b) Find the posterior mean and compare it to the prior mean and the MLE.

(c) Find a 95% equal-tailed credible interval for $p$.

??? solution
    (a) $p \mid X = 7 \sim \text{Beta}(2 + 7, 2 + 3) = \text{Beta}(9, 5)$

    (b) Prior mean $= 2/4 = 0.5$. MLE $= 7/10 = 0.7$. Posterior mean $= 9/14 \approx 0.643$. The posterior mean is between the prior mean and the MLE, pulled toward the data.

    (c) Using `scipy.stats.beta.ppf`: $(0.397, 0.850)$

---

**Exercise 15.9 (Gamma-Beta Connection).** Let $X \sim \Gamma(4, 3)$ and $Y \sim \Gamma(6, 3)$ be independent.

(a) Find the distribution of $F = X/(X + Y)$.

(b) Find $E[F]$ and $\text{Var}(F)$.

(c) What is the distribution of $T = X + Y$?

??? solution
    (a) $F \sim \text{Beta}(4, 6)$

    (b) $E[F] = 4/10 = 0.4$. $\text{Var}(F) = 24/(100 \cdot 11) = 24/1100 \approx 0.0218$

    (c) $T \sim \Gamma(10, 3)$. $T$ is independent of $F$.

---

## Log-Normal Distribution

**Exercise 15.10.** Let $X \sim \text{LogN}(3, 0.5^2)$.

(a) Find $E[X]$, $\text{Var}(X)$, and the median.

(b) Find $P(X > 30)$.

(c) Find the 95th percentile.

??? solution
    (a) $E[X] = e^{3.125} \approx 22.76$. $\text{Var}(X) = e^{6.25}(e^{0.25} - 1) \approx 150.42$. Median $= e^3 \approx 20.09$.

    (b) $P(X > 30) = P(\ln X > \ln 30) = P(Z > (\ln 30 - 3)/0.5) = P(Z > 0.802) = 1 - \Phi(0.802) \approx 0.211$

    (c) $Q(0.95) = \exp(3 + 0.5 \cdot 1.645) = e^{3.822} \approx 45.70$

---

**Exercise 15.11 (Products).** If $X \sim \text{LogN}(1, 0.2^2)$ and $Y \sim \text{LogN}(2, 0.3^2)$ are independent, find the distribution, mean, and median of $XY$.

??? solution
    $XY \sim \text{LogN}(3, 0.13)$ where $\sigma^2 = 0.04 + 0.09 = 0.13$.

    Mean $= e^{3 + 0.065} = e^{3.065} \approx 21.42$

    Median $= e^3 \approx 20.09$

---

## Transformations

**Exercise 15.12 (CDF Method).** Let $X \sim \text{Exp}(1)$ and $Y = \sqrt{X}$. Find the PDF of $Y$.

??? solution
    $F_Y(y) = P(\sqrt{X} \leq y) = P(X \leq y^2) = 1 - e^{-y^2}$ for $y > 0$.

    $f_Y(y) = 2y e^{-y^2}$ for $y > 0$.

    This is a Rayleigh distribution (or equivalently a Weibull with shape 2).

---

**Exercise 15.13 (Jacobian Method).** Let $X \sim U(0, 1)$ and $Y = -\ln X$. Find the PDF of $Y$ and identify the distribution.

??? solution
    $x = e^{-y}$, $|dx/dy| = e^{-y}$. $f_Y(y) = 1 \cdot e^{-y}$ for $y > 0$. This is $\text{Exp}(1)$.

---

**Exercise 15.14 (Probability Integral Transform).** Let $X$ have CDF $F(x) = 1 - (1 + x)^{-2}$ for $x \geq 0$ (a Lomax distribution).

(a) Verify that $F$ is a valid CDF.

(b) Find $F^{-1}(u)$.

(c) How would you simulate $X$ from $U \sim U(0, 1)$?

??? solution
    (a) $F(0) = 0$, $F(\infty) = 1$, $f(x) = 2(1+x)^{-3} > 0$. Valid.

    (b) Setting $u = 1 - (1+x)^{-2}$: $(1+x)^2 = 1/(1-u)$, so $x = (1-u)^{-1/2} - 1$.

    (c) $X = (1 - U)^{-1/2} - 1$, or equivalently $X = U^{-1/2} - 1$ since $1 - U \sim U(0,1)$.

---

**Exercise 15.15 (Box-Muller).** Using the Box-Muller transform with $U_1 = 0.3$ and $U_2 = 0.7$, compute the resulting pair of standard normal values $Z_1, Z_2$.

??? solution
    $R = \sqrt{-2\ln(0.7)} = \sqrt{-2(-0.3567)} = \sqrt{0.7133} = 0.8446$

    $\Theta = 2\pi(0.3) = 1.8850$

    $Z_1 = 0.8446 \cos(1.8850) = 0.8446 \times (-0.3090) = -0.2610$

    $Z_2 = 0.8446 \sin(1.8850) = 0.8446 \times 0.9511 = 0.8033$

---

## Order Statistics

**Exercise 15.16.** Let $X_1, \ldots, X_4 \sim U(0, 1)$ iid.

(a) Find the distribution of $X_{(1)}$ (the minimum).

(b) Find $E[X_{(1)}]$ and $\text{Var}(X_{(1)})$.

(c) Find $P(X_{(1)} > 0.5)$.

??? solution
    (a) $X_{(1)} \sim \text{Beta}(1, 4)$

    (b) $E[X_{(1)}] = 1/5 = 0.2$. $\text{Var}(X_{(1)}) = \frac{1 \cdot 4}{25 \cdot 6} = 4/150 \approx 0.0267$

    (c) $P(X_{(1)} > 0.5) = (1 - 0.5)^4 = 0.0625$

---

**Exercise 15.17.** Let $X_1, \ldots, X_5 \sim \text{Exp}(2)$ iid.

(a) Find the distribution of $X_{(1)}$ (the minimum).

(b) Find $E[X_{(1)}]$.

(c) Find $P(X_{(5)} > 3)$.

??? solution
    (a) $X_{(1)} \sim \text{Exp}(5 \times 2) = \text{Exp}(10)$

    (b) $E[X_{(1)}] = 1/10 = 0.1$

    (c) $P(X_{(5)} > 3) = 1 - P(X_{(5)} \leq 3) = 1 - [1 - e^{-6}]^5 = 1 - (1 - e^{-6})^5$. Since $e^{-6} \approx 0.00248$: $\approx 1 - (0.99752)^5 \approx 0.01236$

---

**Exercise 15.18 (Uniform-Beta).** Let $U_1, \ldots, U_7 \sim U(0, 1)$ iid.

(a) What is the distribution of $U_{(3)}$?

(b) Find $E[U_{(3)}]$ and $P(U_{(3)} < 0.5)$.

(c) Show that $\text{Cov}(U_{(2)}, U_{(5)}) = 3/192$.

??? solution
    (a) $U_{(3)} \sim \text{Beta}(3, 5)$

    (b) $E[U_{(3)}] = 3/8 = 0.375$. $P(U_{(3)} < 0.5) = I_{0.5}(3, 5) \approx 0.855$ (regularized incomplete beta function).

    (c) $\text{Cov}(U_{(2)}, U_{(5)}) = \frac{2 \cdot 3}{64 \cdot 9} = \frac{6}{576} = \frac{1}{96}$. Wait: $\text{Cov}(U_{(i)}, U_{(j)}) = \frac{i(n-j+1)}{(n+1)^2(n+2)} = \frac{2 \cdot 3}{64 \cdot 9} = 6/576 = 1/96$. And $3/192 = 1/64 \neq 1/96$. Correcting: $\frac{2 \cdot 3}{8^2 \cdot 9} = 6/576 = 1/96 \approx 0.01042$.

---

**Exercise 15.19 (Joint Distribution).** For $n = 4$ iid $U(0, 1)$, find the joint PDF of $(X_{(1)}, X_{(4)})$ and compute $E[X_{(4)} - X_{(1)}]$.

??? solution
    $f_{X_{(1)}, X_{(4)}}(x, y) = \frac{4!}{0! \cdot 2! \cdot 0!}(y - x)^2 = 12(y - x)^2$ for $0 < x < y < 1$.

    $E[X_{(4)} - X_{(1)}] = \int_0^1 \int_x^1 12(y - x)^3 \, dy\, dx = 12 \int_0^1 \frac{(1-x)^4}{4}\,dx = 3 \cdot \frac{1}{5} = \frac{3}{5} = 0.6$

    This matches the formula $(n-1)/(n+1) = 3/5$.

---

**Exercise 15.20 (Comprehensive).** A financial analyst models daily stock returns as $r \sim N(0.0004, 0.015^2)$.

(a) Find the probability of a daily loss exceeding 3% (i.e., $P(r < -0.03)$).

(b) If the stock price today is \$100, find the distribution of the price after one day.

(c) Find the 5% Value at Risk for a \$1,000,000 position over one day.

??? solution
    (a) $P(r < -0.03) = \Phi\!\left(\frac{-0.03 - 0.0004}{0.015}\right) = \Phi(-2.027) \approx 0.0213$

    (b) $S_1 = 100 \exp(r)$ where $r \sim N(0.0004, 0.000225)$. So $S_1 \sim \text{LogN}(\ln 100 + 0.0004, 0.015^2) = \text{LogN}(4.6056, 0.000225)$.

    (c) $\text{VaR}_{0.05} = 1{,}000{,}000 \times (1 - \exp(0.0004 + 0.015 \times \Phi^{-1}(0.05))) = 1{,}000{,}000 \times (1 - \exp(0.0004 + 0.015(-1.645))) \approx 1{,}000{,}000 \times (1 - e^{-0.0243}) \approx \$24{,}007$
