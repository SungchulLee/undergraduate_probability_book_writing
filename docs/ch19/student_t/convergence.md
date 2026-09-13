# 자유도가 무한대로 갈 때 정규분포로의 수렴

## 정리의 서술

자유도 $d \to \infty$ 일 때 다음이 성립한다.

$$t_d \xrightarrow{d} N(0, 1)$$

곧 t분포는 표준정규분포로 수렴한다.

## 직관적인 설명

정의를 떠올리자. $Z \sim N(0,1)$ 과 $V \sim \chi^2_d$ 가 독립일 때 $T = Z / \sqrt{V/d}$ 이다.

$W_i$ 가 i.i.d. $N(0,1)$ 일 때 $V = \sum_{i=1}^d W_i^2$ 이므로 큰수의 법칙에 따라 다음이 성립한다.

$$\frac{V}{d} = \frac{1}{d}\sum_{i=1}^d W_i^2 \xrightarrow{p} E[W_1^2] = 1$$

따라서 $\sqrt{V/d} \xrightarrow{p} 1$ 이고, 슬루츠키 정리에 따라 다음을 얻는다.

$$T = \frac{Z}{\sqrt{V/d}} \xrightarrow{d} \frac{Z}{1} = Z \sim N(0,1)$$

## 밀도함수의 각 점에서의 수렴

각 점 $t$ 에서 $t_d$ 의 밀도함수는 표준정규분포의 밀도함수로 수렴한다.

$$\left(1 + \frac{t^2}{d}\right)^{-(d+1)/2} \to e^{-t^2/2} \quad d \to \infty \text{ 일 때}$$

이는 $a = -t^2/2$ 로 둔 $\lim_{d\to\infty}\left(1 + \frac{a}{d}\right)^d = e^a$ 에서 따라 나온다.

## 실제로 어떤 뜻인가

| $d$ | $\text{Var}(t_d) = d/(d-2)$ | $P(\|T\| > 1.96)$ |
|-----|-----|-----|
| $1$ (코시분포) | $\infty$ | $0.3183$ |
| $5$ | $1.667$ | $0.1076$ |
| $10$ | $1.250$ | $0.0785$ |
| $30$ | $1.071$ | $0.0593$ |
| $100$ | $1.020$ | $0.0536$ |
| $\infty$ (정규분포) | $1.000$ | $0.0500$ |

$d \geq 30$ 이면 t분포는 표준정규분포에 매우 가깝다. 실제로 자유도가 크면 $t$ 임곗값 대신 $z$ 임곗값을 써도 오차가 크지 않다.

## 파이썬으로 그려 보기

```python
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

x = np.linspace(-4, 4, 500)

fig, ax = plt.subplots(figsize=(8, 5))
ax.plot(x, stats.norm.pdf(x), 'r-', lw=2.5, label='$N(0,1)$')
for d in range(1, 11):
    alpha = 0.3 + 0.07 * d
    ax.plot(x, stats.t.pdf(x, d), 'b-', alpha=alpha)

ax.set_xlabel('$x$')
ax.set_ylabel('Density')
ax.set_title('$t_d$ converges to $N(0,1)$ as $d \\to \\infty$')
ax.legend()
plt.tight_layout()
plt.show()
```

이 그림은 강의 그림에서 본 수렴을 그대로 재현한다. $d$ 가 커질수록 파란 $t_d$ 곡선이 빨간 $N(0,1)$ 곡선에 다가가고, 두꺼웠던 꼬리가 정규분포의 꼬리 쪽으로 줄어든다.

## 연습문제

**연습문제 1.** $d = 5, 10, 30, 100$ 에 대하여 $t_d$ 의 초과첨도를 구하고 그것이 $0$ 으로 다가감을 확인하여라.

??? success "연습문제 1 풀이"
    $d > 4$ 일 때 $t_d$ 의 초과첨도는 $\gamma_2 = 6/(d - 4)$ 이다.

    - $d = 5$: $6/1 = 6.0$
    - $d = 10$: $6/6 = 1.0$
    - $d = 30$: $6/26 \approx 0.231$
    - $d = 100$: $6/96 = 0.0625$

    $d \to \infty$ 일 때 $\gamma_2 \to 0$ 이 분명하며, 이는 정규분포의 초과첨도인 $0$ 에 다가가는 것이다.

---

**연습문제 2.** $d = 5$ 일 때 $t_5$ 와 $N(0,1)$ 에서의 $P(T > 2)$ 를 견주어라.

??? success "연습문제 2 풀이"
    $t_5$ 에서 $P(T > 2) \approx 0.0510$ 이다.

    $N(0,1)$ 에서 $P(Z > 2) \approx 0.0228$ 이다.

    $t_5$ 의 꼬리가 두 배 넘게 무거우며, 이는 t분포의 두꺼운 꼬리를 그대로 보여 준다.

---

**연습문제 3.** 슬루츠키 정리를 써서 $t_d \xrightarrow{d} N(0,1)$ 을 증명하여라. 정리를 서술하고 각 부분이 무엇에 해당하는지 밝혀라.

??? success "연습문제 3 풀이"
    **슬루츠키 정리:** $X_n \xrightarrow{d} X$ 이고 $Y_n \xrightarrow{p} c$ ($c$ 는 상수)이면 $X_n / Y_n \xrightarrow{d} X/c$ 이다.

    $T_d = Z / \sqrt{V_d/d}$ 에서 $Z \sim N(0,1)$ 은 $d$ 에 의존하지 않으므로 $Z \xrightarrow{d} Z$ 이다. 큰수의 법칙에 따라 $V_d/d \xrightarrow{p} 1$ 이므로 $\sqrt{V_d/d} \xrightarrow{p} 1$ 이다. 슬루츠키 정리에 따라 $T_d = Z/\sqrt{V_d/d} \xrightarrow{d} Z/1 = Z \sim N(0,1)$ 이다. $\square$

---

**연습문제 4.** $d$ 가 얼마쯤 되면 t분포를 대부분의 쓰임에서 $N(0,1)$ 과 사실상 구별할 수 없게 되는가?

??? success "연습문제 4 풀이"
    흔히 쓰는 어림잡기는 $d \geq 30$ 이다. $d = 30$ 이면 $t_{0.025} = 2.042$ 이고 $z_{0.025} = 1.960$ 으로 차이가 약 4%이다. $d = 120$ 이면 $t_{0.025} = 1.980$ 으로 차이가 약 1%이다. 통계의 여러 응용에서 $d \geq 30$ 이면 정규근사를 쓰기에 충분하다고 본다.

---

**연습문제 5.** $d > 2$ 일 때 $t_d$ 의 분산은 $d/(d-2)$ 이다. $d \to \infty$ 일 때 이것이 $1$ 로 수렴함을 보여라.

??? success "연습문제 5 풀이"
    $$
    \text{Var}(t_d) = \frac{d}{d-2} = \frac{1}{1 - 2/d} \to \frac{1}{1 - 0} = 1
    $$

    이 성립한다($d \to \infty$ 일 때). 이는 분산이 $1$ 인 $t_d \to N(0,1)$ 과 들어맞는다. $\square$
