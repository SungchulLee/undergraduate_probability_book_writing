# Chapter 11 Exercises

!!! warning "Exercise page"
    This page collects practice problems for Chapter 11 and does not follow the five-section structure used by concept pages.

Exercises on moment generating functions, characteristic functions, probability generating functions, and their applications.

## Section 11.1 — MGF Basics

**Exercise 11.1.** Find the MGF of $X \sim \text{Uniform}(0, 1)$ and use it to compute $E[X]$ and $\text{Var}(X)$.

**Exercise 11.2.** If $M_X(t) = e^{3t + 8t^2}$, identify the distribution of $X$.

**Exercise 11.3.** Compute the MGF of $X \sim \text{Geo}(p)$ and verify $E[X] = 1/p$ by differentiation.

## Section 11.2 — MGF Examples

**Exercise 11.4.** Use MGFs to prove that $\text{Pois}(\lambda_1) + \text{Pois}(\lambda_2) \sim \text{Pois}(\lambda_1 + \lambda_2)$ for independent summands.

**Exercise 11.5.** Show that $\text{Gamma}(3, 2) + \text{Gamma}(5, 2) \sim \text{Gamma}(8, 2)$ using MGFs.

**Exercise 11.6.** Use the normal MGF to show that if $X \sim N(\mu, \sigma^2)$, then $(X - \mu)/\sigma \sim N(0, 1)$.

## Section 11.3 — MGF Techniques

**Exercise 11.7.** Let $X_1, \ldots, X_n \stackrel{\text{iid}}{\sim} \text{Exp}(\lambda)$. Find the distribution of $\bar{X} = \sum X_i / n$ using MGFs.

**Exercise 11.8.** Prove the Poisson limit theorem using MGFs: show that the MGF of $\text{Bin}(n, \lambda/n)$ converges to $e^{\lambda(e^t - 1)}$.

## Section 11.4 — Characteristic Functions

**Exercise 11.9.** Find the CF of $X \sim \text{Exp}(\lambda)$ and verify $\varphi_X(t) = \lambda/(\lambda - it)$.

**Exercise 11.10.** Explain why the Cauchy distribution has a CF but no MGF.

**Exercise 11.11.** Outline the CLT proof using characteristic functions for iid $X_i$ with mean 0 and variance 1.

## Section 11.5 — Probability Generating Functions

**Exercise 11.12.** Find the PGF of $X \sim \text{Bin}(n, p)$ and use it to compute $E[X(X-1)]$.

**Exercise 11.13.** If $N \sim \text{Pois}(5)$ and $X_i \sim \text{Bern}(0.3)$ are iid, independent of $N$, find $E[S]$ and $\text{Var}(S)$ where $S = \sum_{i=1}^N X_i$. Identify the distribution of $S$.

**Exercise 11.14.** Show that the compound Poisson with $N \sim \text{Pois}(\lambda)$ and $X_i \sim \text{Bern}(p)$ gives $S \sim \text{Pois}(\lambda p)$.
