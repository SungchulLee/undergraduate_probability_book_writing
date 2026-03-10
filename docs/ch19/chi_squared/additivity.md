# Additivity of Chi-Squared


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

## Statement

If $V_1 \sim \chi^2_{d_1}$ and $V_2 \sim \chi^2_{d_2}$ are **independent**, then:

$$V_1 + V_2 \sim \chi^2_{d_1 + d_2}$$

## Proof

This follows directly from the additivity of the Gamma distribution. Since $\chi^2_{d_i} \stackrel{d}{=} \Gamma(d_i/2, 1/2)$:

$$V_1 + V_2 \sim \Gamma\!\left(\frac{d_1}{2}, \frac{1}{2}\right) * \Gamma\!\left(\frac{d_2}{2}, \frac{1}{2}\right) = \Gamma\!\left(\frac{d_1 + d_2}{2}, \frac{1}{2}\right) \stackrel{d}{=} \chi^2_{d_1 + d_2}$$

### Proof via MGFs

Alternatively, using MGFs and independence:

$$\varphi_{V_1 + V_2}(t) = \varphi_{V_1}(t) \cdot \varphi_{V_2}(t) = (1 - 2t)^{-d_1/2} \cdot (1 - 2t)^{-d_2/2} = (1 - 2t)^{-(d_1 + d_2)/2}$$

which is the MGF of $\chi^2_{d_1 + d_2}$. By the uniqueness theorem, $V_1 + V_2 \sim \chi^2_{d_1 + d_2}$.

## General Case

For independent $V_i \sim \chi^2_{d_i}$, $i = 1, \ldots, k$:

$$\sum_{i=1}^k V_i \sim \chi^2_{d_1 + d_2 + \cdots + d_k}$$

This is consistent with the definition: if $V_i = \sum_{j=1}^{d_i} Z_{ij}^2$ where all $Z_{ij}$ are iid $N(0,1)$, then $\sum_i V_i$ is a sum of $d_1 + \cdots + d_k$ independent squared standard normals.

## Application: Cochran's Decomposition

A key application of additivity (used in reverse) appears in the decomposition:

$$\sum_{i=1}^n \left(\frac{X_i - \mu}{\sigma}\right)^2 = \sum_{i=1}^n \left(\frac{X_i - \bar{X}}{\sigma}\right)^2 + \left(\frac{\bar{X} - \mu}{\sigma/\sqrt{n}}\right)^2$$

$$\chi^2_n = \chi^2_{n-1} + \chi^2_1$$

The left side is a sum of $n$ independent squared standard normals. The last term is $\chi^2_1$. If we can show independence between the two right-hand terms, then by the MGF factorization, the first term must be $\chi^2_{n-1}$.
