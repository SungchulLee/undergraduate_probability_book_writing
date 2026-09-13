# 지수확률변수의 합

이 쪽에서는 독립이고 같은 분포를 따르는 지수확률변수의 합이 더하는 개수가 늘어남에 따라 정규분포로 수렴함을 모의실험으로 보인다. 지수분포는 오른쪽으로 몹시 치우쳐 있어서 중심극한정리를 인상 깊게 보여 주는 예가 된다. 출발한 모양이 아무리 비대칭이어도 결국에는 대칭인 종 모양이 나온다.

## 배경

비율이 $\lambda > 0$ 인 **지수**확률변수 $X \sim \text{Exp}(\lambda)$ 의 밀도함수는 다음과 같다.

$$
f(x) = \lambda e^{-\lambda x}, \qquad x \geq 0.
$$

표준적인 경우인 $\lambda = 1$ 에서 평균과 분산은 다음과 같다.

$$
E[X] = 1, \qquad \text{Var}(X) = 1.
$$

독립인 $\text{Exp}(1)$ 확률변수 $n$ 개의 합은 **감마분포**를 따르고

$$
S_n = X_1 + X_2 + \cdots + X_n \sim \text{Gamma}(n, 1),
$$

그 평균과 분산은 다음과 같다.

$$
E[S_n] = n, \qquad \text{Var}(S_n) = n.
$$

$n$ 이 커지면 감마분포의 밀도함수가 정규분포 모양으로 다가간다. 이것은 중심극한정리의 특별한 경우이지만, 정확한 분포를 알고 있으므로 수렴을 자세히 들여다볼 수 있다. 또 푸아송 과정과 이어져 있다는 점에서 실용적으로도 중요하다. $S_n$ 은 $n$ 번째 도착시각을 나타내기 때문이다.

## 코드

```python
"""i.i.d. Exp(1) 확률변수의 합이 정규분포로 다가가는 모습."""
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

np.random.seed(42)
n_sim = 10000

fig, axes = plt.subplots(2, 3, figsize=(14, 8))
for idx, n in enumerate([2, 3, 5, 10, 30, 100]):
    ax = axes.flatten()[idx]
    S = np.sum(np.random.exponential(1.0, (n, n_sim)), axis=0)
    ax.hist(S, bins=100, density=True, alpha=0.7, color='steelblue')
    mu, sigma = n, np.sqrt(n)
    x = np.linspace(max(0, mu - 4*sigma), mu + 4*sigma, 200)
    ax.plot(x, stats.norm.pdf(x, mu, sigma), 'r-', lw=2)
    ax.set_title(f'n = {n}')
    ax.grid(True, alpha=0.3)

plt.suptitle('Sum of Exp(1) -> Normal', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('exponential_clt.png', dpi=150, bbox_inches='tight')
plt.show()
```

## 실행 결과

이 스크립트는 $n = 2, 3, 5, 10, 30, 100$ 에 대한 히스토그램을 $2 \times 3$ 격자로 그린다. 각 히스토그램은 10,000번의 모의실험에서 얻은 $S_n \sim \text{Gamma}(n, 1)$ 의 경험적 분포를 보여 주고, 그 위에 정규분포 밀도함수 $N(n, n)$ 을 빨간 곡선으로 겹쳐 놓는다.

- $n = 2$ 에서는 히스토그램이 $\text{Gamma}(2, 1)$ 의 밀도함수를 보여 주며, 오른쪽으로 치우친 것이 눈에 띈다.
- $n = 5$ 쯤 되면 치우침이 눈에 띄게 줄어들지만 아직 알아볼 수 있다.
- $n = 10$ 에서는 히스토그램이 정규분포 곡선을 바싹 따라간다.
- $n = 30$ 과 $n = 100$ 에서는 둘이 아주 잘 들어맞는다.

## 뜻풀이

지수분포는 출발점이 정규분포와 워낙 멀기 때문에 중심극한정리를 보여 주는 가장 배울 점 많은 예 가운데 하나이다.

1. **왜도가 천천히 줄어든다.** $\text{Gamma}(n, 1)$ 의 왜도는 $2/\sqrt{n}$ 이다. 유한한 모든 $n$ 에 대하여 양수이므로 오른쪽 꼬리가 늘 왼쪽보다 두껍지만, 그 값이 $0$ 쪽으로 줄어든다. 모든 $n$ 에서 왜도가 $0$ 이라 수렴이 더 빠른 균등분포의 경우와 견주어 보면 좋다.
2. **받침이 어긋난다.** $S_n$ 은 언제나 양수이지만 정규근사는 음수에도 양의 확률을 준다. $n$ 이 크면 $0$ 근처의 질량이 지수적으로 작아서 이 어긋남은 무시할 만해진다.
3. **정확한 분포를 안다.** $S_n \sim \text{Gamma}(n, 1)$ 이므로 모의실험에만 기대지 않고 감마분포의 정확한 밀도함수와 정규근사를 해석적으로 견주어 볼 수 있다.

## 연습문제

**연습문제 1.**
$X_i \sim \text{Exp}(1)$ 일 때 합성곱 적분을 계산하여 $S_2 = X_1 + X_2$ 의 밀도함수를 구하여라. $S_2 \sim \text{Gamma}(2, 1)$ 임을 확인하여라.

