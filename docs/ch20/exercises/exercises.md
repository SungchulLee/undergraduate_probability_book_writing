# Chapter 20 Exercises

!!! warning "Exercise page"
    This page collects practice problems for Chapter 20 and does not follow the five-section structure used by concept pages.

Exercises on convergence modes, tail bounds, the weak and strong laws, and applications including Monte Carlo estimation.

## Section 20.1 — Convergence Modes

**Exercise 20.1.** Define convergence in probability, almost sure convergence, and convergence in distribution. State the implication hierarchy.

**Exercise 20.2.** Give an example of a sequence that converges in probability but not almost surely.

**Exercise 20.3.** Prove that $X_n \xrightarrow{d} c$ (constant) implies $X_n \xrightarrow{p} c$.

## Section 20.2 — Tail Bounds

**Exercise 20.4.** Let $X \sim \operatorname{Pois}(50)$. Bound $P(X \ge 75)$ using Markov, Chebyshev, one-sided Chebyshev, and Chernoff. Compare with the exact value.

**Exercise 20.5.** Prove Chebyshev's inequality from Markov's inequality.

**Exercise 20.6.** Show the optimal shift in the one-sided Chebyshev proof is $b = \sigma^2/\varepsilon$.

## Section 20.3 — Weak Law of Large Numbers

**Exercise 20.7.** Let $X_i$ be iid $\operatorname{Exp}(\lambda)$. Use the WLLN and Chebyshev to bound $P(\lvert \bar{X}_n - 1/\lambda \rvert > 0.1)$ for $n = 1000$.

**Exercise 20.8.** Show that $\frac{1}{n}\sum_{i=1}^n X_i^2 \xrightarrow{p} 1/3$ for iid $X_i \sim U(0,1)$.

## Section 20.4 — Strong Law of Large Numbers

**Exercise 20.9.** Explain the Borel-Cantelli argument for why a.s. convergence along the subsequence $n_k = k^2$ suffices.

**Exercise 20.10.** State Borel's theorem and explain its connection to the frequentist interpretation of probability.

## Section 20.5 — Applications

**Exercise 20.11.** Design a Monte Carlo simulation to estimate $\int_0^1 e^{-x^2} dx$. Compute a 95% confidence interval for your estimate using $n = 10{,}000$ samples.

**Exercise 20.12.** In the coupon collector problem with $n = 50$ types, compute $E[T_{50}]$ exactly and verify by simulation.

**Exercise 20.13.** Explain why the gambler's fallacy contradicts the independence assumption of the LLN.

**Exercise 20.14.** Implement Buffon's needle with $n = 10{,}000$ drops and estimate $\pi$. Repeat 500 times and report the mean and standard deviation of the estimates.
