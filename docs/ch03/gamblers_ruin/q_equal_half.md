# Linear Recurrence Solution (q = 1/2)

## Double Root Case

When $p = q = 1/2$, the characteristic equation becomes:

$$

\frac{1}{2}\lambda^2 - \lambda + \frac{1}{2} = 0 \implies (\lambda - 1)^2 = 0

$$

There is a **double root** $\lambda = 1$, yielding only one solution from the standard approach: $Q_1(i) = 1$.

## Finding the Second Solution

For a second-order recurrence with a double characteristic root $\lambda$, a second linearly independent solution is:

$$

Q_2(i) = i \cdot Q_1(i) = i

$$

One can verify directly: $Q_2(i) = i$ satisfies the recurrence $Q(i) = \frac{1}{2}Q(i+1) + \frac{1}{2}Q(i-1)$ since

$$

\frac{1}{2}(i+1) + \frac{1}{2}(i-1) = i \quad \checkmark

$$

## General Solution

$$

Q(i) = \alpha + \beta\,i

$$

## Applying Boundary Conditions

**From $Q(0) = 1$:**

$$

\alpha = 1

$$

**From $Q(N) = 0$:**

$$

1 + \beta\,N = 0 \implies \beta = -\frac{1}{N}

$$

## Solution

$$

\boxed{Q(i) = 1 - \frac{i}{N} = \frac{N - i}{N}}

$$

## Interpretation

In a fair game, the ruin probability decreases **linearly** with initial capital. Starting halfway to the goal ($i = N/2$) gives a ruin probability of exactly \$1/2$.

| Initial Capital $i$ | $Q(i)$ |
|---------------------|---------|
| $0$ | $1$ |
| $N/4$ | \$3/4$ |
| $N/2$ | \$1/2$ |
| $3N/4$ | \$1/4$ |
| $N$ | $0$ |

## Comparison of the Two Cases

| Property | $q > 1/2$ (Unfair) | $q = 1/2$ (Fair) |
|----------|---------------------|-------------------|
| Characteristic roots | $1$ and $q/p > 1$ | $1$ (double root) |
| Solution | $\dfrac{(q/p)^N - (q/p)^i}{(q/p)^N - 1}$ | $\dfrac{N - i}{N}$ |
| Convergence to 1 as $i \downarrow 0$ | Exponential | Linear |
| $Q(N/2)$ for large $N$ | $\approx 1$ | $= 1/2$ |

Even in a perfectly fair game, the gambler who starts with less than the goal has a significant probability of ruin. In the unfair case, ruin is nearly certain unless the gambler starts very close to the goal.
