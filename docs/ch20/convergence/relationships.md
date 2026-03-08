# Relationships Between Modes of Convergence

## Hierarchy of Convergence

The three modes of convergence studied so far satisfy the following implications:

$$
X_n \xrightarrow{a.s.} X \implies X_n \xrightarrow{p} X \implies X_n \xrightarrow{d} X
$$

None of the reverse implications hold in general.

## Special Case: Convergence to a Constant

When the limit is a **constant** $c$, convergence in distribution and convergence in probability are equivalent:

$$
X_n \xrightarrow{d} c \iff X_n \xrightarrow{p} c
$$

This is particularly useful because the Law of Large Numbers states convergence to the constant $\mu$.

## Summary Table

| Mode | Notation | Requires |
|------|----------|----------|
| Almost sure (strong) | $X_n \xrightarrow{a.s.} X$ | $P(\lim X_n = X) = 1$ |
| In probability (weak) | $X_n \xrightarrow{p} X$ | $P(\|X_n - X\| > \varepsilon) \to 0$ for all $\varepsilon > 0$ |
| In distribution | $X_n \xrightarrow{d} X$ | $F_{X_n}(x) \to F_X(x)$ at continuity points |

## Key Takeaway

Almost sure convergence talks about the **behavior of sample paths** (with probability 1, the entire trajectory converges). Convergence in probability talks about **tail probabilities vanishing**. Convergence in distribution talks only about **CDFs approaching** each other. Each successive mode is strictly weaker.
