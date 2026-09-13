# 조건부분산의 정의

## 수로서의 Var(X Y = y)

**$Y = y$ 가 주어졌을 때 $X$ 의 조건부분산**은 $Y = y$ 가 주어졌을 때 $X$ 의 조건부분포로 계산한 것으로, $X$ 가 조건부평균 $E(X \mid Y = y)$ 둘레에 얼마나 퍼져 있는지를 잰다.

$$
\text{Var}(X \mid Y = y) = E\bigl[(X - E(X \mid Y = y))^2 \mid Y = y\bigr]
$$

조건 없는 분산에서와 마찬가지로 **간편식**이 있다.

$$
\text{Var}(X \mid Y = y) = E(X^2 \mid Y = y) - \bigl(E(X \mid Y = y)\bigr)^2
$$

정의의 제곱을 전개하고 조건부기댓값의 선형성을 쓰면 따라 나온다.

## 확률변수로서의 Var(X Y)

$y$ 를 움직여 $E(X \mid Y)$ 를 확률변수로 얻었듯이, $\text{Var}(X \mid Y)$ 도 확률변수이다.

$$
\omega \;\longrightarrow\; y = Y(\omega) \;\longrightarrow\; P(X = x \mid Y = y) \;\longrightarrow\; \text{Var}(X \mid Y = y)
$$

형식을 갖추어 쓰면 다음과 같다.

$$
\text{Var}(X \mid Y)(\omega) = \text{Var}(X \mid Y = Y(\omega))
$$

## 예: 결합확률밀도함수

결합확률밀도함수가 $f(x, y) = \frac{e^{-x/y} e^{-y}}{y}$ 일 때 $X \mid Y = y \sim \text{Exp}(1/y)$ 임을 앞에서 보았다. 비율이 $\lambda = 1/y$ 인 지수분포의 분산은 $1/\lambda^2 = y^2$ 이므로 다음을 얻는다.

$$
\text{Var}(X \mid Y = y) = y^2 \implies \text{Var}(X \mid Y) = Y^2
$$

## 뜻풀이

$\text{Var}(X \mid Y = y)$ 는 $Y = y$ 라는 사실을 알고 난 뒤에도 $X$ 에 남아 있는 **불확실성**을 잰다. $Y$ 를 알면 $X$ 가 정확히 정해지는 경우에는 $\text{Var}(X \mid Y) = 0$ 이다. $Y$ 가 $X$ 에 관하여 아무런 정보도 주지 않는 경우(독립)에는 $\text{Var}(X \mid Y) = \text{Var}(X)$ 이다.

## 연습문제

**연습문제 1.** 참인가 거짓인가: $X$ 와 $Y$ 가 독립이면 $\text{Var}(X \mid Y) = \text{Var}(X)$ 이다. 근거를 들어라.

??? success "연습문제 1 풀이"
    **참이다.** 독립성에 따라 모든 $y$ 에 대하여 $Y = y$ 가 주어졌을 때 $X$ 의 조건부분포는 $X$ 의 주변분포와 같다. 그러므로 $Y$ 의 받침에 있는 모든 $y$ 에 대하여

    $$
    \text{Var}(X \mid Y = y) = \text{Var}(X)
    $$

    이고, 따라서 확률변수 $\text{Var}(X \mid Y)$ 는 상수이며 그 값은 $\text{Var}(X)$ 이다. $\square$
