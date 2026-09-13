# 코시–슈바르츠 부등식

## 왜 필요한가

지금까지 $|\rho(X,Y)| \leq 1$ 이라고 말해 왔지만 아직 증명하지는 않았다. 코시–슈바르츠 부등식이 바로 이 경계를 내어 주는 결과이며, 그것만이 아니다. 이 부등식은 상관계수, 직교사영, 최소제곱 회귀, 힐베르트 공간의 기하를 모두 떠받치는 기본 부등식이다. 기하적으로는 익숙한 명제 $|\langle u, v\rangle| \leq \|u\|\,\|v\|$ 를, 이 장의 앞에서 소개한 내적 $\langle X, Y\rangle = \text{Cov}(X, Y)$ 아래에서 중심화된 확률변수에 적용한 것이다.

---

## 정리의 서술

!!! info "확률변수에 대한 코시–슈바르츠 부등식"
    이차적률이 유한한 임의의 확률변수 $X$ 와 $Y$ 에 대하여 다음이 성립한다.

    $$
    \bigl|E[XY]\bigr|^2 \leq E[X^2]\,E[Y^2]
    $$

    같은 말로, 공분산으로 적으면 다음과 같다.

    $$
    \bigl|\text{Cov}(X, Y)\bigr| \leq \sigma_X \, \sigma_Y
    $$

    **등호 조건.**

    - *원래 꼴* $|E[XY]|^2 = E[X^2]\,E[Y^2]$: 등호가 성립할 필요충분조건은 둘 다 0은 아닌 상수 $\alpha, \beta$ 가 있어 거의 확실하게 $\alpha X = \beta Y$ 인 것이다. 곧 $X$ 와 $Y$ 가 (절편 없이) 선형종속인 경우이다.
    - *공분산 꼴* $|\text{Cov}(X,Y)| = \sigma_X\sigma_Y$: 등호가 성립할 필요충분조건은 어떤 상수 $a \neq 0$ 과 $b$ 에 대하여 거의 확실하게 $Y = aX + b$ 인 것이다.

    공분산 꼴에 절편이 딸려 나오는 까닭은, 이것이 원래 꼴을 *중심화한* 변수 $X - \mu_X$ 와 $Y - \mu_Y$ 에 적용한 뒤 다시 $X$ 와 $Y$ 로 되돌리면서 상수 $b$ 가 생기기 때문이다.

---

## 증명

증명에는 간단하지만 힘센 생각 하나가 쓰인다. 어떤 확률변수의 분산도 음이 아니라는 사실이다.

중심화한 변수를 $U = X - \mu_X$, $V = Y - \mu_Y$ 라 하자. 임의의 실수 $t$ 에 대하여 확률변수 $U + tV$ 를 생각한다. 분산은 음이 아니므로 다음이 성립한다.

$$
0 \leq \text{Var}(U + tV) = E[(U + tV)^2]
$$

펼치면 다음과 같다.

$$
0 \leq E[U^2] + 2t\,E[UV] + t^2\,E[V^2]
$$

이것은 $t$ 에 대한 이차식 $f(t) = E[V^2]\,t^2 + 2\,E[UV]\,t + E[U^2]$ 이다. 모든 $t$ 에 대하여 $f(t) \geq 0$ 이므로 판별식은 양이 아니어야 한다.

$$
\Delta = 4\bigl(E[UV]\bigr)^2 - 4\,E[U^2]\,E[V^2] \leq 0
$$

그러므로 다음을 얻는다.

$$
\bigl(E[UV]\bigr)^2 \leq E[U^2]\,E[V^2]
$$

$E[UV] = \text{Cov}(X, Y)$, $E[U^2] = \text{Var}(X) = \sigma_X^2$, $E[V^2] = \text{Var}(Y) = \sigma_Y^2$ 이므로 다음이 성립한다.

$$
\bigl|\text{Cov}(X, Y)\bigr| \leq \sigma_X\,\sigma_Y
$$

$\square$

---

## 등호 조건

등호가 성립할($\Delta = 0$ 일) 필요충분조건은 어떤 $t^* \in \mathbb{R}$ 에 대하여 $f(t^*) = 0$ 인 것이고, 이는 확률 1로 $U + t^* V = 0$ 이라는 뜻, 곧 거의 확실하게 $X - \mu_X = -t^*(Y - \mu_Y)$ 라는 뜻이다.

