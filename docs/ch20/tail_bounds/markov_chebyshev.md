# Tail Bounds: Markov and Chebyshev Inequalities

Tail bounds provide **upper bounds** on the probability that a random variable deviates from its mean by a large amount. These are essential tools for proving the Law of Large Numbers.

## Markov's Inequality

For any nonnegative random variable $|X|$ and $\varepsilon > 0$,

$$

P(|X| \geq \varepsilon) \leq \frac{\mathbb{E}|X|}{\varepsilon}

$$

**Intuition**: If $X$ has a small expected value, then $X$ cannot be large too often. Markov's inequality makes this precise using only the first moment.

## Chebyshev's Inequality

For any random variable $X$ with finite mean $\mu$ and variance $\sigma^2$, and for $\varepsilon > 0$,

$$

P(|X - \mathbb{E}X| \geq \varepsilon) \leq \frac{Var(X)}{\varepsilon^2}

$$

**Proof**: Apply Markov's inequality to $(X - \mu)^2$:

$$

P(|X - \mu| \geq \varepsilon) = P((X - \mu)^2 \geq \varepsilon^2) \leq \frac{\mathbb{E}(X - \mu)^2}{\varepsilon^2} = \frac{\sigma^2}{\varepsilon^2}

$$

**Intuition**: Chebyshev uses the variance (second moment) to give a tighter bound than Markov. If the variance is small, the random variable is concentrated around its mean.

## Geometric Interpretation

- **Markov**: The area under the curve of $f_{|X|}(x)$ to the right of $\varepsilon$ is bounded by the total area (expectation) divided by $\varepsilon$.
- **Chebyshev**: The area under the curve of $f_{(X-\mu)^2}(x)$ to the right of $\varepsilon^2$ is bounded by the variance divided by $\varepsilon^2$.

## Example: Binomial X ~ B(1000, 0.01)

Here $\mathbb{E}X = np = 10$ and $Var(X) = npq = 9.9$.

**Bound $P(X \geq 20)$:**

**Markov:**

$$

P(X \geq 20) \leq \frac{\mathbb{E}X}{20} = \frac{10}{20} = 0.5

$$

**Chebyshev:**

$$

P(X \geq 20) \leq P(|X - 10| \geq 10) \leq \frac{9.9}{10^2} = 0.0990

$$

**Bound $P(X \geq 100)$:**

**Markov:**

$$

P(X \geq 100) \leq \frac{10}{100} = 0.1

$$

**Chebyshev:**

$$

P(X \geq 100) \leq P(|X - 10| \geq 90) \leq \frac{9.9}{90^2} = 0.0012

$$

## Example: Poisson X ~ Poi(100)

Here $\mathbb{E}X = \lambda = 100$ and $Var(X) = \lambda = 100$.

**Bound $P(X \geq 200)$:**

**Markov:**

$$

P(X \geq 200) \leq \frac{100}{200} = 0.5

$$

**Chebyshev:**

$$

P(X \geq 200) \leq P(|X - 100| \geq 100) \leq \frac{100}{100^2} = 0.0100

$$
