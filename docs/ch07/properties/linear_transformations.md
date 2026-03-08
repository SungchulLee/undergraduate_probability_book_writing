# Variance Under Linear Transformations

## Mean and Variance Lemma

For constants $a$ and $b$:

$$
\mathbb{E}(aX + b) = a\,\mathbb{E}(X) + b
$$

$$
\text{Var}(aX + b) = \text{Var}(aX) = a^2 \text{Var}(X)
$$

The additive constant $b$ shifts the mean but does not affect the variance.

### Proof via Covariance

$$
\begin{aligned}
\text{Var}(aX + b) &= \text{Cov}(aX + b,\; aX + b) \\[4pt]
&= a^2 \text{Var}(X) + 2ab\,\text{Cov}(X, 1) + b^2 \text{Var}(1) \\[4pt]
&= a^2 \text{Var}(X)
\end{aligned}
$$

since $\text{Cov}(X, 1) = 0$ and $\text{Var}(1) = 0$.

## Properties of Variance and Covariance

**(1)** $\;\text{Var}(X) = \text{Cov}(X, X)$

**(2)** $\;\text{Cov}(aX + bY, Z) = a\,\text{Cov}(X, Z) + b\,\text{Cov}(Y, Z)$ &emsp; (bilinearity)

$\quad\;\;\text{Cov}(Z, aX + bY) = a\,\text{Cov}(Z, X) + b\,\text{Cov}(Z, Y)$

**(3)** $\;\text{Cov}(X, Y) = \text{Cov}(Y, X)$ &emsp; (symmetry)

**(4)** $\;\text{Cov}(X, a) = \text{Cov}(a, X) = 0$

**(5)** $\;\text{Cov}(X, Y) = 0$ if $X$ and $Y$ are independent

### Proofs

**Property (2):** Bilinearity of covariance:

$$
\begin{aligned}
\text{Cov}(aX + bY, Z) &= \mathbb{E}[(aX + bY - a\mathbb{E}X - b\mathbb{E}Y)(Z - \mathbb{E}Z)] \\
&= \mathbb{E}[a(X - \mathbb{E}X) + b(Y - \mathbb{E}Y)](Z - \mathbb{E}Z) \\
&= a\,\mathbb{E}[(X - \mathbb{E}X)(Z - \mathbb{E}Z)] + b\,\mathbb{E}[(Y - \mathbb{E}Y)(Z - \mathbb{E}Z)] \\
&= a\,\text{Cov}(X, Z) + b\,\text{Cov}(Y, Z)
\end{aligned}
$$

**Property (5):** If $X$ and $Y$ are independent, then $\mathbb{E}(XY) = \mathbb{E}(X)\mathbb{E}(Y)$, so:

$$
\text{Cov}(X, Y) = \mathbb{E}(XY) - \mathbb{E}(X)\mathbb{E}(Y) = 0
$$

!!! warning "Converse is False"
    $\text{Cov}(X, Y) = 0$ does **not** imply independence in general.

## Worked Example: Computing Variance via Covariance

Let $\text{Var}(X) = 2$, $\text{Var}(Y) = 2$, $\text{Var}(Z) = 3$, $\text{Cov}(X, Y) = 0.25$, with $Z$ independent of both $X$ and $Y$. Compute $\text{Var}(V)$ where $V = X + 2Y - 3Z - 2$.

Using $\text{Var}(V) = \text{Cov}(V, V)$ and expanding via bilinearity:

$$
\begin{aligned}
\text{Var}(V) &= \text{Cov}(X + 2Y - 3Z - 2,\; X + 2Y - 3Z - 2) \\[6pt]
&= \text{Var}(X) + 4\,\text{Cov}(X, Y) - 6\,\text{Cov}(X, Z) \\
&\quad + 4\,\text{Var}(Y) - 12\,\text{Cov}(Y, Z) \\
&\quad + 9\,\text{Var}(Z)
\end{aligned}
$$

Since $Z$ is independent of $X$ and $Y$: $\text{Cov}(X, Z) = \text{Cov}(Y, Z) = 0$. Also, $\text{Cov}(\cdot, \text{constant}) = 0$. Therefore:

$$
\text{Var}(V) = 2 + 4(0.25) + 4(2) + 9(3) = 2 + 1 + 8 + 27 = 38
$$

### Detailed Expansion

The full expansion uses properties (1)–(5) systematically:

| Step | Rule Applied |
|:---|:---|
| $\text{Var}(V) = \text{Cov}(V, V)$ | Property (1) |
| Expand both arguments of Cov | Property (2): bilinearity |
| Combine symmetric terms | Property (3): $\text{Cov}(X,Y) = \text{Cov}(Y,X)$ |
| Drop constant terms | Property (4): $\text{Cov}(X, a) = 0$ |
| Drop independent terms | Property (5): independence $\Rightarrow$ zero covariance |
