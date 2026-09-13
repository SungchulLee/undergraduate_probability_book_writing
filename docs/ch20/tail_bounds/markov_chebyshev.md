# 마르코프 부등식과 체비쇼프 부등식

꼬리 경계는 확률변수가 평균에서 크게 벗어날 확률에 대한 **상계**를 준다. 큰수의 법칙을 증명할 때 없어서는 안 될 도구이다.

## 마르코프 부등식

음이 아닌 확률변수 $|X|$ 와 $\varepsilon > 0$ 에 대하여 다음이 성립한다.

$$
P(|X| \geq \varepsilon) \leq \frac{\mathbb{E}|X|}{\varepsilon}
$$

**직관**: $X$ 의 기댓값이 작다면 $X$ 가 큰 값을 자주 가질 수는 없다. 마르코프 부등식은 이 사실을 오직 1차 적률만으로 정확하게 표현한 것이다.

## 체비쇼프 부등식

평균 $\mu$ 와 분산 $\sigma^2$ 이 유한한 확률변수 $X$ 와 $\varepsilon > 0$ 에 대하여 다음이 성립한다.

$$
P(|X - \mathbb{E}X| \geq \varepsilon) \leq \frac{Var(X)}{\varepsilon^2}
$$

**증명**: $(X - \mu)^2$ 에 마르코프 부등식을 적용한다.

$$
P(|X - \mu| \geq \varepsilon) = P((X - \mu)^2 \geq \varepsilon^2) \leq \frac{\mathbb{E}(X - \mu)^2}{\varepsilon^2} = \frac{\sigma^2}{\varepsilon^2}
$$

**직관**: 체비쇼프 부등식은 분산(2차 적률)을 써서 마르코프 부등식보다 더 촘촘한 경계를 준다. 분산이 작으면 확률변수는 평균 주위에 몰려 있다.

## 기하학적 뜻풀이

- **마르코프**: $f_{|X|}(x)$ 곡선 아래에서 $\varepsilon$ 오른쪽에 있는 넓이는 전체 넓이(기댓값)를 $\varepsilon$ 으로 나눈 값으로 눌린다.
- **체비쇼프**: $f_{(X-\mu)^2}(x)$ 곡선 아래에서 $\varepsilon^2$ 오른쪽에 있는 넓이는 분산을 $\varepsilon^2$ 으로 나눈 값으로 눌린다.

## 예: 이항분포 X ~ B(1000, 0.01)

여기에서 $\mathbb{E}X = np = 10$ 이고 $Var(X) = npq = 9.9$ 이다.

**$P(X \geq 20)$ 의 경계:**

**마르코프:**

$$
P(X \geq 20) \leq \frac{\mathbb{E}X}{20} = \frac{10}{20} = 0.5
$$

**체비쇼프:**

$$
P(X \geq 20) \leq P(|X - 10| \geq 10) \leq \frac{9.9}{10^2} = 0.0990
$$

**$P(X \geq 100)$ 의 경계:**

**마르코프:**

$$
P(X \geq 100) \leq \frac{10}{100} = 0.1
$$

**체비쇼프:**

$$
P(X \geq 100) \leq P(|X - 10| \geq 90) \leq \frac{9.9}{90^2} = 0.0012
$$

## 예: 푸아송분포 X ~ Poi(100)

여기에서 $\mathbb{E}X = \lambda = 100$ 이고 $Var(X) = \lambda = 100$ 이다.

**$P(X \geq 200)$ 의 경계:**

**마르코프:**

$$
P(X \geq 200) \leq \frac{100}{200} = 0.5
$$

**체비쇼프:**

$$
P(X \geq 200) \leq P(|X - 100| \geq 100) \leq \frac{100}{100^2} = 0.0100
$$

## 연습문제

**연습문제 1.**
$X \sim \text{Po}(50)$ 이라고 하자. 마르코프 부등식, 체비쇼프 부등식, 한쪽 체비쇼프 부등식, 체르노프 경계를 써서 $P(X \geq 75)$ 를 어림하여라. 정확한 값 및 중심극한정리 근사와 견주어 보아라.

