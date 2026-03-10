# CLT Proof via Moment Generating Functions


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

## Strategy

We prove the CLT by showing that the MGF of the standardized sum converges to the MGF of $N(0,1)$, then invoke the continuity theorem.

**Recall:** $M_{N(0,1)}(t) = e^{t^2/2}$

## Setup

Let $X_1, X_2, \ldots$ be iid with mean $\mu$ and variance $\sigma^2$. Define standardized variables:

$$Y_k = \frac{X_k - \mu}{\sigma}$$

Then $Y_k$ are iid with $E[Y_k] = 0$ and $E[Y_k^2] = 1$.

The standardized sum is:

$$Z_n = \frac{S_n - n\mu}{\sigma\sqrt{n}} = \sum_{k=1}^n \frac{Y_k}{\sqrt{n}}$$

## Proof

**Step 1.** Write the MGF of $Z_n$ using independence:

$$M_{Z_n}(t) = M_{\sum_{k=1}^n Y_k / \sqrt{n}}(t) = \left(E\left[e^{tY_1/\sqrt{n}}\right]\right)^n = \left(M_{Y_1}\left(\frac{t}{\sqrt{n}}\right)\right)^n$$

**Step 2.** Taylor expand the MGF of $Y_1$ around $0$:

$$M_{Y_1}(t) = E[e^{tY_1}] = E\left[1 + tY_1 + \frac{(tY_1)^2}{2!} + \cdots\right]$$

$$\approx 1 + t \cdot E[Y_1] + \frac{t^2}{2} \cdot E[Y_1^2] = 1 + 0 + \frac{t^2}{2} = 1 + \frac{t^2}{2}$$

**Step 3.** Substitute $t/\sqrt{n}$:

$$M_{Y_1}\left(\frac{t}{\sqrt{n}}\right) \approx 1 + \frac{t^2}{2n}$$

**Step 4.** Take the $n$-th power:

$$M_{Z_n}(t) = \left(M_{Y_1}\left(\frac{t}{\sqrt{n}}\right)\right)^n \approx \left(1 + \frac{t^2}{2n}\right)^n$$

**Step 5.** Take the limit using $\lim_{n\to\infty}\left(1 + \frac{a}{n}\right)^n = e^a$:

$$\lim_{n \to \infty} M_{Z_n}(t) = \lim_{n \to \infty} \left(1 + \frac{t^2}{2n}\right)^n = e^{t^2/2} = M_{N(0,1)}(t)$$

**Step 6.** By the continuity theorem for MGFs:

$$Z_n = \frac{S_n - n\mu}{\sigma\sqrt{n}} \xrightarrow{d} N(0,1) \qquad \blacksquare$$

## Key Ingredients

The proof relies on three facts:

1. **Independence** of the $X_i$ allows factoring the MGF: $M_{Z_n}(t) = \left(M_{Y_1}(t/\sqrt{n})\right)^n$
2. **Finite variance** ensures the Taylor expansion $M_{Y_1}(t) \approx 1 + t^2/2$ is valid
3. **Continuity theorem**: pointwise convergence of MGFs implies convergence in distribution

!!! note "Why Finite Variance Matters"
    The Taylor expansion requires $E[Y_1^2] = 1 < \infty$. If the variance is infinite (e.g., Cauchy distribution), the CLT does not apply and the standardized sum does not converge to a normal distribution.
