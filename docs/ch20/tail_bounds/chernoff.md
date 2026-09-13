# 체르노프 경계

## 정리의 서술

임의의 확률변수 $X$ 와 $\varepsilon > 0$ 에 대하여 다음이 성립한다.

$$
P(X \geq \varepsilon) \leq \min_{t > 0} \frac{\mathbb{E}e^{tX}}{e^{t\varepsilon}}
$$

## 증명

임의의 $t > 0$ 에 대하여 다음이 성립한다.

$$
X \geq \varepsilon \iff tX \geq t\varepsilon \iff e^{tX} \geq e^{t\varepsilon}
$$

$e^{tX}$ 는 음이 아니므로 마르코프 부등식을 적용할 수 있다.

$$
P(X \geq \varepsilon) = P(e^{tX} \geq e^{t\varepsilon}) \leq \frac{\mathbb{E}e^{tX}}{e^{t\varepsilon}}
$$

이 식이 모든 $t > 0$ 에 대하여 성립하므로 오른쪽 값의 최솟값을 취한다.

## 체르노프 경계가 가장 촘촘한 까닭

체르노프 경계는 **적률생성함수** $M_X(t) = \mathbb{E}e^{tX}$ 를 쓰는데, 이 함수는 모든 적률의 정보를 담고 있다. $t$ 에 대하여 최적화하면 경계가 분포의 모양 전체에 맞추어지고, 그래서 지수적으로 줄어드는 경계를 주는 경우가 많다.

## 예: 이항분포 X ~ B(1000, 0.01)

하나의 $X_i \sim B(1, p)$ 의 적률생성함수는 $\mathbb{E}e^{tX_i} = 1 + p(e^t - 1)$ 이다. $X = \sum_{i=1}^n X_i$ 에 대해서는 다음이 성립한다.

$$
\mathbb{E}e^{tX} = \left(1 + p(e^t - 1)\right)^n \leq e^{np(e^t - 1)}
$$

여기에서 부등식 $1 + x \leq e^x$ 를 썼다.

$n = 1000$, $p = 0.01$ 이므로 $np = 10$ 이다. $e^t = 2$ 가 되도록(곧 $t = \log 2$) $t$ 를 고르면 다음을 얻는다.

$$
P(X \geq 20) \leq \frac{e^{10(2-1)}}{e^{20\log 2}} = \frac{e^{10}}{2^{20}} = 0.0210
$$

이는 마르코프($0.5$), 체비쇼프($0.099$), 한쪽 체비쇼프($0.0901$)보다 훨씬 촘촘하다.

$P(X \geq 100)$ 에 대해서는 다음과 같다.

$$
P(X \geq 100) \leq \frac{e^{10(2-1)}}{e^{100\log 2}} = \frac{e^{10}}{2^{100}} = 1.2204 \times 10^{-61}
$$

## 예: 푸아송분포 X ~ Poi(100)

적률생성함수는 $\lambda = 100$ 일 때 $\mathbb{E}e^{tX} = e^{\lambda(e^t - 1)}$ 이다. $e^t = 2$ 로 고르면 다음을 얻는다.

$$
P(X \geq 200) \leq \frac{e^{100(2-1)}}{e^{200\log 2}} = \frac{e^{100}}{2^{200}} = 1.6728 \times 10^{-17}
$$

## 견주어 보기: B(1000, 0.01)

| 경계 | $P(X \geq 20)$ | $P(X \geq 100)$ |
|-------|-----------------|------------------|
| 마르코프 | $0.5$ | $0.1$ |
| 체비쇼프 | $0.0990$ | $0.0012$ |
| 한쪽 체비쇼프 | $0.0901$ | $0.0012$ |
| 체르노프 | $0.0210$ | $1.22 \times 10^{-61}$ |
| 중심극한정리 근사 | $7.41 \times 10^{-4}$ | $\approx 0$ |

## 견주어 보기: Poi(100)

| 경계 | $P(X \geq 200)$ | $P(X \geq 110)$ |
|-------|------------------|------------------|
| 마르코프 | $0.5$ | $0.9091$ |
| 체비쇼프 | $0.0100$ | $1$ |
| 한쪽 체비쇼프 | $0.0099$ | $0.5$ |
| 체르노프 | $1.67 \times 10^{-17}$ | $0.6162$ |
| 중심극한정리 근사 | $7.62 \times 10^{-24}$ | $0.1587$ |

!!! note
    체르노프 경계는 지수적으로 줄어들기 때문에 평균에서 멀리 떨어진 **큰 이탈**에서 특히 힘을 발휘하지만, 평균에 가까운 중간 정도의 이탈에서는 헐거울 수 있다.

## 연습문제

**연습문제 1.**
$X_1, \ldots, X_n$ 이 평균 $\mu$, 분산 $\sigma^2$ 을 갖는 i.i.d. 확률변수라고 하자. 체르노프 경계를 써서 모든 $t > 0$ 에 대하여 다음이 성립함을 보여라.

$$
P(\bar{X}_n - \mu \geq \varepsilon) \leq e^{-n\varepsilon t} \prod_{i=1}^n M_{X_i - \mu}(t)
$$

