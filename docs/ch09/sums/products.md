# 곱의 기댓값(독립인 경우)

## 왜 필요한가

선형성은 $E[X + Y] = E[X] + E[Y]$ 가 언제나 성립함을 알려 준다. 그렇다면 $E[XY]$ 는 어떨까? 일반적으로 $E[XY] \neq E[X]\,E[Y]$ 이다. 그러나 $X$ 와 $Y$ 가 독립이면 기댓값은 곱에 대해서도 **분해된다**.

---

## 정리

!!! info "독립인 확률변수의 곱의 기댓값"
    $X$ 와 $Y$ 가 독립이면 다음이 성립한다.

    $$
    E[XY] = E[X]\,E[Y]
    $$

    단, 두 기댓값이 모두 존재한다고 가정한다.

**증명 (이산인 경우).** 독립성에 따라 $p(x, y) = p_X(x)\,p_Y(y)$ 이므로 다음과 같다.

$$
E[XY] = \sum_x \sum_y xy\,p(x,y) = \sum_x \sum_y xy\,p_X(x)\,p_Y(y)
$$

$$
= \left(\sum_x x\,p_X(x)\right)\!\left(\sum_y y\,p_Y(y)\right) = E[X]\,E[Y]
$$

$\square$

**증명 (연속인 경우).** 독립성에 따라 $f(x,y) = f_X(x)\,f_Y(y)$ 이므로 다음과 같다.

$$
E[XY] = \int_{-\infty}^{\infty}\!\int_{-\infty}^{\infty} xy\,f_X(x)\,f_Y(y)\,dx\,dy = \left(\int x\,f_X(x)\,dx\right)\!\left(\int y\,f_Y(y)\,dy\right)
$$

$\square$

---

## 여러 개의 확률변수로 넓히기

!!! info "독립인 확률변수 n개의 곱"
    $X_1, X_2, \ldots, X_n$ 이 상호독립이면 다음이 성립한다.

    $$
    E\!\left[\prod_{i=1}^n X_i\right] = \prod_{i=1}^n E[X_i]
    $$

이는 $n$ 에 대한 수학적 귀납법으로 얻어진다.

---

## 더 일반적인 함수

독립성은 이보다 강한 결과를 준다. **임의의** 함수 $g$ 와 $h$ 에 대하여 다음이 성립한다.

$$
E[g(X)\,h(Y)] = E[g(X)]\,E[h(Y)]
$$

단, 기댓값들이 존재한다고 가정한다. $X$ 와 $Y$ 가 독립이면 $g(X)$ 와 $h(Y)$ 도 독립이기 때문이다.

---

## 종속일 때는 성립하지 않는다

!!! warning "독립성은 없어서는 안 된다"
    $X$ 와 $Y$ 가 종속이면 $E[XY]$ 는 $E[X]\,E[Y]$ 와 공분산만큼 어긋날 수 있다.

    $$
    E[XY] = E[X]\,E[Y] + \text{Cov}(X, Y)
    $$

??? example "종속인 경우: E[XY] 와 E[X]E[Y] 비교"
    $X \sim \text{Bernoulli}(1/2)$ 이고 $Y = X$ (완전히 종속)라 하자. 그러면 다음과 같다.

    $$
    E[XY] = E[X^2] = E[X] = \frac{1}{2}
    $$

    $$
    E[X]\,E[Y] = \frac{1}{2} \cdot \frac{1}{2} = \frac{1}{4}
    $$

    그 차이가 바로 $\text{Cov}(X,Y) = \text{Var}(X) = 1/4$ 이다.

---

## 응용: 곱의 분산

$X$ 와 $Y$ 가 독립일 때 다음이 성립한다.

$$
\text{Var}(XY) = E[X^2 Y^2] - (E[XY])^2 = E[X^2]\,E[Y^2] - (E[X])^2(E[Y])^2
$$

이것은 다음과 같이 다시 쓸 수 있다.

$$
\text{Var}(XY) = \text{Var}(X)\,\text{Var}(Y) + \text{Var}(X)(E[Y])^2 + (E[X])^2\,\text{Var}(Y)
$$

---

## 파이썬으로 확인하기

```python
import numpy as np

np.random.seed(42)
N = 1_000_000

# 독립인 경우
X = np.random.exponential(2, N)  # E[X] = 2
Y = np.random.poisson(3, N)     # E[Y] = 3

print("--- Independent X, Y ---")
print(f"E[XY] = {np.mean(X * Y):.4f}")
print(f"E[X]*E[Y] = {np.mean(X) * np.mean(Y):.4f}")  # ≈ 6

# 종속인 경우: Y = X
Y_dep = X
print("\n--- Dependent: Y = X ---")
print(f"E[XY] = E[X^2] = {np.mean(X * Y_dep):.4f}")
print(f"E[X]*E[Y] = {np.mean(X) * np.mean(Y_dep):.4f}")
print(f"Cov(X,Y) = {np.cov(X, Y_dep)[0,1]:.4f}")
```

## 연습문제

**연습문제 1.** $X$ 와 $Y$ 가 독립이고 $E[X] = 3$, $E[Y] = -2$, $E[X^2] = 13$, $E[Y^2] = 8$ 이라 하자. $E[XY]$, $E[(X+Y)^2]$, $\text{Cov}(X, Y)$ 를 구하여라.

??? success "연습문제 1 풀이"
    독립성에 따라 $E[XY] = E[X] E[Y] = 3 \cdot (-2) = -6$ 이다. 또한 $\text{Cov}(X, Y) = 0$ 이다.

    $$
    E[(X + Y)^2] = E[X^2] + 2 E[XY] + E[Y^2] = 13 + 2(-6) + 8 = 9
    $$

---

**연습문제 2.** $X$ 와 $Y$ 가 독립이면 다음이 성립함을 보여라.

$$
\text{Var}(XY) = \text{Var}(X) \text{Var}(Y) + \text{Var}(X)(E[Y])^2 + (E[X])^2 \text{Var}(Y)
$$

??? success "연습문제 2 풀이"
    독립성을 쓰면 $E[XY] = E[X] E[Y]$ 이고 $E[X^2 Y^2] = E[X^2] E[Y^2]$ 이다. 그러므로 다음과 같다.

    $$
    \text{Var}(XY) = E[X^2 Y^2] - (E[XY])^2 = E[X^2] E[Y^2] - (E[X])^2 (E[Y])^2
    $$

    $E[X^2] = \text{Var}(X) + (E[X])^2$ 로 적고 $Y$ 에 대해서도 마찬가지로 적자. $\mu_X = E[X]$, $\mu_Y = E[Y]$, $\sigma_X^2 = \text{Var}(X)$, $\sigma_Y^2 = \text{Var}(Y)$ 라 두면 다음을 얻는다.

    $$
    E[X^2] E[Y^2] = (\sigma_X^2 + \mu_X^2)(\sigma_Y^2 + \mu_Y^2) = \sigma_X^2 \sigma_Y^2 + \sigma_X^2 \mu_Y^2 + \mu_X^2 \sigma_Y^2 + \mu_X^2 \mu_Y^2
    $$

    여기에서 $\mu_X^2 \mu_Y^2$ 를 빼면 다음이 된다.

    $$
    \text{Var}(XY) = \sigma_X^2 \sigma_Y^2 + \sigma_X^2 \mu_Y^2 + \mu_X^2 \sigma_Y^2
    $$

    이는 주장한 식과 같다. $\square$
