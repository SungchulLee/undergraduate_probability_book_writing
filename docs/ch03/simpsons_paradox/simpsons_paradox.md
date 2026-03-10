# Simpson's Paradox


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

## Definition

**Simpson's paradox** occurs when a trend that appears in each of several groups of data **reverses** when the groups are combined. The aggregate data shows the opposite conclusion from the stratified data.

## Example — Good Doctor vs. Bad Doctor

| Doctor A | Successes | Fails | Success Rate |
|----------|-----------|-------|-------------|
| Easy operation | 10 | 0 | **100%** |
| Hard operation | 75 | 15 | **83%** |
| **Total** | **85** | **15** | **85%** |

| Doctor B | Successes | Fails | Success Rate |
|----------|-----------|-------|-------------|
| Easy operation | 85 | 5 | 94% |
| Hard operation | 1 | 9 | 10% |
| **Total** | **86** | **14** | **86%** |

Doctor A has a higher success rate **in both categories** (100% vs. 94% for easy operations; 83% vs. 10% for hard operations), yet Doctor B has a higher **overall** success rate (86% vs. 85%).

### Explanation

The paradox arises because the two doctors have very different **case mixes**. Doctor A predominantly performs hard operations (90 out of 100), while Doctor B predominantly performs easy operations (90 out of 100). The aggregate rate is dominated by the type of operation each doctor performs most, masking the within-category advantage of Doctor A.

## Example — Berkeley Gender Bias Case

One of the best-known real-life examples of Simpson's paradox occurred at the University of California, Berkeley, which was sued for bias against women in graduate admissions for fall 1973.

### Aggregate Data

| | Applicants | Admitted Rate |
|---|-----------|-------------|
| Men | 8,442 | 44% |
| Women | 4,321 | 35% |

The difference was large enough to appear statistically significant.

### Department-Level Data

When examining the six largest departments individually, no department showed significant bias against women. In fact, most showed a small but statistically significant bias **in favor of women**:

| Dept | Male Applicants (Admitted) | Female Applicants (Admitted) |
|------|---------------------------|------------------------------|
| A | 825 (62%) | 108 (82%) |
| B | 560 (63%) | 25 (68%) |
| C | 325 (37%) | 593 (34%) |
| D | 417 (33%) | 375 (35%) |
| E | 191 (28%) | 393 (24%) |
| F | 272 (6%) | 341 (7%) |

### Resolution

Women tended to apply to more competitive departments (C, D, E, F) with lower overall admission rates, while men applied more to less competitive departments (A, B) with higher acceptance rates. The aggregate statistic confounded the effect of gender with the choice of department.

## Connection to Conditional Probability

Simpson's paradox is fundamentally about the difference between conditional and marginal probabilities. Let $S$ = success, $G$ = group (e.g., gender), and $C$ = category (e.g., department). It is possible that:

$$
P(S \mid G = A,\; C = c) > P(S \mid G = B,\; C = c) \quad \text{for all } c
$$

yet

$$
P(S \mid G = A) < P(S \mid G = B)
$$

The marginal relationship reverses the conditional relationships because the **lurking variable** $C$ has different distributions across groups. Formally, the marginal success rate is:

$$
P(S \mid G = g) = \sum_{c} P(S \mid G = g, C = c)\,P(C = c \mid G = g)
$$

Even if every term $P(S \mid G = A, C = c) > P(S \mid G = B, C = c)$, the weighted average can reverse if the weights $P(C = c \mid G = g)$ are sufficiently different.

!!! warning "Practical Lesson"
    Always consider whether a lurking variable (confounding factor) could be driving an apparent trend. Aggregate statistics can be misleading when subgroups have different compositions. This insight is central to causal inference, observational studies, and experimental design.
