# Discrete Uniform Distribution
<<<<<<< Updated upstream

## Motivation

When all outcomes are equally likely -- rolling a fair die, picking a random integer, selecting a lottery number -- we have a **discrete uniform distribution**. This is the mathematical formalization of the classical "equally likely outcomes" model from Chapter 2. Despite its simplicity, it appears throughout probability as a building block and a benchmark.

## Definition

A random variable $X$ has a **Discrete Uniform distribution** on $\{a, a+1, \ldots, b\}$, written $X \sim \text{DiscreteUniform}(a, b)$, if each value is equally likely:

$$
P(X = k) = \frac{1}{n}, \quad k = a, a+1, \ldots, b
$$

where $n = b - a + 1$ is the number of possible values.

!!! info "Discrete Uniform PMF"
    The PMF is flat: every outcome has the same probability $1/n$. This is the defining feature that distinguishes the uniform from all other distributions.

---

## Mean

By symmetry, the distribution is centered at the midpoint of its support:

$$
E[X] = \frac{1}{n}\sum_{k=a}^{b} k = \frac{a + b}{2}
$$

This can also be seen by noting that the PMF is symmetric about $(a+b)/2$.

---

## CDF

The CDF increases in equal steps of $1/n$:

$$
F(x) = \frac{\lfloor x \rfloor - a + 1}{n}, \quad a \le x \le b
$$

with $F(x) = 0$ for $x < a$ and $F(x) = 1$ for $x \ge b$.

---

## Variance and Further Properties

The variance, moment generating function, and sum of independent discrete uniforms are developed on the [Properties](properties.md) page:

$$
\text{Var}(X) = \frac{n^2 - 1}{12}
$$

---

## Examples

**Fair die.** Let $X$ be the outcome of rolling a standard die: $X \sim \text{DiscreteUniform}(1, 6)$.

- $n = 6$ values, each with probability $1/6$.
- $E[X] = (1 + 6)/2 = 3.5$.
- $\text{Var}(X) = (36 - 1)/12 = 35/12 \approx 2.917$.
- $P(X \le 4) = 4/6 = 2/3$.

**Random digit.** Select a digit uniformly at random from $\{0, 1, \ldots, 9\}$: $X \sim \text{DiscreteUniform}(0, 9)$.

- $E[X] = 4.5$.
- $\text{Var}(X) = (100 - 1)/12 = 99/12 = 8.25$.

**Lottery draw.** Pick a number from $\{1, 2, \ldots, 49\}$ uniformly at random: $E[X] = 25$ and $\text{Var}(X) = (49^2 - 1)/12 = 200$.

---

## Connection to Classical Probability

Any experiment with $n$ equally likely outcomes and a numerical labeling produces a discrete uniform random variable. The probability of an event $A$ in the classical model is

$$
P(A) = \frac{|A|}{n}
$$

which is simply $P(X \in A)$ when $X \sim \text{DiscreteUniform}(1, n)$. The discrete uniform distribution is where counting methods from Chapter 1 meet the formal probability framework of Chapter 2.
=======
>>>>>>> Stashed changes
