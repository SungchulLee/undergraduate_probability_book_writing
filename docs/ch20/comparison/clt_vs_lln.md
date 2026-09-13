# 중심극한정리와 큰수의 법칙

## 두 가지 근본 정리

중심극한정리와 큰수의 법칙은 모두 $n \to \infty$ 일 때 표본평균 $\bar{X}_n = \frac{1}{n}\sum_{i=1}^n X_i$ 가 어떻게 움직이는지를 말하지만, **서로 다른 물음**에 답한다.

| | 큰수의 법칙 | 중심극한정리 |
|---|---|---|
| **묻는 것** | $\bar{X}_n$ 은 어디로 가는가? | $\bar{X}_n$ 은 극한 주위에서 어떻게 출렁이는가? |
| **서술** | $\bar{X}_n \to \mu$ | $\sqrt{n}(\bar{X}_n - \mu)/\sigma \xrightarrow{d} N(0,1)$ |
| **눈금** | $\bar{X}_n - \mu \to 0$ | $\bar{X}_n - \mu \approx \sigma/\sqrt{n} \cdot Z$ |
| **알려 주는 것** | 극한 | 수렴의 속도와 모양 |

## 둘을 잇기

중심극한정리는 $\bar{X}_n$ 이 $\mu$ 주위에서 $\sigma/\sqrt{n}$ 눈금으로 출렁인다고 말해 준다.

$$
\bar{X}_n \approx \mu + \frac{\sigma}{\sqrt{n}} Z, \quad Z \sim N(0,1)
$$

큰수의 법칙은 $\sigma/\sqrt{n} \to 0$ 이므로 $\bar{X}_n \to \mu$ 라고 말해 준다.

## σ 를 알 때와 모를 때

**$\sigma$ 를 알 때:**

$$
\frac{\bar{X}_n - \mu}{\sigma/\sqrt{n}} \begin{cases} \overset{d}{=} N(0,1) & X_i \text{ 가 i.i.d. } N(\mu, \sigma^2) \text{ 일 때 (정확히)} \\ \approx N(0,1) & X_i \text{ 가 i.i.d. 이고 } \mathbb{E}X_i^2 < \infty \text{ 일 때 (중심극한정리)} \end{cases}
$$

**$\sigma$ 를 모를 때**는 이를 표본표준편차 $S$ 로 바꾼다.

$$
\frac{\bar{X}_n - \mu}{S/\sqrt{n}} \begin{cases} \overset{d}{=} t_{n-1} & X_i \text{ 가 i.i.d. } N(\mu, \sigma^2) \text{ 일 때 (정확히)} \\ \approx N(0,1) & X_i \text{ 가 i.i.d. 이고 } \mathbb{E}X_i^2 < \infty \text{ 일 때 (중심극한정리와 큰수의 법칙)} \end{cases}
$$

$g(X) = (X - \mu)^2$ 에 강법칙을 적용하면 $S^2 \xrightarrow{a.s.} \sigma^2$ 이므로, 큰수의 법칙이 $\sigma$ 를 $S$ 로 바꾸어 쓰는 일을 뒷받침해 준다.

## 정리하며

큰수의 법칙과 중심극한정리는 함께 일한다. 큰수의 법칙은 표본평균이 모평균으로 수렴한다고 말해 주고, 중심극한정리는 그 극한 주위의 정규분포 꼴 출렁임을 그려 준다. 이 둘이 함께 통계적 추론, 신뢰구간, 가설검정의 바탕을 이룬다.


## 연습문제

**연습문제 1.**
확률수렴이 분포수렴을 함의하는데도 중심극한정리가 큰수의 약법칙을 함의하지 **않는** 까닭을 설명하여라. 논리적으로 어디가 갈리는가?
