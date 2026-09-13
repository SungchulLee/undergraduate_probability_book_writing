# 독립인 정규확률변수의 합(합성곱으로)

## 결과

!!! info "정규분포의 합성곱"
    $X \sim N(\mu_1, \sigma_1^2)$ 과 $Y \sim N(\mu_2, \sigma_2^2)$ 가 독립이면 다음이 성립한다.

    $$X + Y \sim N(\mu_1 + \mu_2, \; \sigma_1^2 + \sigma_2^2)$$

    곧 정규분포족은 **합성곱에 대하여 닫혀 있다**. 독립인 정규확률변수의 합은 다시 정규분포를 따른다.

## 적률생성함수를 쓴 증명

적률생성함수를 쓰는 방법이 가장 깔끔하다.

$$M_{X+Y}(t) = M_X(t) \cdot M_Y(t) = e^{\mu_1 t + \sigma_1^2 t^2/2} \cdot e^{\mu_2 t + \sigma_2^2 t^2/2} = e^{(\mu_1+\mu_2)t + (\sigma_1^2+\sigma_2^2)t^2/2}$$

이것은 $N(\mu_1 + \mu_2, \sigma_1^2 + \sigma_2^2)$ 의 적률생성함수이다. 적률생성함수의 유일성에 따라 결론이 따라 나온다.

## 합성곱 적분을 쓴 증명

$X \sim N(0, 1)$ 과 $Y \sim N(0, 1)$ 이 독립인 경우(표준적인 경우)를 보자.

$$f_{X+Y}(a) = \int_{-\infty}^{\infty} \frac{1}{\sqrt{2\pi}} e^{-b^2/2} \cdot \frac{1}{\sqrt{2\pi}} e^{-(a-b)^2/2} \, db$$

지수에서 완전제곱을 만든 뒤 가우스적분을 계산하면 다음을 얻는다.

$$f_{X+Y}(a) = \frac{1}{\sqrt{4\pi}} e^{-a^2/4}$$

이것은 $N(0, 2)$ 의 확률밀도함수이므로 $N(0,1) + N(0,1) = N(0, 2)$ 임이 확인된다.

## 일반적인 합

$X_1, X_2, \ldots, X_n$ 이 독립이고 $X_i \sim N(\mu_i, \sigma_i^2)$ 이면 다음이 성립한다.

$$\sum_{i=1}^n X_i \sim N\!\left(\sum_{i=1}^n \mu_i, \; \sum_{i=1}^n \sigma_i^2\right)$$

특히 $X_i$ 가 i.i.d. $N(\mu, \sigma^2)$ 이면 다음을 얻는다.

$$\bar{X} = \frac{1}{n}\sum_{i=1}^n X_i \sim N\!\left(\mu, \; \frac{\sigma^2}{n}\right)$$

## 파이썬 구현

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

np.random.seed(42)
n_sim = 100000

mu1, sig1 = 2, 1.5
mu2, sig2 = -1, 2.0

X = np.random.normal(mu1, sig1, n_sim)
Y = np.random.normal(mu2, sig2, n_sim)
S = X + Y

mu_sum = mu1 + mu2
sig_sum = np.sqrt(sig1**2 + sig2**2)

fig, ax = plt.subplots(figsize=(8, 5))
ax.hist(S, bins=80, density=True, alpha=0.5, color='steelblue',
        label='Simulated X+Y')
x = np.linspace(mu_sum - 4*sig_sum, mu_sum + 4*sig_sum, 200)
ax.plot(x, stats.norm.pdf(x, mu_sum, sig_sum), 'r-', lw=2,
        label=f'N({mu_sum}, {sig_sum**2:.2f}) PDF')
ax.set_title(f'N({mu1},{sig1**2}) + N({mu2},{sig2**2}) = N({mu_sum},{sig_sum**2:.2f})')
ax.legend()
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('sum_normals.png', dpi=150, bbox_inches='tight')
plt.show()

