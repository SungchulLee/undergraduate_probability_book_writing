# Continuity Correction

## The Problem

When using the CLT to approximate probabilities for **discrete** random variables with a **continuous** normal distribution, a systematic error occurs at the boundaries. The continuity correction adjusts for this.

## The Idea

A discrete random variable $X$ that takes integer values satisfies:

$$P(X = k) = P(k - 0.5 \leq X \leq k + 0.5)$$

in the continuous approximation. Each integer value "occupies" a unit interval centered at that integer.

Therefore:

| Discrete Probability | With Continuity Correction |
|---------------------|---------------------------|
| $P(X \leq k)$ | $P(X \leq k + 0.5)$ |
| $P(X \geq k)$ | $P(X \geq k - 0.5)$ |
| $P(X < k)$ | $P(X \leq k - 0.5)$ |
| $P(X > k)$ | $P(X \geq k + 0.5)$ |
| $P(X = k)$ | $P(k - 0.5 \leq X \leq k + 0.5)$ |

## Example: Poisson with Continuity Correction

Let $X \sim \text{Po}(100)$. To find $P(X \geq 120)$:

**Without continuity correction:**

$$P(X \geq 120) = P\left(\frac{X - 100}{\sqrt{100}} \geq \frac{120 - 100}{\sqrt{100}}\right) \approx 1 - \Phi(2.0) = 0.0228$$

**With continuity correction:**

$$P(X \geq 120) = P(X \geq 119.5) = P\left(\frac{X - 100}{\sqrt{100}} \geq \frac{119.5 - 100}{\sqrt{100}}\right) \approx 1 - \Phi(1.95) = 0.0256$$

**Exact value:** $P(X \geq 120) = 0.0282$

The continuity-corrected answer ($0.0256$) is closer to the exact value ($0.0282$) than the uncorrected answer ($0.0228$).

## When to Use Continuity Correction

- **Use it** when approximating a discrete distribution (Binomial, Poisson, Geometric, etc.) with the normal distribution.
- **Skip it** when the original random variable is already continuous.

!!! tip "Rule of Thumb"
    Continuity correction is most important when $n$ is moderate. For very large $n$, the correction becomes negligible relative to $\sigma\sqrt{n}$.
