# CLT vs LLN — Complementary Perspectives

## Two Fundamental Theorems

The Central Limit Theorem and the Law of Large Numbers both describe the behavior of the sample mean $\bar{X}_n = \frac{1}{n}\sum_{i=1}^n X_i$ as $n \to \infty$, but they answer **different questions**.

| | LLN | CLT |
|---|---|---|
| **Question** | Where does $\bar{X}_n$ go? | How does $\bar{X}_n$ fluctuate around the limit? |
| **Statement** | $\bar{X}_n \to \mu$ | $\sqrt{n}(\bar{X}_n - \mu)/\sigma \xrightarrow{d} N(0,1)$ |
| **Scale** | $\bar{X}_n - \mu \to 0$ | $\bar{X}_n - \mu \approx \sigma/\sqrt{n} \cdot Z$ |
| **Information** | The limit | The rate and shape of convergence |

## Connecting the Two

The CLT tells us that $\bar{X}_n$ fluctuates around $\mu$ on the scale $\sigma/\sqrt{n}$:

$$
\bar{X}_n \approx \mu + \frac{\sigma}{\sqrt{n}} Z, \quad Z \sim N(0,1)
$$

The LLN tells us that $\sigma/\sqrt{n} \to 0$, so $\bar{X}_n \to \mu$.

## When $\sigma$ is Known vs Unknown

**If we know $\sigma$:**

$$
\frac{\bar{X}_n - \mu}{\sigma/\sqrt{n}} \begin{cases} \overset{d}{=} N(0,1) & \text{if } X_i \text{ are iid } N(\mu, \sigma^2) \text{ (exact)} \\ \approx N(0,1) & \text{if } X_i \text{ are iid with } \mathbb{E}X_i^2 < \infty \text{ (by CLT)} \end{cases}
$$

**If we don't know $\sigma$**, replace it with the sample standard deviation $S$:

$$
\frac{\bar{X}_n - \mu}{S/\sqrt{n}} \begin{cases} \overset{d}{=} t_{n-1} & \text{if } X_i \text{ are iid } N(\mu, \sigma^2) \text{ (exact)} \\ \approx N(0,1) & \text{if } X_i \text{ are iid with } \mathbb{E}X_i^2 < \infty \text{ (by CLT and LLN)} \end{cases}
$$

The LLN justifies replacing $\sigma$ with $S$, since $S^2 \xrightarrow{a.s.} \sigma^2$ by the Strong Law applied to $g(X) = (X - \mu)^2$.

## Summary

The LLN and CLT work together: the LLN tells us the sample mean converges to the population mean, while the CLT characterizes the Gaussian fluctuations around that limit. Together, they form the foundation for statistical inference, confidence intervals, and hypothesis testing.
