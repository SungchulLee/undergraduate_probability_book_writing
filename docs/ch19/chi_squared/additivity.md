# Additivity of Chi-Squared

## Motivation

The chi-squared distribution arises as a sum of squared standard normals. A natural question is: what happens when we add two independent chi-squared random variables? Additivity -- the fact that degrees of freedom simply add -- is the key property that makes Cochran's decomposition and analysis of variance work.

## Statement

!!! info "Additivity"
    If $V_1 \sim \chi^2_{d_1}$ and $V_2 \sim \chi^2_{d_2}$ are **independent**, then

    $$V_1 + V_2 \sim \chi^2_{d_1 + d_2}$$

## Proof via Gamma Additivity

Since $\chi^2_{d} \sim \Gamma(d/2, 1/2)$, and independent Gamma random variables with the **same rate** are additive:

$$
V_1 + V_2 \sim \Gamma\!\left(\frac{d_1}{2}, \frac{1}{2}\right) + \Gamma\!\left(\frac{d_2}{2}, \frac{1}{2}\right) = \Gamma\!\left(\frac{d_1 + d_2}{2}, \frac{1}{2}\right) \sim \chi^2_{d_1 + d_2}
$$

where the addition denotes convolution of independent random variables (Chapter 16).

## Proof via MGFs

By independence, $M_{V_1+V_2}(t) = M_{V_1}(t) \cdot M_{V_2}(t)$. Using the chi-squared MGF:

$$
M_{V_1+V_2}(t) = (1-2t)^{-d_1/2} \cdot (1-2t)^{-d_2/2} = (1-2t)^{-(d_1+d_2)/2}
$$

This is the MGF of $\chi^2_{d_1+d_2}$. By the uniqueness theorem, $V_1 + V_2 \sim \chi^2_{d_1+d_2}$.

## General Case

For mutually independent $V_i \sim \chi^2_{d_i}$, $i = 1, \ldots, k$:

$$
\sum_{i=1}^k V_i \sim \chi^2_{d_1 + d_2 + \cdots + d_k}
$$

This is consistent with the definition: each $V_i$ is a sum of $d_i$ independent squared standard normals, so the total is a sum of $d_1 + \cdots + d_k$ independent squared standard normals.

??? example "Numerical Example"
    Let $V_1 \sim \chi^2_3$ and $V_2 \sim \chi^2_7$ be independent. Then $V_1 + V_2 \sim \chi^2_{10}$.

    - $E[V_1 + V_2] = 3 + 7 = 10$
    - $\text{Var}(V_1 + V_2) = 2(3) + 2(7) = 20$

    These match the chi-squared formulas: $E[\chi^2_d] = d$ and $\text{Var}(\chi^2_d) = 2d$.

## Application: Cochran's Decomposition

A key application uses additivity **in reverse**. For $X_1, \ldots, X_n$ iid $N(\mu, \sigma^2)$:

$$
\underbrace{\sum_{i=1}^n \left(\frac{X_i - \mu}{\sigma}\right)^2}_{\chi^2_n} = \underbrace{\sum_{i=1}^n \left(\frac{X_i - \bar{X}}{\sigma}\right)^2}_{?} + \underbrace{\left(\frac{\bar{X} - \mu}{\sigma/\sqrt{n}}\right)^2}_{\chi^2_1}
$$

The left side has $n$ degrees of freedom and the last term has 1. If the two right-hand terms are independent, then by the MGF factorization, the first term must be $\chi^2_{n-1}$. This is proved in the section on the distribution of the sample variance.

!!! warning "Independence Is Essential"
    Additivity requires independence. If $V_1$ and $V_2$ are dependent chi-squared random variables, then $V_1 + V_2$ is generally **not** chi-squared.
