# Applications of Bayes' Theorem

Bayes' theorem produces results that often defy intuition: a 95%-accurate test can give a 99% chance of being wrong, and a doctor who is better in every category can be worse overall. These applications sharpen understanding of conditional probability.

## Definition

This page applies Bayes' theorem and the law of total probability to two settings:

1. **False positive problem:** Why accurate tests produce unreliable results when the condition is rare
2. **Simpson's paradox:** How conditional relationships can reverse when data is aggregated

## Explanation

### False Positives and Base Rate Neglect

When a condition is rare, even a small false positive rate applied to the large healthy population generates far more false alarms than true detections. Ignoring the base rate (prevalence) is called **base rate neglect** and is one of the most common errors in probabilistic reasoning.

### Simpson's Paradox

Simpson's paradox occurs when a trend present in every subgroup **reverses** in the aggregate:

$$
P(S \mid G\!=\!A,\, C\!=\!c) > P(S \mid G\!=\!B,\, C\!=\!c) \quad \text{for all } c
$$

does **not** imply $P(S \mid G\!=\!A) > P(S \mid G\!=\!B)$.

The reversal happens because the groups have different distributions over the confounding variable $C$.

## Examples

**Example 1 (Good doctor, bad odds).** Two doctors perform easy and hard operations:

| Doctor A | Success | Fail | Rate |
|:---|:---:|:---:|:---:|
| Easy | 10 | 0 | 100% |
| Hard | 75 | 15 | 83% |
| **Total** | **85** | **15** | **85%** |

| Doctor B | Success | Fail | Rate |
|:---|:---:|:---:|:---:|
| Easy | 85 | 5 | 94% |
| Hard | 1 | 9 | 10% |
| **Total** | **86** | **14** | **86%** |

Doctor A is better in *both* categories (100% vs 94%, 83% vs 10%), yet Doctor B has a higher overall rate (86% vs 85%). The paradox: Doctor A handles mostly hard cases while Doctor B handles mostly easy ones.

---

**Example 2 (Berkeley admissions).** UC Berkeley was sued for gender bias in 1973 graduate admissions.

Aggregate: Men 44% admitted, Women 35%. But department-level data showed slight bias *in favor of* women in most departments. The explanation: women applied disproportionately to competitive departments with low admission rates.

```python
# Example 1: Simpson's paradox
# Doctor A
A_easy = (10, 0)   # (success, fail)
A_hard = (75, 15)
A_total = (85, 15)

# Doctor B
B_easy = (85, 5)
B_hard = (1, 9)
B_total = (86, 14)

rate = lambda s, f: s / (s + f)
print("Doctor A: easy={:.0%}, hard={:.0%}, total={:.0%}".format(
    rate(*A_easy), rate(*A_hard), rate(*A_total)))
print("Doctor B: easy={:.0%}, hard={:.0%}, total={:.0%}".format(
    rate(*B_easy), rate(*B_hard), rate(*B_total)))
print("\nA better in both categories, but B better overall!")
```
