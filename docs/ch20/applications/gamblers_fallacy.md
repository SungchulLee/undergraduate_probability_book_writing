# Gambler's Fallacy


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

## The Fallacy

The **gambler's fallacy** is the mistaken belief that if a random event has occurred more frequently than expected in the past, it is less likely to occur in the future (or vice versa), as if the process has a "memory" and needs to "balance out."

**Example**: After flipping 10 heads in a row, someone believes tails is "due." But if the coin is fair, $P(\text{heads}) = 0.5$ on the next flip regardless of history.

## What the LLN Actually Says

The Law of Large Numbers says:

$$
\frac{S_n}{n} \to \mu
$$

This convergence happens because **new observations dilute the effect of past deviations**, not because future outcomes compensate for past ones.

After 10 heads in a row ($S_{10} = 10$, so $\bar{X}_{10} = 1.0$), the LLN predicts convergence to 0.5 through dilution:

$$
\frac{S_{10} + S_{11:n}}{n} = \frac{10 + S_{11:n}}{n} \to 0.5
$$

The fixed "excess" of 10 becomes negligible as $n \to \infty$, but the **future** coins are still fair and independent.

## The Distinction

| | Gambler's Fallacy | LLN |
|---|---|---|
| Mechanism | Future compensates for past | New data dilutes past deviations |
| Independence | Violated (future depends on past) | Maintained (each trial is independent) |
| Prediction | Next flip more likely tails | Next flip is still 50-50 |
