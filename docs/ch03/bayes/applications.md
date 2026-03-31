# Applications of Bayes' Theorem

## Application 1 — False Positive (Medical Testing)

### Problem

A laboratory blood test is 95% effective in detecting a certain disease when it is, in fact, present. However, the test also yields a "false positive" result for 1% of healthy persons tested. If 0.01% of the population actually has the disease, what is the probability that a person has the disease given that the test result is positive?

### Events and Given Information

| Event | Description |
|-------|-------------|
| $H$ | Person is healthy |
| $D$ | Person has the disease |
| $h$ | Test reports healthy (negative) |
| $d$ | Test reports disease (positive) |

| Probability | Value | Meaning |
|-------------|-------|---------|
| $P(d \mid D) = 0.95$ | Sensitivity | True positive rate |
| $P(h \mid D) = 0.05$ | | False negative rate |
| $P(d \mid H) = 0.01$ | | False positive rate |
| $P(h \mid H) = 0.99$ | Specificity | True negative rate |
| $P(D) = 0.0001$ | Prevalence | Disease rate in population |
| $P(H) = 0.9999$ | | Healthy rate |

### Solution via Bayes' Rule + Total Probability

$$
P(D \mid d) = \frac{P(D)\,P(d \mid D)}{P(D)\,P(d \mid D) + P(H)\,P(d \mid H)}
$$

$$
= \frac{(0.0001)(0.95)}{(0.0001)(0.95) + (0.9999)(0.01)} = \frac{0.000095}{0.000095 + 0.009999} = 0.0094
$$

### Interpretation

Despite the test being 95% accurate, a positive result corresponds to only a **0.94% probability** of actually having the disease. The key insight: when the disease is very rare ($0.01\%$ prevalence), the vast majority of the population is healthy. Even a small false positive rate (1%) applied to this enormous healthy population produces many more false positives than the true positives from the tiny diseased population.

**Breakdown of positive test results per 1,000,000 people:**

| Group | Population | Positive tests | Rate |
|-------|-----------|---------------|------|
| Diseased | 100 | 95 | True positives |
| Healthy | 999,900 | 9,999 | False positives |
| **Total positive** | | **10,094** | |

Of the 10,094 positive tests, only 95 are true positives: $95/10{,}094 \approx 0.94\%$.

### Python Implementation

```python
import numpy as np

# Given
P_D = 0.0001       # prevalence
P_H = 1 - P_D
P_d_given_D = 0.95  # sensitivity
P_d_given_H = 0.01  # false positive rate

# Bayes' rule
P_D_given_d = (P_D * P_d_given_D) / (P_D * P_d_given_D + P_H * P_d_given_H)

print(f"P(D|d) = {P_D_given_d:.4f}")
# Output: P(D|d) = 0.0094

# Breakdown per million
pop = 1_000_000
diseased = pop * P_D
healthy = pop * P_H
true_pos = diseased * P_d_given_D
false_pos = healthy * P_d_given_H
total_pos = true_pos + false_pos

print(f"\nPer {pop:,} people:")
print(f"  True positives:  {true_pos:.0f}")
print(f"  False positives: {false_pos:.0f}")
print(f"  Total positive:  {total_pos:.0f}")
print(f"  P(D|d) = {true_pos/total_pos:.4f}")
```

## Application 2 — Simpson's Paradox

### The Paradox

**Simpson's paradox** occurs when a trend present in each subgroup of data **reverses** when the subgroups are combined.

### Example — Good Doctor vs. Bad Doctor

| Doctor A | Successes | Fails | Success Rate |
|----------|-----------|-------|-------------|
| Easy operation | 10 | 0 | 100% |
| Hard operation | 75 | 15 | 83% |
| **Total** | **85** | **15** | **85%** |

| Doctor B | Successes | Fails | Success Rate |
|----------|-----------|-------|-------------|
| Easy operation | 85 | 5 | 94% |
| Hard operation | 1 | 9 | 10% |
| **Total** | **86** | **14** | **86%** |

Doctor A has a **higher success rate in both categories** (100% vs. 94% for easy; 83% vs. 10% for hard), yet Doctor B has a higher **overall** success rate (86% vs. 85%).

The resolution: Doctor A takes on mostly hard operations, while Doctor B takes on mostly easy ones. The aggregate comparison is misleading because the composition of cases differs between doctors.

### Berkeley Gender Bias Case

One of the best-known real-life examples: the University of California, Berkeley was sued for bias against women in graduate admissions (fall 1973).

**Aggregate data:**

| | Applicants | Admitted Rate |
|---|-----------|-------------|
| Men | 8,442 | 44% |
| Women | 4,321 | 35% |

But examining individual departments revealed no significant bias against women — most departments had a small bias **in favor of women**:

| Dept | Male Applicants (Admitted) | Female Applicants (Admitted) |
|------|---------------------------|------------------------------|
| A | 825 (62%) | 108 (82%) |
| B | 560 (63%) | 25 (68%) |
| C | 325 (37%) | 593 (34%) |
| D | 417 (33%) | 375 (35%) |
| E | 191 (28%) | 393 (24%) |
| F | 272 (6%) | 341 (7%) |

The explanation: women tended to apply to more competitive departments (C, D, E, F) with lower overall admission rates, while men applied more to less competitive departments (A, B) with higher rates. The aggregate statistic confounds the effect of gender with the choice of department.

### Connection to Conditional Probability

Simpson's paradox illustrates the importance of proper conditioning. Let $S$ = success, $G$ = group (doctor or gender), and $C$ = category (operation type or department):

$$
P(S \mid G = A, C = c) > P(S \mid G = B, C = c) \quad \text{for all } c
$$

does **not** imply

$$
P(S \mid G = A) > P(S \mid G = B)
$$

The marginal relationship can reverse the conditional relationships when the groups have different distributions over categories.