??? success "연습문제 1 풀이"
    푸아송분포에서는 평균과 분산이 같으므로 $\mathbb{E}X = \lambda = 50$, $Var(X) = \lambda = 50$ 이다. 문턱값은 $a = 75$ 이고, 평균에서 벗어난 정도는 $\varepsilon = a - \lambda = 25$ 이다.

    **1단계: 마르코프 부등식.** $X \geq 0$ 이므로 곧바로 적용할 수 있다.

    $$
    P(X \geq 75) \leq \frac{\mathbb{E}X}{75} = \frac{50}{75} = \frac{2}{3} \approx 0.6667
    $$

    1차 적률만 쓰기 때문에 경계가 매우 헐겁다.

    **2단계: 체비쇼프 부등식.** 오른쪽 꼬리는 양쪽 꼬리에 들어 있으므로 $\{X \geq 75\} \subset \{|X - 50| \geq 25\}$ 이다.

    $$
    P(X \geq 75) \leq P(|X - 50| \geq 25) \leq \frac{Var(X)}{25^2} = \frac{50}{625} = 0.0800
    $$

    분산까지 썼더니 경계가 한 자릿수 넘게 촘촘해졌다.

    **3단계: 한쪽 체비쇼프(칸텔리) 부등식.** 우리가 원하는 것은 오른쪽 꼬리뿐이므로 왼쪽 꼬리까지 함께 세는 낭비를 덜 수 있다.

    $$
    P(X - 50 \geq 25) \leq \frac{\sigma^2}{\sigma^2 + \varepsilon^2} = \frac{50}{50 + 625} = \frac{50}{675} \approx 0.0741
    $$

    **4단계: 체르노프 경계.** 푸아송분포의 적률생성함수는 $M_X(t) = \mathbb{E}e^{tX} = e^{\lambda(e^t - 1)}$ 이다. 모든 $t > 0$ 에 대하여 다음이 성립한다.

    $$
    P(X \geq 75) \leq \frac{M_X(t)}{e^{75t}} = \exp\big(50(e^t - 1) - 75t\big)
    $$

    지수부 $h(t) = 50(e^t - 1) - 75t$ 를 최소로 만드는 $t$ 를 찾는다. $h'(t) = 50e^t - 75 = 0$ 에서 $e^t = 3/2$, 곧 다음과 같다.

    $$
    t^* = \log\frac{3}{2} \approx 0.4055 > 0
    $$

    $h''(t) = 50e^t > 0$ 이므로 $h$ 는 아래로 볼록하고 $t^*$ 가 참으로 최솟값을 준다. 일반적으로 $a > \lambda$ 일 때 $t^* = \log(a/\lambda)$ 를 넣으면 다음 꼴을 얻는다.

    $$
    P(X \geq a) \leq \exp\left(a - \lambda - a\log\frac{a}{\lambda}\right) = e^{-\lambda}\left(\frac{e\lambda}{a}\right)^{a}
    $$

    $\lambda = 50$, $a = 75$ 를 넣으면 다음과 같다.

    $$
    P(X \geq 75) \leq e^{-50}\left(\frac{2e}{3}\right)^{75} = e^{\,25 - 75\log(3/2)} = e^{-5.4099} \approx 0.0045
    $$

    **5단계: 정확한 값과 중심극한정리 근사.** 정확한 값은 푸아송 확률질량함수를 그대로 더한 것이다.

    $$
    P(X \geq 75) = \sum_{k=75}^{\infty} e^{-50}\frac{50^k}{k!} \approx 0.000578
    $$

    중심극한정리 근사는 $X \approx N(50, 50)$ 으로 보고 연속성 보정을 넣어 셈한다.

    $$
    P(X \geq 75) \approx 1 - \mathcal{N}\!\left(\frac{74.5 - 50}{\sqrt{50}}\right) = 1 - \mathcal{N}(3.4648) \approx 0.000265
    $$

    **파이썬으로 확인하기.**

    ```python
    import numpy as np
    from scipy import stats

    lam, a = 50, 75
    eps = a - lam

    markov = lam / a
    chebyshev = lam / eps**2
    cantelli = lam / (lam + eps**2)
    t = np.log(a / lam)
    chernoff = np.exp(lam * (np.exp(t) - 1) - a * t)
    exact = stats.poisson.sf(a - 1, lam)
    clt = stats.norm.sf((a - 0.5 - lam) / np.sqrt(lam))

    print(f"Markov          : {markov:.4f}")
    print(f"Chebyshev       : {chebyshev:.4f}")
    print(f"One-sided       : {cantelli:.4f}")
    print(f"Chernoff (t={t:.4f}): {chernoff:.6f}")
    print(f"CLT approx      : {clt:.6f}")
    print(f"Exact           : {exact:.6f}")
    ```

    실행 결과는 다음과 같다.

    ```
    Markov          : 0.6667
    Chebyshev       : 0.0800
    One-sided       : 0.0741
    Chernoff (t=0.4055): 0.004472
    CLT approx      : 0.000265
    Exact           : 0.000578
    ```

    **6단계: 견주어 보기.**

    | 방법 | 쓰는 정보 | $P(X \geq 75)$ | 정확한 값의 몇 배 |
    |---|---|---|---|
    | 마르코프 | 평균 | $0.6667$ | 약 $1150$ 배 |
    | 체비쇼프 | 평균, 분산 | $0.0800$ | 약 $138$ 배 |
    | 한쪽 체비쇼프 | 평균, 분산(한쪽) | $0.0741$ | 약 $128$ 배 |
    | 체르노프 | 적률생성함수 전체 | $0.0045$ | 약 $7.7$ 배 |
    | 중심극한정리 근사 | 점근적 정규성 | $0.000265$ | 약 $0.46$ 배 |
    | 정확한 값 | — | $0.000578$ | $1$ 배 |

    **7단계: 여기에서 배울 것.** 쓰는 정보가 늘어날수록 경계는 차례로 촘촘해진다. 평균만 쓰는 마르코프에서 분산을 더한 체비쇼프로, 꼬리를 한쪽으로 좁힌 칸텔리로, 다시 모든 적률을 담은 적률생성함수를 쓰는 체르노프로 갈수록 경계가 좋아진다. 그럼에도 가장 좋은 체르노프조차 정확한 값의 약 8배로 여전히 헐겁다. 꼬리 경계는 **어떤 분포에도 통하도록** 만들어진 도구여서 개별 분포에 꼭 맞을 수 없기 때문이다.

    중심극한정리 근사는 성격이 다르다는 점에 주의해야 한다. 이 값은 **상계가 아니라 어림값**이며, 실제로 여기에서는 정확한 값보다 작게 나와($0.000265 < 0.000578$) 위험을 절반 이하로 깎아 본 셈이다. 푸아송분포는 오른쪽으로 치우쳐 있어서 평균에서 $3.46$ 표준편차나 떨어진 먼 꼬리에서는 정규근사가 잘 맞지 않는다. **경계가 필요한 곳에서는 경계를, 어림값이 필요한 곳에서는 근사를** 써야 한다. $\square$

