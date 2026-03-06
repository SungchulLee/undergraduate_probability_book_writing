# One-Sided Chebyshev's Inequality

## Statement

For any random variable $X$ with mean $\mu = \mathbb{E}X$ and variance $\sigma^2 = Var(X)$, and for $\varepsilon > 0$,

$$

P(X - \mathbb{E}X \geq \varepsilon) \leq \frac{\sigma^2}{\varepsilon^2 + \sigma^2}

$$

$$

P(X - \mathbb{E}X \leq -\varepsilon) \leq \frac{\sigma^2}{\varepsilon^2 + \sigma^2}

$$

This is also known as the **Cantelli inequality**.

## Proof

The key idea is to shift the random variable by a constant $b > 0$ and then apply Markov's inequality.

For any $b > 0$:

$$

X - \mathbb{E}X \geq \varepsilon \iff X - \mathbb{E}X + b \geq \varepsilon + b

$$

Since $\varepsilon + b > 0$, squaring preserves the inequality:

$$

\implies (X - \mathbb{E}X + b)^2 \geq (\varepsilon + b)^2

$$

Applying Markov's inequality:

$$

P(X - \mathbb{E}X \geq \varepsilon) \leq \frac{\mathbb{E}(X - \mathbb{E}X + b)^2}{(\varepsilon + b)^2} = \frac{\sigma^2 + b^2}{(\varepsilon + b)^2}

$$

where we used $\mathbb{E}(X - \mu + b)^2 = Var(X) + b^2$.

Minimizing over $b > 0$: set $b = \frac{\sigma^2}{\varepsilon}$ to obtain

$$

P(X - \mathbb{E}X \geq \varepsilon) \leq \frac{\sigma^2 + \sigma^4/\varepsilon^2}{(\varepsilon + \sigma^2/\varepsilon)^2} = \frac{\sigma^2}{\varepsilon^2 + \sigma^2}

$$

## Comparison with Chebyshev

The standard Chebyshev inequality bounds $P(|X - \mu| \geq \varepsilon) \leq \sigma^2 / \varepsilon^2$. Since $|X - \mu| \geq \varepsilon$ includes both tails, for a **one-sided** bound the one-sided Chebyshev is tighter:

$$

\frac{\sigma^2}{\varepsilon^2 + \sigma^2} \leq \frac{\sigma^2}{\varepsilon^2}

$$

## Example: Binomial X ~ B(1000, 0.01)

With $\mathbb{E}X = 10$, $Var(X) = 9.9$, bound $P(X \geq 20) = P(X - 10 \geq 10)$:

$$

P(X - 10 \geq 10) \leq \frac{9.9}{10^2 + 9.9} = \frac{9.9}{109.9} = 0.0901

$$

Compare with Chebyshev: $0.0990$. The one-sided bound is tighter.

## Example: Poisson X ~ Poi(100)

With $\mathbb{E}X = 100$, $Var(X) = 100$, bound $P(X \geq 200) = P(X - 100 \geq 100)$:

$$

P(X - 100 \geq 100) \leq \frac{100}{100^2 + 100} = \frac{100}{10100} = 0.0099

$$

Compare with Chebyshev: $0.0100$.
