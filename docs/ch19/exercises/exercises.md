# Exercises: Distributions Related to the Normal

!!! warning "Exercise page"
    These exercises cover the chi-squared, Student's $t$, and $F$ distributions, including their definitions, properties, and applications to sampling from normal populations.

## Chi-Squared Distribution

**Exercise 1.** Let $Z_1, Z_2, Z_3$ be iid $N(0,1)$. Find $E[Z_1^2 + Z_2^2 + Z_3^2]$ and $\operatorname{Var}(Z_1^2 + Z_2^2 + Z_3^2)$.

??? note "Solution"
    $Z_1^2 + Z_2^2 + Z_3^2 \sim \chi^2_3$, so $E = 3$ and $\operatorname{Var} = 2(3) = 6$.

**Exercise 2.** Let $X \sim N(0, \sigma^2)$. Derive the PDF of $Y = X^2$ using the CDF method.

??? note "Solution"
    For $y > 0$:

    $$
    P(Y \le y) = P(-\sqrt{y} \le X \le \sqrt{y}) = \Phi\!\left(\frac{\sqrt{y}}{\sigma}\right) - \Phi\!\left(\frac{-\sqrt{y}}{\sigma}\right)
    $$

    Differentiating:

    $$
    f_Y(y) = \frac{1}{\sigma\sqrt{2\pi y}}\, e^{-y/(2\sigma^2)}
    $$

    When $\sigma = 1$, this is the $\chi^2_1 = \operatorname{Gamma}(1/2, 1/2)$ PDF.

**Exercise 3.** If $V_1 \sim \chi^2_3$ and $V_2 \sim \chi^2_7$ are independent, find the distribution of $V_1 + V_2$.

??? note "Solution"
    $V_1 + V_2 \sim \chi^2_{10}$ by additivity.

**Exercise 4.** A random variable $W$ has MGF $\varphi_W(t) = (1 - 2t)^{-5}$. Identify the distribution.

??? note "Solution"
    $(1-2t)^{-5} = (1-2t)^{-d/2}$ with $d = 10$, so $W \sim \chi^2_{10}$.

## Sample Variance

**Exercise 5.** A sample of $n = 16$ is drawn from $N(\mu, 25)$. Find the distribution of $(n-1)S^2/\sigma^2$.

??? note "Solution"
    $(n-1)S^2/\sigma^2 = 15S^2/25 \sim \chi^2_{15}$, with mean 15 and variance 30.

**Exercise 6.** Let $X_1, \ldots, X_n$ be iid $N(\mu, \sigma^2)$. Show that $\operatorname{Cov}(\bar{X}, X_i - \bar{X}) = 0$ for all $i$.

??? note "Solution"
    $\operatorname{Cov}(\bar{X}, X_i - \bar{X}) = \operatorname{Cov}(\bar{X}, X_i) - \operatorname{Var}(\bar{X}) = \sigma^2/n - \sigma^2/n = 0$.

**Exercise 7.** A sample of $n = 10$ from $N(\mu, 25)$. Find $P(S^2 > 30)$.

??? note "Solution"
    $P(S^2 > 30) = P(\chi^2_9 > 9 \cdot 30/25) = P(\chi^2_9 > 10.8)$.

    ```python
    from scipy import stats
    print(f"{stats.chi2(9).sf(10.8):.4f}")  # 0.2897
    ```

## Student's t Distribution

**Exercise 8.** Let $Z \sim N(0,1)$ and $V \sim \chi^2_4$ be independent. Find the mean and variance of $T = Z/\sqrt{V/4}$.

??? note "Solution"
    $T \sim t_4$. Mean $= 0$ (since $d > 1$). Variance $= 4/(4-2) = 2$.

**Exercise 9.** A sample of $n = 9$ from $N(50, \sigma^2)$ yields $\bar{x} = 53$ and $s = 6$. Find $P(\bar{X} \ge 53)$ under $\mu = 50$.

??? note "Solution"
    $T = (53 - 50)/(6/3) = 1.5$, so $P(\bar{X} \ge 53) = P(t_8 \ge 1.5)$.

    ```python
    from scipy import stats
    print(f"{stats.t(8).sf(1.5):.4f}")  # 0.0856
    ```

**Exercise 10.** Show that $E[T]$ does not exist when $T \sim t_1$ (Cauchy distribution).

??? note "Solution"
    The PDF is $f(t) = 1/[\pi(1+t^2)]$. Then:

    $$
    E[|T|] = \frac{2}{\pi}\int_0^\infty \frac{t}{1+t^2}\,dt = \frac{1}{\pi}\bigl[\ln(1+t^2)\bigr]_0^\infty = \infty
    $$

    Since $E[|T|] = \infty$, the mean does not exist.

## F Distribution

**Exercise 11.** If $T \sim t_{15}$, find $P(T^2 > 4.54)$.

??? note "Solution"
    $T^2 \sim F_{1,15}$.

    ```python
    from scipy import stats
    print(f"{stats.f(1, 15).sf(4.54):.4f}")  # 0.0500
    ```

**Exercise 12.** If $F \sim F_{5,10}$, find $E[F]$ and verify the reciprocal property by simulation.

??? note "Solution"
    $E[F] = 10/8 = 1.25$.

    ```python
    import numpy as np
    from scipy import stats

    np.random.seed(42)
    f_samples = np.random.f(5, 10, 100_000)
    print(f"Mean of F(5,10): {f_samples.mean():.4f}  (theory: 1.25)")

    recip = 1.0 / f_samples
    stat, pval = stats.kstest(recip, 'f', args=(10, 5))
    print(f"KS test 1/F(5,10) ~ F(10,5): p={pval:.4f}")
    ```

## Decomposition and Identities

**Exercise 13.** Verify the identity $\sum(X_i - \mu)^2 = \sum(X_i - \bar{X})^2 + n(\bar{X} - \mu)^2$ by simulation.

??? note "Solution"
    ```python
    import numpy as np

    np.random.seed(42)
    mu, sigma, n = 5, 3, 20
    x = np.random.normal(mu, sigma, n)

    lhs = np.sum((x - mu)**2)
    rhs = np.sum((x - x.mean())**2) + n * (x.mean() - mu)**2
    print(f"LHS: {lhs:.6f}")
    print(f"RHS: {rhs:.6f}")
    print(f"Difference: {abs(lhs - rhs):.2e}")
    ```
