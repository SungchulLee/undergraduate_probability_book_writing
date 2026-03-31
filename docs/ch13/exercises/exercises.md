<<<<<<< Updated upstream
# Chapter 13 Exercises: Poisson Process

---

## Exercise 1: Basic Poisson Process Calculations

Emails arrive at an inbox as a Poisson process with rate $\lambda = 12$ per hour.

**(a)** What is the expected number of emails in a 30-minute window?

**(b)** Compute $P(\text{exactly 4 emails in 30 minutes})$.

**(c)** Compute $P(\text{at least 1 email in 10 minutes})$.

**(d)** Compute $P(\text{no emails in 15 minutes})$.

??? solution "Solution"

    **(a)** In 30 minutes ($t = 0.5$ hours): $E[N(0.5)] = 12 \times 0.5 = 6$.

    **(b)** $N(0.5) \sim \text{Po}(6)$:

    $$
    P(N(0.5) = 4) = \frac{e^{-6} \cdot 6^4}{4!} = \frac{e^{-6} \cdot 1296}{24} \approx 0.1339
    $$

    **(c)** In 10 minutes ($t = 1/6$ hour): $N(1/6) \sim \text{Po}(2)$.

    $$
    P(N(1/6) \geq 1) = 1 - P(N(1/6) = 0) = 1 - e^{-2} \approx 0.8647
    $$

    **(d)** In 15 minutes ($t = 0.25$ hours): $N(0.25) \sim \text{Po}(3)$.

    $$
    P(N(0.25) = 0) = e^{-3} \approx 0.0498
    $$

---

## Exercise 2: Independent Increments

Customers arrive at a coffee shop as a Poisson process with rate $\lambda = 8$ per hour. Let $A = N(0, 1)$ be the count from 8am to 9am and $B = N(2, 3)$ be the count from 10am to 11am.

**(a)** Are $A$ and $B$ independent? State the distributions of $A$ and $B$.

**(b)** Compute $P(A = 5, B = 10)$.

**(c)** Compute $P(A + B = 15)$.

**(d)** Let $C = N(0, 2)$. Are $A$ and $C$ independent? Explain.

??? solution "Solution"

    **(a)** Yes, $A$ and $B$ are independent because $(0, 1]$ and $(2, 3]$ are disjoint. Both follow $\text{Po}(8)$.

    **(b)** By independence:

    $$
    P(A = 5, B = 10) = \frac{e^{-8} \cdot 8^5}{5!} \cdot \frac{e^{-8} \cdot 8^{10}}{10!} \approx 0.0916 \times 0.0993 \approx 0.0091
    $$

    **(c)** Since $A$ and $B$ are independent Poisson, $A + B \sim \text{Po}(16)$:

    $$
    P(A + B = 15) = \frac{e^{-16} \cdot 16^{15}}{15!} \approx 0.0992
    $$

    **(d)** No. $A$ and $C$ are not independent because $C = N(0, 2) = N(0, 1) + N(1, 2) = A + N(1, 2)$, so $C$ contains $A$. In fact, $\text{Cov}(A, C) = \text{Var}(A) = 8 > 0$.

---

## Exercise 3: Stationary Increments

A radioactive source emits particles as a Poisson process with rate $\lambda = 100$ per second.

**(a)** What is the distribution of the number of particles emitted between $t = 5$ and $t = 8$ seconds?

**(b)** Is this distribution different from the number emitted between $t = 0$ and $t = 3$? Explain using the stationarity property.

**(c)** Compute the probability that more than 320 particles are emitted in a 3-second window. Use a Normal approximation.

??? solution "Solution"

    **(a)** $N(5, 8) \sim \text{Po}(100 \times 3) = \text{Po}(300)$.

    **(b)** No, by stationary increments, $N(5, 8)$ and $N(0, 3)$ have the same distribution, $\text{Po}(300)$. The distribution depends only on the interval length (3 seconds), not the starting time.

    **(c)** With $\mu = 300$ and $\sigma = \sqrt{300} \approx 17.32$:

    $$
    P(N > 320) \approx P\!\left(Z > \frac{320 - 300}{\sqrt{300}}\right) = P(Z > 1.155) \approx 0.124
    $$

---

## Exercise 4: Merging Poisson Processes

A tech support center receives requests from three independent sources:

- Phone calls: $\text{PP}(10)$ per hour
- Emails: $\text{PP}(15)$ per hour
- Live chat: $\text{PP}(20)$ per hour

**(a)** What is the distribution of the total number of requests per hour?

**(b)** Compute the probability of fewer than 40 total requests in one hour.

**(c)** What is the probability that the center receives more than 100 total requests in a 2-hour period?

