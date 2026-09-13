# t분포는 왜 필요한가: 모의실험

모분산을 모른 채 표본에서 추정해야 할 때, 표준화한 표본평균은 표준정규분포가 아니라 스튜던트 t분포를 따른다. 이 모의실험은 통계량 $(\bar{X} - \mu)/(S/\sqrt{n})$ 이 $N(0,1)$ 보다 꼬리가 두껍고 $t_{n-1}$ 의 밀도함수와 정확히 맞아떨어짐을 보여 준다.

## 배경

$X_1, X_2, \ldots, X_n$ 이 i.i.d. $N(\mu, \sigma^2)$ 이라고 하자. $\sigma$ 를 안다면 통계량

$$
Z = \frac{\bar{X} - \mu}{\sigma / \sqrt{n}} \sim N(0, 1)
$$

은 표준정규분포를 따른다. 그러나 실제로 $\sigma$ 를 아는 일은 드물기에 그 자리에 표본표준편차 $S = \sqrt{\frac{1}{n-1}\sum_{i=1}^n (X_i - \bar{X})^2}$ 를 넣는다. 그렇게 얻은 통계량

$$
T = \frac{\bar{X} - \mu}{S / \sqrt{n}}
$$

은 더 이상 정규분포를 따르지 않는다. $S$ 자체가 확률변수여서 흔들림을 더 보태기 때문이며, 이는 특히 $n$ 이 작을 때 두드러진다. 그래서 $T$ 는 꼬리가 두껍다. 엄밀히 말하면 $T \sim t_{n-1}$ 이고, 자유도가 $\nu$ 인 t분포의 밀도함수는 다음과 같다.

$$
f_{t_\nu}(x) = \frac{\Gamma\!\left(\frac{\nu+1}{2}\right)}{\sqrt{\nu\pi}\;\Gamma\!\left(\frac{\nu}{2}\right)} \left(1 + \frac{x^2}{\nu}\right)^{-(\nu+1)/2}, \quad x \in \mathbb{R}
$$

핵심은 정규자료에서 $\bar{X}$ 과 $S^2$ 이 독립이라는 것(코크란 정리의 따름)과, $T$ 를 표준정규확률변수를 그와 독립인 $\chi^2$ 확률변수를 자유도로 나눈 것의 제곱근으로 나눈 꼴로 쓸 수 있다는 것이다.

## 코드

```python
"""t분포가 왜 필요한가: 정규자료에서 (X̄ − μ)/(S/√n) 은 t_{n-1} 을 따른다."""
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

np.random.seed(42)

sample_size = 10_000
mu, sigma = 0, 10
n = 10

# 실험 하나마다 관측값 n 개를 뽑고, 이를 sample_size 번 되풀이한다
x = np.random.normal(mu, sigma, (n, sample_size))
x_bar = x.mean(axis=0)
s = x.std(axis=0, ddof=1)

# 스튜던트화한 통계량
t_stat = (x_bar - mu) / (s / np.sqrt(n))

fig, ax = plt.subplots(figsize=(10, 5))
bins = np.arange(-6, 6, 0.1)
ax.hist(t_stat, bins=bins, density=True, alpha=0.6, color="steelblue",
        label="Simulated t-statistic")
ax.plot(bins, stats.t(df=n - 1).pdf(bins), "--r", lw=2, label=f"t({n-1}) PDF")
ax.plot(bins, stats.norm.pdf(bins), ":k", lw=1.5, label="N(0,1) PDF")
ax.set_title(f"(X̄ − μ) / (S/√n)  ~  t({n-1})", fontsize=14)
ax.legend()
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig("why_t_distribution.png", dpi=150, bbox_inches="tight")
plt.show()
```

## 실행 결과

이 코드는 세 곡선이 겹쳐 그려진 그림 하나를 만들어 낸다.

- **파란 히스토그램**: $N(0, 10^2)$ 에서 크기 $n = 10$ 인 표본을 뽑아 $(\bar{X} - \mu)/(S/\sqrt{n})$ 을 계산하기를 10 000번 되풀이하여 얻은 경험적 분포이다.
- **빨간 점선**: 이론적인 $t_9$ 의 밀도함수이다.
- **검은 점선**: 표준정규분포 $N(0,1)$ 의 밀도함수이다.

