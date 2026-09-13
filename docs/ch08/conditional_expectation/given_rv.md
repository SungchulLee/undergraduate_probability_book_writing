# 확률변수가 주어졌을 때의 조건부기댓값

## 수에서 확률변수로

$E(X \mid Y = y)$ 는 $y$ 를 하나 고정할 때마다 수 하나이지만, $y$ 가 $Y$ 의 모든 값에 걸쳐 움직이게 하면 $E(X \mid Y)$ 를 **확률변수**로 정의할 수 있다.

핵심 생각은 이렇다. 결과 $\omega$ 가 $Y(\omega) = y$ 를 정하고, 그 $y$ 가 $P(X = x \mid Y = y)$ 를 정하며, 다시 그것이 $E(X \mid Y = y)$ 를 정한다.

$$
\omega \;\longrightarrow\; y = Y(\omega) \;\longrightarrow\; P(X = x \mid Y = y) \;\longrightarrow\; E(X \mid Y = y)
$$

형식을 갖추어 쓰면 다음과 같다.

$$
E(X \mid Y)(\omega) = E(X \mid Y = Y(\omega))
$$

## Y 의 함수로서의 E(X Y)

$E(X \mid Y)$ 는 확률변수 $Y$ 의 함수이다. $g(y) = E(X \mid Y = y)$ 로 두면 다음과 같다.

$$
E(X \mid Y) = g(Y)
$$

$g(Y)$ 가 확률변수의 함수이므로 $E(X \mid Y)$ 자체도 확률변수이다. 그 무작위성은 온전히 $Y$ 에서 물려받은 것이다.

## 이산인 경우의 표현

$Y$ 가 $y_1, y_2, \ldots, y_n$ 의 값을 가질 때 확률변수 $E(X \mid Y)$ 를 다음과 같이 또렷이 적을 수 있다.

$$
E(X \mid Y) = \begin{cases}
E(X \mid Y = y_1) & Y = y_1 \text{ 일 때, 확률 } P(Y = y_1) \\
E(X \mid Y = y_2) & Y = y_2 \text{ 일 때, 확률 } P(Y = y_2) \\
\vdots & \vdots \\
E(X \mid Y = y_n) & Y = y_n \text{ 일 때, 확률 } P(Y = y_n)
\end{cases}
$$

## 예: 결합확률밀도함수 (이어서)

$f(x, y) = \frac{e^{-x/y} e^{-y}}{y}$ 인 결합확률밀도함수의 예에서 $E(X \mid Y = y) = y$ 를 얻었다. 그러므로 다음과 같다.

$$
E(X \mid Y) = Y
$$

$$
\text{Var}(X \mid Y) = Y^2
$$

여기서 $E(X \mid Y) = Y$ 는 확률변수이다. $Y$ 가 어떤 값을 갖든 그 값을 그대로 가진다.

## 연습문제

**연습문제 1.** $X$ 와 $Y$ 의 결합확률밀도함수가 $0 < x < y < 1$ 에서 $f(x, y) = 2$ 라 하자. $E(X \mid Y = y)$ 와 $\text{Var}(X \mid Y = y)$ 를 구하여라.

??? success "연습문제 1 풀이"
    $Y$ 의 주변밀도는 $0 < y < 1$ 에서 $f_Y(y) = \int_0^y 2 \, dx = 2y$ 이다. 조건부밀도는 다음과 같다.

    $$
    f_{X \mid Y}(x \mid y) = \frac{2}{2y} = \frac{1}{y}, \quad 0 < x < y
    $$

    그러므로 $Y = y$ 가 주어지면 $X \sim \text{Uniform}(0, y)$ 이다. 따라서 다음을 얻는다.

    $$
    E(X \mid Y = y) = \frac{y}{2}, \quad \text{Var}(X \mid Y = y) = \frac{y^2}{12}
    $$

---

**연습문제 2.** $X$ 와 $Y$ 를 i.i.d. 인 $\text{Geometric}(p)$ 확률변수라 하자. 대칭성을 이용하여 $E(X \mid X + Y = n)$ 을 구하여라.

??? success "연습문제 2 풀이"
    대칭성에 따라 $E(X \mid X + Y = n) = E(Y \mid X + Y = n)$ 이다. 이 둘을 더하면 다음을 얻는다.

    $$
    E(X \mid X + Y = n) + E(Y \mid X + Y = n) = E(X + Y \mid X + Y = n) = n
    $$

    그러므로 $E(X \mid X + Y = n) = n/2$ 이다.

---

**연습문제 3.** $X$ 와 $Y$ 의 결합확률밀도함수가 $0 < x < y < \infty$ 에서 $f(x, y) = e^{-y}$ 라 하자. $E(Y \mid X = x)$ 를 구하고 이를 탑 성질에 써서 $E(Y)$ 를 구하여라.

??? success "연습문제 3 풀이"
    **$X$ 의 주변분포.** $x > 0$ 에 대하여 다음과 같다.

    $$
    f_X(x) = \int_x^{\infty} e^{-y} \, dy = e^{-x}
    $$

    그러므로 $X \sim \text{Exp}(1)$ 이다. 조건부밀도는 다음과 같다.

    $$
    f_{Y \mid X}(y \mid x) = \frac{e^{-y}}{e^{-x}} = e^{-(y - x)}, \quad y > x
    $$

    곧 $X = x$ 가 주어지면 $Y - x \sim \text{Exp}(1)$ 이므로 $E(Y \mid X = x) = x + 1$ 이다.

    **탑 성질.**

    $$
    E[Y] = E[E(Y \mid X)] = E[X + 1] = 1 + 1 = 2
    $$
