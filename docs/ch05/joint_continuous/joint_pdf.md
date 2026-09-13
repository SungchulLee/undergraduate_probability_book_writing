# 결합확률밀도함수

## 정의

연속확률변수 $(X, Y)$ 에 대해 다음을 만족하는 함수 $f(x, y)$ 를 **결합확률밀도함수**라 한다.

$$P((X, Y) \in A) = \iint_A f(x, y) \, dx \, dy$$

벽돌 비유로 말하면 다음과 같다.

$$f(x, y) \, dx \, dy = [x, x+dx] \times [y, y+dy] \text{ 안에 있는 벽돌들의 무게}$$

## 성질

올바른 결합확률밀도함수는 다음을 만족한다.

1. **음이 아님:** 모든 $(x, y)$ 에 대해 $f(x, y) \ge 0$ 이다.
2. **정규화:** $\displaystyle\int_{-\infty}^{\infty} \int_{-\infty}^{\infty} f(x, y) \, dx \, dy = 1$ 이다.

## 확률 구하기

직사각형 영역에 대해서는 다음과 같다.

$$P(a \le X \le b, \, c \le Y \le d) = \int_a^b \int_c^d f(x, y) \, dy \, dx$$

일반적인 영역 $A$ 에 대해서는 다음과 같다.

$$P((X, Y) \in A) = \iint_A f(x, y) \, dx \, dy$$

## 예: 단위정사각형 위의 균등분포

$(X, Y)$ 가 $[0,1]^2$ 위에서 균등분포를 따른다고 하자.

$$f(x, y) = \begin{cases} 1 & 0 \le x \le 1, \, 0 \le y \le 1 \\ 0 & \text{그 밖의 경우} \end{cases}$$

그러면 $P(X \le 1/2, Y \le 1/2) = \int_0^{1/2} \int_0^{1/2} 1 \, dy \, dx = 1/4$ 이다.

## 더 높은 차원으로 넓히기

$\mathbb{R}^d$ 안의 확률벡터 $\mathbf{X} = (X_1, \ldots, X_d)$ 에 대해 다음이 성립한다.

$$f(\mathbf{x}) \, d\mathbf{x} = \prod_{i=1}^d [x_i, x_i + dx_i] \text{ 안에 있는 벽돌들의 무게}$$

$$P(\mathbf{X} \in A) = \int \cdots \int_A f(x_1, \ldots, x_d) \, dx_1 \cdots dx_d$$

## 연습문제

**연습문제 1.** $(X, Y)$ 의 결합확률밀도함수가 $0 \leq x \leq 1$, $0 \leq y \leq 2$ 에서 $f(x, y) = c \, x \, y$ 이고 그 밖에서는 $f(x, y) = 0$ 이라 하자. 상수 $c$ 를 구하고 $P(X \leq 1/2, \, Y \leq 1)$ 을 계산하여라.

??? success "연습문제 1 풀이"
    정규화 조건을 쓰면 다음과 같다.

    $$
    \int_0^1 \int_0^2 c x y \, dy \, dx = c \cdot \left(\int_0^1 x \, dx\right)\left(\int_0^2 y \, dy\right) = c \cdot \tfrac{1}{2} \cdot 2 = c = 1
    $$

    그러므로 $c = 1$ 이고 $f(x, y) = xy$ 이다. 따라서 다음을 얻는다.

    $$
    P(X \leq 1/2, Y \leq 1) = \int_0^{1/2} \int_0^1 x y \, dy \, dx = \tfrac{1}{8} \cdot \tfrac{1}{2} = \frac{1}{16}
    $$

---

**연습문제 2.** $(X, Y)$ 의 결합확률밀도함수가 $0 \leq x \leq y \leq 1$ 에서 $f(x, y) = 6(1 - y)$ 이고 그 밖에서는 $0$ 이다. $f$ 의 적분이 1임을 확인하고 $P(X \leq 1/4)$ 을 계산하여라.

??? success "연습문제 2 풀이"
    **정규화.** 삼각형 $0 \leq x \leq y \leq 1$ 위에서 적분한다.

    $$
    \int_0^1 \int_0^y 6(1 - y) \, dx \, dy = \int_0^1 6 y (1 - y) \, dy = 6 \left[\tfrac{y^2}{2} - \tfrac{y^3}{3}\right]_0^1 = 6 \cdot \tfrac{1}{6} = 1
    $$

    **$P(X \leq 1/4)$ 의 계산.** 이 사건은 $\{(x, y) : 0 \leq x \leq 1/4, \, x \leq y \leq 1\}$ 이다.

    $$
    P(X \leq 1/4) = \int_0^{1/4} \int_x^1 6(1 - y) \, dy \, dx = \int_0^{1/4} 3(1 - x)^2 \, dx
    $$

    계산하면 다음과 같다.

    $$
    \int_0^{1/4} 3(1 - x)^2 \, dx = \left[ -(1 - x)^3 \right]_0^{1/4} = 1 - (3/4)^3 = 1 - \tfrac{27}{64} = \frac{37}{64}
    $$
