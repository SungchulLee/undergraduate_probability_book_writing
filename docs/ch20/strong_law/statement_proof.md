# Strong Law of Large Numbers: Statement and Proof


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

## Statement

Let $X_1, X_2, \ldots$ be **iid** random variables with PDF/PMF $f(x)$.

If $\mathbb{E}|X_i| < \infty$, then the sample mean converges **almost surely** to the population mean:

$$
\frac{1}{N}\sum_{i=1}^N X_i \xrightarrow{a.s.} \int x\, f(x)\, dx = \mu
$$

More generally, if $\mathbb{E}|g(X_i)| < \infty$, then

$$
\frac{1}{N}\sum_{i=1}^N g(X_i) \xrightarrow{a.s.} \int g(x)\, f(x)\, dx = \mathbb{E}[g(X)]
$$

## Proof Sketch (Assuming Finite Fourth Moment)

Assume $\mathbb{E}X_i^4 < \infty$. Let $S_n = \sum_{i=1}^n X_i$.

**Step 1**: Show the fourth moment sum converges.

$$
\sum_{n=1}^{\infty} \mathbb{E}\left(\frac{S_n - n\mu}{n}\right)^4 \leq C\sum_{n=1}^{\infty} n^{-2} < \infty
$$

The key computation uses the fact that most cross-terms in expanding $(S_n - n\mu)^4$ vanish by independence, leaving only $O(n^2)$ terms, so $\mathbb{E}(S_n - n\mu)^4 = O(n^2)$.

**Step 2**: Since the sum of expectations is finite, the sum itself is finite almost surely:

$$
\sum_{n=1}^{\infty} \left(\frac{S_n - n\mu}{n}\right)^4 < \infty \quad \text{a.s.}
$$

**Step 3**: If a series of nonnegative terms converges, the terms must go to 0:

$$
\left(\frac{S_n - n\mu}{n}\right)^4 \to 0 \quad \text{a.s.}
$$

**Step 4**: Taking fourth roots:

$$
\frac{S_n}{n} \to \mu \quad \text{a.s.}
$$

$\square$

!!! info "Remark"
    The full SLLN (Kolmogorov's version) requires only $\mathbb{E}|X_i| < \infty$. The proof with finite fourth moment is more accessible and illustrates the main strategy: use summability of moments to establish almost sure convergence.

## WLLN vs SLLN

| Property | Weak Law | Strong Law |
|----------|----------|------------|
| Convergence mode | In probability | Almost surely |
| Assumption (simple proof) | $\sigma^2 < \infty$ | $\mathbb{E}X^4 < \infty$ |
| Assumption (general) | $\mathbb{E}\|X\| < \infty$ | $\mathbb{E}\|X\| < \infty$ |
| Proof technique | Chebyshev inequality | Fourth moment + series convergence |
| Conclusion | $P(\|\bar{X}_n - \mu\| > \varepsilon) \to 0$ | $P(\bar{X}_n \to \mu) = 1$ |
