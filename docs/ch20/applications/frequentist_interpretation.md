# Frequentist Interpretation of Probability

## The Connection

The Law of Large Numbers provides the mathematical foundation for the **frequentist interpretation** of probability. If we repeat an experiment independently many times, the relative frequency of an event $A$ converges to its probability:

$$
\frac{\text{number of times } A \text{ occurs in } n \text{ trials}}{n} \xrightarrow{a.s.} P(A) \quad \text{as } n \to \infty
$$

This follows directly from the Strong Law of Large Numbers applied to the indicator variables $\mathbf{1}_A$:

$$
\frac{1}{n}\sum_{i=1}^n \mathbf{1}_{A_i} \xrightarrow{a.s.} \mathbb{E}[\mathbf{1}_A] = P(A)
$$

## Interpretation

Under the frequentist view, saying "the probability of heads is 0.5" means that if you flip the coin many times, the fraction of heads will converge to 0.5. Probability is defined as the long-run relative frequency.

The LLN makes this precise: it is not merely an empirical observation but a mathematical theorem.

## Limitations

The frequentist interpretation requires the notion of **repeatable experiments**. For one-time events (e.g., "the probability of rain tomorrow" or "the probability that a particular defendant is guilty"), the frequentist framework is less natural. This is one motivation for the **Bayesian** interpretation of probability.
