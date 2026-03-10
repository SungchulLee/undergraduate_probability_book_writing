# Simpson's Paradox

Simpson's paradox occurs when a trend present in every subgroup reverses in the aggregate. It is a fundamental warning about confounding variables and the dangers of naive data aggregation.

## Definition

Simpson's paradox: it is possible that

$$
P(S \mid G\!=\!A,\, C\!=\!c) > P(S \mid G\!=\!B,\, C\!=\!c) \quad \text{for all } c
$$

yet $P(S \mid G\!=\!A) < P(S \mid G\!=\!B)$.

The reversal occurs because the confounding variable $C$ has different distributions across groups:

$$
P(S \mid G\!=\!g) = \sum_c P(S \mid G\!=\!g,\, C\!=\!c)\,P(C\!=\!c \mid G\!=\!g)
$$

Even if every conditional term favors group $A$, the weighted average can reverse if the weights differ enough.

## Explanation

The paradox arises from **confounding**: the groups being compared differ systematically in their exposure to the lurking variable $C$. The aggregate statistic conflates the effect of the treatment with the effect of the confound.

The practical lesson: always check whether a confounding variable could drive an apparent trend. Aggregate statistics are reliable only when subgroups have similar compositions.

## Examples

**Example 1 (Good doctor, bad odds).**

| Doctor A | Easy | Hard | Total |
|:---|:---:|:---:|:---:|
| Success rate | 100% (10/10) | 83% (75/90) | 85% |

| Doctor B | Easy | Hard | Total |
|:---|:---:|:---:|:---:|
| Success rate | 94% (85/90) | 10% (1/10) | 86% |

Doctor A is better in **both** categories, yet Doctor B has higher overall rate. The confound: Doctor A handles mostly hard cases.

---

**Example 2 (Berkeley admissions, 1973).** Aggregate: men 44%, women 35% admitted. Department-level: most departments slightly favored women. The confound: women applied disproportionately to competitive departments.

| Dept | Men (admitted) | Women (admitted) |
|:---|:---:|:---:|
| A | 825 (62%) | 108 (82%) |
| B | 560 (63%) | 25 (68%) |
| C | 325 (37%) | 593 (34%) |
| D | 417 (33%) | 375 (35%) |
| E | 191 (28%) | 393 (24%) |
| F | 272 (6%) | 341 (7%) |

```python
# Doctor example
A_easy, A_hard = (10, 0), (75, 15)
B_easy, B_hard = (85, 5), (1, 9)

rate = lambda s, f: s / (s + f) if s + f > 0 else 0
for label, easy, hard in [("A", A_easy, A_hard), ("B", B_easy, B_hard)]:
    total_s = easy[0] + hard[0]
    total_f = easy[1] + hard[1]
    print(f"Doctor {label}: easy={rate(*easy):.0%}, hard={rate(*hard):.0%}, "
          f"total={rate(total_s, total_f):.0%}")
```
