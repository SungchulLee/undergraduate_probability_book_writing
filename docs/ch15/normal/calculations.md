# Normal Probability Calculations

Computing probabilities for the normal distribution reduces to standardization: convert to Z-scores, then evaluate the standard normal CDF $\Phi$.

## Definition

For $X \sim N(\mu, \sigma^2)$, the probability that $X$ falls in the interval $(a, b)$ is:

$$
P(a < X < b) = \Phi\!\left(\frac{b - \mu}{\sigma}\right) - \Phi\!\left(\frac{a - \mu}{\sigma}\right)
$$

where $\Phi$ is the CDF of the standard normal $N(0,1)$.

The **standardization technique** converts any normal probability into a standard normal probability via the substitution $Z = (X - \mu)/\sigma$:

$$
P(X \leq x) = P\!\left(Z \leq \frac{x - \mu}{\sigma}\right) = \Phi\!\left(\frac{x - \mu}{\sigma}\right)
$$

## Explanation

### The three-step calculation procedure

Every normal probability calculation follows the same pattern:

**Step 1.** Identify $\mu$ and $\sigma$ from the problem.

**Step 2.** Standardize the bounds: replace each bound $x$ with $z = (x - \mu)/\sigma$.

**Step 3.** Evaluate using $\Phi$: use $\Phi(z)$, the symmetry identity $\Phi(-z) = 1 - \Phi(z)$, and the interval formula $P(a < Z < b) = \Phi(b) - \Phi(a)$.

### Common probability patterns

| Desired probability | Formula |
|---|---|
| $P(X \leq x)$ | $\Phi\!\left(\frac{x-\mu}{\sigma}\right)$ |
| $P(X \geq x)$ | $1 - \Phi\!\left(\frac{x-\mu}{\sigma}\right)$ |
| $P(a < X < b)$ | $\Phi\!\left(\frac{b-\mu}{\sigma}\right) - \Phi\!\left(\frac{a-\mu}{\sigma}\right)$ |
| $P(\lvert X - \mu \rvert < k\sigma)$ | $2\Phi(k) - 1$ |

### Inverse problems (finding cutoffs)

Sometimes the probability is given and you need to find the cutoff value $x$. If $P(X \leq x) = p$, then:

$$
\frac{x - \mu}{\sigma} = \Phi^{-1}(p) \quad \implies \quad x = \mu + \sigma \, \Phi^{-1}(p)
$$

### Continuity considerations

Since the normal distribution is continuous, $P(X = x) = 0$ for any single point $x$. This means:

$$
P(X \leq x) = P(X < x), \qquad P(a \leq X \leq b) = P(a < X < b)
$$

Strict and non-strict inequalities give the same result for continuous distributions.

### Working with symmetric intervals

For intervals symmetric about the mean, the calculation simplifies. If $X \sim N(\mu, \sigma^2)$:

$$
P(\lvert X - \mu \rvert < c) = P(-c < X - \mu < c) = P\!\left(-\frac{c}{\sigma} < Z < \frac{c}{\sigma}\right) = 2\Phi\!\left(\frac{c}{\sigma}\right) - 1
$$

The inverse question -- find $c$ such that $P(\lvert X - \mu \rvert < c) = 1 - \alpha$ -- gives:

$$
c = \sigma \, \Phi^{-1}\!\left(1 - \frac{\alpha}{2}\right) = \sigma \, z_{1-\alpha/2}
$$

## Examples

**Example 1: Interval probability.**

Let $X \sim N(50, 8^2)$. Find $P(42 < X < 62)$.

$$
P(42 < X < 62) = \Phi\!\left(\frac{62 - 50}{8}\right) - \Phi\!\left(\frac{42 - 50}{8}\right) = \Phi(1.5) - \Phi(-1) = 0.9332 - 0.1587 = 0.7745
$$

```python
from scipy import stats

mu, sigma = 50, 8
p = stats.norm.cdf(62, mu, sigma) - stats.norm.cdf(42, mu, sigma)
print(f"P(42 < X < 62) = Phi({(62-mu)/sigma}) - Phi({(42-mu)/sigma})")
print(f"               = {stats.norm.cdf((62-mu)/sigma):.4f} - {stats.norm.cdf((42-mu)/sigma):.4f}")
print(f"               = {p:.4f}")
```

**Output:**
```
P(42 < X < 62) = Phi(1.5) - Phi(-1.0)
               = 0.9332 - 0.1587
               = 0.7745
```

**Example 2: Tail probability.**

The lifetime of a component follows $X \sim N(1000, 100^2)$ hours. Find the probability it lasts more than 1150 hours.

$$
P(X > 1150) = 1 - \Phi\!\left(\frac{1150 - 1000}{100}\right) = 1 - \Phi(1.5) = 1 - 0.9332 = 0.0668
$$

```python
from scipy import stats

mu, sigma = 1000, 100
x = 1150
z = (x - mu) / sigma
p = 1 - stats.norm.cdf(z)
print(f"Z-score: z = ({x} - {mu}) / {sigma} = {z:.1f}")
print(f"P(X > {x}) = 1 - Phi({z:.1f}) = 1 - {stats.norm.cdf(z):.4f} = {p:.4f}")
```

**Output:**
```
Z-score: z = (1150 - 1000) / 100 = 1.5
P(X > 1150) = 1 - Phi(1.5) = 1 - 0.9332 = 0.0668
```

**Example 3: Finding a cutoff (inverse problem).**

Exam scores follow $X \sim N(72, 9^2)$. The top 10% of students receive an A. What is the minimum score for an A?

$$
P(X \geq x) = 0.10 \implies P(X \leq x) = 0.90 \implies x = 72 + 9 \cdot \Phi^{-1}(0.90)
$$

```python
from scipy import stats

mu, sigma = 72, 9
z_90 = stats.norm.ppf(0.90)
cutoff = mu + sigma * z_90
print(f"z_{{0.90}} = {z_90:.4f}")
print(f"Minimum A score = {mu} + {sigma} * {z_90:.4f} = {cutoff:.2f}")
print(f"Verification: P(X >= {cutoff:.2f}) = {1 - stats.norm.cdf(cutoff, mu, sigma):.4f}")
```

**Output:**
```
z_{0.90} = 1.2816
Minimum A score = 72 + 9 * 1.2816 = 83.53
Verification: P(X >= 83.53) = 0.1000
```

**Example 4: Symmetric interval.**

A machine fills bottles to a target of $\mu = 500$ mL with $\sigma = 3$ mL. Find the interval that contains 99% of all fill levels.

$$
P(\lvert X - 500 \rvert < c) = 0.99 \implies c = 3 \cdot z_{0.995}
$$

```python
from scipy import stats

mu, sigma = 500, 3
z_995 = stats.norm.ppf(0.995)
c = sigma * z_995
print(f"z_{{0.995}} = {z_995:.4f}")
print(f"Half-width c = {sigma} * {z_995:.4f} = {c:.2f} mL")
print(f"99% of bottles have fill level in ({mu - c:.2f}, {mu + c:.2f}) mL")

# Verify
p = stats.norm.cdf(mu + c, mu, sigma) - stats.norm.cdf(mu - c, mu, sigma)
print(f"Verification: P({mu - c:.2f} < X < {mu + c:.2f}) = {p:.4f}")
```

**Output:**
```
z_{0.995} = 2.5758
Half-width c = 3 * 2.5758 = 7.73 mL
99% of bottles have fill level in (492.27, 507.73) mL
Verification: P(492.27 < X < 507.73) = 0.9900
```
