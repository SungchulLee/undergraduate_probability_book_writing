# 선형변환에서의 분산

## 평균과 분산에 관한 보조정리

상수 $a$, $b$ 에 대하여 다음이 성립한다.

$$
\mathbb{E}(aX + b) = a\,\mathbb{E}(X) + b
$$

$$
\text{Var}(aX + b) = \text{Var}(aX) = a^2 \text{Var}(X)
$$

더해지는 상수 $b$ 는 평균을 옮길 뿐 분산에는 영향을 주지 않는다.

### 공분산을 이용한 증명

$$
\begin{aligned}
\text{Var}(aX + b) &= \text{Cov}(aX + b,\; aX + b) \\[4pt]
&= a^2 \text{Var}(X) + 2ab\,\text{Cov}(X, 1) + b^2 \text{Var}(1) \\[4pt]
&= a^2 \text{Var}(X)
\end{aligned}
$$

$\text{Cov}(X, 1) = 0$ 이고 $\text{Var}(1) = 0$ 이기 때문이다.

## 분산과 공분산의 성질

**(1)** $\;\text{Var}(X) = \text{Cov}(X, X)$

**(2)** $\;\text{Cov}(aX + bY, Z) = a\,\text{Cov}(X, Z) + b\,\text{Cov}(Y, Z)$ &emsp; (쌍선형성)

$\quad\;\;\text{Cov}(Z, aX + bY) = a\,\text{Cov}(Z, X) + b\,\text{Cov}(Z, Y)$

**(3)** $\;\text{Cov}(X, Y) = \text{Cov}(Y, X)$ &emsp; (대칭성)

**(4)** $\;\text{Cov}(X, a) = \text{Cov}(a, X) = 0$

**(5)** $X$ 와 $Y$ 가 독립이면 $\;\text{Cov}(X, Y) = 0$

### 증명

**성질 (2):** 공분산의 쌍선형성은 다음과 같이 보인다.

$$
\begin{aligned}
\text{Cov}(aX + bY, Z) &= \mathbb{E}[(aX + bY - a\mathbb{E}X - b\mathbb{E}Y)(Z - \mathbb{E}Z)] \\
&= \mathbb{E}[a(X - \mathbb{E}X) + b(Y - \mathbb{E}Y)](Z - \mathbb{E}Z) \\
&= a\,\mathbb{E}[(X - \mathbb{E}X)(Z - \mathbb{E}Z)] + b\,\mathbb{E}[(Y - \mathbb{E}Y)(Z - \mathbb{E}Z)] \\
&= a\,\text{Cov}(X, Z) + b\,\text{Cov}(Y, Z)
\end{aligned}
$$

**성질 (5):** $X$ 와 $Y$ 가 독립이면 $\mathbb{E}(XY) = \mathbb{E}(X)\mathbb{E}(Y)$ 이므로 다음을 얻는다.

$$
\text{Cov}(X, Y) = \mathbb{E}(XY) - \mathbb{E}(X)\mathbb{E}(Y) = 0
$$

!!! warning "역은 성립하지 않는다"
    $\text{Cov}(X, Y) = 0$ 이라고 해서 일반적으로 독립인 것은 **아니다**.

## 풀이 예제: 공분산으로 분산 구하기

$\text{Var}(X) = 2$, $\text{Var}(Y) = 2$, $\text{Var}(Z) = 3$, $\text{Cov}(X, Y) = 0.25$ 이고 $Z$ 는 $X$, $Y$ 모두와 독립이라 하자. $V = X + 2Y - 3Z - 2$ 일 때 $\text{Var}(V)$ 를 구하자.

$\text{Var}(V) = \text{Cov}(V, V)$ 를 쓰고 쌍선형성으로 전개하면 다음과 같다.

$$
\begin{aligned}
\text{Var}(V) &= \text{Cov}(X + 2Y - 3Z - 2,\; X + 2Y - 3Z - 2) \\[6pt]
&= \text{Var}(X) + 4\,\text{Cov}(X, Y) - 6\,\text{Cov}(X, Z) \\
&\quad + 4\,\text{Var}(Y) - 12\,\text{Cov}(Y, Z) \\
&\quad + 9\,\text{Var}(Z)
\end{aligned}
$$

