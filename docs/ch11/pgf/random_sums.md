# Random Sums and Compound Distributions

## Setup

Let $N$ be a non-negative integer-valued random variable and let $X_1, X_2, \ldots$ be iid non-negative integer-valued random variables, independent of $N$. The **random sum** is:

$$S = X_1 + X_2 + \cdots + X_N$$

with the convention $S = 0$ when $N = 0$. The distribution of $S$ is called a **compound distribution**.

## The Composition Formula

!!! info "PGF of a Random Sum"
    $$G_S(s) = G_N(G_X(s))$$

    The PGF of the random sum is the PGF of $N$ evaluated at the PGF of $X$.

**Proof.** Condition on $N$:

$$G_S(s) = E[s^S] = \sum_{n=0}^{\infty} E[s^S \mid N = n]\,P(N = n)$$

Given $N = n$, $S = X_1 + \cdots + X_n$, so:

$$E[s^S \mid N = n] = E[s^{X_1 + \cdots + X_n}] = [G_X(s)]^n$$

by independence. Therefore:

$$G_S(s) = \sum_{n=0}^{\infty} [G_X(s)]^n P(N = n) = G_N(G_X(s)) \qquad \square$$

## Moments of the Random Sum

Differentiating $G_S(s) = G_N(G_X(s))$ at $s = 1$:

$$G_S'(s) = G_N'(G_X(s)) \cdot G_X'(s)$$

$$E[S] = G_S'(1) = G_N'(1) \cdot G_X'(1) = E[N] \cdot E[X]$$

For the variance, use the law of total variance or differentiate again:

$$\text{Var}(S) = E[N] \cdot \text{Var}(X) + \text{Var}(N) \cdot (E[X])^2$$

!!! tip "Wald's Identity for Variance"
    The variance formula decomposes into two sources:

    - $E[N] \cdot \text{Var}(X)$: randomness **within** each claim
    - $\text{Var}(N) \cdot (E[X])^2$: randomness in the **number** of claims

## Example: Compound Poisson

Let $N \sim \text{Po}(\lambda)$ and $X_i \stackrel{\text{iid}}{\sim} \text{Geo}(p)$ with PGF $G_X(s) = \frac{ps}{1-(1-p)s}$.

The PGF of $N$ is $G_N(s) = e^{\lambda(s-1)}$. By the composition formula:

$$G_S(s) = \exp\!\left[\lambda\!\left(\frac{ps}{1-(1-p)s} - 1\right)\right] = \exp\!\left[\lambda \cdot \frac{ps - 1 + (1-p)s}{1-(1-p)s}\right]$$

$$= \exp\!\left[\lambda \cdot \frac{s - 1}{1-(1-p)s}\right]$$

**Moments:**

$$E[S] = E[N] \cdot E[X] = \lambda \cdot \frac{1}{p} = \frac{\lambda}{p}$$

$$\text{Var}(S) = \lambda \cdot \frac{1-p}{p^2} + \lambda \cdot \frac{1}{p^2} = \frac{\lambda(2-p)}{p^2}$$

## Example: Compound Binomial

Let $N \sim B(n, q)$ and $X_i \stackrel{\text{iid}}{\sim} \text{Bernoulli}(p)$, all independent. Then:

$$G_S(s) = [1 - q + q(1 - p + ps)]^n = [1 - qp + qps]^n$$

This is the PGF of $B(n, qp)$, so $S \sim B(n, qp)$. The compound binomial with Bernoulli summands collapses to a simple binomial.

## Python Verification

```python
import numpy as np

np.random.seed(42)
n_sim = 100000

# Compound Poisson: N ~ Po(10), X_i ~ Geo(0.4)
lam, p = 10.0, 0.4

S = np.zeros(n_sim)
for i in range(n_sim):
    N = np.random.poisson(lam)
    if N > 0:
        X = np.random.geometric(p, size=N)
        S[i] = X.sum()

EX = 1 / p
VarX = (1 - p) / p**2

print("Compound Poisson: N ~ Po(10), X_i ~ Geo(0.4)")
print(f"  E[S]   = {S.mean():.4f}  (exact: {lam * EX:.4f})")
print(f"  Var(S) = {S.var():.4f}  (exact: {lam*VarX + lam*EX**2:.4f})")
```
