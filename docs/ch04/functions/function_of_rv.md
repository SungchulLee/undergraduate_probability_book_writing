# Distribution of g(X)

## Functions of a Random Variable

If $X$ is a random variable and $g : \mathbb{R} \to \mathbb{R}$ is a function, then $Y = g(X)$ is also a random variable. The distribution of $Y$ is determined by the distribution of $X$ and the function $g$.

## Discrete Case

If $X$ is discrete with PMF $p_X(x)$, then $Y = g(X)$ is discrete with:

$$P(Y = y) = \sum_{x : g(x) = y} P(X = x)$$

That is, collect all values of $X$ that map to the same $y$ and sum their probabilities.

## Example: Generating +/-1 from Bernoulli

If $X \sim \text{B}(p)$, then $Y = 2X - 1$ has distribution:

$$Y = \begin{cases} 1 & \text{with probability } p \\ -1 & \text{with probability } 1 - p \end{cases}$$

**Application to fair coin flips.** Suppose we flip a fair coin $n$ times independently and record each flip as $X_i \in \{0, 1\}$. Let $Y_i = 2X_i - 1$. Then:

$$X_i \stackrel{\text{iid}}{\sim} \begin{cases} 1 & \text{prob } 0.5 \\ 0 & \text{prob } 0.5 \end{cases} \implies Y_i \stackrel{\text{iid}}{\sim} \begin{cases} +1 & \text{prob } 0.5 \\ -1 & \text{prob } 0.5 \end{cases}$$

This transformation is widely used to convert Bernoulli random variables into symmetric $\pm 1$ random variables, which are fundamental in random walk models and financial applications.

## Continuous Case (Preview)

For continuous random variables, finding the distribution of $g(X)$ requires the **change of variables** technique (covered in Chapter 15), which uses the Jacobian of the transformation.
