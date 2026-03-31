# Linear Combinations of Normals
<<<<<<< Updated upstream

## General Linear Combination

!!! info "Linear Combination Theorem"
    If $X_1, \ldots, X_n$ are **independent** normal random variables with $X_i \sim N(\mu_i, \sigma_i^2)$, and $a_1, \ldots, a_n$ are constants, then:

    $$\sum_{i=1}^n a_i X_i \sim N\!\left(\sum_{i=1}^n a_i \mu_i, \; \sum_{i=1}^n a_i^2 \sigma_i^2\right)$$

This extends the sum result from the previous section: the sum of independent normals is a special case with $a_i = 1$ for all $i$.

## Proof via MGF

The MGF of $X_i \sim N(\mu_i, \sigma_i^2)$ is $M_{X_i}(t) = e^{\mu_i t + \frac{1}{2}\sigma_i^2 t^2}$. By independence:

$$M_{\sum a_i X_i}(t) = \prod_{i=1}^n M_{X_i}(a_i t) = \prod_{i=1}^n e^{\mu_i(a_i t) + \frac{1}{2}\sigma_i^2(a_i t)^2}$$

$$= \exp\!\left(\left(\sum a_i \mu_i\right)t + \frac{1}{2}\left(\sum a_i^2 \sigma_i^2\right)t^2\right)$$

This is the MGF of $N\!\left(\sum a_i \mu_i, \sum a_i^2 \sigma_i^2\right)$. By uniqueness of MGFs, the result follows. $\square$

## Difference of Normals

An important special case is the **difference** $X - Y$ where $a_1 = 1$ and $a_2 = -1$.

!!! info "Difference of Independent Normals"
    If $X \sim N(\mu_X, \sigma_X^2)$ and $Y \sim N(\mu_Y, \sigma_Y^2)$ are independent, then:

    $$X - Y \sim N(\mu_X - \mu_Y, \; \sigma_X^2 + \sigma_Y^2)$$

Note that the variances **add** even when subtracting. This is because $\text{Var}(X - Y) = \text{Var}(X) + \text{Var}(Y)$ for independent random variables.

## Affine Transformation

For a single normal $X \sim N(\mu, \sigma^2)$ and constants $a, b$:

$$aX + b \sim N(a\mu + b, \, a^2\sigma^2)$$

This is the $n = 1$ case of the linear combination theorem (with an added constant).

## Worked Examples

??? example "Example: Comparing Test Scores"
    Alice scores $X \sim N(520, 100^2)$ and Bob scores $Y \sim N(490, 110^2)$ independently on a standardized test. Find the probability that Alice outscores Bob.

    $$X - Y \sim N(520 - 490, \; 100^2 + 110^2) = N(30, \; 22100)$$

    $$P(X > Y) = P(X - Y > 0) = 1 - \Phi\!\left(\frac{0 - 30}{\sqrt{22100}}\right) = \Phi\!\left(\frac{30}{148.66}\right) = \Phi(0.202) \approx 0.580$$

    Alice has about a 58% chance of scoring higher.

??? example "Example: Portfolio Return"
    An investor holds \$60{,}000 in asset A with annual return $R_A \sim N(0.08, 0.04^2)$ and \$40{,}000 in asset B with return $R_B \sim N(0.12, 0.09^2)$, independently. Find the distribution of the portfolio return.

    The portfolio return is:

    $$R_P = 0.6 R_A + 0.4 R_B \sim N(0.6 \cdot 0.08 + 0.4 \cdot 0.12, \; 0.6^2 \cdot 0.04^2 + 0.4^2 \cdot 0.09^2)$$

    $$= N(0.096, \; 0.001872)$$

    So the portfolio has expected return 9.6% and standard deviation $\sqrt{0.001872} \approx 4.33\%$.

!!! warning "Independence Required"
    The linear combination of **dependent** normal random variables is not necessarily normal. Normality of the sum is guaranteed when the variables are independent, or more generally, when they are **jointly normal** (see Chapter 18).

## Python Implementation

```python
import numpy as np
from scipy import stats

# Alice vs Bob
mu_diff, var_diff = 520 - 490, 100**2 + 110**2
p = 1 - stats.norm.cdf(0, mu_diff, np.sqrt(var_diff))
print(f"P(Alice > Bob) = {p:.4f}")

# Portfolio return
mu_P = 0.6 * 0.08 + 0.4 * 0.12
var_P = 0.6**2 * 0.04**2 + 0.4**2 * 0.09**2
print(f"Portfolio: N({mu_P:.4f}, {var_P:.6f})")
print(f"  SD = {np.sqrt(var_P):.4f}")
print(f"  P(loss) = P(R_P < 0) = {stats.norm.cdf(0, mu_P, np.sqrt(var_P)):.4f}")
```

**Output:**
```
P(Alice > Bob) = 0.5800
Portfolio: N(0.0960, 0.001872)
  SD = 0.0433
  P(loss) = P(R_P < 0) = 0.0133
```
=======
>>>>>>> Stashed changes
