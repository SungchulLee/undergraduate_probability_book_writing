# 한쪽 체비쇼프 부등식

## 정리의 서술

평균이 $\mu = \mathbb{E}X$ 이고 분산이 $\sigma^2 = Var(X)$ 인 확률변수 $X$ 와 $\varepsilon > 0$ 에 대하여 다음이 성립한다.

$$
P(X - \mathbb{E}X \geq \varepsilon) \leq \frac{\sigma^2}{\varepsilon^2 + \sigma^2}
$$

$$
P(X - \mathbb{E}X \leq -\varepsilon) \leq \frac{\sigma^2}{\varepsilon^2 + \sigma^2}
$$

이를 **칸텔리 부등식**이라고도 부른다.

## 증명

핵심은 확률변수를 상수 $b > 0$ 만큼 옮긴 뒤 마르코프 부등식을 적용하는 것이다.

임의의 $b > 0$ 에 대하여 다음이 성립한다.

$$
X - \mathbb{E}X \geq \varepsilon \iff X - \mathbb{E}X + b \geq \varepsilon + b
$$

$\varepsilon + b > 0$ 이므로 양변을 제곱해도 부등호 방향이 그대로이다.

$$
\implies (X - \mathbb{E}X + b)^2 \geq (\varepsilon + b)^2
$$

여기에 마르코프 부등식을 적용하면 다음을 얻는다.

$$
P(X - \mathbb{E}X \geq \varepsilon) \leq \frac{\mathbb{E}(X - \mathbb{E}X + b)^2}{(\varepsilon + b)^2} = \frac{\sigma^2 + b^2}{(\varepsilon + b)^2}
$$

여기에서 $\mathbb{E}(X - \mu + b)^2 = Var(X) + b^2$ 을 썼다.

$b > 0$ 에 대하여 오른쪽 값을 가장 작게 만들려면 $b = \frac{\sigma^2}{\varepsilon}$ 으로 두면 되고, 그러면 다음을 얻는다.

$$
P(X - \mathbb{E}X \geq \varepsilon) \leq \frac{\sigma^2 + \sigma^4/\varepsilon^2}{(\varepsilon + \sigma^2/\varepsilon)^2} = \frac{\sigma^2}{\varepsilon^2 + \sigma^2}
$$

## 체비쇼프 부등식과 견주어 보기

보통의 체비쇼프 부등식은 $P(|X - \mu| \geq \varepsilon) \leq \sigma^2 / \varepsilon^2$ 이라는 경계를 준다. $|X - \mu| \geq \varepsilon$ 은 양쪽 꼬리를 모두 담고 있으므로, **한쪽** 꼬리만 다룰 때에는 한쪽 체비쇼프 부등식이 더 촘촘하다.

$$
\frac{\sigma^2}{\varepsilon^2 + \sigma^2} \leq \frac{\sigma^2}{\varepsilon^2}
$$

## 예: 이항분포 X ~ B(1000, 0.01)

$\mathbb{E}X = 10$, $Var(X) = 9.9$ 일 때 $P(X \geq 20) = P(X - 10 \geq 10)$ 의 경계는 다음과 같다.

$$
P(X - 10 \geq 10) \leq \frac{9.9}{10^2 + 9.9} = \frac{9.9}{109.9} = 0.0901
$$

체비쇼프 부등식이 준 $0.0990$ 과 견주어 보면 한쪽 경계가 더 촘촘하다.

## 예: 푸아송분포 X ~ Poi(100)

$\mathbb{E}X = 100$, $Var(X) = 100$ 일 때 $P(X \geq 200) = P(X - 100 \geq 100)$ 의 경계는 다음과 같다.

$$
P(X - 100 \geq 100) \leq \frac{100}{100^2 + 100} = \frac{100}{10100} = 0.0099
$$

체비쇼프 부등식이 준 $0.0100$ 과 견주어 보아라.

## 연습문제

**연습문제 1.**
$X$ 의 평균이 $\mu$ 이고 분산이 $\sigma^2$ 이라고 하자. 한쪽 체비쇼프 부등식의 증명에서 $E[(X - \mu + b)^2] \geq (\varepsilon + b)^2 P(X - \mu \geq \varepsilon)$ 의 $b$ 를 가장 알맞게 고르면 $b = \sigma^2 / \varepsilon$ 임을 보여라.