이는 상수 $a = -1/t^*$ 와 $b = \mu_Y - a\mu_X$ 에 대하여 $Y = aX + b$ 인 것과 같다.

---

## 따름정리: 상관계수는 유계이다

$|\text{Cov}(X,Y)| \leq \sigma_X \sigma_Y$ 의 양변을 $\sigma_X \sigma_Y > 0$ 으로 나누면 다음을 얻는다.

$$
|\rho(X, Y)| \leq 1 \qquad\text{즉}\qquad -1 \leq \rho(X, Y) \leq 1
$$

이것이 앞 절에서 말한 상관계수의 범위에 대한 엄밀한 근거이다.

---

## 기하적인 뜻풀이

앞에서 소개한 내적의 말로 하면 이 부등식은 각에 관한 명제이다. $\tilde X = X - \mu_X$, $\tilde Y = Y - \mu_Y$ 로 적고 $\langle \tilde X, \tilde Y\rangle = \text{Cov}(X, Y)$ 와 $\|\tilde X\| = \sigma_X$ 를 쓰면 다음과 같다.

$$
|\langle \tilde X, \tilde Y\rangle| \leq \|\tilde X\|\,\|\tilde Y\|
$$

양변을 $\|\tilde X\|\,\|\tilde Y\|$ 로 나누면 $|\cos\theta| \leq 1$ 이 된다. 여기서 $\theta$ 는 $L^2$ 안에서 $\tilde X$ 와 $\tilde Y$ 가 이루는 각이다. 이 관점에서 보면 다음과 같다.

- 이 부등식은 그저 $|\cos\theta| \leq 1$ 일 뿐이다.
- 등호 $|\rho| = 1$ 은 $\theta = 0$ 또는 $\pi$ 를 뜻하고, 곧 $\tilde X$ 와 $\tilde Y$ 가 평행하다는 것, 즉 완전한 선형 관계임을 뜻한다.
- 직교 $\theta = \pi/2$ 는 정확히 $\rho = 0$ (무상관)이다.

같은 그림이 사영, 회귀, 그리고 분산의 피타고라스 분해를 떠받친다.

---

## E[XY] 꼴

중심화하지 않은 변수 $X$ 와 $Y$ 에 부등식을 바로 적용하면 다음과 같다.

$$
\bigl(E[XY]\bigr)^2 \leq E[X^2]\,E[Y^2]
$$

이를 **기댓값에 대한 슈바르츠 부등식**이라고 부르기도 하며, 섞인 적률의 경계를 잡을 때 쓸모가 있다.

---

## 예제

??? example "모르는 기댓값의 경계 잡기"
    $E[X^2] = 4$ 이고 $E[Y^2] = 9$ 라 하자. 결합분포를 몰라도 다음과 같이 경계를 잡을 수 있다.

    $$
    |E[XY]| \leq \sqrt{E[X^2]\,E[Y^2]} = \sqrt{4 \cdot 9} = 6
    $$

    그러므로 $-6 \leq E[XY] \leq 6$ 이다.

??? example "상관계수에 적용하기"
    $\text{Var}(X) = 16$, $\text{Var}(Y) = 25$, $\text{Cov}(X,Y) = -15$ 라 하자. 그러면 다음과 같다.

    $$
    |\text{Cov}(X,Y)| = 15 \leq \sqrt{16 \cdot 25} = 20 \quad\checkmark
    $$

    $$
    \rho(X,Y) = \frac{-15}{\sqrt{16}\sqrt{25}} = \frac{-15}{20} = -0.75
    $$

    이 값은 $|\rho| \leq 1$ 을 만족한다.

---

## 파이썬으로 확인하기

```python
import numpy as np

np.random.seed(42)
N = 1_000_000

# 상관된 확률변수를 만든다
X = np.random.normal(0, 2, N)  # sigma_X = 2
Y = 0.6 * X + np.random.normal(0, 1, N)

cov_XY = np.cov(X, Y)[0, 1]
sigma_X = np.std(X, ddof=0)
sigma_Y = np.std(Y, ddof=0)

print(f"|Cov(X,Y)| = {abs(cov_XY):.4f}")
print(f"sigma_X * sigma_Y = {sigma_X * sigma_Y:.4f}")
print(f"Cauchy-Schwarz satisfied: {abs(cov_XY) <= sigma_X * sigma_Y}")
```

