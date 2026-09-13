# 몬테카를로로 원주율 구하기: 모의실험

이 모의실험은 단위정사각형 안에 무작위로 점을 던지고 그 가운데 몇 개가 사분원 안에 떨어지는지를 세어 $\pi$ 를 어림한다. 큰수의 법칙은 점의 수가 늘어남에 따라 이 어림값이 $\pi$ 의 참값으로 수렴함을 보장한다.

## 배경

단위정사각형 $[0, 1]^2$ 과 사분원 $\{(x, y) : x^2 + y^2 < 1,\; x \geq 0,\; y \geq 0\}$ 을 생각하자. $(X, Y)$ 가 $[0, 1]^2$ 위에서 균등분포를 따를 때 다음 지시확률변수를 정의한다.

$$
I = \mathbf{1}(X^2 + Y^2 < 1)
$$

무작위로 뽑은 점이 사분원 안에 떨어질 확률은 넓이의 비와 같다.

$$
P(I = 1) = \frac{\text{사분원의 넓이}}{\text{단위정사각형의 넓이}} = \frac{\pi/4}{1} = \frac{\pi}{4}
$$

균등분포에서 i.i.d. 로 뽑은 점 $n$ 개에 대하여 그에 대응하는 지시확률변수를 $I_1, I_2, \ldots, I_n$ 이라고 하자. 큰수의 강법칙에 따라 다음이 성립한다.

$$
\frac{1}{n}\sum_{i=1}^n I_i \xrightarrow{a.s.} \frac{\pi}{4}
$$

이를 고쳐 쓰면 $\pi$ 의 **몬테카를로 추정량**을 얻는다.

$$
\hat{\pi}_n = \frac{4}{n}\sum_{i=1}^n I_i \xrightarrow{a.s.} \pi
$$

이는 큰수의 법칙의 가장 간단하면서도 가장 널리 알려진 응용 가운데 하나이다.

## 코드

```python
"""몬테카를로로 π 어림하기: 단위정사각형 안의 무작위 점."""
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

N_POINTS = 5_000

x = np.random.uniform(0, 1, (2, N_POINTS))
inside = (x[0] ** 2 + x[1] ** 2) < 1

# --- 산점도 ---
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

ax1.scatter(x[0, inside], x[1, inside], s=1, color="red", label="Inside")
ax1.scatter(x[0, ~inside], x[1, ~inside], s=1, color="blue", label="Outside")
theta = np.linspace(0, np.pi / 2, 200)
ax1.plot(np.cos(theta), np.sin(theta), "k-", lw=2)
ax1.set_aspect("equal")
ax1.set_title(f"Random Points (n = {N_POINTS:,})")
ax1.legend(markerscale=5)

# --- 수렴 그림 ---
pi_est = 4 * inside.cumsum() / np.arange(1, N_POINTS + 1)
ax2.plot(pi_est[10:], linewidth=1.5)
ax2.axhline(np.pi, color="r", linestyle="--", lw=2, label=f"π ≈ {np.pi:.5f}")
ax2.set_title("Monte Carlo Estimate of π")
ax2.set_xlabel("Number of points")
ax2.set_ylabel("Estimated π")
ax2.legend()
ax2.grid(True, alpha=0.3)

plt.suptitle("Monte Carlo Estimation of π", fontsize=14, fontweight="bold")
plt.tight_layout()
plt.savefig("monte_carlo_pi.png", dpi=150, bbox_inches="tight")
plt.show()

print(f"Final estimate of π: {pi_est[-1]:.5f}")
```

## 실행 결과

이 스크립트는 두 칸짜리 그림 하나와 출력된 어림값 하나를 내놓는다.

**왼쪽 그림(산점도):** $[0, 1]^2$ 안의 무작위 점 5,000개를 그리되, 사분원 안($x^2 + y^2 < 1$)에 떨어진 점은 빨간색으로, 그 밖의 점은 파란색으로 칠한다. 검은 곡선은 사분원의 경계이다. 점의 약 78.5%가 빨간색이며, 이는 $\pi/4 \approx 0.7854$ 와 들어맞는다.

**오른쪽 그림(수렴 그림):** 그때까지의 어림값 $\hat{\pi}_n = 4 \cdot (\text{안에 든 비율})$ 을 $n$ 에 대한 함수로 그린 것이다. $n$ 이 작을 때에는 크게 출렁이다가 $n$ 이 커지면서 $\pi \approx 3.14159$ 에 있는 빨간 점선으로 다가간다.

**출력된 값:** `Final estimate of π: 3.12880` (정확한 값은 씨앗값에 따라 달라진다).

## 뜻풀이

1. **큰수의 법칙이 일하는 모습.** 수렴 그림은 큰수의 법칙을 그대로 보여 준다. 표본평균 $\frac{1}{n}\sum I_i$ 가 $E[I] = \pi/4$ 로 수렴하므로 표본평균의 $4$ 배는 $\pi$ 로 수렴한다.

