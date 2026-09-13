# 조건부확률밀도함수

## 정의

$Y = y$ 가 주어졌을 때 $X$ 의 **조건부확률밀도함수**는 다음과 같다.

$$f_{X|Y}(x \mid y) = \frac{f(x, y)}{f_Y(y)}$$

단 $f_Y(y) > 0$ 이어야 한다. 마찬가지로 다음이 성립한다.

$$f_{Y|X}(y \mid x) = \frac{f(x, y)}{f_X(x)}$$

## 뜻풀이

조건부확률밀도함수는 "잘라 내고 정규화하기"의 연속판이다.

- **잘라 내기:** $Y = y$ 로 고정하고 그 수평선을 따라 결합밀도를 본다. 그러면 $f(x, y)$ 가 $x$ 만의 함수가 된다.
- **정규화:** $f_Y(y)$ 로 나누어 $x$ 에 대한 적분이 1이 되도록 한다.

## 확인

조건부확률밀도함수는 올바른 확률밀도함수여야 한다.

$$\int_{-\infty}^{\infty} f_{X|Y}(x \mid y) \, dx = \int_{-\infty}^{\infty} \frac{f(x, y)}{f_Y(y)} \, dx = \frac{1}{f_Y(y)} \int_{-\infty}^{\infty} f(x, y) \, dx = \frac{f_Y(y)}{f_Y(y)} = 1$$

## 예: 삼각형 위의 균등분포

$(X, Y)$ 가 $\{0 \le y \le x \le 1\}$ 위에서 균등분포를 따르고 $f(x, y) = 2$ 인 경우를 보자.

$X$ 의 주변분포는 $0 \le x \le 1$ 에서 $f_X(x) = 2x$ 이다.

$X = x$ 가 주어졌을 때 $Y$ 의 조건부확률밀도함수는 다음과 같다.

$$f_{Y|X}(y \mid x) = \frac{f(x, y)}{f_X(x)} = \frac{2}{2x} = \frac{1}{x}, \quad 0 \le y \le x$$

이는 Uniform$(0, x)$ 분포이다. 곧 $X = x$ 가 주어지면 $Y$ 는 $[0, x]$ 위에서 균등분포를 따른다.

## 조건부기댓값(미리 보기)

조건부확률밀도함수를 쓰면 $X = x$ 가 주어졌을 때 $Y$ 의 조건부기댓값은 다음과 같다.

$$E[Y \mid X = x] = \int_{-\infty}^{\infty} y \, f_{Y|X}(y \mid x) \, dy$$

이는 8장에서 깊이 다룬다.

## 연습문제

**연습문제 1.** $(X, Y)$ 의 결합확률밀도함수가 $0 \leq x \leq y \leq 1$ 에서 $f(x,y) = 6(1-y)$ 라 하자. $f_{X|Y}(x \mid y)$ 를 구하여라.

??? success "연습문제 1 풀이"
    먼저 $0 \leq y \leq 1$ 에서 $f_Y(y) = \int_0^y 6(1-y)\,dx = 6y(1-y)$ 를 구한다.

    $$
    f_{X|Y}(x \mid y) = \frac{f(x,y)}{f_Y(y)} = \frac{6(1-y)}{6y(1-y)} = \frac{1}{y}, \quad 0 \leq x \leq y
    $$

    그러므로 $X \mid Y = y \sim \text{Uniform}(0, y)$ 이다.

---

**연습문제 2.** $(X, Y)$ 의 결합확률밀도함수가 $0 \leq x \leq y < \infty$ 에서 $f(x,y) = e^{-y}$ 라 하자. $f_{Y|X}(y \mid x)$ 를 구하여라.

??? success "연습문제 2 풀이"
    먼저 $x \geq 0$ 에서 $f_X(x) = \int_x^{\infty} e^{-y}\,dy = e^{-x}$ 를 구한다.

    $$
    f_{Y|X}(y \mid x) = \frac{e^{-y}}{e^{-x}} = e^{-(y-x)}, \quad y \geq x
    $$

    이는 $Y - x \mid X = x \sim \text{Exp}(1)$ 임을, 곧 $X = x$ 가 주어졌을 때 초과분 $Y - X$ 가 지수분포를 따름을 보여 준다.

---

**연습문제 3.** $X \sim \text{Exp}(1)$ 이고 $Y \mid X = x \sim \text{Uniform}(0, x)$ 라 하자. 결합확률밀도함수 $f(x, y)$ 와 조건부확률밀도함수 $f_{X|Y}(x \mid y)$ 를 구하여라.

??? success "연습문제 3 풀이"
    $0 < y < x$ 에서 $f(x, y) = f_X(x)\,f_{Y|X}(y \mid x) = e^{-x} \cdot \frac{1}{x}$ 이다.

    $f_{X|Y}(x \mid y)$ 를 구하려면 먼저 $f_Y(y) = \int_y^{\infty} \frac{e^{-x}}{x}\,dx$ 를 계산해야 한다(닫힌 꼴이 없다).

    그러면 $x > y$ 에서 $f_{X|Y}(x \mid y) = \frac{e^{-x}/x}{\int_y^{\infty} e^{-s}/s\,ds}$ 이다.

---

**연습문제 4.** $(X, Y)$ 가 단위원판 $\{(x,y) : x^2 + y^2 \leq 1\}$ 위에서 균등분포를 따른다고 하자. $f_{Y|X}(y \mid x)$ 와 $E[Y \mid X = x]$ 를 구하여라.

??? success "연습문제 4 풀이"
    결합확률밀도함수는 원판 위에서 $f(x,y) = 1/\pi$ 이다. 주변분포는 $-1 \leq x \leq 1$ 에서 $f_X(x) = \frac{2\sqrt{1-x^2}}{\pi}$ 이다.

    $$
    f_{Y|X}(y \mid x) = \frac{1/\pi}{2\sqrt{1-x^2}/\pi} = \frac{1}{2\sqrt{1-x^2}}, \quad -\sqrt{1-x^2} \leq y \leq \sqrt{1-x^2}
    $$

    이는 $\text{Uniform}(-\sqrt{1-x^2}, \sqrt{1-x^2})$ 이므로 대칭성에 의해 다음을 얻는다.

    $$
    E[Y \mid X = x] = 0
    $$

---

**연습문제 5.** $0 < x < \infty$, $0 < y < \infty$ 에서 $f(x,y) = 2e^{-x}e^{-2y}$ 라 하자. $X$ 와 $Y$ 가 독립임을 보이고 두 조건부확률밀도함수를 모두 구하여라.

??? success "연습문제 5 풀이"
    결합확률밀도함수가 $f(x,y) = (e^{-x})(2e^{-2y})$ 로 인수분해된다. 이는 $x$ 만의 함수와 $y$ 만의 함수의 곱이고 각각의 적분이 1이다. 따라서 $X \sim \text{Exp}(1)$ 과 $Y \sim \text{Exp}(2)$ 는 독립이다.

    조건부확률밀도함수는 주변확률밀도함수와 같다.

    $$
    f_{X|Y}(x \mid y) = e^{-x}, \quad x > 0
    $$

    $$
    f_{Y|X}(y \mid x) = 2e^{-2y}, \quad y > 0
    $$
