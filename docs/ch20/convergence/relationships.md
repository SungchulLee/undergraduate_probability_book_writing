# Relationships Between Modes of Convergence

## Hierarchy of Convergence

The three modes of convergence satisfy the following implications:

$$
X_n \xrightarrow{a.s.} X \implies X_n \xrightarrow{p} X \implies X_n \xrightarrow{d} X
$$

None of the reverse implications hold in general.

## Why a.s. Implies in Probability

If $P(\lim X_n = X) = 1$, then for any $\varepsilon > 0$, the set of outcomes where $|X_n - X| > \varepsilon$ must shrink. More precisely, almost sure convergence implies that the "bad" events $\{|X_n - X| > \varepsilon\}$ can only occur finitely often (with probability 1), so their probabilities must tend to zero:

$$
P(|X_n - X| > \varepsilon) \to 0
$$

which is convergence in probability.

## Why in Probability Implies in Distribution

If $P(|X_n - X| > \varepsilon) \to 0$ for all $\varepsilon > 0$, then for any continuity point $x$ of $F_X$, one can show that $F_{X_n}(x) \to F_X(x)$ by bounding the CDF difference in terms of the deviation probability.

## Reverse Implications Fail

??? example "Convergence in Probability but Not Almost Surely"
    Let $\Omega = [0,1]$ with the uniform distribution. Define $X_n = \mathbf{1}_{I_n}$ where the intervals $I_n$ cycle through $[0,1]$ with shrinking length: $I_1 = [0,1]$, $I_2 = [0,1/2]$, $I_3 = [1/2,1]$, $I_4 = [0,1/3]$, $I_5 = [1/3,2/3]$, $I_6 = [2/3,1]$, and so on.

    Then $P(X_n = 1) \to 0$, so $X_n \xrightarrow{p} 0$. But for every $\omega \in [0,1]$, the sequence $X_n(\omega)$ takes the value 1 infinitely often, so $X_n(\omega) \not\to 0$ for any $\omega$. Thus $X_n$ does **not** converge almost surely.

??? example "Convergence in Distribution but Not in Probability"
    Let $X \sim N(0,1)$ and define $X_n = -X$ for all $n$. Then $X_n \sim N(0,1)$ for every $n$, so $X_n \xrightarrow{d} X$. But $|X_n - X| = 2|X|$, so $P(|X_n - X| > \varepsilon) = P(2|X| > \varepsilon) > 0$ for all $\varepsilon > 0$ and all $n$. Thus $X_n$ does **not** converge to $X$ in probability.

## Special Case: Convergence to a Constant

When the limit is a **constant** $c$, convergence in distribution and convergence in probability are equivalent:

$$
X_n \xrightarrow{d} c \iff X_n \xrightarrow{p} c
$$

This is particularly important because the Law of Large Numbers asserts convergence to the constant $\mu$.

## Summary Table

| Mode | Notation | Definition |
|------|----------|------------|
| Almost sure (strong) | $X_n \xrightarrow{a.s.} X$ | $P(\lim X_n = X) = 1$ |
| In probability (weak) | $X_n \xrightarrow{p} X$ | $P(\|X_n - X\| > \varepsilon) \to 0$ for all $\varepsilon > 0$ |
| In distribution | $X_n \xrightarrow{d} X$ | $F_{X_n}(x) \to F_X(x)$ at continuity points |

## Where Each Mode Appears

| Theorem | Mode of Convergence |
|---------|---------------------|
| Central Limit Theorem | In distribution |
| Weak Law of Large Numbers | In probability |
| Strong Law of Large Numbers | Almost sure |

Each successive theorem makes a stronger claim about how the sample mean behaves.