---

**연습문제 2.**
확률변수 $(X - \mu)^2$ 에 마르코프 부등식을 적용하면 체비쇼프 부등식이 따라 나옴을 증명하여라.

??? success "연습문제 2 풀이"
    $X$ 의 평균 $\mu = \mathbb{E}X$ 와 분산 $\sigma^2 = Var(X)$ 가 모두 유한하다고 하자. $\varepsilon > 0$ 을 아무렇게나 고정한다.

    **1단계: 사건을 제곱꼴로 바꾼다.** $Y = (X - \mu)^2$ 으로 두자. 제곱함수 $u \mapsto u^2$ 이 $[0, \infty)$ 에서 증가하고 $|X - \mu| \geq 0$, $\varepsilon > 0$ 이므로 다음이 성립한다.

    $$
    |X - \mu| \geq \varepsilon \iff (X - \mu)^2 \geq \varepsilon^2
    $$

    이는 **두 사건이 같다**는 뜻이지 한쪽이 다른 쪽을 품는다는 뜻이 아니다. 따라서 확률도 같다.

    $$
    P(|X - \mu| \geq \varepsilon) = P(Y \geq \varepsilon^2)
    $$

    **2단계: 마르코프 부등식을 적용한다.** $Y = (X - \mu)^2 \geq 0$ 이므로 마르코프 부등식을 쓸 수 있는 조건(음이 아닌 확률변수)이 갖추어졌다. 문턱값은 $\varepsilon^2 > 0$ 이다.

    $$
    P(Y \geq \varepsilon^2) \leq \frac{\mathbb{E}Y}{\varepsilon^2}
    $$

    **3단계: 기댓값을 분산으로 알아본다.** 분산의 정의가 바로 $\mathbb{E}(X - \mu)^2$ 이다.

    $$
    \mathbb{E}Y = \mathbb{E}(X - \mu)^2 = Var(X) = \sigma^2
    $$

    **4단계: 합친다.** 1단계부터 3단계를 이으면 다음을 얻는다.

    $$
    P(|X - \mu| \geq \varepsilon) = P\big((X - \mu)^2 \geq \varepsilon^2\big) \leq \frac{\mathbb{E}(X - \mu)^2}{\varepsilon^2} = \frac{\sigma^2}{\varepsilon^2}
    $$

    이것이 곧 체비쇼프 부등식이다.

    **덧붙임.** 이 논법에서 제곱이 하는 일은 두 가지이다. 첫째, 부호가 있는 이탈 $X - \mu$ 를 음이 아닌 값으로 바꾸어 마르코프 부등식을 쓸 수 있게 한다. 둘째, 이렇게 얻은 기댓값이 마침 **분산**이 되어 이미 아는 양으로 경계를 적을 수 있게 한다.

    같은 요령을 $|X - \mu|^k$ 에 쓰면 더 높은 차수의 적률 경계를 얻는다.

    $$
    P(|X - \mu| \geq \varepsilon) \leq \frac{\mathbb{E}|X - \mu|^k}{\varepsilon^k} \qquad (k \geq 1)
    $$

    $k$ 를 키울수록 $\varepsilon$ 이 클 때 경계가 빨리 줄어들지만, 그만큼 높은 적률이 유한해야 한다는 대가를 치른다. 이 생각을 끝까지 밀고 나가 $e^{tX}$ 를 쓰는 것이 체르노프 경계이다. $\square$