??? success "연습문제 1 풀이"
    $\bar{X}_n = \frac{1}{n}\sum_{i=1}^n X_i$ 이고 중심화한 확률변수를 $Y_i = X_i - \mu$ 라고 하자. $Y_1, \ldots, Y_n$ 도 독립이고 같은 분포를 따르며 $\mathbb{E}Y_i = 0$ 이다. 적률생성함수는 $M_{X_i - \mu}(t) = \mathbb{E}e^{tY_i}$ 로 적는다(이 $t$ 에서 유한하다고 가정한다).

    **1단계: 사건을 합의 꼴로 다시 적는다.** 양변에 $n$ 을 곱해도 부등호는 그대로이다.

    $$
    \bar{X}_n - \mu \geq \varepsilon \iff \sum_{i=1}^n (X_i - \mu) \geq n\varepsilon \iff S_n^Y := \sum_{i=1}^n Y_i \geq n\varepsilon
    $$

    **2단계: 지수를 씌운다.** $t > 0$ 을 고정하자. $u \mapsto e^{tu}$ 는 $t > 0$ 일 때 **증가**함수이므로 부등호의 방향이 보존된다.

    $$
    S_n^Y \geq n\varepsilon \iff t S_n^Y \geq t n \varepsilon \iff e^{t S_n^Y} \geq e^{t n \varepsilon}
    $$

    $t > 0$ 이라는 조건이 여기에서 꼭 필요하다. $t < 0$ 이면 부등호가 뒤집혀 엉뚱한 방향의 경계가 나온다.

    **3단계: 마르코프 부등식을 적용한다.** $e^{tS_n^Y} > 0$ 이므로 음이 아닌 확률변수에 대한 마르코프 부등식을 쓸 수 있다. 문턱값은 $e^{tn\varepsilon} > 0$ 이다.

    $$
    P(\bar{X}_n - \mu \geq \varepsilon) = P\big(e^{t S_n^Y} \geq e^{t n \varepsilon}\big) \leq \frac{\mathbb{E}e^{t S_n^Y}}{e^{t n \varepsilon}} = e^{-n\varepsilon t}\, \mathbb{E}e^{t S_n^Y}
    $$

    **4단계: 독립성으로 기댓값을 쪼갠다.** $S_n^Y = Y_1 + \cdots + Y_n$ 이므로 지수법칙에 따라 다음과 같다.

    $$
    e^{t S_n^Y} = e^{t(Y_1 + \cdots + Y_n)} = \prod_{i=1}^n e^{t Y_i}
    $$

    $Y_1, \ldots, Y_n$ 이 독립이면 그 함수인 $e^{tY_1}, \ldots, e^{tY_n}$ 도 독립이고, 독립인 확률변수들의 곱의 기댓값은 기댓값의 곱이다.

    $$
    \mathbb{E}e^{t S_n^Y} = \mathbb{E}\left[\prod_{i=1}^n e^{t Y_i}\right] = \prod_{i=1}^n \mathbb{E}e^{t Y_i} = \prod_{i=1}^n M_{X_i - \mu}(t)
    $$

    **5단계: 합친다.** 3단계와 4단계를 이으면 모든 $t > 0$ 에 대하여 다음을 얻는다.

    $$
    P(\bar{X}_n - \mu \geq \varepsilon) \leq e^{-n\varepsilon t} \prod_{i=1}^n M_{X_i - \mu}(t)
    $$

    이것이 보이려던 식이다.

    **덧붙임: i.i.d. 이면 더 간단해진다.** $X_i$ 가 같은 분포를 따르므로 $M_{X_i - \mu}(t)$ 는 $i$ 에 따라 달라지지 않는다. $M(t) = M_{X_1 - \mu}(t)$ 로 두면 곱이 거듭제곱이 된다.

    $$
    P(\bar{X}_n - \mu \geq \varepsilon) \leq \left[e^{-\varepsilon t} M(t)\right]^n
    $$

    이 식이 중요한 까닭은 대괄호 안의 값이 $n$ 과 무관하다는 데에 있다. 어떤 $t_0 > 0$ 에 대하여 $\rho := e^{-\varepsilon t_0} M(t_0) < 1$ 이 되도록 만들 수만 있다면 경계가 $\rho^n$ 이 되어 **$n$ 에 대하여 지수적으로** 줄어든다. 체비쇼프가 주는 $\sigma^2/(n\varepsilon^2)$ 이 $1/n$ 꼴로만 줄어드는 것과 견주면 엄청나게 빠르다.

    실제로 그런 $t_0$ 이 있음은 $g(t) = e^{-\varepsilon t}M(t)$ 를 $t = 0$ 근처에서 살펴보면 알 수 있다. $g(0) = 1$ 이고 $M'(0) = \mathbb{E}Y_1 = 0$ 이므로 다음과 같다.

    $$
    g'(0) = -\varepsilon M(0) + M'(0) = -\varepsilon < 0
    $$

    곧 $g$ 는 $t = 0$ 에서 줄어들기 시작하므로 충분히 작은 $t_0 > 0$ 에서 $g(t_0) < 1$ 이 된다. 마지막으로 모든 $t > 0$ 에 대하여 경계가 참이므로 가장 좋은 경계를 얻으려면 최솟값을 취한다.

    $$
    P(\bar{X}_n - \mu \geq \varepsilon) \leq \left[\inf_{t > 0} e^{-\varepsilon t} M(t)\right]^n
    $$

    이것이 큰 이탈 이론(large deviations)에서 말하는 지수적 감소율의 출발점이다. $\square$
