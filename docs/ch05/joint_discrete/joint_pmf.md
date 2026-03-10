# Joint PMF


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

## Random Vectors

A **random vector** is a function that maps outcomes from a sample space to $\mathbb{R}^d$:

$$\mathbf{X} : \Omega \longrightarrow \mathbb{R}^d$$

For a pair of discrete random variables $(X, Y)$, the random vector maps each outcome $\omega$ to the point $(X(\omega), Y(\omega))$ in $\mathbb{R}^2$.

## Joint Distribution via the Brick Analogy

The **joint distribution** of $(X, Y)$ is defined by moving bricks from $\Omega$ to $\mathbb{R}^2$:

- Each outcome $\omega$ has a brick with weight $P(\{\omega\})$.
- The function $\mathbf{X}$ moves each brick from $\omega$ to $\mathbf{X}(\omega)$ in $\mathbb{R}^d$.
- The total weight of all bricks in $\mathbb{R}^d$ is 1.
- This weight distribution over $\mathbb{R}^d$ is the **joint distribution** of $\mathbf{X}$.

## Definition of Joint PMF

For discrete random variables $X$ and $Y$, the **joint PMF** is:

$$p(x, y) = P(X = x, Y = y)$$

This gives the weight of the brick at each point $(x, y)$ in $\mathbb{R}^2$.

## Properties

1. **Non-negativity:** $p(x, y) \ge 0$ for all $(x, y)$.
2. **Normalization:** $\displaystyle\sum_x \sum_y p(x, y) = 1$.

## Computing Probabilities

For any set $A \subseteq \mathbb{R}^2$:

$$P((X, Y) \in A) = \sum_{(x,y) \in A} p(x, y)$$

## Example: Coin Flips

Consider flipping a fair coin 3 times. Let $X$ = number of heads in the first two flips, and $Y$ = total number of heads.

The sample space and the mapping to $(X, Y)$:

| Outcome | $X$ | $Y$ |
|---------|-----|-----|
| HHH | 2 | 3 |
| HHT | 2 | 2 |
| HTH | 1 | 2 |
| HTT | 1 | 1 |
| THH | 1 | 2 |
| THT | 1 | 1 |
| TTH | 0 | 1 |
| TTT | 0 | 0 |

The joint PMF table (each outcome has probability $1/8$):

| | $X=0$ | $X=1$ | $X=2$ |
|---|---|---|---|
| $Y=3$ | 0 | 0 | $1/8$ |
| $Y=2$ | 0 | $2/8$ | $1/8$ |
| $Y=1$ | $1/8$ | $2/8$ | 0 |
| $Y=0$ | $1/8$ | 0 | 0 |

Note that $Y \ge X$ always holds (the total heads cannot be less than heads in the first two flips), so some entries are necessarily 0.
