# Uniqueness Theorem
<<<<<<< Updated upstream

## Statement

!!! info "MGF Uniqueness Theorem"
    If $M_X(t)$ exists (is finite) for all $t$ in some open interval $(-\delta, \delta)$ containing $0$, then $M_X(t)$ uniquely determines the distribution of $X$.

    That is, if $M_X(t) = M_Y(t)$ for all $t \in (-\delta, \delta)$, then $X$ and $Y$ have the same CDF.

This is the property that makes MGFs a powerful identification tool: once you compute the MGF of a sum or transformation and recognize it as the MGF of a known distribution, you can conclude the two distributions are identical.

## Why a Neighborhood of Zero Suffices

The MGF is an analytic function wherever it is finite. If two analytic functions agree on any open interval, they agree everywhere on their common domain. Therefore, agreement on $(-\delta, \delta)$, no matter how small $\delta$ is, forces agreement wherever both MGFs are defined.

## When the MGF Does Not Exist

Not every distribution has an MGF. The expectation $E[e^{tX}]$ may diverge for all $t \neq 0$.

???+ example "Cauchy distribution"
    If $X$ has the standard Cauchy distribution with PDF $f(x) = \frac{1}{\pi(1 + x^2)}$, then $E[e^{tX}] = \infty$ for every $t \neq 0$. The Cauchy distribution has no MGF.

    The heavy tails of the Cauchy make $e^{tX}$ grow too fast for the integral to converge.

???+ example "Log-normal distribution"
    If $X \sim \text{Lognormal}(\mu, \sigma^2)$, then $M_X(t) = \infty$ for all $t > 0$. The MGF exists only at $t \leq 0$, so it is not finite on any open interval around $0$.

When the MGF does not exist, alternative tools such as the **characteristic function** $\varphi_X(t) = E[e^{itX}]$ (which always exists) can be used instead.

## Connection to the Moment Problem

Two distinct distributions can share all moments $E[X^n]$ for $n = 1, 2, 3, \ldots$ without being identical. This is the **Hamburger moment problem**.

!!! warning "Moments Alone Do Not Determine a Distribution"
    There exist pairs of distinct distributions that have the same moments of all orders. The classic example is the log-normal: the distribution of $X \sim \text{Lognormal}(0, 1)$ is not uniquely determined by its moments.

The MGF, when it exists, resolves this ambiguity. Existence of $M_X(t)$ in a neighborhood of $0$ implies that the moment sequence $\{E[X^n]\}$ grows slowly enough to uniquely determine the distribution. Specifically, the Taylor series $\sum E[X^n]\,t^n / n!$ converges, and this convergent generating function pins down the distribution.

## Convergence Theorem

The uniqueness theorem has a companion result for sequences of random variables.

!!! info "MGF Convergence Theorem"
    If $M_{X_n}(t) \to M_X(t)$ for all $t$ in a neighborhood of $0$, and $M_X(t)$ is the MGF of a random variable $X$ (finite in that neighborhood), then:

    $$X_n \xrightarrow{d} X$$

This theorem is the MGF route to proving the **Central Limit Theorem**: show that the MGF of the standardized sum converges pointwise to $e^{t^2/2}$, the MGF of $N(0, 1)$.

## Summary of Applicability

| Tool | Exists for | Uniqueness |
|:---|:---|:---|
| MGF $M_X(t) = E[e^{tX}]$ | Some distributions | Yes, when it exists in a neighborhood of $0$ |
| CF $\varphi_X(t) = E[e^{itX}]$ | All distributions | Always |

When the MGF exists, it is often the more convenient tool because it avoids complex arithmetic. When it does not exist, the characteristic function is the universal alternative.
=======
>>>>>>> Stashed changes
