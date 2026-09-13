# 동전 던지기의 약법칙: 모의실험

이 모의실험은 공정한 동전 던지기로 큰수의 약법칙(WLLN)을 눈으로 보여 준다. $n$ 을 점점 키워 가며 표본평균 $\bar{X}_n$ 의 분포를 그려 보면, 그 분포가 참확률 $p = 0.5$ 주위로 몰리는 모습을 볼 수 있다. 이는 $\bar{X}_n \xrightarrow{P} p$ 임을 눈으로 확인시켜 주는 증거이다.

## 배경

$X_1, X_2, \ldots$ 를 $P(X_i = 1) = p = 0.5$ 인 i.i.d. 베르누이확률변수라고 하자. $n$ 번 던진 뒤의 표본평균은 다음과 같다.

$$
\bar{X}_n = \frac{1}{n}\sum_{i=1}^n X_i
$$

**큰수의 약법칙**은 모든 $\varepsilon > 0$ 에 대하여 다음이 성립한다고 말한다.

$$
P\!\left(|\bar{X}_n - p| > \varepsilon\right) \to 0 \quad n \to \infty \text{ 일 때}
$$

이것이 확률수렴이다. 표본 크기가 커질수록, 여러 번 독립적으로 되풀이한 실험에서 얻은 $\bar{X}_n$ 의 히스토그램이 $p$ 주위로 점점 더 몰린다. 체비쇼프 부등식은 이를 수치로 재는 경계를 준다.

$$
P\!\left(|\bar{X}_n - p| > \varepsilon\right) \leq \frac{\operatorname{Var}(\bar{X}_n)}{\varepsilon^2} = \frac{p(1-p)}{n\varepsilon^2}
$$

$p = 0.5$ 이면 $\operatorname{Var}(\bar{X}_n) = 1/(4n)$ 이므로 분포의 퍼짐은 $1/\sqrt{n}$ 의 속도로 줄어든다.

## 코드

```python
"""큰수의 약법칙: 표본평균의 분포가 p 주위로 몰린다."""
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)

p = 0.5
num_paths = 10_000
num_steps = 10_000

flips = np.random.binomial(1, p, (num_paths, num_steps))
cumsum = flips.cumsum(axis=1)

fig, axes = plt.subplots(1, 4, figsize=(16, 4))
for ax, n in zip(axes, [10, 100, 1_000, 10_000]):
    sample_means = cumsum[:, n - 1] / n
    ax.hist(sample_means, bins=40, density=True, alpha=0.7, color="steelblue")
    ax.axvline(p, color="r", linestyle="--", lw=2)
    ax.set_title(f"n = {n:,}")
    ax.set_xlim(0, 1)
    ax.grid(True, alpha=0.3)

plt.suptitle("WLLN: Distribution of X̄ₙ Concentrates Around p = 0.5",
             fontsize=14, fontweight="bold")
plt.tight_layout()
plt.savefig("wlln_coin_flips.png", dpi=150, bbox_inches="tight")
plt.show()
```

## 실행 결과

이 스크립트는 $n \in \{10,\; 100,\; 1{,}000,\; 10{,}000\}$ 각각에 대한 히스토그램 네 개를 담은 그림을 그려 낸다. 각 히스토그램은 실험을 10,000번 독립적으로 되풀이해 얻은 표본평균 $\bar{X}_n$ 의 분포를 보여 준다. 빨간 점선 세로줄은 참평균 $p = 0.5$ 를 나타낸다.

- **$n = 10$:** 히스토그램이 넓게 퍼져 대략 0에서 1까지 뻗어 있으며, 변동이 크다는 것을 보여 준다.
- **$n = 100$:** 분포가 눈에 띄게 좁아져 대부분의 질량이 약 0.35에서 0.65 사이에 놓인다.
- **$n = 1{,}000$:** 히스토그램이 0.5 주위, 대략 $(0.47, 0.53)$ 구간에 빽빽하게 몰린다.
- **$n = 10{,}000$:** 거의 모든 질량이 0.5 주위의 아주 좁은 띠, 곧 대략 $(0.49, 0.51)$ 안에 놓인다.

