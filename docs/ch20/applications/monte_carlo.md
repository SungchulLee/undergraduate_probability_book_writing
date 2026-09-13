# 몬테카를로 모의실험

## 생각의 얼개

몬테카를로 방법은 해석적으로 셈하기 어려운 값을 **무작위 표집**으로 어림한다. 표본평균이 기댓값으로 수렴한다는 큰수의 법칙이 그 이론적 바탕이다.

분포를 아는 확률변수 $X$ 에 대하여 $\theta = \mathbb{E}[g(X)]$ 를 셈하고 싶다면 다음과 같이 하면 된다.

1. $X$ 의 분포에서 i.i.d. 표본 $X_1, \ldots, X_n$ 을 뽑는다.
2. 표본평균 $\hat{\theta}_n = \frac{1}{n}\sum_{i=1}^n g(X_i)$ 를 셈한다.
3. 큰수의 법칙에 따라 $n \to \infty$ 일 때 $\hat{\theta}_n \to \theta$ 이다.

## 몬테카를로로 원주율 어림하기

### 문제 설정

정사각형 $[-1, 1]^2$ 에서 고르게 무작위로 점 $X_i$ 를 $n$ 개 뽑는다. 다음과 같이 정의하자.

$$
R_i = \begin{cases} 1 & X_i \text{ 가 단위원 안에 있을 때} \\ 0 & \text{그 밖의 경우} \end{cases}
$$

그러면 $R_i \overset{iid}{\sim} \text{Bernoulli}(p)$ 이고 여기에서 $p$ 는 다음과 같다.

$$
p = \frac{\text{단위원의 넓이}}{\text{정사각형의 넓이}} = \frac{\pi}{4}
$$

### 어림하기

큰수의 법칙에 따라 다음이 성립한다.

$$
\frac{1}{n}\sum_{i=1}^n R_i \xrightarrow{a.s.} \frac{\pi}{4}
$$

따라서 다음을 얻는다.

$$
\pi \approx \frac{4}{n}\sum_{i=1}^n R_i = 4 \times \frac{\text{원 안에 든 점의 수}}{n}
$$

### 파이썬 구현

```python
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
n = 5000

# [-1, 1]^2 안에서 무작위로 점을 만든다
x = 2 * np.random.rand(2, n) - 1

# 단위원 안에 있는지 확인한다
r2 = x[0]**2 + x[1]**2
inside = r2 <= 1

# 원주율을 어림한다
estimated_pi = 4 * np.sum(inside) / n
print(f"Estimated pi: {estimated_pi:.4f}")

# 그림 그리기
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

# 산점도
axes[0].scatter(x[0, inside], x[1, inside], c='red', s=1, label='Inside')
axes[0].scatter(x[0, ~inside], x[1, ~inside], c='blue', s=1, label='Outside')
axes[0].set_aspect('equal')
axes[0].set_title(f'{n} Random Darts')
axes[0].legend()

# 그때까지의 어림값
running_pi = 4 * np.cumsum(inside) / np.arange(1, n + 1)
axes[1].plot(range(1, n + 1), running_pi, 'r-', alpha=0.7)
axes[1].axhline(y=np.pi, color='k', linestyle='-', label='True π')
axes[1].set_xlabel('Number of darts')
axes[1].set_ylabel('Estimate of π')
axes[1].set_title('Running Estimate (Strong Law)')
axes[1].legend()

# 실험을 되풀이한 결과의 히스토그램
m = 1000  # 실험 횟수
n_each = 100  # 실험 한 번에 던지는 다트 수
estimates = np.array([
    4 * np.sum(np.sum((2*np.random.rand(2, n_each)-1)**2, axis=0) <= 1) / n_each
    for _ in range(m)
])
axes[2].hist(estimates, bins=30, edgecolor='black')
axes[2].axvline(x=np.pi, color='r', linestyle='--', label='True π')
axes[2].set_xlabel('Estimate of π')
axes[2].set_ylabel('Frequency')
axes[2].set_title(f'Histogram ({m} experiments, {n_each} darts each)')
axes[2].legend()

plt.tight_layout()
plt.savefig('monte_carlo_pi.png', dpi=150, bbox_inches='tight')
plt.show()
```

