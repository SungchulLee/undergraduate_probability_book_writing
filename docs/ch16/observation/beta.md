# 베타확률변수의 합

이 쪽에서는 독립이고 같은 분포를 따르는 베타확률변수의 합이 더하는 개수가 늘어남에 따라 정규분포로 수렴함을 모의실험으로 보인다. $\text{Beta}(1, 5)$ 분포는 받침이 $[0, 1]$ 이면서 오른쪽으로 크게 치우쳐 있지만, 여러 개를 더한 합은 대칭인 종 모양을 갖추어 간다.

## 배경

**베타**확률변수 $X \sim \text{Beta}(\alpha, \beta)$ 의 밀도함수는 다음과 같다.

$$
f(x) = \frac{x^{\alpha - 1}(1 - x)^{\beta - 1}}{B(\alpha, \beta)}, \qquad 0 < x < 1,
$$

여기에서 $B(\alpha, \beta) = \Gamma(\alpha)\Gamma(\beta)/\Gamma(\alpha + \beta)$ 는 베타함수이다. $\alpha = 1$ 이고 $\beta = 5$ 이면 다음과 같다.

$$
E[X] = \frac{\alpha}{\alpha + \beta} = \frac{1}{6}, \qquad \text{Var}(X) = \frac{\alpha \beta}{(\alpha + \beta)^2(\alpha + \beta + 1)} = \frac{5}{252}.
$$

독립인 $\text{Beta}(1, 5)$ 확률변수 $n$ 개의 합

$$
S_n = X_1 + X_2 + \cdots + X_n
$$

의 평균과 분산은 다음과 같다.

$$
E[S_n] = \frac{n}{6}, \qquad \text{Var}(S_n) = \frac{5n}{252}.
$$

푸아송족이나 지수족과 달리 베타족은 덧셈에 대하여 닫혀 있지 **않다**. $S_n$ 의 분포는 간단한 닫힌 꼴이 없고, 그래서 중심극한정리에 따른 근사가 더욱 값지다. 여기에서 $\text{Beta}(1, 5)$ 를 고른 까닭은 이 분포가 크게 치우쳐 있기 때문이다(밀도가 $0$ 근처에서 가장 높고 가파르게 떨어진다). 중심극한정리가 분포를 어떻게 "대칭으로 만들어" 가는지를 눈으로 확인하기에 좋다.

## 코드

```python
"""i.i.d. Beta(1,5) 확률변수의 합이 정규분포로 다가가는 모습."""
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

np.random.seed(42)
n_sim = 10000
a, b = 1, 5

fig, axes = plt.subplots(2, 3, figsize=(14, 8))
for idx, n in enumerate([2, 3, 5, 10, 30, 100]):
    ax = axes.flatten()[idx]
    S = np.sum(np.random.beta(a, b, (n, n_sim)), axis=0)
    ax.hist(S, bins=100, density=True, alpha=0.7, color='steelblue')
    mu = n * a / (a + b)
    sigma = np.sqrt(n * a * b / ((a+b)**2 * (a+b+1)))
    x = np.linspace(max(0, mu - 4*sigma), mu + 4*sigma, 200)
    ax.plot(x, stats.norm.pdf(x, mu, sigma), 'r-', lw=2)
    ax.set_title(f'n = {n}')
    ax.grid(True, alpha=0.3)

plt.suptitle('Sum of Beta(1,5) → Normal', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('beta_clt.png', dpi=150, bbox_inches='tight')
plt.show()
```

## 실행 결과

이 스크립트는 $n = 2, 3, 5, 10, 30, 100$ 에 대한 히스토그램을 $2 \times 3$ 격자로 그린다. 각 히스토그램은 10,000번의 모의실험에서 얻은 $S_n$ 의 경험적 분포를 보여 주고, 그 위에 정규분포 밀도함수 $N(n/6, \, 5n/252)$ 를 빨간 곡선으로 겹쳐 놓는다.

- $n = 2$ 에서는 히스토그램이 눈에 띄게 오른쪽으로 치우쳐 작은 값 쪽에 몰려 있다.
- $n = 5$ 쯤 되면 모양이 더 대칭에 가까워지지만 아직 조금 치우쳐 있다.
- $n = 10$ 에서는 겹쳐 놓은 정규분포 곡선이 그런대로 잘 들어맞는다.
- $n = 30$ 과 $n = 100$ 에서는 히스토그램이 거의 대칭이고 정규분포 곡선과 잘 맞는다.

## 뜻풀이

베타분포는 중심극한정리에 대하여 몇 가지를 일러 준다.

1. **받침이 유계여도 정규분포가 되는 데 걸림돌이 되지 않는다.** 각 $X_i$ 가 $[0, 1]$ 안에 있으므로 $S_n$ 은 $[0, n]$ 안에 있다. 정규분포의 받침은 유계가 아니지만, $n$ 이 크면 경계 근처의 확률이 무시할 만해지므로 근사가 잘 맞는다.
2. **모수가 비대칭이면 왜도가 생긴다.** $\text{Beta}(1, 5)$ 의 밀도함수는 $f(x) = 5(1-x)^4$ 로 $x = 0$ 에서 봉우리를 이룬다. 왜도는 $2(\beta - \alpha)\sqrt{\alpha + \beta + 1}/[(\alpha + \beta + 2)\sqrt{\alpha\beta}] = 2(4)\sqrt{7}/(8\sqrt{5}) \approx 1.18$ 이다. 이만큼 왜도가 크면 대칭인 베타분포보다 더 많이 더해야 정규분포에 다가간다.
3. **특별한 경우: Beta(1,1) = U(0,1).** $\alpha = \beta = 1$ 이면 베타분포는 균등분포가 된다. 곧 이 쪽은 출발 분포를 치우친 것으로 바꾸어 균등분포의 경우를 더 넓힌 것이다.