## 뜻풀이

네 그림은 큰수의 약법칙을 또렷하게 눈으로 보여 준다.

1. **몰림.** $n$ 이 커질수록 $\bar{X}_n$ 의 분포는 참확률 $p = 0.5$ 로 무너져 내린다. 허용오차 $\varepsilon > 0$ 을 아무리 작게 잡아도 결국에는 히스토그램 전체가 구간 $(p - \varepsilon,\; p + \varepsilon)$ 안에 들어간다.

2. **수렴 속도.** $\bar{X}_n$ 의 표준편차는 $\sqrt{p(1-p)/n} = 1/(2\sqrt{n})$ 이다. 곧 히스토그램의 "폭"이 $1/\sqrt{n}$ 에 비례해 줄어든다는 뜻이다. $n = 100$ 에서 $n = 10{,}000$ 으로(100배) 키우면 퍼짐은 10배 줄어든다.

3. **모양.** 중심극한정리에 따라 $n$ 이 크면 히스토그램은 $p$ 를 중심으로 하는 정규분포의 종 모양에 다가가며, 이는 $n = 100$ 부터 보이는 모양과 들어맞는다.

4. **확률수렴과 거의 확실한 수렴.** 큰수의 약법칙은 확률수렴을 주장하며, 이는 여기에서 보인 것처럼 여러 실험에 걸친 $\bar{X}_n$ 의 분포에 대한 이야기이다. 한 줄기의 움직임에 대해서는 아무 말도 하지 않는다. 따로 다루는 강법칙이 경로별 수렴을 이야기한다.

## 연습문제

**연습문제 1.** 모의실험을 고쳐 $p = 0.3$ 인 편향된 동전을 쓰도록 하여라. 공정한 동전일 때와 견주어 히스토그램이 어떻게 달라지는지 설명하여라.

??? success "연습문제 1 풀이"
    `p = 0.5` 를 `p = 0.3` 으로 바꾼다. 이제 히스토그램은 0.5 대신 0.3 을 중심으로 놓인다. $\bar{X}_n$ 의 분산은 공정한 동전의 $0.25/n$ 대신 $p(1-p)/n = 0.21/n$ 이 된다. $0.21 < 0.25$ 이므로 각 $n$ 에서 히스토그램이 오히려 조금 더 좁다. 성질 자체는 똑같다. $n$ 이 커지면 분포가 $p = 0.3$ 주위로 몰린다.

---

**연습문제 2.** 공정한 동전 던지기에 대하여 $P(|\bar{X}_n - 0.5| > 0.01) \leq 0.05$ 가 되도록 하는 가장 작은 $n$ 을 체비쇼프 부등식으로 구하여라.

??? success "연습문제 2 풀이"
    체비쇼프 부등식에서 다음을 얻는다.

    $$
    P\!\left(|\bar{X}_n - 0.5| > 0.01\right) \leq \frac{p(1-p)}{n(0.01)^2} = \frac{0.25}{n \cdot 0.0001} = \frac{2500}{n}
    $$

    이 값이 0.05 이하가 되게 하면 다음과 같다.

    $$
    \frac{2500}{n} \leq 0.05 \implies n \geq 50{,}000
    $$

    따라서 체비쇼프 부등식이 보장해 주는 가장 작은 표본 크기는 $n = 50{,}000$ 이다. (체비쇼프 부등식은 넉넉하게 잡은 경계이므로, 실제로는 중심극한정리에 바탕을 둔 경계가 훨씬 작은 $n$ 을 준다.) $\square$

---

**연습문제 3.** i.i.d. 베르누이($p$) 확률변수에 대하여 $\operatorname{Var}(\bar{X}_n) = p(1-p)/n$ 임을 증명하여라.

