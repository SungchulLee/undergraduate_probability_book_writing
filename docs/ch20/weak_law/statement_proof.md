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
