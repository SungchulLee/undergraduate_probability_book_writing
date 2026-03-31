<<<<<<< Updated upstream
# Chapter 15 Exercises

## Uniform Distribution

**Exercise 15.1.** Let $X \sim U(2, 8)$.

(a) Find $P(3 < X < 6)$.

(b) Find $E[X^2]$.

(c) Find the median of $X$.

??? solution
    (a) $P(3 < X < 6) = \frac{6 - 3}{8 - 2} = \frac{1}{2}$

    (b) $E[X^2] = \frac{a^2 + ab + b^2}{3} = \frac{4 + 16 + 64}{3} = 28$

    (c) The median is $\frac{a + b}{2} = 5$, which equals the mean by symmetry.

---

**Exercise 15.2 (Simulation).** Let $U \sim U(0, 1)$. Find the PDF of $Y = -3\ln(U)$.

??? solution
    $F_Y(y) = P(-3\ln U \leq y) = P(\ln U \geq -y/3) = P(U \geq e^{-y/3}) = 1 - e^{-y/3}$ for $y > 0$.

    This is the CDF of $\text{Exp}(1/3)$, so $f_Y(y) = \frac{1}{3}e^{-y/3}$ for $y > 0$.

---

## Normal Distribution

**Exercise 15.3.** Heights of adult women follow $X \sim N(64, 9)$ (inches).

(a) Find $P(X > 70)$.

(b) Find the height that separates the tallest 5%.

(c) Find $P(61 < X < 67)$.

??? solution
    (a) $P(X > 70) = 1 - \Phi\!\left(\frac{70 - 64}{3}\right) = 1 - \Phi(2) = 1 - 0.9772 = 0.0228$

    (b) We need $c$ with $P(X > c) = 0.05$, so $c = 64 + 3 \cdot z_{0.95} = 64 + 3(1.645) = 68.93$ inches.

    (c) $P(61 < X < 67) = \Phi(1) - \Phi(-1) = 0.8413 - 0.1587 = 0.6827$

---

**Exercise 15.4 (Linear Combination).** Let $X \sim N(100, 225)$ and $Y \sim N(110, 400)$ be independent. Find $P(X > Y)$.

??? solution
    $X - Y \sim N(100 - 110, 225 + 400) = N(-10, 625)$.

    $P(X > Y) = P(X - Y > 0) = 1 - \Phi\!\left(\frac{0 - (-10)}{25}\right) = 1 - \Phi(0.4) = 1 - 0.6554 = 0.3446$

---

**Exercise 15.5 (Sample Mean).** Suppose $X_1, \ldots, X_{16} \overset{\text{iid}}{\sim} N(50, 64)$. Find $P(\bar{X} > 53)$.

??? solution
    $\bar{X} \sim N(50, 64/16) = N(50, 4)$.

    $P(\bar{X} > 53) = 1 - \Phi\!\left(\frac{53 - 50}{2}\right) = 1 - \Phi(1.5) = 1 - 0.9332 = 0.0668$

---

## Beta Distribution

**Exercise 15.6.** Let $X \sim \text{Beta}(3, 5)$.

(a) Find $E[X]$ and $\text{Var}(X)$.

(b) Find $E[X^2]$.

(c) Find the distribution of $1 - X$.

??? solution
    (a) $E[X] = \frac{3}{8} = 0.375$, $\text{Var}(X) = \frac{15}{64 \cdot 9} = \frac{15}{576} \approx 0.0260$

    (b) $E[X^2] = \text{Var}(X) + (E[X])^2 = \frac{15}{576} + \frac{9}{64} = \frac{15 + 81}{576} = \frac{96}{576} = \frac{1}{6}$

    (c) By the reflection property, $1 - X \sim \text{Beta}(5, 3)$.

---

**Exercise 15.7 (Bayesian Updating).** A coin has unknown probability $p$ of heads. Your prior is $p \sim \text{Beta}(2, 2)$. You flip the coin 10 times and observe 7 heads. Find the posterior distribution and the posterior mean.

??? solution
    By Beta-Binomial conjugacy, the posterior is:

    $$p \mid X = 7 \sim \text{Beta}(2 + 7, 2 + 3) = \text{Beta}(9, 5)$$

    The posterior mean is $\frac{9}{14} \approx 0.643$.

    This is between the prior mean $\frac{2}{4} = 0.5$ and the MLE $\frac{7}{10} = 0.7$, closer to the data because $n = 10$ is larger than the prior pseudo-count $\alpha + \beta = 4$.

---

## Log-Normal Distribution

**Exercise 15.8.** Stock returns are modeled as $X = e^Y$ where $Y \sim N(0.05, 0.04)$.

(a) Find $E[X]$ and $\text{Var}(X)$.

(b) Find $P(X > 1.2)$.

(c) Find the median of $X$.

??? solution
    (a) $E[X] = e^{0.05 + 0.02} = e^{0.07} \approx 1.0725$

    $\text{Var}(X) = (e^{0.04} - 1) \cdot e^{0.10 + 0.04} = (e^{0.04} - 1) \cdot e^{0.14} \approx 0.04082 \cdot 1.1503 \approx 0.04695$

    (b) $P(X > 1.2) = P(Y > \ln 1.2) = P\!\left(Z > \frac{0.1823 - 0.05}{0.2}\right) = 1 - \Phi(0.662) \approx 0.254$

    (c) Median of $X$ is $e^{\mu} = e^{0.05} \approx 1.0513$