??? success "연습문제 1 풀이"
    합성곱 적분은 다음과 같다.

    $$
    f_{S_2}(s) = \int_0^s e^{-x} \cdot e^{-(s-x)} \, dx = e^{-s} \int_0^s 1 \, dx = s \, e^{-s}, \qquad s \geq 0.
    $$

    이것은 $\text{Gamma}(2, 1)$ 의 밀도함수 $f(s) = \frac{s^{2-1} e^{-s}}{\Gamma(2)} = s e^{-s}$ 이므로 결론이 확인된다.

---

**연습문제 2.**
$S_n \sim \text{Gamma}(n, 1)$ 의 왜도가 $2/\sqrt{n}$ 임을 보여라. 왜도가 $0.1$ 보다 작아지려면 $n$ 이 얼마나 커야 하는가?

??? success "연습문제 2 풀이"
    $\text{Exp}(1)$ 의 3차 중심적률은 $E[(X-1)^3] = 2$ 이다($\text{Exp}(1)$ 의 3차 누적률이 $2$ 이기 때문이다). 독립성에 따라 $S_n$ 의 3차 중심적률은 $2n$ 이고 표준편차는 $\sqrt{n}$ 이다. 따라서 왜도는 다음과 같다.

    $$
    \gamma_1 = \frac{2n}{(\sqrt{n})^3} = \frac{2}{\sqrt{n}}.
    $$

    $\gamma_1 < 0.1$ 로 놓으면 $2/\sqrt{n} < 0.1 \implies \sqrt{n} > 20 \implies n > 400$ 이다. 곧 왜도가 $0.1$ 아래로 내려가려면 적어도 $n = 401$ 이어야 한다.

---

**연습문제 3.**
합 $S_n \sim \text{Gamma}(n, 1)$ 의 적률생성함수를 정확히 구할 수 있다. 그것을 유도하고, 이를 써서 $E[S_n] = n$ 과 $\text{Var}(S_n) = n$ 을 확인하여라.

??? success "연습문제 3 풀이"
    $\text{Exp}(1)$ 의 적률생성함수는 $t < 1$ 에서 $M_X(t) = 1/(1-t)$ 이다. 독립성에 따라 다음이 성립한다.

    $$
    M_{S_n}(t) = \left(\frac{1}{1-t}\right)^n = (1-t)^{-n}.
    $$

    미분하면 $M_{S_n}'(t) = n(1-t)^{-(n+1)}$ 이므로 $E[S_n] = M_{S_n}'(0) = n$ 이다. 또 $M_{S_n}''(t) = n(n+1)(1-t)^{-(n+2)}$ 이므로 $E[S_n^2] = n(n+1)$ 이다. 따라서 다음을 얻는다.

    $$
    \text{Var}(S_n) = E[S_n^2] - (E[S_n])^2 = n(n+1) - n^2 = n.
    $$

---

**연습문제 4.**
비율이 $\lambda = 1$ 인 푸아송 과정에서 $S_n$ 은 $n$ 번째 사건의 도착시각이다. 이 뜻풀이를 써서 $N(t) \sim \text{Po}(t)$ 일 때 $P(S_n > t) = P(N(t) < n)$ 이 성립하는 까닭을 설명하여라.

??? success "연습문제 4 풀이"
    $n$ 번째 도착이 시각 $t$ 뒤에 일어나는 것은 시각 $t$ 까지 도착이 $n$ 번보다 적게 일어난 것과 같은 말이다. 기호로 적으면 다음과 같다.

    $$
    \{S_n > t\} = \{N(t) < n\} = \{N(t) \leq n - 1\}.
    $$

    $N(t) \sim \text{Po}(t)$ 이므로 다음을 얻는다.

    $$
    P(S_n > t) = P(N(t) \leq n-1) = \sum_{k=0}^{n-1} \frac{t^k e^{-t}}{k!}.
    $$

    $P(S_n \leq t) = 1 - \sum_{k=0}^{n-1} \frac{t^k e^{-t}}{k!}$ 를 $t$ 에 대하여 미분하면 $\text{Gamma}(n, 1)$ 의 밀도함수가 다시 나온다.

---

**연습문제 5.**
$\lambda = 5$ 인 $\text{Exp}(\lambda)$ 를 쓰도록 코드를 고쳐라. $n$ 과 $\lambda$ 로 나타낸 $E[S_n]$ 과 $\text{Var}(S_n)$ 은 무엇인가? 정규근사가 여전히 잘 맞는지 확인하여라.

??? success "연습문제 5 풀이"
    $X_i \sim \text{Exp}(\lambda)$ 에 대하여 $E[X_i] = 1/\lambda$ 이고 $\text{Var}(X_i) = 1/\lambda^2$ 이다. 따라서 다음이 성립한다.

    $$
    E[S_n] = \frac{n}{\lambda}, \qquad \text{Var}(S_n) = \frac{n}{\lambda^2}.
    $$

    $\lambda = 5$ 이면 $E[S_n] = n/5$ 이고 $\text{Var}(S_n) = n/25$ 이다. 코드에서는 `np.random.exponential(1.0, ...)` 를 `np.random.exponential(1/5, ...)` 로 바꾸고(NumPy의 `exponential` 은 척도 $1/\lambda$ 를 받는다) `mu, sigma = n/5, np.sqrt(n)/5` 로 두면 된다. 수렴 속도는 왜도 $2/\sqrt{n}$ 에 좌우되는데 이 값이 $\lambda$ 와 무관하므로, 정규분포로의 수렴은 달라지지 않는다.