### 관찰

- **왼쪽 그림**(한 줄기의 그때까지의 어림값)은 **강법칙**을 보여 준다. 표본경로 하나가 $\pi$ 로 수렴한다.
- **오른쪽 그림**(여러 어림값의 히스토그램)은 **약법칙**을 보여 준다. 표본평균의 분포가 $\pi$ 주위로 몰린다.
- 다트를 더 많이 던질수록 $\Rightarrow$ 더 좋은 어림값을 얻는다. 표준오차는 $\sigma/\sqrt{n}$ 이며 $1/\sqrt{n}$ 의 속도로 줄어든다.

## 연습문제

**연습문제 1.**
$\theta = \int_0^1 e^{-x^2} \, dx$ 를 어림하는 몬테카를로 모의실험을 설계하여라. $U \sim U(0,1)$ 에 대하여 $\theta = E[g(U)]$ 로 적고, $g(U_1), \ldots, g(U_n)$ 의 표본평균을 셈한 뒤, 중심극한정리를 써서 $n = 10{,}000$ 일 때 $\theta$ 의 95% 신뢰구간을 만들어라.

??? success "연습문제 1 풀이"
    **1단계: 적분을 기댓값으로 바꾼다.** $U \sim U(0,1)$ 의 확률밀도함수는 $[0,1]$ 위에서 $f(u) = 1$ 이다. 그러므로 무의식적 통계학자의 법칙(LOTUS)에서 임의의 함수 $g$ 에 대하여 다음이 성립한다.

    $$
    \mathbb{E}[g(U)] = \int_0^1 g(u) \cdot 1 \, du = \int_0^1 g(u)\, du
    $$

    따라서 $g(u) = e^{-u^2}$ 으로 두면 우리가 원하는 적분이 그대로 기댓값이 된다.

    $$
    \theta = \int_0^1 e^{-x^2}\, dx = \mathbb{E}\!\left[e^{-U^2}\right] = \mathbb{E}[g(U)]
    $$

    **2단계: 추정량을 세운다.** $U_1, \ldots, U_n$ 을 i.i.d. $U(0,1)$ 로 뽑고 다음과 같이 둔다.

    $$
    \hat{\theta}_n = \frac{1}{n}\sum_{i=1}^n g(U_i) = \frac{1}{n}\sum_{i=1}^n e^{-U_i^2}
    $$

    $Y_i = g(U_i)$ 는 i.i.d. 이고 $0 < e^{-1} \leq Y_i \leq 1$ 로 **유계**이므로 모든 적률이 유한하다. 큰수의 강법칙에서 다음이 성립한다.

    $$
    \hat{\theta}_n \xrightarrow{a.s.} \theta
    $$

    또한 $\mathbb{E}[\hat{\theta}_n] = \theta$ 이므로 이 추정량은 **불편추정량**이다.

    **3단계: 분산을 셈한다.** 신뢰구간의 폭을 정하는 것은 $\sigma^2 = \text{Var}(g(U))$ 이다.

    $$
    \sigma^2 = \mathbb{E}[g(U)^2] - \theta^2 = \int_0^1 e^{-2x^2}\, dx - \left(\int_0^1 e^{-x^2}\, dx\right)^{\!2}
    $$

    두 적분은 오차함수로 정확히 적힌다.

    $$
    \int_0^1 e^{-x^2}dx = \frac{\sqrt{\pi}}{2}\,\text{erf}(1) = 0.7468, \qquad \int_0^1 e^{-2x^2}dx = \frac{\sqrt{\pi}}{2\sqrt{2}}\,\text{erf}(\sqrt{2}) = 0.5981
    $$

    그러므로 다음과 같다.

    $$
    \sigma^2 = 0.5981 - (0.7468)^2 = 0.0404, \qquad \sigma = 0.2010
    $$

    **4단계: 중심극한정리로 신뢰구간을 만든다.** $Y_i$ 가 i.i.d. 이고 분산이 유한하므로 중심극한정리를 쓸 수 있다.

    $$
    \frac{\hat{\theta}_n - \theta}{\sigma/\sqrt{n}} \xrightarrow{d} N(0,1)
    $$

    표준정규분포의 $97.5$ 백분위수가 $z_{0.025} = 1.96$ 이므로 $95\%$ 신뢰구간은 다음과 같다.

    $$
    \hat{\theta}_n \pm 1.96 \frac{\sigma}{\sqrt{n}}
    $$

    $n = 10{,}000$ 을 넣으면 표준오차와 반폭이 다음과 같이 나온다.

    $$
    \frac{\sigma}{\sqrt{n}} = \frac{0.2010}{100} = 0.0020, \qquad 1.96 \times 0.0020 = 0.0039
    $$

    곧 $n = 10{,}000$ 이면 소수 둘째 자리까지는 믿을 수 있고 셋째 자리는 아슬아슬하다.

    **5단계: 실제로 돌려 본다.** 실제 상황에서는 $\sigma$ 를 모르므로 표본표준편차 $S$ 로 바꾸어 쓴다. 큰수의 법칙이 $S \xrightarrow{a.s.} \sigma$ 를 보장하므로 이 바꿔치기가 정당하다.

    $$
    \hat{\theta}_n \pm 1.96 \frac{S}{\sqrt{n}}, \qquad S^2 = \frac{1}{n-1}\sum_{i=1}^n \left(g(U_i) - \hat{\theta}_n\right)^2
    $$

    ```python
    import numpy as np
    from scipy import integrate

    theta, _ = integrate.quad(lambda x: np.exp(-x**2), 0, 1)
    m2, _ = integrate.quad(lambda x: np.exp(-2 * x**2), 0, 1)
    var = m2 - theta**2

    rng = np.random.default_rng(42)
    n = 10000
    g = np.exp(-rng.random(n)**2)
    est, s = g.mean(), g.std(ddof=1)
    half = 1.96 * s / np.sqrt(n)

    print(f"theta (exact)   = {theta:.4f}")
    print(f"Var(g(U))       = {var:.4f}   sd = {np.sqrt(var):.4f}")
    print(f"MC estimate     = {est:.4f}   sample sd = {s:.4f}")
    print(f"95% CI          = ({est - half:.4f}, {est + half:.4f})")
    ```

    실행 결과는 다음과 같다.

    ```
    theta (exact)   = 0.7468
    Var(g(U))       = 0.0404   sd = 0.2010
    MC estimate     = 0.7489   sample sd = 0.2005
    95% CI          = (0.7450, 0.7529)
    ```

    표본표준편차 $0.2005$ 가 참값 $0.2010$ 과 거의 같고, 얻은 신뢰구간 $(0.7450,\, 0.7529)$ 는 참값 $\theta = 0.7468$ 을 제대로 품고 있다.

    **6단계: 얼마나 더 뽑아야 하는가.** 반폭이 $1.96\sigma/\sqrt{n}$ 이므로 정밀도는 $1/\sqrt{n}$ 으로만 좋아진다. 자릿수를 하나 더 얻으려면 표본을 **100배** 늘려야 한다는 뜻이다.

    | $n$ | 반폭 $1.96\sigma/\sqrt{n}$ |
    |---|---|
    | $100$ | $0.0394$ |
    | $10{,}000$ | $0.0039$ |
    | $1{,}000{,}000$ | $0.0004$ |

    이것이 몬테카를로의 근본적인 한계이며, 동시에 차원이 높아져도 이 속도가 그대로라는 점이 몬테카를로의 힘이기도 하다. 일차원 적분이라면 사다리꼴 공식이 훨씬 빠르지만, 차원이 수십으로 올라가면 격자를 쓰는 방법은 무너지고 $1/\sqrt{n}$ 만 남는다. $\square$
