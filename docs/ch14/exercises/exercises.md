# Chapter 14 Exercises

## Exponential Distribution

**Exercise 14.1.** Let $X \sim \text{Exp}(3)$.

(a) Find $P(X > 2)$.

(b) Find $P(1 < X < 4)$.

(c) Find the median of $X$.

??? solution
    (a) $P(X > 2) = e^{-3 \cdot 2} = e^{-6} \approx 0.00248$

    (b) $P(1 < X < 4) = e^{-3} - e^{-12} \approx 0.0498$

    (c) Solve $1 - e^{-3m} = 1/2$, giving $m = \frac{\ln 2}{3} \approx 0.231$

---

**Exercise 14.2 (Memoryless Property).** A light bulb has an exponentially distributed lifetime with mean 1000 hours. Given that the bulb has already lasted 500 hours, what is the expected remaining lifetime?

??? solution
    By the memoryless property, the remaining lifetime is still $\text{Exp}(1/1000)$ with mean 1000 hours. The 500 hours already elapsed provide no information about the remaining time.

---

**Exercise 14.3 (Simulation).** Using a uniform random variable $U \sim U(0,1)$, generate a random variable $X \sim \text{Exp}(0.5)$.

??? solution
    $F(x) = 1 - e^{-0.5x}$, so $X = F^{-1}(U) = -2\log(1 - U) \sim \text{Exp}(0.5)$.

    Since $1 - U \sim U(0,1)$, we can simplify: $X = -2\log(U) \sim \text{Exp}(0.5)$.

---

**Exercise 14.4 (Minimum of Exponentials).** Machines A and B have lifetimes that are independent and exponentially distributed with rates $\lambda_A = 0.1$ and $\lambda_B = 0.2$ (per year). Find the expected time until the first machine fails.

??? solution
    $\min(T_A, T_B) \sim \text{Exp}(\lambda_A + \lambda_B) = \text{Exp}(0.3)$.

    $E[\min(T_A, T_B)] = \frac{1}{0.3} \approx 3.33$ years.

---

## Gamma Distribution

**Exercise 14.5.** Let $X \sim \Gamma(3, 2)$. Find $E[X]$, $\text{Var}(X)$, and $E[X^2]$.

??? solution
    $E[X] = \alpha/\lambda = 3/2 = 1.5$

    $\text{Var}(X) = \alpha/\lambda^2 = 3/4 = 0.75$

    $E[X^2] = \text{Var}(X) + (E[X])^2 = 0.75 + 2.25 = 3.0$

    Alternatively: $E[X^2] = \alpha(\alpha+1)/\lambda^2 = 3 \cdot 4 / 4 = 3.0$

---

**Exercise 14.6 (Gamma Additivity).** If $X \sim \Gamma(2, 5)$ and $Y \sim \Gamma(3, 5)$ are independent, find the distribution, mean, and variance of $X + Y$.

??? solution
    $X + Y \sim \Gamma(2 + 3, 5) = \Gamma(5, 5)$.

    $E[X + Y] = 5/5 = 1$

    $\text{Var}(X + Y) = 5/25 = 0.2$

---

**Exercise 14.7 (Gamma Function).** Evaluate:

(a) $\Gamma(6)$

(b) $\Gamma(5/2)$

(c) $B(3, 4)$ where $B$ is the Beta function.

??? solution
    (a) $\Gamma(6) = 5! = 120$

    (b) $\Gamma(5/2) = \frac{3}{2} \cdot \Gamma(3/2) = \frac{3}{2} \cdot \frac{1}{2} \cdot \Gamma(1/2) = \frac{3}{4}\sqrt{\pi} \approx 1.329$

    (c) $B(3, 4) = \frac{\Gamma(3)\Gamma(4)}{\Gamma(7)} = \frac{2! \cdot 3!}{6!} = \frac{12}{720} = \frac{1}{60}$

---

## Erlang Distribution and Poisson Process Waiting Times

