# Sample Spaces and Outcomes

The sample space is the starting point of every probability model. Before assigning probabilities, we must specify what outcomes are possible.

## Definition

An **experiment** is any procedure with observable results. An **outcome** (or **sample point**) $\omega$ is a single result. The **sample space** $\Omega$ is the set of all possible outcomes:

$$
\Omega = \{\text{all possible outcomes } \omega\}
$$

Sample spaces are classified by size:

- **Finite:** $|\Omega| < \infty$ (e.g., rolling a die: $\Omega = \{1,2,3,4,5,6\}$)
- **Countably infinite:** in bijection with $\mathbb{N}$ (e.g., counting coin flips until first heads)
- **Uncountable:** cardinality of $\mathbb{R}$ (e.g., measuring a stock return: $\Omega = \mathbb{R}$)

## Explanation

### The Probability Measure

For a discrete sample space, assign a "weight" $P(\{\omega\})$ to each outcome, with all weights non-negative and summing to 1. The probability of any event $A \subseteq \Omega$ is

$$
P(A) = \sum_{\omega \in A} P(\{\omega\})
$$

Think of each weight as a brick on a number line: the probability of $A$ is the total mass of bricks landing inside $A$.

### Choosing the Right Sample Space

The sample space must be chosen with care:

- It must include *every* possible outcome (exhaustive)
- Outcomes should be *mutually exclusive* (each run of the experiment produces exactly one $\omega$)
- The sample space should be as coarse as needed — don't distinguish outcomes you'll never care about

## Examples

**Example 1 (Three coin flips).**

$$
\Omega = \{HHH, HHT, HTH, HTT, THH, THT, TTH, TTT\}, \quad |\Omega| = 8
$$

Under the fair-coin model, each outcome has probability $1/8$.

**Example 2 (Rolling two dice).** $\Omega = \{(i,j) : 1 \le i,j \le 6\}$, so $|\Omega| = 36$.

```python
# Three coin flips
omega = ['HHH', 'HHT', 'HTH', 'HTT', 'THH', 'THT', 'TTH', 'TTT']
prob = {w: 1/len(omega) for w in omega}

A = [w for w in omega if w.count('H') >= 2]
print(f"|Ω| = {len(omega)}")
print(f"P(at least 2 heads) = {len(A)}/{len(omega)} = {sum(prob[w] for w in A):.4f}")
```
