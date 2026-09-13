# 결합누적분포함수

## 정의

확률벡터 $\mathbf{X} = (X_1, \ldots, X_d)$ 의 **결합누적분포함수**는 다음과 같이 정의된다.

$$F(\mathbf{x}) = P(\mathbf{X} \le \mathbf{x}) = P(X_1 \le x_1, X_2 \le x_2, \ldots, X_d \le x_d)$$

벽돌 비유로 말하면 다음과 같다.

$$F(\mathbf{x}) = -\boldsymbol{\infty} \text{ 부터 } \mathbf{x} \text{ 까지 쌓아 올린 벽돌들의 무게}$$

## 두 변수의 결합누적분포함수

이변량인 경우 $(X, Y)$ 에 대해 다음과 같다.

$$F(x, y) = P(X \le x, Y \le y)$$

### 이산인 경우

$$F(x, y) = \sum_{x_i \le x} \sum_{y_j \le y} p(x_i, y_j)$$

### 연속인 경우

$$F(x, y) = \int_{-\infty}^{x} \int_{-\infty}^{y} f(s, t) \, dt \, ds$$

## 성질

1. **단조성:** $F$ 는 각 변수에 대해 감소하지 않는다.
2. **극한:**
    - $F(-\infty, y) = F(x, -\infty) = 0$
    - $F(\infty, \infty) = 1$
3. **오른쪽 연속성:** $F$ 는 각 변수에 대해 오른쪽 연속이다.

## 결합확률밀도함수 되찾기

연속확률변수에서는 다음이 성립한다.

$$f(x, y) = \frac{\partial^2}{\partial x \, \partial y} F(x, y)$$

## 결합누적분포함수로 확률 구하기

$$P(a < X \le b, \, c < Y \le d) = F(b, d) - F(a, d) - F(b, c) + F(a, c)$$

이는 직사각형 $(a, b] \times (c, d]$ 에 적용한 2차원 포함배제 공식이다.

## 연습문제

**연습문제 1.** $x \geq 0$, $y \geq 0$ 에서 결합누적분포함수가 $F(x, y) = (1 - e^{-x})(1 - e^{-2y})$ 로 주어질 때 다음을 구하여라.

**(a)** $P(X > 1, \, Y > 1)$

**(b)** 결합확률밀도함수 $f(x, y)$

??? success "연습문제 1 풀이"
    **(a)** 누적분포함수가 인수분해되므로(독립이므로) $P(X > 1, Y > 1) = P(X > 1) P(Y > 1)$ 이다. 주변누적분포함수는 $F_X(x) = 1 - e^{-x}$ 와 $F_Y(y) = 1 - e^{-2y}$ 이므로 다음을 얻는다.

    $$
    P(X > 1) = e^{-1}, \quad P(Y > 1) = e^{-2}, \quad P(X > 1, Y > 1) = e^{-3} \approx 0.0498
    $$

    **(b)** 미분하면 다음과 같다.

    $$
    f(x, y) = \frac{\partial^2}{\partial x \partial y} F(x, y) = \frac{\partial}{\partial x}\left[2 e^{-2y}(1 - e^{-x})\right] = 2 e^{-x} e^{-2y}, \quad x, y \geq 0
    $$

    그러므로 $X \sim \text{Exp}(1)$ 과 $Y \sim \text{Exp}(2)$ 가 서로 독립이다.
