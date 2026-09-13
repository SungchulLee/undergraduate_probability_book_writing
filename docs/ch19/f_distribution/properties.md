# 성질

## 평균과 분산

| 성질 | 값 | 조건 |
|----------|-------|-----------|
| 평균 | $\frac{d_2}{d_2 - 2}$ | $d_2 > 2$ |
| 분산 | $\frac{2d_2^2(d_1 + d_2 - 2)}{d_1(d_2 - 2)^2(d_2 - 4)}$ | $d_2 > 4$ |
| 최빈값 | $\frac{d_1 - 2}{d_1} \cdot \frac{d_2}{d_2 + 2}$ | $d_1 > 2$ |

!!! note
    평균은 $d_1$ 과는 상관없이 **오직** $d_2$ 에만 달려 있다. $d_2$ 가 작으면 평균이 $1$ 보다 꽤 클 수 있다.

## 주요 성질

### 받침과 모양

F분포의 받침은 $(0, \infty)$ 이고 **오른쪽으로 치우쳐** 있다. $d_1$ 과 $d_2$ 가 모두 커질수록 왜도는 줄어든다.

### 역수 성질

$F \sim F_{d_1, d_2}$ 이면 다음이 성립한다.

$$\frac{1}{F} \sim F_{d_2, d_1}$$

이는 정의에서 바로 따라 나온다. 분자와 분모를 맞바꾸면 자유도도 맞바뀐다.

## t분포와의 관계

$T \sim t_d$ 이면 다음이 성립한다.

$$T^2 \sim F_{1, d}$$

**증명.** 독립인 $Z \sim N(0,1)$ 과 $V \sim \chi^2_d$ 에 대하여 $T = Z / \sqrt{V/d}$ 로 쓰면 다음과 같다.

$$T^2 = \frac{Z^2}{V/d} = \frac{Z^2 / 1}{V / d} = \frac{\chi^2_1 / 1}{\chi^2_d / d} \sim F_{1, d}$$

이 관계는 자유도가 $d$ 인 양쪽꼬리 $t$ 검정이 자유도가 $(1, d)$ 인 $F$ 검정과 같음을 뜻한다.

## 베타분포와의 관계

$F \sim F_{d_1, d_2}$ 이면 다음이 성립한다.

$$\frac{d_1 F / d_2}{1 + d_1 F / d_2} \sim \text{Beta}\!\left(\frac{d_1}{2}, \frac{d_2}{2}\right)$$

## 파이썬으로 살펴보기

```python
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

x = np.linspace(0.01, 5, 500)

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# d1 을 바꾸어 가며 그리기
ax = axes[0]
d2 = 10
for d1 in [1, 2, 5, 10, 30]:
    ax.plot(x, stats.f.pdf(x, d1, d2), label=f'$F_{{{d1},{d2}}}$')
ax.set_title(f'Varying $d_1$ (fixed $d_2 = {d2}$)')
ax.set_xlabel('$x$'); ax.set_ylabel('Density')
ax.legend()

# d2 를 바꾸어 가며 그리기
ax = axes[1]
d1 = 5
for d2 in [3, 5, 10, 30, 100]:
    ax.plot(x, stats.f.pdf(x, d1, d2), label=f'$F_{{{d1},{d2}}}$')
ax.set_title(f'Varying $d_2$ (fixed $d_1 = {d1}$)')
ax.set_xlabel('$x$'); ax.set_ylabel('Density')
ax.legend()

plt.tight_layout()
plt.show()
```

## 연습문제

**연습문제 1.**
$F \sim F_{5, 10}$ 일 때 $E[F]$ 를 구하고 역수 성질을 모의실험으로 확인하여라.

??? success "연습문제 1 풀이"
    $E[F] = \frac{d_2}{d_2 - 2} = \frac{10}{8} = 1.25$ 이다.

    ```python
    import numpy as np
    from scipy import stats

    np.random.seed(42)
    f_samples = np.random.f(5, 10, 100_000)
    print(f"Simulated mean of F(5,10): {f_samples.mean():.4f}  (theory: 1.25)")

    # 역수 성질
    recip = 1.0 / f_samples
    ks_stat, pval = stats.kstest(recip, 'f', args=(10, 5))
    print(f"KS test 1/F(5,10) ~ F(10,5): p = {pval:.4f}")
    ```