---

## Order Statistics

**Exercise 15.9.** Let $X_1, \ldots, X_6 \overset{\text{iid}}{\sim} U(0, 1)$.

(a) Find $E[X_{(2)}]$ and $\text{Var}(X_{(2)})$.

(b) Find $P(X_{(6)} < 0.9)$.

(c) Find $E[X_{(6)} - X_{(1)}]$.

??? solution
    (a) $U_{(2)} \sim \text{Beta}(2, 5)$, so $E[U_{(2)}] = \frac{2}{7} \approx 0.286$ and $\text{Var}(U_{(2)}) = \frac{10}{49 \cdot 8} = \frac{10}{392} \approx 0.0255$

    (b) $P(X_{(6)} < 0.9) = [F(0.9)]^6 = 0.9^6 \approx 0.5314$

    (c) $E[X_{(6)} - X_{(1)}] = \frac{6}{7} - \frac{1}{7} = \frac{5}{7} \approx 0.7143$

---

**Exercise 15.10 (Minimum of Exponentials).** Let $X_1, \ldots, X_5 \overset{\text{iid}}{\sim} \text{Exp}(2)$.

(a) Find the distribution of $X_{(1)} = \min(X_1, \ldots, X_5)$.

(b) Find $P(X_{(1)} > 0.5)$.

??? solution
    (a) $X_{(1)} \sim \text{Exp}(5 \cdot 2) = \text{Exp}(10)$

    (b) $P(X_{(1)} > 0.5) = e^{-10 \cdot 0.5} = e^{-5} \approx 0.0067$

---

**Exercise 15.11 (k-th Order Statistic).** For $n = 7$ iid $U(0, 1)$ samples, write the PDF of the median $X_{(4)}$ and verify it integrates to 1 using the Beta function.

??? solution
    $$f_{X_{(4)}}(x) = \frac{7!}{3!\cdot 3!} x^3(1-x)^3 = 140\, x^3(1-x)^3, \quad 0 < x < 1$$

    This is $\text{Beta}(4, 4)$, so:

    $$\int_0^1 140\, x^3(1-x)^3\, dx = 140 \cdot B(4, 4) = 140 \cdot \frac{3!\cdot 3!}{7!} = 140 \cdot \frac{36}{5040} = 140 \cdot \frac{1}{140} = 1 \checkmark$$

---

## Transformations

**Exercise 15.12 (Change of Variables).** Let $X \sim \text{Exp}(1)$ and $Y = \sqrt{X}$. Find the PDF of $Y$.

??? solution
    **CDF method:** $F_Y(y) = P(\sqrt{X} \leq y) = P(X \leq y^2) = 1 - e^{-y^2}$ for $y > 0$.

    $f_Y(y) = 2y\, e^{-y^2}$ for $y > 0$.

    This is a **Rayleigh distribution** (or equivalently, a Weibull distribution with shape 2).

---

**Exercise 15.13 (Probability Integral Transform).** Let $X$ have CDF $F(x) = 1 - e^{-x^2}$ for $x > 0$. Show that $F(X) \sim U(0, 1)$.

??? solution
    For $0 < u < 1$:

    $$P(F(X) \leq u) = P(X \leq F^{-1}(u))= F(F^{-1}(u)) = u$$

    This is the CDF of $U(0, 1)$. The result holds for any continuous CDF $F$.

---

**Exercise 15.14 (Joint Order Statistics).** Let $U_1, \ldots, U_4 \overset{\text{iid}}{\sim} U(0, 1)$. Write the joint PDF of $(U_{(1)}, U_{(4)})$ and compute $E[U_{(4)} - U_{(1)}]$.

??? solution
    With $i = 1$, $j = 4$, $n = 4$, $F(x) = x$, $f(x) = 1$:

    $$f_{U_{(1)}, U_{(4)}}(s, t) = \frac{4!}{0!\cdot 2!\cdot 0!}(t - s)^2 = 12(t - s)^2, \quad 0 < s < t < 1$$

    $$E[U_{(4)} - U_{(1)}] = E[U_{(4)}] - E[U_{(1)}] = \frac{4}{5} - \frac{1}{5} = \frac{3}{5}$$

    Alternatively, the range $R = U_{(4)} - U_{(1)}$ has $E[R] = \frac{n-1}{n+1} = \frac{3}{5}$.

---

**Exercise 15.15 (Box-Muller).** Let $U_1, U_2 \overset{\text{iid}}{\sim} U(0, 1)$. Define $Z_1 = \sqrt{-2\ln U_1}\cos(2\pi U_2)$ and $Z_2 = \sqrt{-2\ln U_1}\sin(2\pi U_2)$.

(a) What are the distributions of $Z_1$ and $Z_2$?

(b) Are $Z_1$ and $Z_2$ independent?

??? solution
    (a) $Z_1 \sim N(0, 1)$ and $Z_2 \sim N(0, 1)$.

    (b) Yes, $Z_1$ and $Z_2$ are independent standard normals. This follows from the Box-Muller transform: if $R^2 = -2\ln U_1 \sim \text{Exp}(1/2)$ and $\Theta = 2\pi U_2 \sim U(0, 2\pi)$ are independent, then $(R\cos\Theta, R\sin\Theta)$ is a pair of iid $N(0,1)$ random variables.
=======
# Exercises
>>>>>>> Stashed changes
