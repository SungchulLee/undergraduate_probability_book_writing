# Correlation Coefficient

Correlation is the standardized version of covariance — it is unitless and always lies between $-1$ and $+1$.

## Definition

The **correlation** (or Pearson correlation coefficient) of $X$ and $Y$ is

$$
\rho(X, Y) = \text{Corr}(X, Y) = \frac{\text{Cov}(X, Y)}{\text{SD}(X)\,\text{SD}(Y)} = \frac{\text{Cov}(X, Y)}{\sqrt{\text{Var}(X)\,\text{Var}(Y)}}
$$

provided both standard deviations are positive.

## Explanation

### Range and Extreme Cases

The Cauchy-Schwarz inequality guarantees $-1 \le \rho \le 1$.

| $\rho$ value | Interpretation |
|:-------------|:---------------|
| $\rho = 1$ | Perfect positive linear relationship: $Y = a + bX$, $b > 0$ |
| $\rho = -1$ | Perfect negative linear relationship: $Y = a + bX$, $b < 0$ |
| $\rho = 0$ | Uncorrelated (no linear association) |
| $0 < \rho < 1$ | Positive linear tendency |
| $-1 < \rho < 0$ | Negative linear tendency |

### Properties

- **Scale invariant:** $\text{Corr}(aX + b, cY + d) = \text{sign}(ac)\,\text{Corr}(X, Y)$ for $ac \ne 0$
- **Symmetric:** $\text{Corr}(X, Y) = \text{Corr}(Y, X)$
- **Self-correlation:** $\text{Corr}(X, X) = 1$

### Correlation Is Not Causation

$\rho$ measures linear association, not causal effect. Two variables can have $\rho = 0$ yet be strongly dependent (e.g., $X \sim N(0,1)$ and $Y = X^2$).

## Examples

**Example.** $X$ = first die, $Y$ = sum of two dice. With $\text{Cov}(X, Y) = 35/12$, $\text{Var}(X) = 35/12$, $\text{Var}(Y) = 35/6$:

$$
\rho(X, Y) = \frac{35/12}{\sqrt{(35/12)(35/6)}} = \frac{1}{\sqrt{2}} \approx 0.707
$$

```python
import numpy as np

np.random.seed(42)
n_sim = 200_000

X = np.random.randint(1, 7, n_sim)
Z = np.random.randint(1, 7, n_sim)
Y = X + Z

rho = np.corrcoef(X, Y)[0, 1]
print(f"Corr(X, Y) = {rho:.4f}  (theory: {1/np.sqrt(2):.4f})")

# Uncorrelated but dependent: X ~ N(0,1), Y = X^2
X2 = np.random.standard_normal(n_sim)
Y2 = X2**2
rho2 = np.corrcoef(X2, Y2)[0, 1]
print(f"\nCorr(X, X^2) = {rho2:.4f}  (theory: 0)")
print(f"But E[Y|X=x] = x^2, clearly dependent!")
```
