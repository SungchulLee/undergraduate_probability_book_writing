# F분포의 밀도함수와 분포함수

$F$ 분포는 독립인 두 카이제곱확률변수를 각각의 자유도로 나눈 것의 비로 나타난다. 이 절에서는 $F(5, 10)$ 분포의 밀도함수와 누적분포함수를 그리고 그 주요 성질을 살펴본다.

## 배경

$U \sim \chi^2_{d_1}$ 과 $V \sim \chi^2_{d_2}$ 가 독립이면 다음이 성립한다.

$$
F = \frac{U / d_1}{V / d_2} \sim F(d_1, d_2)
$$

여기에서 $d_1$ 과 $d_2$ 를 각각 분자의 자유도, 분모의 자유도라고 한다. $F(d_1, d_2)$ 분포의 밀도함수는 다음과 같다.

$$
f(x) = \frac{1}{B\!\left(\frac{d_1}{2}, \frac{d_2}{2}\right)} \left(\frac{d_1}{d_2}\right)^{d_1/2} x^{d_1/2 - 1} \left(1 + \frac{d_1}{d_2} x\right)^{-(d_1 + d_2)/2}, \quad x > 0
$$

여기에서 $B(\alpha, \beta) = \Gamma(\alpha)\Gamma(\beta)/\Gamma(\alpha + \beta)$ 는 베타함수이다. $F$ 분포는 다음과 같은 성질을 지닌다.

- **평균**: $d_2 > 2$ 일 때 $E[F] = d_2 / (d_2 - 2)$ 이다.
- **분산**: $d_2 > 4$ 일 때 $\text{Var}(F) = \frac{2\,d_2^2\,(d_1 + d_2 - 2)}{d_1\,(d_2 - 2)^2\,(d_2 - 4)}$ 이다.
- **역수 성질**: $F \sim F(d_1, d_2)$ 이면 $1/F \sim F(d_2, d_1)$ 이다.

누적분포함수는 간단한 닫힌 꼴이 없으며 정규화된 불완전 베타함수로 나타낸다.

## 코드

```python
"""F분포의 밀도함수와 누적분포함수."""
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

df1, df2 = 5, 10
x = np.linspace(0, 5, 300)

fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(x, stats.f(df1, df2).pdf(x), label="PDF", linewidth=2)
ax.plot(x, stats.f(df1, df2).cdf(x), label="CDF", linewidth=2)
ax.set_title(f"F({df1}, {df2}) Distribution", fontsize=14)
ax.set_xlabel("x")
ax.set_ylabel("Value")
ax.legend()
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig("f_pdf_cdf.png", dpi=150, bbox_inches="tight")
plt.show()
```

## 실행 결과

$[0, 5]$ 구간에서 $F(5, 10)$ 분포에 대한 두 곡선이 그려진다.

- **밀도함수 곡선**: $0$ 에서 올라와 $x \approx 0.6$ 언저리에서 최댓값 약 $0.74$ 에 이른 뒤 긴 오른쪽 꼬리를 끌며 줄어든다. $x = 4$ 쯤에서는 밀도가 거의 $0$ 이다.
- **누적분포함수 곡선**: $0$ 에서 출발하여 밀도가 높은 구간에서 가파르게 올라가고 차츰 $1$ 에 다가간다. $x \approx 0.9$ (중앙값) 언저리에서 $0.5$ 를 지나며 $x = 4$ 에서 약 $0.98$ 에 이른다.

## 뜻풀이

$F(5, 10)$ 분포는 오른쪽으로 치우쳐 있고 받침은 $(0, \infty)$ 이다. 평균은 $E[F] = 10/(10-2) = 1.25$ 로 최빈값과 중앙값보다 오른쪽에 놓이며, 이는 오른쪽으로 치우친 모양을 반영한다. 밀도함수를 보면 확률의 대부분이 $0$ 과 $3$ 사이에 몰려 있지만 꼬리는 그보다 훨씬 멀리까지 뻗는다.

$F$ 분포는 분산분석(ANOVA)과 회귀분석의 중심에 놓인다. 그곳에서는 검정통계량이 두 분산 추정값의 비이기 때문이다. 귀무가설 아래에서 이 비는 $F$ 분포를 따르며, 오른쪽 꼬리 쪽의 큰 값이 나오면 귀무가설에 어긋나는 증거가 된다. $p$ 값을 구하는 데에는 누적분포함수를 쓴다. 곧 $p = 1 - F_{d_1, d_2}(x_{\text{obs}})$ 이다.

## 연습문제

**연습문제 1.**
코드를 고쳐 $(d_1, d_2) \in \{(2, 5), (5, 10), (10, 20), (50, 50)\}$ 에 대한 $F(d_1, d_2)$ 의 밀도함수를 한 그림에 그려라. 모양이 어떻게 달라지는지 말하여라.

??? success "연습문제 1 풀이"
    ```python
    import numpy as np
    import matplotlib.pyplot as plt
    from scipy import stats

    x = np.linspace(0, 5, 300)
    fig, ax = plt.subplots(figsize=(10, 5))
    for d1, d2 in [(2, 5), (5, 10), (10, 20), (50, 50)]:
        ax.plot(x, stats.f(d1, d2).pdf(x), label=f"F({d1},{d2})")
    ax.legend()
    ax.grid(True, alpha=0.3)
    plt.show()
    ```

    $d_1$ 과 $d_2$ 가 함께 커질수록 분포가 평균 $d_2/(d_2 - 2)$ 언저리로 더 몰리고($d_2 \to \infty$ 이면 이 값은 $1$ 로 간다) 치우침이 줄어 대칭에 가까워진다. $(50, 50)$ 이면 밀도함수가 거의 종 모양이고 중심이 $1$ 에 가깝다. 반면 $F(2, 5)$ 는 최빈값이 작은 양수 자리에 있고 오른쪽 꼬리가 매우 길다.