## 연습문제

**연습문제 1.**
$\alpha = \beta = 1$ 인 베타분포의 밀도함수를 간단히 하여 $\text{Beta}(1, 1) = U(0, 1)$ 임을 보여라.

??? success "연습문제 1 풀이"
    $\alpha = \beta = 1$ 이면 다음과 같다.

    $$
    f(x) = \frac{x^{1-1}(1-x)^{1-1}}{B(1,1)} = \frac{1}{B(1,1)}.
    $$

    $B(1,1) = \Gamma(1)\Gamma(1)/\Gamma(2) = 1 \cdot 1 / 1 = 1$ 이므로 $0 < x < 1$ 에서 $f(x) = 1$ 이고, 이것은 $U(0,1)$ 의 밀도함수이다. $\square$

---

**연습문제 2.**
일반적인 $\text{Beta}(\alpha, \beta)$ 의 왜도를 구하고, $\alpha = \beta$ 일 때 그 값이 $0$ 임을 확인하여라.

??? success "연습문제 2 풀이"
    $\text{Beta}(\alpha, \beta)$ 의 왜도는 다음과 같다.

    $$
    \gamma_1 = \frac{2(\beta - \alpha)\sqrt{\alpha + \beta + 1}}{(\alpha + \beta + 2)\sqrt{\alpha\beta}}.
    $$

    $\alpha = \beta$ 이면 $\gamma_1 = \frac{2(0)\sqrt{2\alpha + 1}}{(2\alpha + 2)\sqrt{\alpha^2}} = 0$ 이다. $\alpha = \beta$ 일 때 분포가 $1/2$ 을 중심으로 대칭이므로 왜도가 $0$ 임이 확인된다.

---

**연습문제 3.**
베타확률변수를 더한 $S_n$ 의 분포에는 따로 정해진 이름이 없다. 모의실험 코드를 써서 모의실험으로 얻은 $S_{100}$ 의 평균과 분산이 이론값 $100/6$ 과 $500/252$ 에 가까움을 수치로 확인하여라.

??? success "연습문제 3 풀이"
    모의실험 반복문 뒤에 다음을 덧붙인다.

    ```python
    S_100 = np.sum(np.random.beta(1, 5, (100, n_sim)), axis=0)
    print(f"Simulated mean: {np.mean(S_100):.4f}, Theoretical: {100/6:.4f}")
    print(f"Simulated var:  {np.var(S_100):.4f}, Theoretical: {500/252:.4f}")
    ```

    이론적인 평균은 $100/6 \approx 16.667$ 이고 이론적인 분산은 $500/252 \approx 1.984$ 이다. 모의실험으로 얻은 값은 (표집오차 안에서) 이 값들에 아주 가까워야 한다.

---

**연습문제 4.**
베타확률변수의 합이 다시 베타분포가 되지 않는 까닭을 설명하여라. (힌트: 받침을 생각해 보아라.)

??? success "연습문제 4 풀이"
    $\text{Beta}(\alpha, \beta)$ 확률변수의 받침은 $[0, 1]$ 이다. $X_i \sim \text{Beta}(\alpha, \beta)$ 에 대하여 $S_2 = X_1 + X_2$ 라 하면 $S_2$ 의 받침은 $[0, 2]$ 이다. 받침이 $[0, 2]$ 인 베타분포는 없으므로(모든 베타분포의 받침은 $[0, 1]$ 이다) $S_2$ 는 베타분포일 수 없다. 더 일반적으로 $S_n$ 의 받침은 $[0, n]$ 이므로 베타족일 가능성이 더욱 없다. 이는 합성곱에 대하여 닫혀 있는 푸아송족이나 감마족과 대비된다.

---

**연습문제 5.**
대칭인 분포인 $\text{Beta}(5, 5)$ 를 쓰도록 모의실험을 고쳐라. $\text{Beta}(1, 5)$ 인 경우와 수렴 속도를 견주어라. 어느 쪽이 정규분포로 더 빨리 다가가며 그 까닭은 무엇인가?

??? success "연습문제 5 풀이"
    `a, b = 1, 5` 를 `a, b = 5, 5` 로 바꾼다. $\text{Beta}(5, 5)$ 분포는 $1/2$ 을 중심으로 대칭이고 왜도가 $0$ 이므로, 모든 $n$ 에 대하여 합 $S_n$ 이 대칭이다. 따라서 $\text{Beta}(1, 5)$ 인 경우보다 더 작은 $n$ 에서도 정규근사가 눈으로 보기에 잘 맞을 것이다.

    수치로 보면 $\text{Beta}(5, 5)$ 의 초과첨도는 $-6/(5 \cdot 11) = -6/55 \approx -0.109$ 로 이미 $0$ 에 가깝다. 이에 견주어 $\text{Beta}(1, 5)$ 의 왜도는 약 $1.18$ 이라서 이것이 흩어져 사라지려면 많이 더해야 한다. 대칭인 경우에는 가장 큰 보정 항(왜도)이 아예 없고 $O(1/n)$ 인 첨도 보정만 남으므로 수렴이 더 빠르다.