## 연습문제

**연습문제 1.** 코시–슈바르츠 부등식을 써서 $E[X^2] < \infty$ 인 임의의 확률변수 $X$ 에 대하여 다음이 성립함을 보여라.

$$
\bigl(E[|X|]\bigr)^2 \leq E[X^2]
$$

??? success "연습문제 1 풀이"
    $U = |X|$, $V = 1$ (곧 $V$ 는 결정적인 값)로 두고 코시–슈바르츠를 적용한다.

    $$
    (E[UV])^2 \leq E[U^2] E[V^2]
    $$

    $$
    (E[|X| \cdot 1])^2 \leq E[X^2] \cdot 1
    $$

    그러므로 $(E[|X|])^2 \leq E[X^2]$ 이다. 등호가 성립할 필요충분조건은 $|X|$ 가 거의 확실하게 상수인 것이다. $\square$

---

**연습문제 2.** $E[X^2] = 9$ 이고 $E[Y^2] = 16$ 이라 하자. $E[XY]$ 에 대한 가장 좁은 경계를 구하고, 여기에 더하여 $\mu_X = 1$, $\mu_Y = 2$ 일 때 $\text{Cov}(X, Y)$ 에 대한 가장 좁은 경계를 구하여라.

??? success "연습문제 2 풀이"
    **원래 꼴.** 코시–슈바르츠에 따라 다음이 성립한다.

    $$
    |E[XY]| \leq \sqrt{E[X^2]\,E[Y^2]} = \sqrt{9 \cdot 16} = 12
    $$

    그러므로 $-12 \leq E[XY] \leq 12$ 이다.

    **공분산 꼴.** $\sigma_X^2 = E[X^2] - \mu_X^2 = 9 - 1 = 8$ 과 $\sigma_Y^2 = 16 - 4 = 12$ 를 쓰면 다음을 얻는다.

    $$
    |\text{Cov}(X, Y)| \leq \sigma_X \sigma_Y = \sqrt{8 \cdot 12} = \sqrt{96} = 4\sqrt{6} \approx 9.80
    $$

    여기서 원래 꼴이 주는 경계($\pm 12$)가 공분산 경계($\pm 9.80$)에 $\mu_X\mu_Y = 2$ 를 더한 것보다 *느슨하다*는 점에 유의하자. 둘을 합치면 $E[XY] = \text{Cov}(X,Y) + \mu_X\mu_Y \in [2 - 9.80,\, 2 + 9.80] = [-7.80,\, 11.80]$ 이다. 곧 평균을 알고 나면 공분산 꼴이 $E[XY]$ 에 대해 엄밀히 더 좁은 경계를 준다. $\square$

---

**연습문제 3.** *$L^2$ 에서의 삼각부등식.* 코시–슈바르츠 부등식을 써서 $L^2$ 노름에 대한 **민코프스키 부등식**

$$
\sqrt{E[(X + Y)^2]} \leq \sqrt{E[X^2]} + \sqrt{E[Y^2]}
$$

이 이차적률이 유한한 임의의 확률변수 $X, Y$ 에 대하여 성립함을 증명하여라.

??? success "연습문제 3 풀이"
    왼쪽 변을 펼친다.

    $$
    E[(X + Y)^2] = E[X^2] + 2\,E[XY] + E[Y^2]
    $$

    코시–슈바르츠 $E[XY] \leq |E[XY]| \leq \sqrt{E[X^2]\,E[Y^2]}$ 를 써서 교차항의 경계를 잡는다.

    $$
    E[(X + Y)^2] \leq E[X^2] + 2\sqrt{E[X^2]\,E[Y^2]} + E[Y^2] = \left(\sqrt{E[X^2]} + \sqrt{E[Y^2]}\right)^2
    $$

    양변에 제곱근을 씌우면 원하는 결과를 얻는다. 이것이 $L^2$ 노름 $\|X\| = \sqrt{E[X^2]}$ 에 대한 삼각부등식이며, $L^2$ 가 노름공간임을, 나아가 완비성과 합쳐 힐베르트 공간임을 확인해 준다. $\square$

