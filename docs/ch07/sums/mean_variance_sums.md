# Mean and Variance of Sums of Random Variables

## Mean of Sums

### General Case

For **any** random variables $X_1, X_2, \ldots, X_n$ (not necessarily independent):

$$
E\left[\sum_{i=1}^n X_i\right] = \sum_{i=1}^n E[X_i]
$$

This follows directly from **linearity of expectation**.

### iid Case

If $X_1, \ldots, X_n$ are iid (independent and identically distributed):

$$
E\left[\sum_{i=1}^n X_i\right] = n \, E[X_1]
$$

---

## Variance of Sums

### General Case

$$
\text{Var}\left(\sum_{i=1}^n X_i\right) = \sum_{i=1}^n \text{Var}(X_i) + \sum_{i \neq j} \text{Cov}(X_i, X_j)
= \sum_{i=1}^n \text{Var}(X_i) + 2\sum_{1 \leq i < j \leq n} \text{Cov}(X_i, X_j)
$$

### Independent Case

If $X_1, \ldots, X_n$ are **independent**:

$$
\text{Var}\left(\sum_{i=1}^n X_i\right) = \sum_{i=1}^n \text{Var}(X_i)
$$

### iid Case

If $X_1, \ldots, X_n$ are **iid**:

$$
\text{Var}\left(\sum_{i=1}^n X_i\right) = n \, \text{Var}(X_1)
$$

---

## Weighted Sums

### General Case

For constants $a_1, a_2, \ldots, a_n$:

$$
E\left[\sum_{i=1}^n a_i X_i\right] = \sum_{i=1}^n a_i E[X_i]
$$

$$
\text{Var}\left(\sum_{i=1}^n a_i X_i\right) = \sum_{i=1}^n a_i^2 \, \text{Var}(X_i) + 2\sum_{1 \leq i < j \leq n} a_i a_j \, \text{Cov}(X_i, X_j)
$$

### Independent Case

$$
\text{Var}\left(\sum_{i=1}^n a_i X_i\right) = \sum_{i=1}^n a_i^2 \, \text{Var}(X_i)
$$

### iid Case

$$
E\left[\sum_{i=1}^n a_i X_i\right] = \left(\sum_{i=1}^n a_i\right) E[X_1]
$$

$$
\text{Var}\left(\sum_{i=1}^n a_i X_i\right) = \left(\sum_{i=1}^n a_i^2\right) \text{Var}(X_1)
$$

---

## Matrix Form

Let $S = \sum_{i=1}^n a_i X_i = \mathbf{a}^T \mathbf{X}$ where $\mathbf{a} = (a_1, \ldots, a_n)^T$ and $\mathbf{X} = (X_1, \ldots, X_n)^T$.

Define:

- $\mu_i = E[X_i]$: mean of $X_i$
- $\sigma_i^2 = \text{Var}(X_i)$: variance of $X_i$
- $\sigma_{ij} = \text{Cov}(X_i, X_j)$: covariance between $X_i$ and $X_j$
- $\rho_{ij}$: correlation between $X_i$ and $X_j$

**Mean**:

$$
E[S] = \sum_{i=1}^n a_i \mu_i = \mathbf{a}^T \boldsymbol{\mu}
$$

**Variance**:

$$
\text{Var}(S) = \sum_{i=1}^n a_i^2 \sigma_i^2 + 2\sum_{1 \leq i < j \leq n} a_i a_j \sigma_{ij}
= \sum_{i=1}^n a_i^2 \sigma_i^2 + 2\sum_{1 \leq i < j \leq n} a_i a_j \rho_{ij} \sigma_i \sigma_j
$$

In matrix form:

$$
\text{Var}(S) = \mathbf{a}^T \boldsymbol{\Sigma} \, \mathbf{a}
$$

where the **covariance matrix** is

$$
\boldsymbol{\Sigma} = \begin{pmatrix}
\sigma_1^2 & \sigma_{12} & \cdots & \sigma_{1n} \\
\sigma_{21} & \sigma_2^2 & \cdots & \sigma_{2n} \\
\vdots & \vdots & \ddots & \vdots \\
\sigma_{n1} & \sigma_{n2} & \cdots & \sigma_n^2
\end{pmatrix}
$$

---

## Decomposition Examples

### Example 1: Binomial via Bernoulli

Flip a $p$-coin $n$ times independently. Let $\mathbf{1}_{A_i} \stackrel{iid}{\sim} \text{Bernoulli}(p)$.

$$
S = \sum_{i=1}^n \mathbf{1}_{A_i} \sim \text{Binomial}(n, p)
$$

$$
E[S] = \sum_{i=1}^n E[\mathbf{1}_{A_i}] = np
$$

$$
\text{Var}(S) = \sum_{i=1}^n \text{Var}(\mathbf{1}_{A_i}) = npq
$$

### Example 2: Negative Binomial via Geometric

Flip a $p$-coin until the $r$-th head. Let $X_i \stackrel{iid}{\sim} \text{Geo}(p)$ be the number of flips from the $(i-1)$-th to the $i$-th head.

$$
S = \sum_{i=1}^r X_i \sim \text{NB}(r, p)
$$

$$
E[S] = \sum_{i=1}^r E[X_i] = \frac{r}{p}
$$

$$
\text{Var}(S) = \sum_{i=1}^r \text{Var}(X_i) = \frac{rq}{p^2}
$$

### Example 3: Roll the Dice 1000 Times

