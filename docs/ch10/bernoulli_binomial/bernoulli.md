# Bernoulli Distribution

## Motivation

Many real-world experiments have exactly two outcomes: a coin lands heads or tails, a manufactured part is defective or not, a patient recovers or does not. The **Bernoulli distribution** is the simplest probability model for such binary experiments. It serves as the building block for the Binomial, Geometric, and Negative Binomial distributions studied in the rest of this chapter.

## Definition

A random variable $X$ has a **Bernoulli distribution** with parameter $p \in [0, 1]$, written $X \sim \text{Bernoulli}(p)$, if it takes only two values:

$$
P(X = 1) = p, \qquad P(X = 0) = 1 - p = q
$$

We call $X = 1$ a **success** and $X = 0$ a **failure**. The notation $q = 1 - p$ is used throughout this chapter.

!!! info "Bernoulli PMF"
    The PMF can be written in a single expression:

    $$P(X = k) = p^k (1-p)^{1-k}, \quad k \in \{0, 1\}$$

---

## Mean and Variance

**Mean.** Since $X$ takes only two values:

$$
E[X] = 0 \cdot q + 1 \cdot p = p
$$

**Second moment.** Because $X$ only takes the values 0 and 1, we have $X^2 = X$, so $E[X^2] = p$.

**Variance.** Applying the shortcut formula:

$$
\text{Var}(X) = E[X^2] - (E[X])^2 = p - p^2 = p(1 - p) = pq
$$

The variance is maximized at $p = 1/2$, where $\text{Var}(X) = 1/4$, and equals zero at the extremes $p = 0$ or $p = 1$.

---

## Connection to Indicator Variables

A Bernoulli random variable is precisely an **indicator variable**. If $A$ is an event, then

$$
I_A = \begin{cases} 1 & \text{if } A \text{ occurs} \\ 0 & \text{if } A \text{ does not occur} \end{cases}
$$

satisfies $I_A \sim \text{Bernoulli}(P(A))$. This connection is fundamental: any time we count how many events occur out of a collection, we are summing Bernoulli random variables.

---

## CDF

The cumulative distribution function is a step function:

$$
F(x) = \begin{cases} 0 & x < 0 \\ q & 0 \le x < 1 \\ 1 & x \ge 1 \end{cases}
$$

---

## Examples

**Coin flip.** Toss a fair coin and let $X = 1$ for heads. Then $X \sim \text{Bernoulli}(1/2)$ with $E[X] = 1/2$ and $\text{Var}(X) = 1/4$.

**Quality control.** A factory produces items with a 3% defect rate. Let $X = 1$ if a randomly selected item is defective. Then $X \sim \text{Bernoulli}(0.03)$ with $E[X] = 0.03$ and $\text{Var}(X) = 0.03 \times 0.97 = 0.0291$.

**Free throw.** A basketball player makes 80% of free throws. Let $X = 1$ if the next shot is made. Then $X \sim \text{Bernoulli}(0.8)$ with $E[X] = 0.8$ and $\text{Var}(X) = 0.16$.
