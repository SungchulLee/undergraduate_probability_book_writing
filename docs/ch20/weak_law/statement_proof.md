# Weak Law of Large Numbers: Statement and Proof


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

## Statement

Let $X_1, X_2, \ldots$ be **iid** random variables with PDF/PMF $f(x)$.

If $\mathbb{E}|X_i| < \infty$, then the sample mean converges in probability to the population mean:

$$
\frac{1}{N}\sum_{i=1}^N X_i \xrightarrow{p} \int x\, f(x)\, dx = \mu
$$

More generally, if $\mathbb{E}|g(X_i)| < \infty$, then

$$
\frac{1}{N}\sum_{i=1}^N g(X_i) \xrightarrow{p} \int g(x)\, f(x)\, dx = \mathbb{E}[g(X)]
$$

## Proof (Assuming Finite Second Moment)

Let $S_n = \sum_{i=1}^n X_i$ and assume $\mathbb{E}X_i^2 < \infty$, so $Var(X_i) = \sigma^2 < \infty$.

**Step 1: Compute the mean of $\bar{X}_n = S_n / n$.**

$$
\mathbb{E}\left[\frac{S_n}{n}\right] = \frac{1}{n}\sum_{i=1}^n \mathbb{E}X_i = \mu
$$

**Step 2: Compute the variance of $\bar{X}_n$.**

$$
Var\left(\frac{S_n}{n}\right) = \frac{1}{n^2}\sum_{i=1}^n Var(X_i) = \frac{\sigma^2}{n}
$$

**Step 3: Apply Chebyshev's inequality.**

$$
P\left(\left|\frac{S_n}{n} - \mu\right| > \varepsilon\right) \leq \frac{Var(S_n/n)}{\varepsilon^2} = \frac{\sigma^2/n}{\varepsilon^2} = \frac{\sigma^2}{n\varepsilon^2} \to 0 \quad \text{as } n \to \infty
$$

Therefore $\bar{X}_n \xrightarrow{p} \mu$. $\square$

!!! info "Remark"
    The proof above requires $\sigma^2 < \infty$ (finite second moment). The full WLLN only requires $\mathbb{E}|X_i| < \infty$ (finite first moment), but the proof is more involved and uses truncation arguments.

## Interpretation

The Weak Law says that for large $n$, the sample mean $\bar{X}_n$ is **unlikely** to be far from $\mu$. It does not guarantee that $\bar{X}_n$ stays close to $\mu$ for all sufficiently large $n$ — that is the statement of the Strong Law.
