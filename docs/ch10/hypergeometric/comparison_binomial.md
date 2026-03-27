# Comparison with Binomial

## The Core Question

The Binomial models sampling **with** replacement; the Hypergeometric models sampling **without** replacement. When the population is large relative to the sample, removing a few items barely changes the population composition, so the two distributions should be nearly identical. This page makes that intuition precise.

## Side-by-Side Summary

|  | Binomial $\text{Bin}(n, p)$ | Hypergeometric $\text{HGeom}(N, K, n)$ |
|:---|:---:|:---:|
| Sampling | With replacement | Without replacement |
| Independence | Draws are independent | Draws are dependent |
| Mean | $np$ | $n \cdot K/N$ |
| Variance | $npq$ | $npq \cdot \dfrac{N-n}{N-1}$ |
| Parameter link | $p = K/N$ | $p = K/N$ |

With $p = K/N$ and $q = 1 - p$, the means are **identical**. The variances differ only by the finite population correction factor.

---

## Finite Population Correction

!!! info "Finite Population Correction"
    The ratio of the Hypergeometric variance to the Binomial variance is

    $$\frac{\text{Var}_{\text{HGeom}}}{\text{Var}_{\text{Bin}}} = \frac{N - n}{N - 1}$$

    This factor is always $\le 1$. Sampling without replacement reduces variability because the draws are negatively correlated.

When $n = 1$, the correction factor is $\frac{N-1}{N-1} = 1$ and both distributions agree exactly. When $n = N$, the correction is $0$: you draw the entire population, so there is no randomness left.

**Rule of thumb.** When the sampling fraction $n/N$ is less than 5%, the finite population correction is at least $0.95$, and the Binomial approximation is excellent.

---

## Formal Limit

Fix $n$ and $k$, and let $N, K \to \infty$ with $K/N \to p$. Then each Hypergeometric probability converges to the corresponding Binomial probability:

$$
\frac{\binom{K}{k}\binom{N-K}{n-k}}{\binom{N}{n}} \to \binom{n}{k} p^k (1-p)^{n-k}
$$

??? note "Proof Sketch"
    Write $\binom{K}{k} = \frac{K!}{k!(K-k)!} = \frac{K(K-1)\cdots(K-k+1)}{k!}$ and similarly for the other terms. Then

    $$\frac{\binom{K}{k}\binom{N-K}{n-k}}{\binom{N}{n}} = \binom{n}{k} \cdot \frac{K(K-1)\cdots(K-k+1)}{N(N-1)\cdots(N-k+1)} \cdot \frac{(N-K)(N-K-1)\cdots(N-K-n+k+1)}{(N-k)(N-k-1)\cdots(N-n+1)}$$

    As $N \to \infty$ with $K/N \to p$, the first ratio converges to $p^k$ and the second to $(1-p)^{n-k}$.

---

## Numerical Comparison

Consider $N = 1000$, $K = 200$ (so $p = 0.2$), and draw $n = 10$ items.

| $k$ | $P_{\text{HGeom}}$ | $P_{\text{Bin}}$ | Relative error |
|:---:|:---:|:---:|:---:|
| 0 | 0.1044 | 0.1074 | 2.8% |
| 1 | 0.2687 | 0.2684 | 0.1% |
| 2 | 0.3032 | 0.3020 | 0.4% |
| 3 | 0.1969 | 0.2013 | 2.2% |
| 4 | 0.0831 | 0.0881 | 5.7% |

The probabilities are very close. With $n/N = 0.01$, the Binomial is an excellent approximation.

---

## When to Use Which

- **Use Hypergeometric** when sampling without replacement from a finite, known population (e.g., quality inspection of a batch, card games, committee selection).
- **Use Binomial** when sampling with replacement, or when the population is so large that the sampling fraction $n/N$ is negligible.
- **Practical guideline**: if $n/N < 0.05$, use the Binomial for simplicity. If $n/N \ge 0.05$, the Hypergeometric is more accurate.
