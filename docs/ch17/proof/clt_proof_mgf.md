# 적률생성함수를 쓴 중심극한정리 증명

## 증명의 얼개

표준화한 합의 적률생성함수가 $N(0,1)$ 의 적률생성함수로 수렴함을 보인 뒤 연속성 정리를 불러오는 방식으로 중심극한정리를 증명한다.

**되새기기:** $M_{N(0,1)}(t) = e^{t^2/2}$

## 문제 설정

$X_1, X_2, \ldots$ 가 i.i.d. 이고 평균이 $\mu$, 분산이 $\sigma^2$ 이라 하자. 표준화한 확률변수를 다음과 같이 정의한다.

$$Y_k = \frac{X_k - \mu}{\sigma}$$

그러면 $Y_k$ 는 i.i.d. 이고 $E[Y_k] = 0$, $E[Y_k^2] = 1$ 이다.

표준화한 합은 다음과 같다.

$$Z_n = \frac{S_n - n\mu}{\sigma\sqrt{n}} = \sum_{k=1}^n \frac{Y_k}{\sqrt{n}}$$

## 증명

**1단계.** 독립성을 써서 $Z_n$ 의 적률생성함수를 적는다.

$$M_{Z_n}(t) = M_{\sum_{k=1}^n Y_k / \sqrt{n}}(t) = \left(E\left[e^{tY_1/\sqrt{n}}\right]\right)^n = \left(M_{Y_1}\left(\frac{t}{\sqrt{n}}\right)\right)^n$$

**2단계.** $Y_1$ 의 적률생성함수를 $0$ 둘레에서 테일러 전개한다.

$$M_{Y_1}(t) = E[e^{tY_1}] = E\left[1 + tY_1 + \frac{(tY_1)^2}{2!} + \cdots\right]$$

$$\approx 1 + t \cdot E[Y_1] + \frac{t^2}{2} \cdot E[Y_1^2] = 1 + 0 + \frac{t^2}{2} = 1 + \frac{t^2}{2}$$

**3단계.** $t$ 자리에 $t/\sqrt{n}$ 을 넣는다.

$$M_{Y_1}\left(\frac{t}{\sqrt{n}}\right) \approx 1 + \frac{t^2}{2n}$$

**4단계.** $n$ 제곱을 한다.

$$M_{Z_n}(t) = \left(M_{Y_1}\left(\frac{t}{\sqrt{n}}\right)\right)^n \approx \left(1 + \frac{t^2}{2n}\right)^n$$

**5단계.** $\lim_{n\to\infty}\left(1 + \frac{a}{n}\right)^n = e^a$ 를 써서 극한을 취한다.

$$\lim_{n \to \infty} M_{Z_n}(t) = \lim_{n \to \infty} \left(1 + \frac{t^2}{2n}\right)^n = e^{t^2/2} = M_{N(0,1)}(t)$$

**6단계.** 적률생성함수에 대한 연속성 정리에 따라 다음을 얻는다.

$$Z_n = \frac{S_n - n\mu}{\sigma\sqrt{n}} \xrightarrow{d} N(0,1) \qquad \square$$

## 핵심 재료

이 증명은 세 가지 사실에 기댄다.

1. $X_i$ 의 **독립성** 덕분에 적률생성함수를 인수분해할 수 있다. 곧 $M_{Z_n}(t) = \left(M_{Y_1}(t/\sqrt{n})\right)^n$ 이다.
2. **분산이 유한**해야 테일러 전개 $M_{Y_1}(t) \approx 1 + t^2/2$ 가 정당하다.
3. **연속성 정리**: 적률생성함수가 각 점별로 수렴하면 분포수렴이 따라 나온다.

!!! note "분산이 유한해야 하는 까닭"
    테일러 전개를 하려면 $E[Y_1^2] = 1 < \infty$ 이어야 한다. 분산이 무한하면(예를 들어 코시분포) 중심극한정리를 적용할 수 없고, 표준화한 합도 정규분포로 수렴하지 않는다.

## 연습문제

**연습문제 1.**
적률생성함수를 쓴 중심극한정리 증명의 빈틈을 채워라. 특히 테일러 전개 단계 $M_{Y_1}(t) \approx 1 + t^2/2$ 와 극한 $\left(1 + \frac{t^2}{2n}\right)^n \to e^{t^2/2}$ 을 엄밀하게 정당화하여라.
