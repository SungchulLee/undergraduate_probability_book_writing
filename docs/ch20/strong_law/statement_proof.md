# 서술과 증명의 얼개

## 정리의 서술

$X_1, X_2, \ldots$ 를 확률밀도함수 또는 확률질량함수가 $f(x)$ 인 **i.i.d.** 확률변수라고 하자.

$\mathbb{E}|X_i| < \infty$ 이면 표본평균은 모평균으로 **거의 확실하게** 수렴한다.

$$
\frac{1}{N}\sum_{i=1}^N X_i \xrightarrow{a.s.} \int x\, f(x)\, dx = \mu
$$

더 일반적으로 $\mathbb{E}|g(X_i)| < \infty$ 이면 다음이 성립한다.

$$
\frac{1}{N}\sum_{i=1}^N g(X_i) \xrightarrow{a.s.} \int g(x)\, f(x)\, dx = \mathbb{E}[g(X)]
$$

## 증명의 얼개(4차 적률이 유한하다고 가정할 때)

$\mathbb{E}X_i^4 < \infty$ 라고 가정하고 $S_n = \sum_{i=1}^n X_i$ 라고 하자.

**1단계**: 4차 적률의 합이 수렴함을 보인다.

$$
\sum_{n=1}^{\infty} \mathbb{E}\left(\frac{S_n - n\mu}{n}\right)^4 \leq C\sum_{n=1}^{\infty} n^{-2} < \infty
$$

여기에서 핵심은 $(S_n - n\mu)^4$ 을 펼쳤을 때 독립성에 의해 대부분의 교차항이 사라지고 $O(n^2)$ 개의 항만 남는다는 사실이며, 그래서 $\mathbb{E}(S_n - n\mu)^4 = O(n^2)$ 이 된다.

**2단계**: 기댓값들의 합이 유한하므로 그 합 자체가 거의 확실하게 유한하다.

$$
\sum_{n=1}^{\infty} \left(\frac{S_n - n\mu}{n}\right)^4 < \infty \quad \text{a.s.}
$$

**3단계**: 음이 아닌 항으로 이루어진 급수가 수렴하면 그 항들은 0으로 가야 한다.

$$
\left(\frac{S_n - n\mu}{n}\right)^4 \to 0 \quad \text{a.s.}
$$

**4단계**: 네제곱근을 취하면 다음을 얻는다.

$$
\frac{S_n}{n} \to \mu \quad \text{a.s.}
$$

$\square$

!!! info "덧붙이는 말"
    큰수의 강법칙 전체(콜모고로프의 형태)는 $\mathbb{E}|X_i| < \infty$ 만 요구한다. 4차 적률이 유한하다고 가정한 증명은 더 쉽게 다가갈 수 있으면서도 핵심 전략을 잘 보여 준다. 곧 적률의 합이 유한하다는 사실로부터 거의 확실한 수렴을 이끌어 내는 것이다.

## 약법칙과 강법칙

| 성질 | 약법칙 | 강법칙 |
|----------|----------|------------|
| 수렴의 뜻 | 확률수렴 | 거의 확실한 수렴 |
| 가정(간단한 증명) | $\sigma^2 < \infty$ | $\mathbb{E}X^4 < \infty$ |
| 가정(일반적인 경우) | $\mathbb{E}\|X\| < \infty$ | $\mathbb{E}\|X\| < \infty$ |
| 증명 방법 | 체비쇼프 부등식 | 4차 적률 + 급수의 수렴 |
| 결론 | $P(\|\bar{X}_n - \mu\| > \varepsilon) \to 0$ | $P(\bar{X}_n \to \mu) = 1$ |

## 연습문제

**연습문제 1.** 큰수의 강법칙과 약법칙의 차이를 각각 한 문장으로 서술하여라.

??? success "연습문제 1 풀이"
    **약법칙:** 임의의 $\varepsilon > 0$ 에 대하여 $P(|\bar{X}_n - \mu| > \varepsilon) \to 0$ 이다(벗어날 확률이 줄어든다).

    **강법칙:** $P(\bar{X}_n \to \mu) = 1$ 이다(거의 모든 결과의 수열에 대하여 표본평균이 $\mu$ 로 수렴한다).