$Z$ 가 $X$, $Y$ 와 독립이므로 $\text{Cov}(X, Z) = \text{Cov}(Y, Z) = 0$ 이다. 또한 $\text{Cov}(\cdot, \text{상수}) = 0$ 이다. 그러므로 다음을 얻는다.

$$
\text{Var}(V) = 2 + 4(0.25) + 4(2) + 9(3) = 2 + 1 + 8 + 27 = 38
$$

### 자세한 전개

전체 전개는 성질 (1)–(5)를 차례로 쓴 것이다.

| 단계 | 쓴 규칙 |
|:---|:---|
| $\text{Var}(V) = \text{Cov}(V, V)$ | 성질 (1) |
| Cov의 두 자리를 모두 전개 | 성질 (2): 쌍선형성 |
| 대칭인 항끼리 묶음 | 성질 (3): $\text{Cov}(X,Y) = \text{Cov}(Y,X)$ |
| 상수 항을 버림 | 성질 (4): $\text{Cov}(X, a) = 0$ |
| 독립인 항을 버림 | 성질 (5): 독립 $\Rightarrow$ 공분산 0 |

## 연습문제

**연습문제 1.** $X$ 의 평균이 10이고 분산이 4라 하자. $E[3X + 5]$ 와 $\text{Var}(3X + 5)$ 를 구하여라.

??? success "연습문제 1 풀이"
    $$
    E[3X + 5] = 3(10) + 5 = 35
    $$

    $$
    \text{Var}(3X + 5) = 9 \cdot \text{Var}(X) = 9 \times 4 = 36
    $$

---

**연습문제 2.** 섭씨온도 $C$ 가 $E[C] = 20$, $\text{SD}(C) = 5$ 를 만족할 때 화씨온도 $F = 1.8C + 32$ 의 평균과 표준편차를 구하여라.

??? success "연습문제 2 풀이"
    $$
    E[F] = 1.8 \times 20 + 32 = 68
    $$

    $$
    \text{SD}(F) = |1.8| \times \text{SD}(C) = 1.8 \times 5 = 9
    $$

---

**연습문제 3.** $\text{Var}(X) = 3$, $\text{Var}(Y) = 5$, $\text{Cov}(X, Y) = -1$ 일 때 $\text{Var}(2X - Y + 4)$ 를 구하여라.

??? success "연습문제 3 풀이"
    $$
    \text{Var}(2X - Y + 4) = 4\,\text{Var}(X) + \text{Var}(Y) - 4\,\text{Cov}(X,Y)
    $$

    $$
    = 4(3) + 5 - 4(-1) = 12 + 5 + 4 = 21
    $$

---

**연습문제 4.** 공분산의 쌍선형성을 써서 $\text{Var}(X - Y) = \text{Var}(X) + \text{Var}(Y) - 2\,\text{Cov}(X,Y)$ 임을 증명하여라.

??? success "연습문제 4 풀이"
    $$
    \text{Var}(X - Y) = \text{Cov}(X - Y, X - Y)
    $$

    쌍선형성에 따라 다음과 같다.

    $$
    = \text{Cov}(X, X) - \text{Cov}(X, Y) - \text{Cov}(Y, X) + \text{Cov}(Y, Y)
    $$

    $$
    = \text{Var}(X) - 2\,\text{Cov}(X, Y) + \text{Var}(Y)
    $$

    $\square$

---

**연습문제 5.** $\text{Cov}(X, Y) = 0$ 이지만 $X$ 와 $Y$ 가 독립이 아닌 예를 들어라.

??? success "연습문제 5 풀이"
    $X \sim \text{Uniform}(-1, 1)$ 이고 $Y = X^2$ 이라 하자. 그러면 $E[X] = 0$ 이므로 다음을 얻는다.

    $$
    \text{Cov}(X, Y) = E[XY] - E[X]E[Y] = E[X^3] - 0 = 0
    $$

    $X^3$ 이 대칭인 확률변수의 기함수이기 때문이다. 그러나 $Y$ 는 $X$ 에 의해 완전히 결정되므로 두 변수는 독립이 **아니다**. (예를 들어 $P(Y \leq 0.25 \mid X = 0.4) = 0 \neq P(Y \leq 0.25)$ 이다.)