??? solution "Solution"

    **(a)** By merging, the total is $\text{PP}(10 + 15 + 20) = \text{PP}(45)$. The count per hour is $\text{Po}(45)$.

    **(b)**

    ```python
    from scipy.stats import poisson
    print(f"P(N < 40) = {poisson.cdf(39, 45):.6f}")
    ```

    $P(N(1) < 40) = P(N(1) \leq 39) \approx 0.2088$.

    **(c)** In 2 hours: $N(2) \sim \text{Po}(90)$.

    ```python
    print(f"P(N > 100) = {1 - poisson.cdf(100, 90):.6f}")
    ```

    $P(N(2) > 100) \approx 0.1303$.

---

## Exercise 5: Splitting (Thinning)

Vehicles pass through a toll booth as a Poisson process with rate $\lambda = 60$ per hour. Each vehicle is independently a car (probability 0.7), a truck (probability 0.2), or a bus (probability 0.1).

**(a)** What are the rates of the car, truck, and bus arrival processes?

**(b)** Are these three processes independent?

**(c)** Compute the probability of exactly 2 buses in a 30-minute window.

**(d)** Compute the probability that at least 1 truck and at least 1 bus arrive in a 10-minute window.

??? solution "Solution"

    **(a)** By splitting: cars at rate $0.7 \times 60 = 42$/hr, trucks at $0.2 \times 60 = 12$/hr, buses at $0.1 \times 60 = 6$/hr.

    **(b)** Yes, by the splitting theorem, the three resulting processes are independent Poisson processes.

    **(c)** Buses in 30 min: $\text{Po}(6 \times 0.5) = \text{Po}(3)$.

    $$
    P(\text{buses} = 2) = \frac{e^{-3} \cdot 9}{2} \approx 0.2240
    $$

    **(d)** In 10 min ($= 1/6$ hr): trucks $\sim \text{Po}(2)$, buses $\sim \text{Po}(1)$, independently.

    $$
    P(\text{trucks} \geq 1, \text{buses} \geq 1) = (1 - e^{-2})(1 - e^{-1}) \approx 0.8647 \times 0.6321 \approx 0.5467
    $$

---

## Exercise 6: Conditional Uniform Arrivals

Customers arrive at a bank as a Poisson process with rate $\lambda = 10$ per hour. Given that exactly 5 customers arrive between 9:00 and 10:00:

**(a)** What is the conditional distribution of the arrival time of each customer?

**(b)** What is the expected arrival time of the 3rd customer?

**(c)** What is the probability that all 5 customers arrive in the first 40 minutes?

??? solution "Solution"

    **(a)** By the conditional uniformity theorem, given $N(1) = 5$, the 5 arrival times behave as order statistics of 5 iid $\text{Uniform}(0, 1)$ (in hours from 9:00).

    **(b)** The expected value of the $k$-th order statistic of $n$ iid $\text{Uniform}(0, 1)$ is $k/(n+1)$:

    $$
    E[S_3 \mid N(1) = 5] = \frac{3}{6} = 0.5 \text{ hours}
    $$

    So the expected time is 9:30.

    **(c)** Given $N(1) = 5$, each arrival is independently $\text{Uniform}(0, 1)$. The probability that a single arrival falls in $[0, 2/3]$ (first 40 minutes) is $2/3$. So:

    $$
    P(\text{all 5 in first 40 min} \mid N(1) = 5) = \left(\frac{2}{3}\right)^5 = \frac{32}{243} \approx 0.1317
    $$

---

## Exercise 7: Combined Properties

Accidents occur on a highway as a Poisson process with rate $\lambda = 2$ per day. Each accident independently is either minor (probability 0.8) or major (probability 0.2).

**(a)** What is the expected number of major accidents in a 30-day month?

**(b)** Compute the probability of no major accidents in a week (7 days).

**(c)** Given that exactly 3 accidents occurred on a particular day, what is the probability that all 3 were minor?

**(d)** Given that exactly 3 accidents occurred on a particular day, what is the expected time of the first accident (in hours after midnight)?

??? solution "Solution"

    **(a)** Major accidents form $\text{PP}(0.2 \times 2) = \text{PP}(0.4)$ per day. In 30 days: $E = 0.4 \times 30 = 12$.

    **(b)** Major accidents in 7 days: $\text{Po}(0.4 \times 7) = \text{Po}(2.8)$.

    $$
    P(\text{no major in 7 days}) = e^{-2.8} \approx 0.0608
    $$

    **(c)** Given $N(1) = 3$ total accidents, each is independently minor with probability 0.8:

    $$
    P(\text{all 3 minor} \mid N(1) = 3) = 0.8^3 = 0.512
    $$

    **(d)** Given $N(1) = 3$ (measuring in days), the arrival times are order statistics of 3 iid $\text{Uniform}(0, 1)$. The expected first arrival is:

    $$
    E[S_1 \mid N(1) = 3] = \frac{1}{4} \text{ day} = 6 \text{ hours}
    $$

    So the expected time of the first accident is 6:00 am.

