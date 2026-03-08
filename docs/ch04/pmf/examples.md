# Examples of PMFs

## Bernoulli PMF

For $X \sim \text{Bern}(p)$:

$$P(X = k) = \begin{cases} 1 - p & k = 0 \\ p & k = 1 \end{cases}$$

This is the simplest non-trivial PMF: flip a $p$-coin and record 1 for heads, 0 for tails.

## Binomial PMF

For $X \sim \text{Bin}(n, p)$:

$$P(X = k) = \binom{n}{k} p^k (1-p)^{n-k}, \quad k = 0, 1, \ldots, n$$

This counts the number of heads in $n$ independent flips of a $p$-coin.

## Geometric PMF

For $X \sim \text{Geo}(p)$:

$$P(X = k) = p(1-p)^{k-1}, \quad k = 1, 2, 3, \ldots$$

This counts the number of flips until the first head.

## Negative Binomial PMF

For $X \sim \text{NB}(r, p)$:

$$P(X = k) = \binom{k-1}{r-1} p^r (1-p)^{k-r}, \quad k = r, r+1, r+2, \ldots$$

This counts the number of flips until the $r$-th head.

## Summary Table

| Distribution | Expectation | Variance |
|-------------|-------------|----------|
| $\text{Bern}(p)$ | $p$ | $pq$ |
| $\text{Bin}(n,p)$ | $np$ | $npq$ |
| $\text{Geo}(p)$ | $1/p$ | $q/p^2$ |
| $\text{NB}(r,p)$ | $r/p$ | $rq/p^2$ |

where $q = 1 - p$.

## Coin Flip Distributions Visualized

The Bernoulli, Binomial, Geometric, and Negative Binomial distributions are all related to the same experiment — flipping a $p$-coin — but they count different things:

| Distribution | Random Variable |
|---|---|
| $\text{Bern}(p)$ | Flip a $p$-coin and check whether we have a head |
| $\text{Bin}(n,p)$ | Flip a $p$-coin $n$ times and count the number of heads |
| $\text{Geo}(p)$ | Flip a $p$-coin until first head and count the number of flips |
| $\text{NB}(r,p)$ | Flip a $p$-coin until $r$-th head and count the number of flips |
