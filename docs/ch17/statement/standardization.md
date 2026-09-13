# 표준화

## 확률변수의 표준화

$X$ 의 평균이 $\mu$ 이고 표준편차가 $\sigma$ 이면

$$Z = \frac{X - \mu}{\sigma}$$

는 평균이 $0$ 이고 표준편차가 $1$ 이다.

$X$ 가 정규분포를 따르면 $Z$ 도 정규분포를 따른다. 곧 $Z \sim N(0,1)$ 이다.

## 거꾸로 하는 표준화

$Z$ 의 평균이 $0$ 이고 표준편차가 $1$ 이면

$$X = \mu + \sigma Z$$

는 평균이 $\mu$ 이고 표준편차가 $\sigma$ 이다.

$Z$ 가 정규분포를 따르면 $X$ 도 정규분포를 따른다. 곧 $X \sim N(\mu, \sigma^2)$ 이다.

## 중심극한정리에서의 표준화

중심극한정리는 평균이 $\mu$ 이고 분산이 $\sigma^2$ 인 i.i.d. $X_1, \ldots, X_n$ 에 대하여 다음이 성립함을 말해 준다.

$$Z_n = \frac{S_n - n\mu}{\sigma\sqrt{n}} \xrightarrow{d} N(0,1)$$

곧 **표준화한 합**이 표준정규분포로 수렴한다. 같은 말로, 표준화를 거꾸로 하면 다음과 같다.

$$S_n \approx n\mu + \sigma\sqrt{n} \cdot Z \quad \text{여기에서 } Z \sim N(0,1)$$

따라서 $S_n \approx N(n\mu, \, n\sigma^2)$ 이다.

## 표준화로 확률 구하기

$P(a \leq S_n \leq b)$ 를 어림하려면 다음과 같이 한다.

**1단계.** 표준화한다.

$$P(a \leq S_n \leq b) = P\left(\frac{a - n\mu}{\sigma\sqrt{n}} \leq \frac{S_n - n\mu}{\sigma\sqrt{n}} \leq \frac{b - n\mu}{\sigma\sqrt{n}}\right)$$

**2단계.** 중심극한정리에 따른 근사를 쓴다.

$$\approx \mathcal{N}\left(\frac{b - n\mu}{\sigma\sqrt{n}}\right) - \mathcal{N}\left(\frac{a - n\mu}{\sigma\sqrt{n}}\right)$$

여기에서 $\mathcal{N}$ 은 $N(0,1)$ 의 누적분포함수이다.

## 연습문제

**연습문제 1.**
$X_i$ 를 공정한 동전의 $i$ 번째 던지기 결과라 하고, 앞면이면 $+1$, 뒷면이면 $-1$ 로 적는다고 하자. $t \in [0,1]$ 에 대하여 $W_n = \frac{1}{\sqrt{n}} \sum_{i=1}^{\lfloor nt \rfloor} X_i$ 로 정의한다.

(a) $E[W_n]$ 과 $\text{Var}(W_n)$ 을 구하여라.

(b) 중심극한정리를 써서 $W_n$ 의 근사적인 분포를 구하여라.

(c) $0 \leq s < t \leq 1$ 이고 $W_n(t) = \frac{1}{\sqrt{n}}\sum_{i=1}^{\lfloor nt \rfloor} X_i$ 일 때 $W_n(t) - W_n(s)$ 의 근사적인 분포를 구하여라.