히스토그램은 $t_9$ 곡선과는 잘 맞지만 $N(0,1)$ 과는 맞지 않는다. 그 차이는 꼬리에서 가장 뚜렷하다. $|x| > 2$ 에서 $t_9$ 의 밀도가 정규분포의 밀도보다 눈에 띄게 높다.

## 뜻풀이

이 모의실험은 $\sigma$ 를 $S$ 로 추정할 때 표준화한 통계량이 표준정규분포가 아니라 자유도 $n - 1 = 9$ 인 t분포를 따른다는 사실을 확인해 준다. $S$ 에서 오는 여분의 무작위성이 꼬리를 부풀리기에 $T$ 의 극단적인 값이 $N(0,1)$ 에서보다 더 자주 나온다. $n$ 이 작을 때 t분포에 바탕을 둔 신뢰구간과 가설검정이 $N(0,1)$ 에 바탕을 둔 것보다 넓은 까닭이 여기에 있다. $n$ 이 커지면 $S$ 가 $\sigma$ 로 수렴하고 t분포는 $N(0,1)$ 에 가까워진다.

## 연습문제

**연습문제 1.**
모의실험을 고쳐 $n = 50$ 과 $n = 200$ 으로 실행하여라. $n$ 이 커질 때 히스토그램은 $N(0,1)$ 곡선과 견주어 어떻게 되는가?

??? success "연습문제 1 풀이"
    $n$ 이 커지면 $S$ 가 $\sigma$ 를 더 정확히 추정하므로 $\sigma$ 를 추정하면서 생기는 여분의 무작위성이 줄어든다. $n = 50$ ($\nu = 49$)이면 t분포가 이미 $N(0,1)$ 에 매우 가까워 히스토그램이 거의 겹친다. $n = 200$ ($\nu = 199$)이면 눈으로는 차이를 알 수 없다. 엄밀히 말하면 $\nu \to \infty$ 일 때 $t_\nu \xrightarrow{d} N(0,1)$ 이다.

---

**연습문제 2.**
$n = 10$ 인 모의실험에서 $P(|T| > 2)$ 를 구하고, $t_9$ 와 $N(0,1)$ 에서의 이론값과 견주어라.

??? success "연습문제 2 풀이"
    ```python
    import numpy as np
    from scipy import stats

    np.random.seed(42)
    n = 10
    x = np.random.normal(0, 10, (n, 10_000))
    t_stat = (x.mean(axis=0) - 0) / (x.std(axis=0, ddof=1) / np.sqrt(n))

    sim_prob = np.mean(np.abs(t_stat) > 2)
    t_prob = 2 * stats.t(df=n-1).sf(2)
    z_prob = 2 * stats.norm.sf(2)
    print(f"Simulated: {sim_prob:.4f}")
    print(f"t(9):      {t_prob:.4f}")
    print(f"N(0,1):    {z_prob:.4f}")
    ```

    보통 모의실험값은 $\approx 0.077$, $t_9$ 의 이론값은 $\approx 0.0773$, $N(0,1)$ 의 이론값은 $\approx 0.0455$ 로 나온다. 모의실험값이 $t_9$ 와 맞아떨어지며, 이 꼬리확률은 $N(0,1)$ 의 것보다 약 70% 크다.

---

**연습문제 3.**
$Z \sim N(0,1)$, $V \sim \chi^2_\nu$, $Z \perp V$, $\nu = n - 1$ 일 때 $T = \frac{\bar{X} - \mu}{S/\sqrt{n}}$ 을 $Z / \sqrt{V/\nu}$ 꼴로 쓸 수 있음을 보여라.

