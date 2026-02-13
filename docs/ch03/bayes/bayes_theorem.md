# Bayes' Theorem and Prior–Posterior Updating

## Bayes' Rule

**Bayes' theorem** provides a way to "reverse" a conditional probability — computing $P(B \mid A)$ from $P(A \mid B)$:

$$
P(B \mid A) = \frac{P(A \mid B)\,P(B)}{P(A)}
$$

### Derivation

From the definition of conditional probability and the chain rule:

$$
P(AB) = P(A)\,P(B \mid A) = P(B)\,P(A \mid B)
$$

Solving for $P(B \mid A)$:

$$
P(B \mid A) = \frac{P(B)\,P(A \mid B)}{P(A)}
$$

## Bayes' Rule with Total Probability

When the sample space is partitioned as $\Omega = \bigcup_{k=1}^{n} B_k$ (disjointly), Bayes' rule becomes:

$$
P(B_1 \mid A) = \frac{P(B_1)\,P(A \mid B_1)}{\displaystyle\sum_{k=1}^{n} P(B_k)\,P(A \mid B_k)}
$$

More generally, for any $B_j$ in the partition:

$$
P(B_j \mid A) = \frac{P(B_j)\,P(A \mid B_j)}{\displaystyle\sum_{k=1}^{n} P(B_k)\,P(A \mid B_k)}
$$

## Prior–Posterior Interpretation

Bayes' theorem is the foundation of **Bayesian inference**, which updates beliefs in light of evidence:

| Term | Expression | Interpretation |
|------|-----------|----------------|
| **Prior** | $P(B_j)$ | Initial belief about $B_j$ before observing data |
| **Likelihood** | $P(A \mid B_j)$ | How likely the observed data $A$ is under hypothesis $B_j$ |
| **Evidence** (marginal likelihood) | $P(A) = \sum_k P(B_k)\,P(A \mid B_k)$ | Total probability of observing $A$ |
| **Posterior** | $P(B_j \mid A)$ | Updated belief about $B_j$ after observing data $A$ |

The updating formula can be summarized as:

$$
\text{Posterior} = \frac{\text{Likelihood} \times \text{Prior}}{\text{Evidence}}
$$

## Odds Form of Bayes' Rule

For two competing hypotheses $B_1$ and $B_2$, the **posterior odds** equal the **prior odds** times the **likelihood ratio** (also called the Bayes factor):

$$
\frac{P(B_1 \mid A)}{P(B_2 \mid A)} = \frac{P(B_1)}{P(B_2)} \cdot \frac{P(A \mid B_1)}{P(A \mid B_2)}
$$

$$
\text{Posterior odds} = \text{Prior odds} \times \text{Bayes factor}
$$

This form is useful because the normalizing constant $P(A)$ cancels out.
