# Law of Total Variance (Eve's Law)

Total variance splits into within-group variance and between-group variance — the variance analogue of the tower property.

## Definition

For any random variables $X$ and $Y$:

$$
\text{Var}(X) = E\bigl[\text{Var}(X \mid Y)\bigr] + \text{Var}\bigl(E[X \mid Y]\bigr)
$$

The mnemonic **EVVE** helps: **E**xpected **V**ariance + **V**ariance of **E**xpectation.

## Explanation

### Two Components

| Component | Name | Measures |
|:----------|:-----|:---------|
| $E[\text{Var}(X \mid Y)]$ | Within-group (unexplained) | Average spread within each $Y$-group |
| $\text{Var}(E[X \mid Y])$ | Between-group (explained) | How much group means differ |

Since both are non-negative: $\text{Var}(X) \ge E[\text{Var}(X \mid Y)]$ and $\text{Var}(X) \ge \text{Var}(E[X \mid Y])$. Conditioning can only reduce average variance.

### Proof

By the conditional shortcut formula: $E[X^2 \mid Y] = \text{Var}(X \mid Y) + (E[X \mid Y])^2$. Applying the tower property to both sides:

$$
E[X^2] = E[\text{Var}(X \mid Y)] + E[(E[X \mid Y])^2]
$$

Also $(E[X])^2 = (E[E[X \mid Y]])^2$ by the tower property. Subtracting:

$$
\text{Var}(X) = E[\text{Var}(X \mid Y)] + \underbrace{E[(E[X \mid Y])^2] - (E[E[X \mid Y]])^2}_{\text{Var}(E[X \mid Y])}
$$

### Application to Random Sums

For $T = \sum_{i=1}^N X_i$ with iid $X_i$ (mean $\mu$, variance $\sigma^2$) independent of $N$:

$$
\text{Var}(T) = \underbrace{\sigma^2 E[N]}_{E[\text{Var}(T \mid N)]} + \underbrace{\mu^2 \text{Var}(N)}_{\text{Var}(E[T \mid N])}
$$

### Recursive Applications

For self-referencing problems (trapped miner, waiting for HH), Eve's law gives an equation with $\text{Var}(T)$ on both sides:

$$
\text{Var}(T) = A + c\,\text{Var}(T) \implies \text{Var}(T) = \frac{A}{1 - c}
$$

## Examples

**Example 1 (Department store).** $N$ customers (mean 50, variance 100), each spending $X_i$ (mean \$8, variance 16):

| Component | Computation | Value |
|:----------|:-----------|------:|
| $E[\text{Var}(T \mid N)]$ | $16 \times 50$ | 800 |
| $\text{Var}(E[T \mid N])$ | $64 \times 100$ | 6400 |
| $\text{Var}(T)$ | $800 + 6400$ | 7200 |

The between-group term (6400) dominates: variability in customer count matters more than variability in individual spending.

**Example 2 (Trapped miner).** With $E[T] = 15$:

$$
\text{Var}(T) = 72.67 + \tfrac{2}{3}\text{Var}(T) \implies \text{Var}(T) = 218
$$

**Example 3 (Waiting for HH).** With $E[W_{HH}] = 6$:

$$
\text{Var}(W_{HH}) = 9 + 2 + \tfrac{1}{2}\text{Var}(W_{HH}) \implies \text{Var}(W_{HH}) = 22
$$

```python
import numpy as np

np.random.seed(42)
n_sim = 500_000

# Verify Eve's law: X|Y=y ~ Exp(1/y), Y ~ Exp(1)
Y = np.random.exponential(1, n_sim)
X = np.array([np.random.exponential(y) for y in Y])

# E[X|Y] = Y, Var(X|Y) = Y^2
within = np.mean(Y**2)
between = np.var(Y)
total = np.var(X)

print("=== Eve's Law Verification ===")
print(f"Var(X)                = {total:.3f}")
print(f"E[Var(X|Y)]           = {within:.3f}")
print(f"Var(E[X|Y])           = {between:.3f}")
print(f"Within + Between      = {within + between:.3f}")
print(f"Match: {abs(total - (within + between)) < 0.1}")
```