??? success "연습문제 1 풀이"
    **1단계: 무엇을 최소로 만들 것인가.** 증명에서 임의의 $b > 0$ 에 대하여 다음 경계를 얻었다.

    $$
    P(X - \mu \geq \varepsilon) \leq \frac{\mathbb{E}(X - \mu + b)^2}{(\varepsilon + b)^2} = \frac{\sigma^2 + b^2}{(\varepsilon + b)^2}
    $$

    여기에서 $\mathbb{E}(X - \mu + b)^2 = \mathbb{E}(X-\mu)^2 + 2b\,\mathbb{E}(X - \mu) + b^2 = \sigma^2 + b^2$ 을 썼다(가운데 항은 $\mathbb{E}(X - \mu) = 0$ 이므로 사라진다).

    이 경계는 **모든** $b > 0$ 에 대하여 참이므로, 가장 좋은 경계는 오른쪽 값을 가장 작게 만드는 $b$ 에서 나온다. 그러므로 다음 함수를 최소로 만들면 된다.

    $$
    f(b) = \frac{\sigma^2 + b^2}{(\varepsilon + b)^2}, \qquad b > 0
    $$

    **2단계: 미분한다.** 몫의 미분법을 쓴다.

    $$
    f'(b) = \frac{2b(\varepsilon + b)^2 - (\sigma^2 + b^2)\cdot 2(\varepsilon + b)}{(\varepsilon + b)^4}
    $$

    분자와 분모에서 공통인자 $(\varepsilon + b)$ 를 약분하면 다음과 같이 깔끔해진다.

    $$
    f'(b) = \frac{2\big[b(\varepsilon + b) - (\sigma^2 + b^2)\big]}{(\varepsilon + b)^3} = \frac{2\big[b\varepsilon + b^2 - \sigma^2 - b^2\big]}{(\varepsilon + b)^3} = \frac{2(b\varepsilon - \sigma^2)}{(\varepsilon + b)^3}
    $$

    **3단계: 임계점을 찾는다.** $b > 0$ 이고 $\varepsilon > 0$ 이므로 분모 $(\varepsilon + b)^3 > 0$ 이다. 따라서 $f'(b)$ 의 부호는 오직 분자 $b\varepsilon - \sigma^2$ 이 정한다.

    $$
    f'(b) = 0 \iff b\varepsilon = \sigma^2 \iff b^* = \frac{\sigma^2}{\varepsilon}
    $$

    **4단계: 참으로 최솟값임을 확인한다.** 분자가 $b$ 에 대하여 증가하는 일차식이므로 부호가 한 번만 바뀐다.

    $$
    f'(b) < 0 \quad (0 < b < b^*), \qquad f'(b) > 0 \quad (b > b^*)
    $$

    곧 $f$ 는 $b^*$ 앞에서 줄어들다가 뒤에서 늘어나므로 $b^* = \sigma^2/\varepsilon$ 에서 **전역 최솟값**을 가진다. 또한 $\sigma^2 > 0$ 이면 $b^* > 0$ 이므로 이 값은 우리가 허용한 범위 안에 있다.

    **5단계: 넣어서 정리한다.** $b^* = \sigma^2/\varepsilon$ 을 $f$ 에 넣는다. 분자와 분모를 각각 정리하면 다음과 같다.

    $$
    \sigma^2 + (b^*)^2 = \sigma^2 + \frac{\sigma^4}{\varepsilon^2} = \frac{\sigma^2(\varepsilon^2 + \sigma^2)}{\varepsilon^2}
    $$

    $$
    (\varepsilon + b^*)^2 = \left(\varepsilon + \frac{\sigma^2}{\varepsilon}\right)^2 = \left(\frac{\varepsilon^2 + \sigma^2}{\varepsilon}\right)^2 = \frac{(\varepsilon^2 + \sigma^2)^2}{\varepsilon^2}
    $$

    나누면 $\varepsilon^2$ 과 $(\varepsilon^2 + \sigma^2)$ 이 한 번씩 약분된다.

    $$
    f(b^*) = \frac{\sigma^2(\varepsilon^2 + \sigma^2)/\varepsilon^2}{(\varepsilon^2 + \sigma^2)^2/\varepsilon^2} = \frac{\sigma^2}{\varepsilon^2 + \sigma^2}
    $$

    이로써 한쪽 체비쇼프 부등식을 얻는다.

    $$
    P(X - \mu \geq \varepsilon) \leq \frac{\sigma^2}{\varepsilon^2 + \sigma^2}
    $$

    **뜻풀이.** 최적의 옮김량 $b^* = \sigma^2/\varepsilon$ 은 두 힘이 맞서는 자리이다. $b$ 를 키우면 분모 $(\varepsilon + b)^2$ 이 커져서 좋지만 분자의 $b^2$ 도 함께 커진다. $b$ 가 작을 때에는 분모가 $\varepsilon^2$ 에서 출발해 상대적으로 빨리 커지므로 이득이 크고, $b$ 가 커지면 분자와 분모가 모두 $b^2$ 에 끌려가 이득이 사라진다. 그 사이의 균형점이 $\sigma^2/\varepsilon$ 이며, 이탈 $\varepsilon$ 이 클수록 옮김량은 작아진다. $\square$