---

**연습문제 2.** 큰수의 강법칙은 $E|X_i| < \infty$ 를 요구한다. 이것이 성립하지 않아 강법칙도 성립하지 않는 분포의 예를 들어라.

??? success "연습문제 2 풀이"
    코시분포의 확률밀도함수는 $f(x) = \frac{1}{\pi(1+x^2)}$ 이고 $E|X| = \int_{-\infty}^{\infty}\frac{|x|}{\pi(1+x^2)}dx = \infty$ 이다. i.i.d. 코시확률변수에 대하여 $\bar{X}_n$ 은 모든 $n$ 에 대하여 같은 코시분포를 따른다(수렴하지 않는다). 표본평균은 어떤 값 주위로도 몰리지 않는다.

---

**연습문제 3.** $X_i$ 가 $E[X_i] = 3$ 이고 $E[X_i^4] < \infty$ 인 i.i.d. 확률변수라고 하자. 4차 적률을 쓰는 큰수의 강법칙 증명은 $E[(\bar{X}_n - \mu)^4] = O(1/n^2)$ 을 쓴다. 이로부터 $\sum P(|\bar{X}_n - \mu| > \varepsilon) < \infty$ 가 따라 나오는 까닭을 설명하여라.

??? success "연습문제 3 풀이"
    $(\bar{X}_n - \mu)^4$ 에 마르코프 부등식을 적용하면 다음을 얻는다.

    $$
    P(|\bar{X}_n - \mu| > \varepsilon) \leq \frac{E[(\bar{X}_n - \mu)^4]}{\varepsilon^4} = O(1/n^2)
    $$

    $\sum_{n=1}^{\infty} 1/n^2 < \infty$ 이므로(수렴하는 $p$-급수), 보렐–칸텔리 보조정리에 따라 $P(|\bar{X}_n - \mu| > \varepsilon \text{ i.o.}) = 0$ 이고, 이는 거의 확실한 수렴을 뜻한다. $\square$

---

**연습문제 4.** 일반화한 큰수의 강법칙은 $\frac{1}{N}\sum g(X_i) \xrightarrow{a.s.} E[g(X)]$ 라고 말한다. 이를 써서 $\frac{1}{N}\sum X_i^2 \xrightarrow{a.s.} E[X^2]$ 임을 보여라.

??? success "연습문제 4 풀이"
    $g(x) = x^2$ 으로 두자. $E[X_i^2] < \infty$ 이면 $E|g(X_i)| = E[X_i^2] < \infty$ 이므로 큰수의 강법칙을 적용할 수 있다.

    $$
    \frac{1}{N}\sum_{i=1}^N X_i^2 \xrightarrow{a.s.} E[X^2]
    $$

    이를 $\bar{X}_N \xrightarrow{a.s.} \mu$ 와 합치면 $S_N^2 \xrightarrow{a.s.} \sigma^2$ 을 얻는다(분산의 일치추정).

---

**연습문제 5.** 몬테카를로 모의실험에서 $\theta = E[h(X)]$ 를 $\hat{\theta}_n = \frac{1}{n}\sum h(X_i)$ 로 어림한다고 하자. 큰수의 강법칙은 $\hat{\theta}_n \to \theta$ (a.s.)를 보장한다. 중심극한정리는 여기에 어떤 정보를 더해 주는가?

??? success "연습문제 5 풀이"
    중심극한정리는 수렴의 **속도**와 오차의 **분포**를 알려 준다. 구체적으로 다음이 성립한다.

    $$
    \sqrt{n}(\hat{\theta}_n - \theta) \xrightarrow{d} N(0, \sigma^2_h)
    $$

    여기에서 $\sigma^2_h = \text{Var}(h(X))$ 이다. 이로부터 신뢰구간 $\hat{\theta}_n \pm z_{\alpha/2} \cdot \hat{\sigma}_h / \sqrt{n}$ 을 만들 수 있다. 큰수의 강법칙은 추정량이 수렴한다고 말하고, 중심극한정리는 유한한 $n$ 에서 대략 얼마나 빗나갈 법한지를 말해 준다.
