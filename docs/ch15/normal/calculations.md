# Normal Probability Calculations
<<<<<<< Updated upstream

## Standardization

Every normal probability calculation reduces to the standard normal via the **Z-score transformation**.

!!! info "Standardization"
    If $X \sim N(\mu, \sigma^2)$, then $Z = \dfrac{X - \mu}{\sigma} \sim N(0, 1)$, and:

    $$P(a < X < b) = \Phi\!\left(\frac{b - \mu}{\sigma}\right) - \Phi\!\left(\frac{a - \mu}{\sigma}\right)$$

    where $\Phi$ is the standard normal CDF.

## Computing Tail Probabilities

**Left tail.** $P(X \leq x) = \Phi\!\left(\dfrac{x - \mu}{\sigma}\right)$

**Right tail.** Using the complement rule:

$$P(X > x) = 1 - \Phi\!\left(\frac{x - \mu}{\sigma}\right)$$

**Symmetry shortcut.** Since $\Phi(-z) = 1 - \Phi(z)$:

$$P(X < \mu - c) = P(X > \mu + c) = 1 - \Phi\!\left(\frac{c}{\sigma}\right)$$

## Worked Examples

??? example "Example: Exam Scores"
    Exam scores follow $X \sim N(65, 9)$ (so $\sigma = 3$).

    **(a)** Find $P(X > 70)$.

    $$P(X > 70) = 1 - \Phi\!\left(\frac{70 - 65}{3}\right) = 1 - \Phi(1.67) \approx 1 - 0.9525 = 0.0475$$

    About 4.8% of students score above 70.

    **(b)** Find $P(60 < X < 68)$.

    $$P(60 < X < 68) = \Phi\!\left(\frac{68 - 65}{3}\right) - \Phi\!\left(\frac{60 - 65}{3}\right) = \Phi(1) - \Phi(-1.67)$$

    $$= 0.8413 - 0.0475 = 0.7938$$

??? example "Example: Manufacturing Tolerance"
    A machine produces rods with length $X \sim N(50, 4)$ cm (so $\sigma = 2$). Rods are rejected if they deviate from the mean by more than 3 cm. Find the rejection rate.

    $$P(|X - 50| > 3) = P(X < 47) + P(X > 53) = 2\bigl[1 - \Phi(1.5)\bigr] = 2(1 - 0.9332) = 0.1336$$

    About 13.4% of rods are rejected.

## The 68-95-99.7 Rule

For any $X \sim N(\mu, \sigma^2)$:

| Interval | Probability |
|:---:|:---:|
| $\mu \pm \sigma$ | $\approx 0.6827$ |
| $\mu \pm 2\sigma$ | $\approx 0.9545$ |
| $\mu \pm 3\sigma$ | $\approx 0.9973$ |

These follow from $P(|Z| \leq k) = 2\Phi(k) - 1$.

## Finding Percentiles

To find the value $x_\alpha$ such that $P(X \leq x_\alpha) = \alpha$, invert the standardization:

$$x_\alpha = \mu + \sigma \cdot z_\alpha$$

where $z_\alpha = \Phi^{-1}(\alpha)$ is the $\alpha$-quantile of $N(0, 1)$.

??? example "Example: Top 10% Cutoff"
    Scores are $N(65, 9)$. Find the cutoff for the top 10%.

    We need $P(X > c) = 0.10$, so $P(X \leq c) = 0.90$.

    $$c = 65 + 3 \cdot z_{0.90} = 65 + 3 \cdot 1.282 = 68.85$$

    A score of about 68.85 places a student in the top 10%.

## Python Implementation

```python
from scipy import stats

mu, sigma = 65, 3  # N(65, 9)

# Interval probability
p1 = stats.norm.cdf(70, mu, sigma) - stats.norm.cdf(60, mu, sigma)
print(f"P(60 < X < 70) = {p1:.4f}")

# Upper-tail probability
p2 = 1 - stats.norm.cdf(70, mu, sigma)
print(f"P(X > 70) = {p2:.4f}")

# Percentile (top 10% cutoff)
c = stats.norm.ppf(0.90, mu, sigma)
print(f"Top 10% cutoff: {c:.2f}")

# 68-95-99.7 verification
for k in [1, 2, 3]:
    p = stats.norm.cdf(k) - stats.norm.cdf(-k)
    print(f"P(|Z| <= {k}) = {p:.4f}")
```

**Output:**
```
P(60 < X < 70) = 0.8940
P(X > 70) = 0.0478
Top 10% cutoff: 68.84
P(|Z| <= 1) = 0.6827
P(|Z| <= 2) = 0.9545
P(|Z| <= 3) = 0.9973
```
=======
>>>>>>> Stashed changes