??? success "연습문제 3 풀이"
    $X_1, \ldots, X_n$ 이 i.i.d. 이고 $\operatorname{Var}(X_i) = p(1-p)$ 이므로 다음이 성립한다.

    $$
    \operatorname{Var}(\bar{X}_n) = \operatorname{Var}\!\left(\frac{1}{n}\sum_{i=1}^n X_i\right) = \frac{1}{n^2}\sum_{i=1}^n \operatorname{Var}(X_i) = \frac{1}{n^2}\cdot n \cdot p(1-p) = \frac{p(1-p)}{n}
    $$

    두 번째 등호에서는 독립인 확률변수들에 대하여 분산이 더해진다는 사실을 썼다. $\square$

---

**연습문제 4.** 모의실험은 독립인 실험을 `num_paths = 10_000` 번 되풀이한다. $n = 100$ 일 때 모의실험으로 확률 $P(|\bar{X}_n - 0.5| > 0.1)$ 을 어림하고 체비쇼프 경계와 견주어 보아라.

??? success "연습문제 4 풀이"
    모의실험에서 $n = 100$ 일 때의 표본평균 10,000개 가운데 $(0.4, 0.6)$ 밖에 놓인 것이 몇 개인지 세어 본다.

    ```python
    sample_means_100 = cumsum[:, 99] / 100
    empirical_prob = np.mean(np.abs(sample_means_100 - 0.5) > 0.1)
    ```

    보통 대략 0.03(약 3%)이 나온다.

    체비쇼프 경계는 다음과 같다.

    $$
    P(|\bar{X}_{100} - 0.5| > 0.1) \leq \frac{0.25}{100 \cdot 0.01} = 0.25
    $$

    실제 확률(약 0.03)은 체비쇼프 경계 0.25보다 훨씬 작으며, 이는 체비쇼프 부등식이 넉넉하게 잡은 상계임을 보여 준다. $\square$

---

**연습문제 5.** 분산이 유한한 i.i.d. 확률변수에 대하여 체비쇼프 부등식을 써서 큰수의 약법칙을 증명하여라.

??? success "연습문제 5 풀이"
    $X_1, X_2, \ldots$ 가 $E[X_i] = \mu$, $\operatorname{Var}(X_i) = \sigma^2 < \infty$ 인 i.i.d. 확률변수라고 하자. 그러면 $E[\bar{X}_n] = \mu$ 이고 $\operatorname{Var}(\bar{X}_n) = \sigma^2/n$ 이다. 체비쇼프 부등식에 따라 임의의 $\varepsilon > 0$ 에 대하여 다음이 성립한다.

    $$
    P\!\left(|\bar{X}_n - \mu| \geq \varepsilon\right) \leq \frac{\operatorname{Var}(\bar{X}_n)}{\varepsilon^2} = \frac{\sigma^2}{n\varepsilon^2} \to 0 \quad n \to \infty \text{ 일 때}
    $$

    따라서 $\bar{X}_n \xrightarrow{P} \mu$ 이다. $\square$

---

**연습문제 6.** 큰수의 약법칙이 분포가 베르누이분포일 것을 요구하지 않는 까닭을 설명하여라. 체비쇼프 부등식에 바탕을 둔 증명에 필요한 분포에 대한 최소한의 가정은 무엇인가?

??? success "연습문제 6 풀이"
    체비쇼프 부등식에 바탕을 둔 큰수의 약법칙 증명이 요구하는 것은 다음뿐이다.

    1. 확률변수 $X_1, X_2, \ldots$ 가 **독립**일 것(적어도 무상관일 것).
    2. 공통의 평균 $\mu$ 를 갖는 **같은 분포**를 따를 것.
    3. **분산이 유한**할 것, 곧 $\sigma^2 < \infty$ 일 것.

    분포의 모양(베르누이분포인지 정규분포인지 등)에 대한 가정은 전혀 필요하지 않다. 증명은 오직 $\operatorname{Var}(\bar{X}_n) = \sigma^2/n \to 0$ 이라는 사실만 쓴다. 분산이 유한하다는 가정조차 필요 없는 더 높은 수준의 큰수의 약법칙(잘라내기 논법이나 특성함수를 쓰는)도 있지만, 체비쇼프 부등식을 쓴 증명이 가장 간단하고 직관적이다. $\square$