---

## Exercise 8: Poisson Process from Axioms

Let $\{N(t)\}$ be a counting process with $N(0) = 0$, independent increments, and stationary increments. Suppose $P(N(h) = 1) = \lambda h + o(h)$ and $P(N(h) \geq 2) = o(h)$.

**(a)** Show that $P_0(t) = P(N(t) = 0) = e^{-\lambda t}$ by deriving and solving a differential equation.

**(b)** Show that $P_1(t) = P(N(t) = 1) = \lambda t e^{-\lambda t}$ using the recursion $P_1'(t) = -\lambda P_1(t) + \lambda P_0(t)$.

**(c)** Verify that $P_0(t) + P_1(t) + P_2(t) + \cdots = 1$ for the Poisson PMF.

??? solution "Solution"

    **(a)** From $P_0(t+h) = P_0(t) \cdot P(N(h) = 0) = P_0(t)(1 - \lambda h + o(h))$:

    $$
    \frac{P_0(t+h) - P_0(t)}{h} = -\lambda P_0(t) + \frac{o(h)}{h}
    $$

    Taking $h \to 0$: $P_0'(t) = -\lambda P_0(t)$. With $P_0(0) = 1$, the solution is $P_0(t) = e^{-\lambda t}$.

    **(b)** The ODE is $P_1'(t) = -\lambda P_1(t) + \lambda e^{-\lambda t}$ with $P_1(0) = 0$. Using the integrating factor $e^{\lambda t}$:

    $$
    \frac{d}{dt}\bigl[e^{\lambda t} P_1(t)\bigr] = \lambda
    $$

    Integrating: $e^{\lambda t} P_1(t) = \lambda t + C$. With $P_1(0) = 0$, we get $C = 0$, so $P_1(t) = \lambda t e^{-\lambda t}$.

    **(c)** $\sum_{k=0}^{\infty} P_k(t) = \sum_{k=0}^{\infty} \frac{e^{-\lambda t}(\lambda t)^k}{k!} = e^{-\lambda t} \cdot e^{\lambda t} = 1$, using the Taylor series for $e^{\lambda t}$.

---

## Exercise 9: Simulation

**(a)** Write a Python simulation that generates a Poisson process with $\lambda = 5$ on $[0, 10]$ using the conditional uniform method: first draw $N \sim \text{Po}(50)$, then generate $N$ iid $\text{Uniform}(0, 10)$ values and sort them.

**(b)** Repeat using exponential interarrival times. Compare the two methods by plotting sample paths.

**(c)** Verify empirically that the count in $[0, 2]$ has mean $\approx 10$ and variance $\approx 10$ over 10,000 replications.

??? solution "Solution"

    ```python
    import numpy as np
    import matplotlib.pyplot as plt

    np.random.seed(42)
    lam = 5
    T = 10

    # (a) Conditional uniform method
    N = np.random.poisson(lam * T)
    arrivals_uniform = np.sort(np.random.uniform(0, T, N))

    # (b) Exponential interarrival method
    interarrivals = np.random.exponential(1 / lam, size=200)
    arrivals_exp = np.cumsum(interarrivals)
    arrivals_exp = arrivals_exp[arrivals_exp < T]

    fig, axes = plt.subplots(2, 1, figsize=(12, 4))
    axes[0].step(arrivals_uniform,
                 np.arange(1, len(arrivals_uniform) + 1),
                 where='post', label='Uniform method')
    axes[0].set_ylabel('N(t)')
    axes[0].legend()

    axes[1].step(arrivals_exp,
                 np.arange(1, len(arrivals_exp) + 1),
                 where='post', color='orange',
                 label='Exponential method')
    axes[1].set_xlabel('t')
    axes[1].set_ylabel('N(t)')
    axes[1].legend()
    plt.tight_layout()
    plt.show()

    # (c) Verify mean and variance
    n_rep = 10_000
    counts = np.random.poisson(lam * 2, n_rep)
    print(f"Mean of N(0,2): {counts.mean():.3f} (theory: 10)")
    print(f"Var of N(0,2):  {counts.var(ddof=1):.3f} (theory: 10)")
    ```
=======
# Exercises
>>>>>>> Stashed changes