Roll a die 1000 times. Gain the face value on odd rolls, lose the face value on even rolls. With a $+0.5$ bonus per game:

$$
D_i = \begin{cases} +1 & \text{w.p. } 1/6 \\ -2 & \text{w.p. } 1/6 \\ +3 & \text{w.p. } 1/6 \\ -4 & \text{w.p. } 1/6 \\ +5 & \text{w.p. } 1/6 \\ -6 & \text{w.p. } 1/6 \end{cases}
\qquad X_i = D_i + 0.5 \stackrel{iid}{\sim}
$$

Computing moments of $D_i$:

$$
E[D_i] = \frac{1 - 2 + 3 - 4 + 5 - 6}{6} = \frac{-3}{6} = -0.5
$$

$$
E[D_i^2] = \frac{1 + 4 + 9 + 16 + 25 + 36}{6} = \frac{91}{6} \approx 15.1667
$$

$$
\text{Var}(D_i) = E[D_i^2] - (E[D_i])^2 = 15.1667 - 0.25 = 14.9167
$$

Since $X_i = D_i + 0.5$: $E[X_i] = 0$ and $\text{Var}(X_i) = 14.9167$.

The total P\&L $S = \sum_{i=1}^{1000} X_i$:

$$
E[S] = 1000 \times 0 = 0
$$

$$
\text{Var}(S) = 1000 \times 14.9167 = 14916.7, \quad \text{SD}(S) \approx 122.1
$$

### Example 4: Coupon Collector Problem

To collect all $n$ types of toys, let $\tau_i \sim \text{Geo}\left(\frac{n-(i-1)}{n}\right)$ independently. Then $T_n = \sum_{i=1}^n \tau_i$:

$$
E[T_n] = \sum_{i=1}^n \frac{n}{n - (i-1)} = n\left(1 + \frac{1}{2} + \frac{1}{3} + \cdots + \frac{1}{n}\right) = nH_n \sim n\log n
$$

$$
\text{Var}(T_n) = \sum_{k=1}^n \frac{1 - k/n}{(k/n)^2} = n^2 \sum_{k=1}^n \frac{1}{k^2} - n\sum_{k=1}^n \frac{1}{k} \approx \frac{\pi^2}{6} n^2 - n\log n
$$

---

## Python Implementation

```python
import numpy as np
import matplotlib.pyplot as plt

# ============================================================
# Example: Roll the dice 1000 times
# ============================================================
np.random.seed(42)
NumSimu = 10000
NumRolling = 1000

# Generate dice rolls
rolls = np.random.randint(1, 7, size=(NumRolling, NumSimu))

# Map to P&L: odd face -> +value, even face -> -value
increment = np.where(rolls % 2 == 1, rolls, -rolls).astype(float)
increment += 0.5  # bonus

# Cumulative P&L
Sn = np.cumsum(increment, axis=0)

# Theoretical values
E_D = (-3) / 6
Var_D = 91/6 - 0.25
print(f"E[D_i] = {E_D:.4f}")
print(f"Var(D_i) = {Var_D:.4f}")
print(f"E[X_i] = {E_D + 0.5:.4f}")
print(f"Var(X_i) = {Var_D:.4f}")
print(f"E[S] = {1000 * (E_D + 0.5):.4f}")
print(f"Var(S) = {1000 * Var_D:.4f}")
print(f"SD(S) = {np.sqrt(1000 * Var_D):.4f}")

# Simulation verification
total_pnl = Sn[-1, :]
print(f"\nSimulated E[S] = {np.mean(total_pnl):.4f}")
print(f"Simulated SD(S) = {np.std(total_pnl):.4f}")

# Plot
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

axes[0].hist(total_pnl, bins=50, edgecolor='black')
axes[0].set_xlabel('Total P&L')
axes[0].set_title('Histogram of Total P&L after 1000 Games')
axes[0].grid(True, alpha=0.3)

axes[1].plot(range(1, NumRolling + 1), Sn[:, 0])
axes[1].set_xlabel('Game number')
axes[1].set_ylabel('Cumulative P&L')
axes[1].set_title('Sample Path of Cumulative P&L')
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('dice_1000_pnl.png', dpi=150, bbox_inches='tight')
plt.show()

# ============================================================
# Coupon Collector
# ============================================================
n_toys = 50
harmonic = sum(1/k for k in range(1, n_toys + 1))
E_Tn = n_toys * harmonic
Var_Tn = n_toys**2 * sum(1/k**2 for k in range(1, n_toys + 1)) - n_toys * harmonic
print(f"\nCoupon Collector (n={n_toys}):")
print(f"E[T_n] = {E_Tn:.2f}")
print(f"SD(T_n) = {np.sqrt(Var_Tn):.2f}")

# ============================================================
# Matrix form example
# ============================================================
# Portfolio variance with 3 assets
a = np.array([0.4, 0.35, 0.25])  # weights
sigma = np.array([0.20, 0.15, 0.25])  # asset SDs
rho = np.array([[1.0, 0.3, 0.1],
                [0.3, 1.0, 0.5],
                [0.1, 0.5, 1.0]])  # correlation matrix

# Build covariance matrix
Sigma = np.outer(sigma, sigma) * rho
portfolio_var = a @ Sigma @ a
print(f"\nPortfolio Example:")
print(f"Weights: {a}")
print(f"Asset SDs: {sigma}")
print(f"Portfolio Var = a'Σa = {portfolio_var:.6f}")
print(f"Portfolio SD = {np.sqrt(portfolio_var):.4f}")
```
