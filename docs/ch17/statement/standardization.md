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

??? success "연습문제 1 풀이"
    **0단계: 한 번 던지기의 평균과 분산.** $X_i$ 는 $+1$ 과 $-1$ 을 각각 확률 $\tfrac12$ 로 가지므로 다음과 같다.

    $$
    E[X_i] = (+1)\cdot\tfrac12 + (-1)\cdot\tfrac12 = 0, \qquad E[X_i^2] = (+1)^2\cdot\tfrac12 + (-1)^2\cdot\tfrac12 = 1
    $$

    그러므로 $\text{Var}(X_i) = E[X_i^2] - (E[X_i])^2 = 1 - 0 = 1$ 이다. 곧 $\mu = 0$, $\sigma^2 = 1$ 이다.

    **(a) 평균과 분산.** 더하는 항의 개수 $\lfloor nt \rfloor$ 는 확률변수가 아니라 $n$ 과 $t$ 로 정해지는 상수임에 유의하여라. 기댓값의 선형성에서 다음을 얻는다.

    $$
    E[W_n] = \frac{1}{\sqrt{n}} \sum_{i=1}^{\lfloor nt \rfloor} E[X_i] = \frac{1}{\sqrt{n}} \cdot \lfloor nt \rfloor \cdot 0 = 0
    $$

    분산에서는 $X_i$ 들의 독립성이 필요하다. 독립이므로 공분산 항이 모두 사라지고 분산이 그대로 더해진다. 또 상수 $c$ 를 곱하면 분산은 $c^2$ 배가 된다.

    $$
    \text{Var}(W_n) = \frac{1}{n} \sum_{i=1}^{\lfloor nt \rfloor} \text{Var}(X_i) = \frac{1}{n} \cdot \lfloor nt \rfloor \cdot 1 = \frac{\lfloor nt \rfloor}{n}
    $$

    $nt - 1 < \lfloor nt \rfloor \le nt$ 이므로 $n$ 이 커지면 이 값은 $t$ 로 다가간다.

    $$
    \frac{\lfloor nt \rfloor}{n} \to t \qquad (n \to \infty)
    $$

    **(b) 근사적인 분포.** $m = \lfloor nt \rfloor$ 로 두면 $W_n = \dfrac{1}{\sqrt{n}} S_m$ 이고, $S_m = X_1 + \cdots + X_m$ 은 평균 $0$, 분산 $1$ 인 i.i.d. 확률변수의 합이다. 중심극한정리에 따라 $m$ 이 크면 다음이 성립한다.

    $$
    \frac{S_m}{\sqrt{m}} \approx N(0,1), \qquad \text{곧} \quad S_m \approx N(0, m)
    $$

    여기에 $\dfrac{1}{\sqrt{n}}$ 을 곱하면 분산은 $\dfrac{1}{n}$ 배가 되므로 다음을 얻는다.

    $$
    W_n = \frac{S_m}{\sqrt{n}} \approx N\!\left(0, \; \frac{\lfloor nt \rfloor}{n}\right) \xrightarrow{d} N(0, t)
    $$

    곧 $t > 0$ 이 고정되어 있고 $n \to \infty$ 이면 다음과 같다.

    $$
    W_n \xrightarrow{d} N(0, t)
    $$

    분산이 $n$ 이 아니라 $t$ 로 남는다는 점이 핵심이다. $\sqrt{n}$ 으로 나누어 크기를 맞춘 덕분에, 시간 $t$ 만이 퍼짐을 결정한다.

    **(c) 증분의 분포.** 정의에서 앞의 $\lfloor ns \rfloor$ 개 항이 서로 지워진다.

    $$
    W_n(t) - W_n(s) = \frac{1}{\sqrt{n}} \sum_{i=1}^{\lfloor nt \rfloor} X_i - \frac{1}{\sqrt{n}} \sum_{i=1}^{\lfloor ns \rfloor} X_i = \frac{1}{\sqrt{n}} \sum_{i=\lfloor ns \rfloor + 1}^{\lfloor nt \rfloor} X_i
    $$

    남은 합은 서로 다른 $\lfloor nt \rfloor - \lfloor ns \rfloor$ 개의 던지기로 이루어져 있으므로, (a)와 똑같은 계산에서 평균은 $0$ 이고 분산은 다음과 같다.

    $$
    \text{Var}\big(W_n(t) - W_n(s)\big) = \frac{\lfloor nt \rfloor - \lfloor ns \rfloor}{n} \to t - s \qquad (n \to \infty)
    $$

    다시 중심극한정리를 적용하면 다음을 얻는다.

    $$
    W_n(t) - W_n(s) \xrightarrow{d} N(0, \, t - s)
    $$

    **마무리: 브라운 운동의 그림자.** 증분의 분포가 $s$ 와 $t$ 에 따로따로 기대지 않고 오직 그 차이 $t - s$ 에만 달려 있다는 점에 주목하여라. 이것이 **정상증분**이다. 또 서로 겹치지 않는 시간 구간에는 서로 다른 $X_i$ 가 쓰이므로, 그 구간들의 증분은 서로 **독립**이다. 평균 $0$ 에 분산 $t-s$ 인 정규분포를 따르는 독립증분, 이것이 바로 브라운 운동 $B(t)$ 의 정의이다. 곧 $W_n$ 은 $n \to \infty$ 에서 브라운 운동으로 다가가며, 이를 정밀하게 만든 것이 돈스커의 불변원리이다. $\square$
