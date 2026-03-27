# Gambler's Fallacy

## The Fallacy

The **gambler's fallacy** is the mistaken belief that if a random event has occurred more frequently than expected in the past, it is less likely to occur in the future (or vice versa), as if the process has a "memory" and needs to "balance out."

**Example.** After flipping 10 heads in a row, someone believes tails is "due." But if the coin is fair, $P(\text{heads}) = 0.5$ on the next flip regardless of history. The coin has no memory.

## What the LLN Actually Says

The Law of Large Numbers states that

$$
\bar{X}_n = \frac{S_n}{n} \xrightarrow{a.s.} \mu
$$

This convergence happens because **new observations dilute the effect of past deviations**, not because future outcomes compensate for past ones.

After 10 heads in a row ($S_{10} = 10$, so $\bar{X}_{10} = 1.0$), the SLLN predicts convergence to 0.5 through dilution:

$$
\frac{S_{10} + S_{11:n}}{n} = \frac{10 + S_{11:n}}{n} \xrightarrow{a.s.} 0.5
$$

where $S_{11:n} = X_{11} + \cdots + X_n$ is the sum of **future** flips. The fixed excess of 10 becomes negligible as $n \to \infty$, but the future coins are still fair and independent.

??? example "A Concrete Calculation"
    After 10 heads in a row, the sample mean is $\bar{X}_{10} = 1.0$. After $n = 1{,}000$ additional fair flips, we expect about 500 heads and 500 tails among the new flips. The total is then approximately $510$ heads in $1{,}010$ flips, giving $\bar{X}_{1010} \approx 0.505$. After $n = 100{,}000$ additional flips, $\bar{X}_{100{,}010} \approx 0.50005$. The initial excess is swamped, with no compensation required.

## The Distinction

| | Gambler's Fallacy | Law of Large Numbers |
|---|---|---|
| Mechanism | Future compensates for past | New data dilutes past deviations |
| Independence | Falsely assumes dependence | Each trial is independent |
| Prediction | Next flip more likely tails | Next flip is still 50-50 |

!!! warning "The Fallacy in Both Directions"
    The gambler's fallacy works in reverse too. After a run of losses, a gambler may believe a win is "due," and after a run of wins, they may believe they are on a "hot streak." Both beliefs are incorrect for independent trials: past outcomes carry no information about future ones.

## Connection to the iid Assumption

The mathematical root of the fallacy lies in confusing two statements:

1. **True**: $\bar{X}_n \to \mu$ as $n \to \infty$ (the LLN)
2. **False**: Future outcomes adjust to correct past deviations

Statement 1 holds because the ratio $S_n / n$ has the excess in the numerator but $n$ grows in the denominator. Statement 2 would require the future $X_i$ to depend on the past, violating the iid assumption.
