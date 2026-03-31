# Exercises: Law of Large Numbers

## Tail Bounds

<<<<<<< Updated upstream
**Exercise 20.1.** Let $X \sim \text{Po}(50)$. Use Markov's, Chebyshev's, one-sided Chebyshev's, and Chernoff's bounds to estimate $P(X \geq 75)$. Compare with the exact value and the CLT approximation.

**Exercise 20.2.** Prove that Chebyshev's inequality follows from Markov's inequality applied to the random variable $(X - \mu)^2$.

**Exercise 20.3.** Let $X$ have mean $\mu$ and variance $\sigma^2$. In the proof of the one-sided Chebyshev inequality, show that the optimal choice of $b$ in $E[(X - \mu + b)^2] \geq (\varepsilon + b)^2 P(X - \mu \geq \varepsilon)$ is $b = \sigma^2 / \varepsilon$.

**Exercise 20.4.** Let $X_1, \ldots, X_n$ be iid with mean $\mu$ and variance $\sigma^2$. Use the Chernoff bound to show that for all $t > 0$:

$$
P(\bar{X}_n - \mu \geq \varepsilon) \leq e^{-n\varepsilon t} \prod_{i=1}^n M_{X_i - \mu}(t)
$$

## Weak Law of Large Numbers

**Exercise 20.5.** Let $X_1, X_2, \ldots$ be iid $\text{Exp}(\lambda)$. Use the Weak Law of Large Numbers to show that $\bar{X}_n \xrightarrow{p} 1/\lambda$.

**Exercise 20.6.** Let $X_1, X_2, \ldots$ be iid $\text{Uniform}(0, 1)$. Show that $\frac{1}{n}\sum_{i=1}^n X_i^2 \xrightarrow{p} 1/3$.

*Hint: Apply the WLLN to $g(X_i) = X_i^2$.*

**Exercise 20.7.** Let $X_1, X_2, \ldots$ be independent (but not identically distributed) with $E[X_i] = \mu$ and $\text{Var}(X_i) \leq C$ for all $i$ and some constant $C$. Prove that the WLLN still holds: $\bar{X}_n \xrightarrow{p} \mu$.

## Strong Law and Convergence Modes

**Exercise 20.8.** Give an example of a sequence $X_n$ that converges in probability to 0 but does not converge almost surely to 0.

*Hint: Consider indicator functions on shrinking, cycling intervals on $[0,1]$ with the uniform distribution.*

**Exercise 20.9.** Let $X_n \xrightarrow{d} c$ where $c$ is a constant. Prove that $X_n \xrightarrow{p} c$.

*Hint: For any $\varepsilon > 0$, express $P(|X_n - c| > \varepsilon)$ in terms of $F_{X_n}$ and use the CDF convergence at the continuity points $c - \varepsilon$ and $c + \varepsilon$.*

**Exercise 20.10.** Explain why the CLT does **not** imply the WLLN, even though convergence in probability implies convergence in distribution. What is the logical distinction?

## Applications

**Exercise 20.11.** In the coupon collector problem with $n = 50$ coupon types, compute the exact expected value $E[T_{50}]$ and use Chebyshev's inequality to give an upper bound on $P(|T_{50} - E[T_{50}]| > 100)$.

**Exercise 20.12.** Design a Monte Carlo simulation to estimate $\theta = \int_0^1 e^{-x^2} \, dx$. Write $\theta = E[g(U)]$ for $U \sim U(0,1)$, compute the sample mean of $g(U_1), \ldots, g(U_n)$, and use the CLT to construct a 95% confidence interval for $\theta$ with $n = 10{,}000$.

**Exercise 20.13.** Explain why the Gambler's Fallacy is inconsistent with the Law of Large Numbers. Specifically, after observing 20 heads in a row from a fair coin, what does the LLN predict about the sample proportion after the next 1000 flips? Does the LLN say anything about the 21st flip?

## Conceptual

**Exercise 20.14.** In the coin-flipping illustration of WLLN vs SLLN, explain which plot (single trajectory converging vs histogram of many experiments concentrating) corresponds to which law and why.

**Exercise 20.15.** State whether each of the following is true or false, and justify briefly:

(a) Almost sure convergence implies convergence in probability.

(b) Convergence in distribution implies convergence in probability.

(c) If $X_n \xrightarrow{p} X$ and $Y_n \xrightarrow{p} Y$, then $X_n + Y_n \xrightarrow{p} X + Y$.

(d) If $X_n \xrightarrow{d} X$ and $Y_n \xrightarrow{d} Y$, then $X_n + Y_n \xrightarrow{d} X + Y$.
=======
**Exercise 1.** Let $X \sim \text{Poi}(50)$. Use Markov's, Chebyshev's, one-sided Chebyshev's, and Chernoff's bounds to estimate $P(X \geq 75)$. Compare with the CLT approximation.

**Exercise 2.** Prove that Chebyshev's inequality follows from Markov's inequality applied to the random variable $(X - \mu)^2$.

**Exercise 3.** Let $X$ have mean $\mu$ and variance $\sigma^2$. Show that the optimal choice of $b$ in the one-sided Chebyshev proof is $b = \sigma^2/\varepsilon$.

## Law of Large Numbers

**Exercise 4.** Let $X_1, X_2, \ldots$ be iid $\text{Exp}(\lambda)$. Use the Weak Law of Large Numbers to show that $\bar{X}_n \xrightarrow{p} 1/\lambda$.

**Exercise 5.** Let $X_1, X_2, \ldots$ be iid $\text{Uniform}(0, 1)$. Show that $\frac{1}{n}\sum_{i=1}^n X_i^2 \xrightarrow{p} 1/3$.

**Exercise 6.** In the coupon collector problem with $n = 50$ coupon types, approximately how many purchases are needed to collect all types? Compute the exact expected value $\mathbb{E}T_{50}$.

## Monte Carlo

**Exercise 7.** Design a Monte Carlo simulation to estimate $\int_0^1 e^{-x^2} dx$.

*Hint*: Write the integral as $\mathbb{E}[g(U)]$ where $U \sim \text{Uniform}(0,1)$.

**Exercise 8.** In the Monte Carlo estimation of $\pi$, if we use $n = 10{,}000$ darts, what is the approximate standard deviation of the estimate? Use the CLT.

**Exercise 9.** Implement Buffon's needle simulation in Python. Run $n = 10{,}000$ drops and estimate $\pi$. Repeat the experiment 500 times and plot a histogram of the estimates.

## Conceptual

**Exercise 10.** Explain why the Gambler's Fallacy is inconsistent with the Law of Large Numbers. Specifically, after observing 20 heads in a row from a fair coin, what does the LLN predict about the next 1000 flips?

**Exercise 11.** In the coin-flipping illustration of WLLN vs SLLN (see notes), explain which plot corresponds to which law and why.

**Exercise 12.** Give an example of a sequence that converges in probability but not almost surely.
>>>>>>> Stashed changes