2. **정확도.** $\hat{\pi}_n$ 의 표준편차는 다음과 같다.

    $$
    \text{SD}(\hat{\pi}_n) = 4\sqrt{\frac{p(1-p)}{n}} = 4\sqrt{\frac{(\pi/4)(1-\pi/4)}{n}} \approx \frac{1.64}{\sqrt{n}}
    $$

    $n = 5{,}000$ 이면 $\text{SD} \approx 0.023$ 이므로 어림값은 보통 $\pi$ 에서 0.05쯤 안에 놓인다. 소수점 아래 한 자리를 더 정확하게 얻으려면 점을 대략 100배 더 던져야 한다.

3. **기하학적 확률.** 산점도는 기하학적인 직관을 준다. $\pi/4$ 는 말 그대로 사분원이 단위정사각형에서 차지하는 비율이다. 몬테카를로 어림은 기하학적이고 해석적인 양을 세는 문제로 바꾸어 놓는다.

4. **일반성.** 똑같은 원리가 모든 적분으로 뻗어 나간다. $\int_0^1 g(x)\,dx$ 를 어림하려면 $X_1, \ldots, X_n \sim \text{Uniform}(0, 1)$ 을 만들고 $\frac{1}{n}\sum g(X_i)$ 를 셈하면 된다. 사분원 방법은 (한 변수를 적분으로 없앤 뒤) $g(x) = 4\sqrt{1 - x^2}$ 인 특별한 경우이다.

## 연습문제

**연습문제 1.** 점 $n = 100{,}000$ 개를 써서 $\pi$ 를 어림하도록 모의실험을 고쳐라. 어림값을 보고하고 $n = 5{,}000$ 인 경우와 정확도를 견주어 보아라.

??? success "연습문제 1 풀이"
    `N_POINTS = 100_000` 으로 바꾼다. 보통 한 번 돌리면 $\hat{\pi} \approx 3.1426$ 이 나오고 오차는 약 0.001이다. $n = 5{,}000$ 일 때 오차는 약 0.01이었다. 표준편차가 $1/\sqrt{n}$ 에 비례하므로 $n$ 을 20배 키우면 표준편차는 $\sqrt{20} \approx 4.5$ 배 줄어들고, 이는 오차가 $\approx 0.013$ 에서 $\approx 0.003$ 으로 줄어드는 것과 들어맞는다. $\square$

---

**연습문제 2.** 몬테카를로 추정량 $\hat{\pi}_n = \frac{4}{n}\sum_{i=1}^n I_i$ 의 분산을 유도하여라.

??? success "연습문제 2 풀이"
    각 $I_i \sim \text{Bernoulli}(\pi/4)$ 이므로 $\operatorname{Var}(I_i) = \frac{\pi}{4}\left(1 - \frac{\pi}{4}\right)$ 이다. $I_i$ 들이 독립이므로 다음이 성립한다.

    $$
    \operatorname{Var}(\hat{\pi}_n) = \operatorname{Var}\!\left(\frac{4}{n}\sum_{i=1}^n I_i\right) = \frac{16}{n^2} \cdot n \cdot \frac{\pi}{4}\!\left(1 - \frac{\pi}{4}\right) = \frac{4\pi(4-\pi)}{4n}
    $$

    정리하면 다음과 같다.

    $$
    \operatorname{Var}(\hat{\pi}_n) = \frac{\pi(4-\pi)}{n} \approx \frac{3.1416 \times 0.8584}{n} \approx \frac{2.698}{n}
    $$

    표준편차는 $\sqrt{2.698/n} \approx 1.643/\sqrt{n}$ 이다. $\square$

---

**연습문제 3.** $\pi$ 의 95% 신뢰구간의 반너비가 0.01 이하가 되려면 점이 몇 개 필요한가?

??? success "연습문제 3 풀이"
    95% 신뢰구간의 반너비는 $1.96 \cdot \text{SD}(\hat{\pi}_n)$ 이다. 이 값이 0.01 이하가 되게 하면 다음과 같다.

    $$
    1.96 \cdot \frac{1.643}{\sqrt{n}} \leq 0.01
    $$

    $$
    \sqrt{n} \geq \frac{1.96 \times 1.643}{0.01} = 322.0
    $$

    $$
    n \geq 322.0^2 \approx 103{,}700
    $$

    따라서 반너비가 0.01인 95% 신뢰구간을 얻으려면 점이 대략 $n = 104{,}000$ 개 필요하다. $\square$

---

