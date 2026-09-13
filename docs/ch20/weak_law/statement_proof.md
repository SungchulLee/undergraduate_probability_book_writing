# 서술과 체비쇼프를 쓴 증명

## 정리의 서술

$X_1, X_2, \ldots$ 를 확률밀도함수 또는 확률질량함수가 $f(x)$ 인 **i.i.d.** 확률변수라고 하자.

$\mathbb{E}|X_i| < \infty$ 이면 표본평균은 모평균으로 확률수렴한다.

$$
\frac{1}{N}\sum_{i=1}^N X_i \xrightarrow{p} \int x\, f(x)\, dx = \mu
$$

더 일반적으로 $\mathbb{E}|g(X_i)| < \infty$ 이면 다음이 성립한다.

$$
\frac{1}{N}\sum_{i=1}^N g(X_i) \xrightarrow{p} \int g(x)\, f(x)\, dx = \mathbb{E}[g(X)]
$$

## 증명(2차 적률이 유한하다고 가정할 때)

$S_n = \sum_{i=1}^n X_i$ 라 하고 $\mathbb{E}X_i^2 < \infty$ 라고 가정하자. 그러면 $Var(X_i) = \sigma^2 < \infty$ 이다.

**1단계: $\bar{X}_n = S_n / n$ 의 평균을 구한다.**

$$
\mathbb{E}\left[\frac{S_n}{n}\right] = \frac{1}{n}\sum_{i=1}^n \mathbb{E}X_i = \mu
$$

**2단계: $\bar{X}_n$ 의 분산을 구한다.**

$$
Var\left(\frac{S_n}{n}\right) = \frac{1}{n^2}\sum_{i=1}^n Var(X_i) = \frac{\sigma^2}{n}
$$

**3단계: 체비쇼프 부등식을 적용한다.**

$$
P\left(\left|\frac{S_n}{n} - \mu\right| > \varepsilon\right) \leq \frac{Var(S_n/n)}{\varepsilon^2} = \frac{\sigma^2/n}{\varepsilon^2} = \frac{\sigma^2}{n\varepsilon^2} \to 0 \quad n \to \infty \text{ 일 때}
$$

따라서 $\bar{X}_n \xrightarrow{p} \mu$ 이다. $\square$

!!! info "덧붙이는 말"
    위 증명은 $\sigma^2 < \infty$ (2차 적률이 유한함)를 요구한다. 큰수의 약법칙 전체는 $\mathbb{E}|X_i| < \infty$ (1차 적률이 유한함)만 있으면 되지만, 그 증명은 더 까다로워서 잘라내기 논법을 쓴다.

## 뜻풀이

약법칙은 $n$ 이 클 때 표본평균 $\bar{X}_n$ 이 $\mu$ 에서 멀리 떨어져 있기가 **어렵다**고 말한다. 충분히 큰 모든 $n$ 에 대하여 $\bar{X}_n$ 이 $\mu$ 가까이에 머문다고 보장하지는 않는다. 그것은 강법칙이 하는 말이다.

## 연습문제

**연습문제 1.**
$X_1, X_2, \ldots$ 가 i.i.d. $\text{Exp}(\lambda)$ 라고 하자. 큰수의 약법칙을 써서 $\bar{X}_n \xrightarrow{p} 1/\lambda$ 임을 보여라.

??? success "연습문제 1 풀이"
    지수분포는 2차 적률이 유한하므로 위에서 증명한 체비쇼프 판 약법칙을 그대로 쓸 수 있다. 가정이 참으로 만족되는지 하나씩 확인한다.

    **1단계: 평균을 구한다.** $X \sim \text{Exp}(\lambda)$ 의 확률밀도함수는 $f(x) = \lambda e^{-\lambda x}$ $(x > 0)$ 이다. 부분적분을 쓰면 다음과 같다.

    $$
    \mathbb{E}X = \int_0^\infty x\, \lambda e^{-\lambda x}\, dx = \Big[-x e^{-\lambda x}\Big]_0^\infty + \int_0^\infty e^{-\lambda x}\, dx = 0 + \frac{1}{\lambda} = \frac{1}{\lambda}
    $$

    따라서 $\mu = 1/\lambda < \infty$ 이다.

    **2단계: 2차 적률과 분산을 구한다.** 같은 방법으로 한 번 더 부분적분한다.

    $$
    \mathbb{E}X^2 = \int_0^\infty x^2 \lambda e^{-\lambda x}\, dx = \frac{2}{\lambda^2}
    $$

    그러므로 분산은 다음과 같다.

    $$
    Var(X) = \mathbb{E}X^2 - (\mathbb{E}X)^2 = \frac{2}{\lambda^2} - \frac{1}{\lambda^2} = \frac{1}{\lambda^2} = \sigma^2 < \infty
    $$

    $\lambda > 0$ 이므로 $\mu$ 와 $\sigma^2$ 이 모두 유한하고, 약법칙의 가정이 갖추어졌다.

    **3단계: 표본평균의 평균과 분산을 구한다.** 기댓값의 선형성에서 다음과 같다.

    $$
    \mathbb{E}\bar{X}_n = \frac{1}{n}\sum_{i=1}^n \mathbb{E}X_i = \frac{1}{n} \cdot n \cdot \frac{1}{\lambda} = \frac{1}{\lambda}
    $$

    독립이므로 분산이 더해지고, 상수배는 제곱으로 빠져나온다.

    $$
    Var(\bar{X}_n) = \frac{1}{n^2}\sum_{i=1}^n Var(X_i) = \frac{1}{n^2} \cdot n \cdot \frac{1}{\lambda^2} = \frac{1}{n\lambda^2}
    $$

    **4단계: 체비쇼프 부등식을 적용한다.** $\varepsilon > 0$ 을 아무렇게나 고정한다. $\bar{X}_n$ 의 평균이 $1/\lambda$ 이므로 곧바로 다음을 얻는다.

    $$
    P\left(\left|\bar{X}_n - \frac{1}{\lambda}\right| \geq \varepsilon\right) \leq \frac{Var(\bar{X}_n)}{\varepsilon^2} = \frac{1}{n\lambda^2\varepsilon^2}
    $$

    오른쪽에서 $\lambda$ 와 $\varepsilon$ 은 고정된 양수이므로 이 값은 $n \to \infty$ 일 때 $0$ 으로 간다.

    $$
    \frac{1}{n\lambda^2\varepsilon^2} \longrightarrow 0 \qquad (n \to \infty)
    $$

    $\varepsilon > 0$ 이 아무렇게나 고른 것이었으므로 다음이 성립한다.

    $$
    \bar{X}_n \xrightarrow{p} \frac{1}{\lambda} \qquad \square
    $$

    **얼마나 큰 $n$ 이 필요한가.** 이 경계는 숫자를 넣어 쓸 수 있다는 점에서 값지다. $\lambda = 1$ 이면 $\mu = 1$ 이고, 표본평균이 참값에서 $0.01$ 이상 벗어날 확률을 $0.05$ 아래로 누르고 싶다면 다음을 풀면 된다.

    $$
    \frac{1}{n (0.01)^2} \leq 0.05 \iff n \geq \frac{1}{0.05 \times 0.0001} = 200{,}000
    $$

    체비쇼프 경계는 분포의 모양을 전혀 쓰지 않으므로 매우 안전한 쪽으로 치우쳐 있다. 중심극한정리를 쓰면 같은 요구를 훨씬 작은 $n$ 으로 채울 수 있지만, 그것은 근사일 뿐 보장이 아니다.
