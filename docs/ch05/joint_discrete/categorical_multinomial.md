# Categorical and Multinomial Distributions


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

## Distributions Related to Dice Rolling

Just as the Bernoulli and Binomial distributions arise from coin flipping, the **Categorical** and **Multinomial** distributions arise from dice rolling — experiments with more than two outcomes.

## Parameters

The parameter is a probability vector $\mathbf{p} = (p_1, \ldots, p_K)$ where:

$$p_j \ge 0, \qquad \sum_{j=1}^K p_j = 1$$

This represents a $K$-sided die where face $j$ appears with probability $p_j$.

## Categorical Distribution Cat(p)

Roll a $\mathbf{p}$-die once and record the result. The outcome is represented by a vector $(X_1, \ldots, X_K)$ where exactly one component equals 1 and the rest equal 0:

$$P(X_1 = 0, \ldots, X_j = 1, \ldots, X_K = 0) = p_j$$

The Categorical distribution generalizes the Bernoulli distribution from 2 outcomes to $K$ outcomes.

## Multinomial Distribution Mul(n, p)

Roll a $\mathbf{p}$-die $n$ times independently and count the number of each outcome. If $X_j$ denotes the number of times face $j$ appears:

$$P(X_1 = n_1, \ldots, X_K = n_K) = \binom{n}{n_1 \cdots n_K} p_1^{n_1} \cdots p_K^{n_K}$$

where $\binom{n}{n_1 \cdots n_K} = \frac{n!}{n_1! \cdots n_K!}$ is the **multinomial coefficient**, and $n_1 + \cdots + n_K = n$.

The Multinomial distribution generalizes the Binomial distribution from 2 outcomes to $K$ outcomes.

## Relationship Summary

| Coin (2 outcomes) | Dice ($K$ outcomes) |
|---|---|
| Bernoulli $\text{B}(p)$ | Categorical $\text{Cat}(\mathbf{p})$ |
| Binomial $\text{B}(n, p)$ | Multinomial $\text{Mul}(n, \mathbf{p})$ |

## Marginals of the Multinomial

Each individual component of a Multinomial is Binomial:

$$X_j \sim \text{B}(n, p_j)$$

However, the components are **not independent** since they must sum to $n$.
