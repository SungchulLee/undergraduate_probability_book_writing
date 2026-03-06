# Gambler's Ruin Problem

## Problem Statement

Suppose you have \$$i$ in initial capital. Each round you bet \$$1$ on a game where you win \$$1$ with probability $p \le 1/2$ and lose \$$1$ with probability $q := 1 - p$. If you lose all your money, you are **ruined**. If you reach \$$N$, you happily quit.

### Notation

| Symbol | Meaning |
|--------|---------|
| $R$ | Ruin event |
| $I$ | Initial capital |
| $Q(i) = P(R \mid I = i)$ | Ruin probability starting with initial capital \$$i$ |
| $p$ | Probability of winning a single bet |
| $q = 1 - p$ | Probability of losing a single bet |
| $N$ | Goal amount (quit if reached) |

**Goal:** Calculate $Q(i)$ for $0 \le i \le N$.

### Boundary Conditions

$$

Q(0) = 1 \quad \text{(starting with nothing means certain ruin)}

$$

$$

Q(N) = 0 \quad \text{(reaching the goal means no ruin)}

$$

## Summary of Solutions

### Case 1: q > 1/2 (unfair game, equivalently q/p > 1)

$$

Q(i) = \frac{(q/p)^N - (q/p)^i}{(q/p)^N - 1}

$$

Since $q/p > 1$, we have $(q/p)^N \gg 1$ for large $N$, and hence

$$

Q(i) \approx 1 - \left(\frac{q}{p}\right)^{-(N-i)} = 1 - e^{-(N-i)\ln(q/p)}

$$

The ruin probability approaches 1 **exponentially fast** as the initial capital $i$ decreases from $N$.

### Case 2: q = 1/2 (fair game)

$$

Q(i) = \frac{N - i}{N}

$$

The ruin probability approaches 1 **linearly** as the initial capital decreases.

### Why "Gambler's Ruin"?

Even with a nearly fair game (e.g., $p = 0.49$), the ruin probability is devastatingly high. For example, with initial capital $i = 100$ and goal $N = 200$, the ruin probability exceeds 95%. The house edge, no matter how small, compounds over the many rounds needed to double one's money, making ruin nearly certain.