---

**연습문제 4.** *이산인 경우 되찾기.* 코시–슈바르츠 부등식을 유한개의 값을 같은 확률로 갖는 두 확률변수에 특수화하여 다음 고전적인 부등식을 되찾아라.

$$
\left(\sum_{i=1}^n a_i b_i\right)^2 \leq \left(\sum_{i=1}^n a_i^2\right)\left(\sum_{i=1}^n b_i^2\right)
$$

??? success "연습문제 4 풀이"
    $n$ 개의 결과 $\omega_1, \ldots, \omega_n$ 이 같은 정도로 일어나는 확률공간 위에 $X$ 와 $Y$ 를 정의하고 $X(\omega_i) = a_i$, $Y(\omega_i) = b_i$ 라 하자. 그러면 다음과 같다.

    $$
    E[XY] = \frac{1}{n}\sum_{i=1}^n a_i b_i, \quad E[X^2] = \frac{1}{n}\sum_{i=1}^n a_i^2, \quad E[Y^2] = \frac{1}{n}\sum_{i=1}^n b_i^2
    $$

    코시–슈바르츠 $(E[XY])^2 \leq E[X^2]\,E[Y^2]$ 는 다음이 된다.

    $$
    \frac{1}{n^2}\left(\sum_{i=1}^n a_i b_i\right)^2 \leq \frac{1}{n^2}\left(\sum_{i=1}^n a_i^2\right)\left(\sum_{i=1}^n b_i^2\right)
    $$

    양변에 $n^2$ 을 곱하면 고전적인 부등식이 되살아난다. 그러므로 확률론적인 꼴은 진짜 일반화이며, 이 페이지의 증명(분산이 음이 아님)은 선형대수에서 보던 완전제곱 만들기 논법을 일반화한 것이다. $\square$

---

**연습문제 5.** *개념 문제.* 기하적으로 읽으면 $|\rho| \leq 1$ 은 $|\cos\theta| \leq 1$ 에 해당한다. 중심화된 확률변수 사이의 각 $\theta$ 가운데 $\rho = 0.8$ 에 해당하는 것은 무엇인가? 이를 써서 상관계수가 흔히 "보기보다 대단하지 않은" 까닭을, 예를 들어 $\rho = 0.8$ 이 "관계의 $80\%$ 가 설명된다"는 뜻이 아닌 까닭을 직관적으로 설명하여라.

??? success "연습문제 5 풀이"
    $\rho = \cos\theta$ 이고 $\rho = 0.8$ 이므로 다음과 같다.

    $$
    \theta = \arccos(0.8) \approx 36.87^\circ
    $$

    곧 중심화된 확률변수 $\tilde X$ 와 $\tilde Y$ 는 $L^2$ 안에서 약 $37^\circ$ 의 각을 이룬다. 평행에 가깝기는 하지만 겹쳐 있는 것과는 거리가 멀다.

    **왜 $\rho$ 는 설명되는 몫을 부풀려 보이게 하는가.** "설명되는 분산의 몫"을 제대로 재는 값은 $\rho$ 가 아니라 $\rho^2$ 이다. 정의 페이지의 연습문제 3에서 얻은 피타고라스 분해에 따르면 다음과 같다.

    $$
    \text{Var}(X) = \underbrace{\rho^2 \text{Var}(X)}_{Y \text{ 로 설명되는 몫}} + \underbrace{(1 - \rho^2)\text{Var}(X)}_{\text{잔차}}
    $$

    그러므로 $\rho = 0.8$ 은 분산의 $\rho^2 = 0.64$, 곧 $80\%$ 가 아니라 $64\%$ 를 설명한다. 남은 $36\%$ 는 $Y$ 와 직교하는 잔차 분산이다. 이것이 선형회귀에서 쓰는 바로 그 $R^2$ 통계량이며, 기하적으로 옳은 값이기도 하다. 코사인의 제곱, 곧 방향이 이루는 각이 아니라 사영의 *길이*에 해당하기 때문이다. $\square$