**Exercise 14.8 (Bank Waiting Time).** Customers arrive at a single-server bank at rate $\lambda = 6$ per hour (Poisson process). You are third in line. What is the distribution, mean, and standard deviation of your total waiting time (until you finish being served)?

??? solution
    You must wait for 3 services to complete. If service times are iid $\text{Exp}(6)$ (per hour), the total wait is $S_3 = T_1 + T_2 + T_3 \sim \Gamma(3, 6)$.

    $E[S_3] = 3/6 = 0.5$ hours = 30 minutes

    $\text{SD}(S_3) = \sqrt{3/36} = \sqrt{3}/6 \approx 0.289$ hours $\approx 17.3$ minutes

---

**Exercise 14.9 (Fraction of Waiting Time).** When you enter a bank, one person is in line and there are 5 service desks, each with iid $\text{Exp}(\lambda_B)$ service times where $\lambda_B^{-1} = 10$ minutes. After the bank, you visit a post office where 2 people are in line, there are 2 service desks, and service times are iid $\text{Exp}(\lambda_P)$ where $\lambda_P^{-1} = 4$ minutes.

Let $F$ be the fraction of total waiting time spent at the bank. Find $E[F]$ and $\text{Var}(F)$.

??? solution
    **Bank:** With 5 desks and 2 people (you + 1 ahead), the effective service rate is $5\lambda_B = 0.5$ per minute. You wait for 2 services: $T_B = X_1 + X_2$ where $X_i \sim \text{Exp}(0.5)$, so $T_B \sim \Gamma(2, 0.5)$.

    **Post office:** With 2 desks and 3 people (you + 2 ahead), the effective service rate is $2\lambda_P = 0.5$ per minute. You wait for 3 services: $T_P = Y_1 + Y_2 + Y_3$ where $Y_j \sim \text{Exp}(0.5)$, so $T_P \sim \Gamma(3, 0.5)$.

    Since $T_B \sim \Gamma(2, 0.5)$ and $T_P \sim \Gamma(3, 0.5)$ are independent with the same rate:

    $$F = \frac{T_B}{T_B + T_P} \sim \text{Beta}(2, 3)$$

    $$E[F] = \frac{\alpha}{\alpha + \beta} = \frac{2}{5} = 0.4$$

    $$\text{Var}(F) = \frac{\alpha\beta}{(\alpha+\beta)^2(\alpha+\beta+1)} = \frac{6}{25 \cdot 6} = \frac{1}{25} = 0.04$$

---

**Exercise 14.10 (Inspection Paradox).** Buses arrive at a stop according to a Poisson process with rate $\lambda = 4$ per hour. You arrive at a random time.

(a) What is the expected length of the interarrival interval you land in?

(b) What is the expected time until the next bus?

(c) Explain why your answer to (b) is $1/\lambda$, not $1/(2\lambda)$.

??? solution
    (a) By the inspection paradox, $\tau \sim \Gamma(2, 4)$, so $E[\tau] = 2/4 = 0.5$ hours = 30 minutes. This is twice the mean interarrival time of 15 minutes.

    (b) By the memoryless property, the forward recurrence time is $\text{Exp}(4)$, so the expected wait is \$1/4$ hour = 15 minutes.

    (c) The naive argument "you arrive in the middle on average, so wait half" assumes uniform arrival within the interval. But you're more likely to land in longer intervals, which exactly cancels the "middle" effect. The memoryless property gives the correct answer directly: regardless of when the last bus came, the time to the next bus is always $\text{Exp}(\lambda)$.

---

## Chi-Squared Connection

**Exercise 14.11.** If $Z_1, Z_2, \ldots, Z_8$ are iid $N(0,1)$, find the distribution, mean, and variance of $W = Z_1^2 + Z_2^2 + \cdots + Z_8^2$.

??? solution
    $W \sim \chi^2_8 = \Gamma(4, 1/2)$.

    $E[W] = 8$, $\text{Var}(W) = 16$.
