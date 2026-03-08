# Exercises: Law of Large Numbers

## Tail Bounds

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

**Exercise 11.** In the coin-flipping illustration of WLLN vs SLLN (see the SLLN intuition section), explain which plot corresponds to which law and why.

**Exercise 12.** Give an example of a sequence that converges in probability but not almost surely.