**연습문제 4.** 사분원 대신 적분 $\pi = 4\int_0^1 \sqrt{1 - x^2}\,dx$ 를 써서 $\pi$ 를 어림하여라. 이 식에 바탕을 둔 몬테카를로 추정량을 적고 그 분산을 지시확률변수를 쓰는 방법과 견주어 보아라.

??? success "연습문제 4 풀이"
    $g(x) = 4\sqrt{1 - x^2}$ 로 두자. $X \sim \text{Uniform}(0, 1)$ 이면 $E[g(X)] = 4\int_0^1 \sqrt{1-x^2}\,dx = \pi$ 이다. 몬테카를로 추정량은 다음과 같다.

    $$
    \hat{\pi}_n = \frac{1}{n}\sum_{i=1}^n 4\sqrt{1 - X_i^2}
    $$

    분산은 $\operatorname{Var}(g(X))/n$ 이다. 셈해 보면 다음과 같다.

    $$
    E[g(X)^2] = 16\int_0^1 (1-x^2)\,dx = 16\left[x - \frac{x^3}{3}\right]_0^1 = 16 \cdot \frac{2}{3} = \frac{32}{3}
    $$

    $$
    \operatorname{Var}(g(X)) = \frac{32}{3} - \pi^2 \approx 10.667 - 9.870 = 0.797
    $$

    따라서 $\operatorname{Var}(\hat{\pi}_n) = 0.797/n$ 이고, 지시확률변수를 쓰는 방법의 $2.698/n$ 과 견주면 분산이 약 3.4배 작다. 곧 적분에 바탕을 둔 추정량이 더 효율적이다. $\square$

---

**연습문제 5.** 몬테카를로 추정량 $\hat{\pi}_n$ 이 $\pi$ 의 일치추정량임을 증명하여라. 어떤 형태의 큰수의 법칙을 쓰는지 정확히 밝혀라.

??? success "연습문제 5 풀이"
    점 $(X_i, Y_i)$ 들은 i.i.d. 이고 $X_i, Y_i \sim \text{Uniform}(0,1)$ 이며 서로 독립이다. 따라서 지시확률변수 $I_i = \mathbf{1}(X_i^2 + Y_i^2 < 1)$ 들도 i.i.d. 이고 $E[I_i] = \pi/4$ 이다.

    $E[|I_i|] = E[I_i] = \pi/4 < \infty$ 이므로 큰수의 강법칙을 적용할 수 있다.

    $$
    \frac{1}{n}\sum_{i=1}^n I_i \xrightarrow{a.s.} \frac{\pi}{4}
    $$

    양변에 4를 곱하면 다음을 얻는다.

    $$
    \hat{\pi}_n = \frac{4}{n}\sum_{i=1}^n I_i \xrightarrow{a.s.} \pi
    $$

    거의 확실한 수렴은 확률수렴을 함의하므로 $\hat{\pi}_n$ 은 $\pi$ 의 일치추정량이다. 여기에서는 1차 적률이 유한한 i.i.d. 확률변수에 대한 큰수의 강법칙을 썼다. $\square$

---

**연습문제 6.** 몬테카를로 방법이 적분 영역의 차원과 관계없이 $O(1/\sqrt{n})$ 의 속도로 수렴하는 까닭을 설명하여라. 이 점이 높은 차원의 적분에서 몬테카를로를 매력적으로 만드는 까닭은 무엇인가?

??? success "연습문제 6 풀이"
    적분 $I = E[g(X)]$ 에 대한 몬테카를로 추정량 $\hat{I}_n = \frac{1}{n}\sum_{i=1}^n g(X_i)$ 의 표준편차는 다음과 같다.

    $$
    \text{SD}(\hat{I}_n) = \frac{\sigma}{\sqrt{n}}
    $$

    여기에서 $\sigma^2 = \operatorname{Var}(g(X))$ 는 함수 $g$ 에는 기대지만 적분 영역의 차원에는 기대지 않는다. 따라서 수렴 속도 $O(1/\sqrt{n})$ 은 **차원과 무관하다**.

    이와 달리 결정론적인 수치적분 방법(사다리꼴 공식이나 심프슨 공식 등)은 차원이 커질수록 수렴 속도가 나빠진다. 이를테면 $d$ 차원에서 격자점을 모두 $n$ 개 쓰는 사다리꼴 공식은 $O(n^{-2/d})$ 의 속도로 수렴한다. $d = 10$ 이면 이는 $O(n^{-0.2})$ 로, 몬테카를로의 $O(n^{-0.5})$ 보다 훨씬 느리다.

    이 현상을 **차원의 저주**라고 부른다. 결정론적 방법은 $d$ 가 커질수록 지수적으로 많은 점을 필요로 하지만 몬테카를로는 그렇지 않다. 높은 차원의 적분(물리학, 금융, 베이즈 통계에서 흔하다)에서는 몬테카를로가 유일하게 실용적인 방법인 경우가 많다. $\square$
