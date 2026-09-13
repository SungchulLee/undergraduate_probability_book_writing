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
