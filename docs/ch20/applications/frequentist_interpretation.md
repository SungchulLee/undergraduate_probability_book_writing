# Frequentist Interpretation of Probability

## From the LLN to Long-Run Frequency

The Law of Large Numbers provides the mathematical foundation for the **frequentist interpretation** of probability. If we repeat an experiment independently many times, the relative frequency of an event converges to its probability.

Let $\mathbf{1}_{A,i}$ denote the indicator of the event $A$ occurring on the $i$-th independent trial. Since each $\mathbf{1}_{A,i}$ is Bernoulli with parameter $P(A)$, the Strong Law of Large Numbers gives:

$$
\frac{1}{n}\sum_{i=1}^n \mathbf{1}_{A,i} \xrightarrow{a.s.} E[\mathbf{1}_{A}] = P(A)
$$

The left side is the **relative frequency** of $A$ in $n$ trials. The SLLN guarantees that this ratio converges to $P(A)$ with probability 1.

The Weak Law gives the weaker but still useful statement:

$$
\frac{1}{n}\sum_{i=1}^n \mathbf{1}_{A,i} \xrightarrow{p} P(A)
$$

## Interpretation

Under the frequentist view, saying "the probability of heads is 0.5" means that if you flip the coin many, many times, the fraction of heads will converge to 0.5. Probability is **defined** as the long-run relative frequency.

The LLN makes this precise: it is not merely an empirical observation but a mathematical theorem.

??? example "Concrete Example"
    Suppose we roll a fair die $n$ times and count the number of sixes. The relative frequency of sixes satisfies

    $$\frac{\text{number of sixes}}{n} \xrightarrow{a.s.} \frac{1}{6} \approx 0.1667$$

    After $n = 600$ rolls, the CLT tells us the relative frequency is approximately $N(1/6, \; 5/(36 \cdot 600))$, so it will typically be within about $\pm 0.015$ of $1/6$.

## Rate of Convergence

The CLT refines the frequentist picture by describing **how fast** the relative frequency converges. Since $\text{Var}(\mathbf{1}_A) = P(A)(1 - P(A))$:

$$
\frac{\hat{p}_n - P(A)}{\sqrt{P(A)(1-P(A))/n}} \xrightarrow{d} N(0,1)
$$

where $\hat{p}_n = \frac{1}{n}\sum_{i=1}^n \mathbf{1}_{A,i}$. The fluctuations around $P(A)$ are of order $1/\sqrt{n}$.

## Limitations

The frequentist interpretation requires the notion of **repeatable experiments**. For one-time events -- such as "the probability of rain tomorrow" or "the probability that a particular defendant is guilty" -- the frequentist framework is less natural, because there is no sequence of identical, independent trials to appeal to.

!!! note "Bayesian Alternative"
    This limitation is one motivation for the **Bayesian** interpretation, which treats probability as a measure of belief or uncertainty rather than long-run frequency. In the Bayesian view, $P(A) = 0.7$ means the observer assigns 70% credence to $A$, without requiring repeated trials.
