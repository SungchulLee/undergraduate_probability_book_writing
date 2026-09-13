# 반복 기댓값의 법칙(탑 성질)

## 정리의 서술

임의의 확률변수 $X$ 와 $Y$ 에 대하여 다음이 성립한다.

$$
E(X) = E\bigl[E(X \mid Y)\bigr]
$$

이를 **탑 성질** 또는 **전기댓값 법칙**이라고도 한다. 바깥쪽 기댓값은 $Y$ 의 무작위성에 대하여 취한 것이다.

## 조건부기댓값의 성질

다음 성질들이 성립하며, 조건부기댓값을 계산할 때 없어서는 안 될 도구이다.

**(1) 선형성:** $E(X + Y \mid Z) = E(X \mid Z) + E(Y \mid Z)$

**(2) 상수배:** $E(aX \mid Y) = a \, E(X \mid Y)$

**(3) 이미 아는 값은 그대로:** $E(g(Y) \mid Y) = g(Y)$

**(4) 아는 것은 끄집어내기:** $E(g(Y) \cdot X \mid Y) = g(Y) \cdot E(X \mid Y)$

**(5) 독립:** $X$ 와 $Y$ 가 독립이면 $E(X \mid Y) = E(X)$

**(6) 탑 성질:** $E(X) = E\bigl[E(X \mid Y)\bigr]$

성질 (3)과 (4)는 $Y$ 로 조건을 줄 때 $Y$ 의 함수는 상수처럼 굴어 기댓값 밖으로 끄집어낼 수 있다는 생각을 담고 있다.

## 탑 성질의 증명 (이산인 경우)

$$
\begin{aligned}
E\bigl[E(X \mid Y)\bigr] &= \sum_{y_j} E(X \mid Y = y_j) \, P(Y = y_j) \\[6pt]
&= \sum_{y_j} \left( \sum_{x_i} x_i \, P(X = x_i \mid Y = y_j) \right) P(Y = y_j) \\[6pt]
&= \sum_{x_i} x_i \left( \sum_{y_j} P(X = x_i \mid Y = y_j) \, P(Y = y_j) \right) \\[6pt]
&= \sum_{x_i} x_i \, P(X = x_i) \\[6pt]
&= E(X)
\end{aligned}
$$

핵심이 되는 단계에서는 전확률 법칙 $\sum_{y_j} P(X = x_i \mid Y = y_j) \, P(Y = y_j) = P(X = x_i)$ 를 썼다.

## 직관

탑 성질이 말하는 바는 이렇다. $X$ 의 전체 평균을 구하려면, 먼저 $Y$ 가 나누어 놓은 각 무리 안에서 $X$ 의 평균을 구한 다음, 그 무리별 평균들을 각 무리의 확률로 가중평균하면 된다는 것이다. 층화표집이나 "무리로 묶은 뒤 합치기"와 같은 생각이다.

## 예: 대칭성을 이용하는 논증

$X$ 와 $Y$ 를 i.i.d. 인 $\text{Binomial}(n, p)$ 확률변수라 하자. $E(X \mid X + Y = m)$ 을 구해 보자.

**이미 아는 정보:** $X + Y = m$ 이 주어졌으므로 $E(X + Y \mid X + Y = m) = m$ 이다.

**선형성에 따라:** $E(X + Y \mid X + Y = m) = E(X \mid X + Y = m) + E(Y \mid X + Y = m)$ 이다.

**대칭성에 따라:** $X$ 와 $Y$ 가 i.i.d. 이므로 $X + Y$ 를 이루는 데서 똑같은 구실을 한다. 그러므로 $E(X \mid X + Y = m) = E(Y \mid X + Y = m)$ 이다.

**모아 보면:** $2 \, E(X \mid X + Y = m) = m$ 이므로 다음을 얻는다.

$$
E(X \mid X + Y = m) = \frac{m}{2}
$$

## 파이썬 모의실험

```python
import numpy as np

np.random.seed(42)
n_sim = 200_000
n, p = 10, 0.3

X = np.random.binomial(n, p, n_sim)
Y = np.random.binomial(n, p, n_sim)
S = X + Y

# E(X | X+Y = m) = m/2 확인
for m in [3, 5, 8, 10]:
    mask = (S == m)
    if mask.sum() > 0:
        cond_mean = X[mask].mean()
        print(f"E(X | X+Y={m}) = {cond_mean:.3f}  (theory: {m/2:.1f})")

# 탑 성질 확인: E[E(X|Y)] = E(X)
print(f"\nE(X) = {X.mean():.4f}  (theory: {n*p})")
```