---

**연습문제 2.**
`scipy.stats` 를 써서 $F(5, 10)$ 의 95 백분위수를 구하여라. 누적분포함수로 확인하여라.

??? success "연습문제 2 풀이"
    ```python
    from scipy import stats

    f_dist = stats.f(5, 10)
    q95 = f_dist.ppf(0.95)
    print(f"95th percentile: {q95:.4f}")
    print(f"CDF at q95:      {f_dist.cdf(q95):.4f}")
    ```

    실행 결과, 95 백분위수는 약 $3.3258$ 이고 `cdf(3.3258)` 은 $0.9500$ 을 돌려주어 결과가 확인된다. 곧 $P(F \leq 3.3258) = 0.95$ 이므로 $F$ 가 $3.33$ 을 넘는 값은 위쪽 5% 꼬리에 들어간다.

---

**연습문제 3.**
$F \sim F(d_1, d_2)$ 이면 $1/F \sim F(d_2, d_1)$ 임을 보여라.

??? success "연습문제 3 풀이"
    정의에 따라 독립인 $U \sim \chi^2_{d_1}$ 과 $V \sim \chi^2_{d_2}$ 에 대하여 $F = (U/d_1) / (V/d_2)$ 이다. 그러면

    $$
    \frac{1}{F} = \frac{V/d_2}{U/d_1}
    $$

    이다. 이것은 독립인 $V \sim \chi^2_{d_2}$ 와 $U \sim \chi^2_{d_1}$ 에 대하여 $V/d_2$ 와 $U/d_1$ 의 비이므로, $F$ 분포의 정의에 따라 $F(d_2, d_1)$ 이다. $\square$

---

**연습문제 4.**
$T \sim t_\nu$ 이면 $T^2 \sim F(1, \nu)$ 임을 증명하여라.

??? success "연습문제 4 풀이"
    정의에 따라 독립인 $Z \sim N(0,1)$ 과 $V \sim \chi^2_\nu$ 에 대하여 $T = Z / \sqrt{V/\nu}$ 이다. 그러면

    $$
    T^2 = \frac{Z^2}{V/\nu}
    $$

    이다. $Z^2 \sim \chi^2_1$ 이므로 다음과 같이 쓸 수 있다.

    $$
    T^2 = \frac{Z^2 / 1}{V / \nu} = \frac{U / d_1}{V / d_2}
    $$

    여기에서 $U = Z^2 \sim \chi^2_1$, $d_1 = 1$, $d_2 = \nu$ 이다. $Z$ 와 $V$ 가 독립이므로 $U = Z^2$ 과 $V$ 도 독립이다. 따라서 $F$ 분포의 정의에 따라 $T^2 \sim F(1, \nu)$ 이다. $\square$

---

**연습문제 5.**
배경 절의 공식을 써서 $F \sim F(5, 10)$ 의 $E[F]$ 와 $\text{Var}(F)$ 를 구하여라. 모의실험으로 확인하여라.

??? success "연습문제 5 풀이"
    $d_1 = 5$, $d_2 = 10$ 이므로 다음과 같다.

    $$
    E[F] = \frac{d_2}{d_2 - 2} = \frac{10}{8} = 1.25
    $$

    $$
    \text{Var}(F) = \frac{2 \cdot d_2^2 \cdot (d_1 + d_2 - 2)}{d_1 \cdot (d_2 - 2)^2 \cdot (d_2 - 4)} = \frac{2 \cdot 100 \cdot 13}{5 \cdot 64 \cdot 6} = \frac{2600}{1920} \approx 1.3542
    $$

    모의실험으로 확인하면 다음과 같다.

    ```python
    import numpy as np
    from scipy import stats

    np.random.seed(42)
    data = stats.f(5, 10).rvs(100_000)
    print(f"Sample mean: {data.mean():.4f}  (theoretical: 1.2500)")
    print(f"Sample var:  {data.var(ddof=1):.4f}  (theoretical: 1.3542)")
    ```

    보통 표본평균은 $\approx 1.25$, 표본분산은 $\approx 1.35$ 로 나와 이론값과 잘 맞는다.

---

**연습문제 6.**
$F$ 분포가 언제나 오른쪽으로 치우치는 까닭을 설명하여라. $d_1$ 과 $d_2$ 가 함께 커지면 왜도는 어떻게 되는가?

??? success "연습문제 6 풀이"
    $F$ 분포는 양수인 두 양(카이제곱확률변수에 상수를 곱한 것)의 비이므로 받침이 $(0, \infty)$ 이고 $0$ 에서 딱 잘린다. 오른쪽 꼬리가 무거운 까닭은 분모가 대부분의 경우 $0$ 에서 멀리 떨어져 있는 동안 분자의 카이제곱확률변수가 이따금 아주 큰 값을 가질 수 있어 큰 비가 가끔 나타나기 때문이다.

    수치로 말하면 $d_2 > 6$ 일 때 $F(d_1, d_2)$ 의 왜도는 다음과 같다.

    $$
    \gamma_1 = \frac{(2d_1 + d_2 - 2)\sqrt{8(d_2 - 4)}}{(d_2 - 6)\sqrt{d_1(d_1 + d_2 - 2)}}
    $$

    $d_1, d_2 \to \infty$ 이면 왜도 $\gamma_1 \to 0$ 이고 분포는 $1$ 언저리를 중심으로 거의 정규분포가 된다. 많은 i.i.d. 항을 평균한 두 값의 비가 평균의 비인 $1$ 로 수렴하고, 중심극한정리와 델타 방법에 따라 그 흔들림이 대칭이 되기 때문이다.