print(f"Simulated: mean={np.mean(S):.4f}, var={np.var(S):.4f}")
print(f"Theory:    mean={mu_sum:.4f}, var={sig_sum**2:.4f}")
```

## 연습문제

**연습문제 1.**
확률변수 $W$ 의 적률생성함수가 $t < 1/2$ 에서 $M_W(t) = (1 - 2t)^{-5}$ 라고 하자. $W$ 의 분포가 무엇인지 알아내어라. 또 $V_1 \sim \chi^2_3$ 과 $V_2 \sim \chi^2_7$ 이 독립이고 $W = V_1 + V_2$ 라 할 때, $V_1 + V_2$ 의 적률생성함수가 $M_W(t)$ 와 일치함을 확인하고 그 분포가 무엇인지 밝혀라.

??? success "연습문제 1 풀이"
    **1단계: 자유도 읽어 내기.** 자유도가 $k$ 인 카이제곱분포의 적률생성함수는 다음과 같다.

    $$
    M(t) = (1 - 2t)^{-k/2}, \qquad t < \frac{1}{2}
    $$

    주어진 $M_W(t) = (1-2t)^{-5}$ 와 지수를 맞추면 $-k/2 = -5$, 곧 $k = 10$ 이다. 적률생성함수는 분포를 하나로 결정하므로 다음을 얻는다.

    $$
    W \sim \chi^2_{10}
    $$

    **2단계: $V_1 + V_2$ 의 적률생성함수.** $V_1 \sim \chi^2_3$ 과 $V_2 \sim \chi^2_7$ 이 독립이므로 적률생성함수는 곱해진다.

    $$
    M_{V_1 + V_2}(t) = M_{V_1}(t) \cdot M_{V_2}(t) = (1-2t)^{-3/2} \cdot (1-2t)^{-7/2}
    $$

    밑이 같으므로 지수를 더하면 된다. $\dfrac{3}{2} + \dfrac{7}{2} = \dfrac{10}{2} = 5$ 이므로 다음과 같다.

    $$
    M_{V_1 + V_2}(t) = (1-2t)^{-5} = M_W(t), \qquad t < \frac{1}{2}
    $$

    **3단계: 결론.** 두 적률생성함수가 같은 구간 $t < 1/2$ 에서 일치하므로, 유일성에 따라 두 분포는 같다.

    $$
    V_1 + V_2 \sim \chi^2_{3 + 7} = \chi^2_{10}
    $$

    자유도가 그냥 더해진다는 이 성질은 정규분포의 합에서 분산이 더해지는 것과 뿌리가 같다. $\chi^2_k$ 는 독립인 표준정규확률변수 $k$ 개의 제곱합이므로, $V_1$ 을 만드는 $3$ 개와 $V_2$ 를 만드는 $7$ 개를 이어 붙이면 $10$ 개의 제곱합이 된다. 따라서 $E[W] = 10$, $\text{Var}(W) = 2 \cdot 10 = 20$ 이다. $\square$

---

**연습문제 2.**
$X_1, \ldots, X_4$ 가 독립이고 $X_i \sim N(i, i^2)$ 이라고 하자. $S = X_1 + X_2 + X_3 + X_4$ 의 정확한 분포를 구하여라.

??? success "연습문제 2 풀이"
    **1단계: 모수 읽기.** $X_i \sim N(i, i^2)$ 이라는 표기에서 둘째 자리는 **분산**이다. 그러므로 다음과 같다.

    | $i$ | $\mu_i = i$ | $\sigma_i^2 = i^2$ |
    |:---:|:---:|:---:|
    | $1$ | $1$ | $1$ |
    | $2$ | $2$ | $4$ |
    | $3$ | $3$ | $9$ |
    | $4$ | $4$ | $16$ |

    **2단계: 평균 더하기.** 기댓값의 선형성은 독립을 요구하지 않으므로 언제나 쓸 수 있다.

    $$
    E[S] = \sum_{i=1}^{4} i = 1 + 2 + 3 + 4 = 10
    $$

    **3단계: 분산 더하기.** 여기에서는 독립성이 꼭 필요하다. 독립이므로 공분산 항이 모두 $0$ 이 되어 분산이 그대로 더해진다.

    $$
    \text{Var}(S) = \sum_{i=1}^{4} i^2 = 1 + 4 + 9 + 16 = 30
    $$

    **4단계: 정규성.** 독립인 정규확률변수의 합은 다시 정규분포를 따른다. 적률생성함수로 확인해 보면 다음과 같다.

    $$
    M_S(t) = \prod_{i=1}^{4} e^{\,i t + i^2 t^2/2} = e^{\,10 t + 30 t^2/2}
    $$

    이것은 평균 $10$, 분산 $30$ 인 정규분포의 적률생성함수이다. 따라서 다음을 얻는다.

    $$
    S \sim N(10, \, 30)
    $$

    표준편차는 $\sqrt{30} \approx 5.4772$ 이다. 분산이 **표준편차가 아니라** 더해진다는 점에 주의하여라. 표준편차를 더하면 $1 + 2 + 3 + 4 = 10$ 이 되는데, 이는 참값 $5.4772$ 와 전혀 다르다. $\square$

---

**연습문제 3.**
$X \sim N(3, 4)$ 와 $Y \sim N(-1, 9)$ 가 독립이라고 하자. $P(X + Y > 5)$ 를 구하여라.

*힌트: 먼저 $X + Y$ 의 분포를 알아낸 다음 표준화한다.*

??? success "연습문제 3 풀이"
    **1단계: 합의 분포.** $X \sim N(3, 4)$ 와 $Y \sim N(-1, 9)$ 가 독립이므로 평균과 분산이 각각 더해진다.

    $$
    E[X + Y] = 3 + (-1) = 2, \qquad \text{Var}(X + Y) = 4 + 9 = 13
    $$

    독립인 정규확률변수의 합은 정규분포를 따르므로 다음과 같다.

    $$
    S = X + Y \sim N(2, \, 13)
    $$

    표준편차는 $\sqrt{13} \approx 3.6056$ 이다.

    **2단계: 표준화.** $Z = \dfrac{S - 2}{\sqrt{13}} \sim N(0,1)$ 로 놓는다.

    $$
    P(S > 5) = P\!\left(\frac{S - 2}{\sqrt{13}} > \frac{5 - 2}{\sqrt{13}}\right) = P\!\left(Z > \frac{3}{\sqrt{13}}\right)
    $$

    **3단계: Z-점수 계산.**

    $$
    \frac{3}{\sqrt{13}} \approx \frac{3}{3.6056} \approx 0.8321
    $$

    **4단계: 표준정규분포표에서 값 읽기.** $\Phi(0.8321) \approx 0.7973$ 이므로 다음을 얻는다.

    $$
    P(X + Y > 5) = 1 - \Phi(0.8321) \approx 1 - 0.7973 = 0.2027
    $$

    기준값 $5$ 가 평균보다 표준편차의 약 $0.83$ 배만큼 위에 있으므로 확률이 $20\%$ 를 조금 넘는 것은 자연스럽다. 여기에서도 분산을 더한 뒤에 제곱근을 취해야 하며, 표준편차를 먼저 더해 $2 + 3 = 5$ 로 쓰면 잘못된 답이 나온다. $\square$