??? success "연습문제 3 풀이"
    다음과 같이 쓴다.

    $$
    T = \frac{\bar{X} - \mu}{S/\sqrt{n}} = \frac{(\bar{X} - \mu)/(\sigma/\sqrt{n})}{S/\sigma}
    $$

    분자는 $Z = (\bar{X} - \mu)/(\sigma/\sqrt{n}) \sim N(0,1)$ 이다. 분모에 대해서는 $(n-1)S^2/\sigma^2 \sim \chi^2_{n-1}$ 이므로 $V = (n-1)S^2/\sigma^2$ 으로 두면 다음과 같다.

    $$
    \frac{S}{\sigma} = \sqrt{\frac{V}{n-1}}
    $$

    따라서 $\nu = n - 1$ 일 때 $T = Z / \sqrt{V/(n-1)}$ 이다. 코크란 정리에 따라 정규자료에서 $\bar{X}$ 과 $S^2$ 이 독립이므로 $Z \perp V$ 이다. 이것이 바로 자유도 $\nu$ 인 t분포의 정의이다. $\square$

---

**연습문제 4.**
$X_1, \ldots, X_n$ 이 평균 $\mu$, 분산 $\sigma^2$ 인 분포에서 뽑은 i.i.d. 표본이지만 그 분포가 정규분포가 **아니라면**, $(\bar{X} - \mu)/(S/\sqrt{n})$ 은 여전히 t분포를 따르는가? 설명하여라.

??? success "연습문제 4 풀이"
    따르지 않는다. t분포라는 정확한 결과에는 정규성이 필요하다. 그 유도는 정규모집단에서만 성립하는 두 사실, 곧 (1) $\bar{X}$ 과 $S^2$ 이 독립이라는 것과 (2) $(n-1)S^2/\sigma^2 \sim \chi^2_{n-1}$ 이라는 것에 기대고 있다. 정규분포가 아닌 모집단에서는 둘 다 일반적으로 성립하지 않는다. 다만 $n$ 이 크면 중심극한정리에 따라 $(\bar{X} - \mu)/(\sigma/\sqrt{n})$ 이 대략 $N(0,1)$ 이고 $S \xrightarrow{p} \sigma$ 이므로 $(\bar{X} - \mu)/(S/\sqrt{n})$ 도 대략 $N(0,1)$ 이다($\nu \to \infty$ 일 때 $t_\nu \to N(0,1)$ 이므로 대략 $t_{n-1}$ 이라고 해도 된다). 정규분포가 아닌 자료에서 $n$ 이 작으면 정규분포도 t분포도 정확하지 않다.

---

**연습문제 5.**
$\nu > 2$ 일 때 $t_\nu$ 의 분산이 $\nu / (\nu - 2)$ 임을 증명하여라.

??? success "연습문제 5 풀이"
    독립인 $Z \sim N(0,1)$ 과 $V \sim \chi^2_\nu$ 에 대하여 $T = Z / \sqrt{V/\nu}$ 로 쓰자. $E[Z] = 0$ 이므로 대칭성에 따라 $E[T] = E[Z] \cdot E[1/\sqrt{V/\nu}] = 0$ 이다. 2차 적률은 독립성에 따라 다음과 같다.

    $$
    E[T^2] = E\!\left[\frac{Z^2}{V/\nu}\right] = E[Z^2] \cdot E\!\left[\frac{\nu}{V}\right] = 1 \cdot \nu \cdot E\!\left[\frac{1}{V}\right]
    $$

    $V \sim \chi^2_\nu = \Gamma(\nu/2, 1/2)$ 이므로 역적률 공식을 쓴다. $\alpha > 1$ 인 $V \sim \Gamma(\alpha, \lambda)$ 에 대하여 $E[1/V] = \lambda / (\alpha - 1)$ 이다. 여기에서는 $\alpha = \nu/2$, $\lambda = 1/2$ 이므로 $\nu > 2$ 일 때 다음이 성립한다.

    $$
    E\!\left[\frac{1}{V}\right] = \frac{1/2}{\nu/2 - 1} = \frac{1}{\nu - 2}
    $$

    따라서 다음을 얻는다.

    $$
    \text{Var}(T) = E[T^2] = \nu \cdot \frac{1}{\nu - 2} = \frac{\nu}{\nu - 2}
    $$

    이는 유한한 $\nu > 2$ 모두에 대하여 $1$ 보다 크며, t분포가 $N(0,1)$ 보다 꼬리가 두껍다는 사실을 확인해 준다. $\square$