## 연습문제

**연습문제 1.** $P(\text{앞면}) = 1/3$ 인 동전을 던진다. 앞면이 나오면 공정한 주사위를 던져 나온 눈을 $X$ 라 하고, 뒷면이 나오면 $X = 10$ 이라 한다. 탑 성질을 써서 $E[X]$ 를 구하여라.

??? success "연습문제 1 풀이"
    $E[X \mid H] = E[\text{주사위 눈}] = 3.5$ 이고 $E[X \mid T] = 10$ 이다.

    $$
    E[X] = E[E[X \mid \text{동전}]] = E[X \mid H] \cdot P(H) + E[X \mid T] \cdot P(T) = 3.5 \times \frac{1}{3} + 10 \times \frac{2}{3} = \frac{23.5}{3} \approx 7.833
    $$

---

**연습문제 2.** $N \sim \text{Poisson}(\lambda)$ 이고 $N = n$ 이 주어졌을 때 $X \mid N = n \sim \text{Binomial}(n, p)$ 라 하자. $E[X]$ 를 구하여라.

??? success "연습문제 2 풀이"
    $E[X \mid N = n] = np$ 이므로 확률변수로 보면 $E[X \mid N] = Np$ 이다. 탑 성질에 따라 다음을 얻는다.

    $$
    E[X] = E[E[X \mid N]] = E[Np] = pE[N] = p\lambda
    $$

---

**연습문제 3.** $X$ 와 $Y$ 를 i.i.d. 인 $\text{Geometric}(p)$ 확률변수라 하자. 탑 성질과 대칭성을 써서 $E[X \mid X + Y = m]$ 을 구하여라.

??? success "연습문제 3 풀이"
    대칭성에 따라(이항분포 예제와 같은 논증) $X$ 와 $Y$ 가 i.i.d. 이므로 $E[X \mid X + Y = m] = E[Y \mid X + Y = m]$ 이다. 둘을 더하면 다음을 얻는다.

    $$
    2E[X \mid X + Y = m] = E[X + Y \mid X + Y = m] = m
    $$

    $$
    E[X \mid X + Y = m] = \frac{m}{2}
    $$

---

**연습문제 4.** 성질 (4) $E[g(Y) \cdot X \mid Y] = g(Y) \cdot E[X \mid Y]$ 를 증명하여라. (힌트: $Y = y$ 로 조건을 주고 $g(y)$ 를 상수로 다루어라.)

??? success "연습문제 4 풀이"
    값 $Y = y$ 를 고정하면 다음과 같다.

    $$
    E[g(Y) \cdot X \mid Y = y] = E[g(y) \cdot X \mid Y = y] = g(y) \cdot E[X \mid Y = y]
    $$

    둘째 등호가 성립하는 것은 $Y = y$ 가 고정되면 $g(y)$ 가 상수이므로 (조건부) 기댓값 밖으로 빠져나오기 때문이다. 이것이 모든 $y$ 에 대하여 성립하므로 확률변수 꼴로 다음과 같이 쓸 수 있다.

    $$
    E[g(Y) \cdot X \mid Y] = g(Y) \cdot E[X \mid Y]
    $$

    $\square$

---

**연습문제 5.** 하루에 일어나는 사고의 수가 $\text{Poisson}(\Lambda)$ 를 따르고, $\Lambda$ 자체가 $E[\Lambda] = 3$, $\text{Var}(\Lambda) = 2$ 인 확률변수라 하자. 사고의 수를 $N$ 이라 할 때 $E[N]$ 과 $\text{Var}(N)$ 을 구하여라.

??? success "연습문제 5 풀이"
    탑 성질에 따라 $E[N] = E[E[N \mid \Lambda]] = E[\Lambda] = 3$ 이다.

    전분산 법칙에 따라 다음을 얻는다.

    $$
    \text{Var}(N) = E[\text{Var}(N \mid \Lambda)] + \text{Var}(E[N \mid \Lambda]) = E[\Lambda] + \text{Var}(\Lambda) = 3 + 2 = 5
    $$
