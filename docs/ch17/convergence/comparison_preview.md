# Convergence in Distribution vs Other Modes (Preview)


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

## Overview of Convergence Modes

There are several notions of convergence for sequences of random variables, listed here from **strongest to weakest**:

| Mode | Notation | Intuitive Meaning |
|------|----------|-------------------|
| Almost Sure | $X_n \xrightarrow{a.s.} X$ | Sample paths converge for almost every $\omega$ |
| In Probability | $X_n \xrightarrow{p} X$ | Probability of large deviations vanishes |
| In Distribution | $X_n \xrightarrow{d} X$ | CDFs converge pointwise |

## Implications

$$X_n \xrightarrow{a.s.} X \implies X_n \xrightarrow{p} X \implies X_n \xrightarrow{d} X$$

The reverse implications are **not** true in general.

!!! warning "Special Case"
    If $X_n \xrightarrow{d} c$ where $c$ is a **constant**, then $X_n \xrightarrow{p} c$ as well. Convergence in distribution to a constant is equivalent to convergence in probability to that constant.

## Why This Matters for the CLT

The CLT is a statement about **convergence in distribution**:

$$\frac{S_n - n\mu}{\sigma\sqrt{n}} \xrightarrow{d} N(0,1)$$

It tells us the **shape** of the distribution of the standardized sum approaches the standard normal, but it does not say anything about the sample-path behavior.

The **Law of Large Numbers** (Ch 20) makes the stronger statement of convergence in probability (WLLN) or almost sure convergence (SLLN) for the sample mean $\bar{X}_n \xrightarrow{p} \mu$.

!!! note "Full Treatment"
    The detailed comparison of convergence modes, including proofs of the implication hierarchy, is presented in **Chapter 20: Law of Large Numbers**.
