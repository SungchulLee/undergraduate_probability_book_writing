# 성질과 응용

## 대칭성

$X \sim U(a, b)$ 이면 $X$ 는 평균 $(a+b)/2$ 에 대하여 대칭이다.

$$a + b - X \sim U(a, b)$$

곧 $X$ 와 $a + b - X$ 는 같은 분포를 따른다. 특히 $U \sim U(0,1)$ 이면 $1 - U \sim U(0,1)$ 이다.

## 일차변환

$X \sim U(a, b)$ 이고 $c > 0$ 에 대하여 $Y = cX + d$ 이면 다음이 성립한다.

$$Y \sim U(ca + d, \; cb + d)$$

어떤 균등분포든 표준균등분포에서 얻을 수 있다. $U \sim U(0,1)$ 이면 $X = a + (b-a)U \sim U(a,b)$ 이다.

## 쪼개기 방법

균등분포 문제를 다룰 때 쓸모 있는 방법은 확률변수를 알려진 상수와 더 간단한 균등분포 조각의 합으로 **쪼개는** 것이다.

??? example "예: 막대 부러뜨리기"
    길이가 $L$ 인 막대를 $[0, L]$ 위에서 균등하게 고른 지점에서 부러뜨려 두 조각을 만든다. **더 긴** 조각의 길이를 $X$ 라 할 때 그 평균과 분산을 구하여라.

    **핵심 통찰:** 더 긴 조각의 길이는 언제나 $L/2$ 이상이다. $X$ 를 다음과 같이 쪼개자.

    $$X = \underbrace{\frac{L}{2}}_{\text{막대의 절반}} + \underbrace{Y}_{\text{남는 부분}}$$

    여기서 $Y$ 는 한가운데에서 부러뜨린 지점까지의 거리이며, 늘 양수가 되도록 접어 놓은 것이다. 부러뜨리는 지점이 $[0, L]$ 위에서 균등하므로 남는 부분 $Y$ 는 $U(0, L/2)$ 이다.

    **평균:**

    $$E[X] = \frac{L}{2} + E[Y] = \frac{L}{2} + \frac{L}{4} = \frac{3L}{4}$$

    **분산:** 상수만큼 옮겨도 분산은 달라지지 않으므로 다음을 얻는다.

    $$\text{Var}(X) = \text{Var}(Y) = \frac{1}{12}\left(\frac{L}{2}\right)^2 = \frac{L^2}{48}$$

## 균등분포의 보편성

$U(0,1)$ 분포는 두 가지 뜻에서 보편적이다.

1. **어떤 누적분포함수든 자기 확률변수에 먹이면 $U(0,1)$ 이 된다:** $X$ 의 누적분포함수 $F$ 가 연속이면 $F(X) \sim U(0,1)$ 이다(확률적분변환).

2. **어떤 분포든 $U(0,1)$ 에서 만들어 낼 수 있다:** $U \sim U(0,1)$ 이면 $F^{-1}(U)$ 의 누적분포함수는 $F$ 이다(역변환 방법, 변환 절을 보라).

## 균등확률변수의 합

독립인 균등확률변수를 더하면 그 분포는 균등분포가 **아니다**(낱낱의 균등분포가 한 점에 몰린 퇴화분포가 아닌 한 그렇다). i.i.d. $U(0,1)$ 두 개의 합은 $(0, 2)$ 위의 삼각분포를 따른다. 더 많은 균등확률변수를 더하면 중심극한정리에 따라 그 분포는 정규분포에 가까워진다(합성곱에 대한 자세한 내용은 16장을 보라).

## 파이썬 구현

```python
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
n_sim = 100000

# 막대 부러뜨리기 예제
L = 10.0
break_points = np.random.uniform(0, L, n_sim)
longer_piece = np.maximum(break_points, L - break_points)

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# 더 긴 조각의 분포
axes[0].hist(longer_piece, bins=60, density=True, alpha=0.7,
             color='steelblue', label='Simulated')
axes[0].axvline(np.mean(longer_piece), color='red', lw=2, linestyle='--',
                label=f'Mean = {np.mean(longer_piece):.3f}')
axes[0].axvline(3*L/4, color='black', lw=2, linestyle=':',
                label=f'Theory = {3*L/4:.3f}')
axes[0].set_title(f'Length of Longer Piece (L={L})')
axes[0].set_xlabel('Length')
axes[0].legend()
axes[0].grid(True, alpha=0.3)

print(f"Break the stick (L={L}):")
print(f"  E[X] = {np.mean(longer_piece):.4f} (theory {3*L/4:.4f})")
print(f"  Var(X) = {np.var(longer_piece):.4f} (theory {L**2/48:.4f})")

# 보편성: F(X) ~ U(0,1)
from scipy import stats
X_exp = np.random.exponential(2.0, n_sim)  # Exp(0.5)
U_transform = stats.expon.cdf(X_exp, scale=2.0)  # F(X)

axes[1].hist(U_transform, bins=50, density=True, alpha=0.7,
             color='orange', label='F(X) where X ~ Exp(0.5)')
axes[1].axhline(1.0, color='black', lw=2, linestyle='--',
                label='U(0,1) PDF')
axes[1].set_title('Probability Integral Transform: F(X) ~ U(0,1)')
axes[1].set_xlabel('u')
axes[1].set_ylabel('Density')
axes[1].legend()
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('uniform_properties.png', dpi=150, bbox_inches='tight')
plt.show()
```

## 연습문제

**연습문제 1.**
$U \sim U(0, 1)$ 이라 하자. $Y = -3\ln(U)$ 의 확률밀도함수를 구하여라.

??? success "연습문제 1 풀이"
    $y > 0$ 에 대하여 $F_Y(y) = P(-3\ln U \leq y) = P(\ln U \geq -y/3) = P(U \geq e^{-y/3}) = 1 - e^{-y/3}$ 이다.

    이것은 $\text{Exp}(1/3)$ 의 누적분포함수이므로 $y > 0$ 에 대하여 $f_Y(y) = \frac{1}{3}e^{-y/3}$ 이다.

---

**연습문제 2.** *공정한 동전 던지기로 확률 만들기.* 독립인 공정한 동전 던지기만을 써서 성공확률이 다음과 같은 절차를 설계하여라.

$$
\frac{1}{4}, \qquad \frac{1}{3}, \qquad \frac{1}{\pi}
$$

각 절차는 공정한 동전 던지기만을 쓰고, 확률 $1$ 로 끝나야 하며, **성공** 또는 **실패**를 내놓고, 목표 $p$ 에 대하여 $P(\text{성공}) = p$ 를 만족해야 한다. 앞의 두 경우는 몸풀기로, 세 번째를 본 문제로 삼아라.

??? success "연습문제 2 풀이"
    **(a) $p = 1/4$.** 동전을 두 번 던진다. 두 번 모두 앞면일 때 그리고 오직 그때만 성공이라고 선언한다. 독립성에 따라 다음이 성립한다.

    $$
    P(\text{성공}) = P(HH) = \tfrac{1}{2} \cdot \tfrac{1}{2} = \tfrac{1}{4}
    $$

    **(b) $p = 1/3$ (기각 표집).** 동전을 두 번 던지고 그 짝을 다음과 같이 읽는다.

    - $HH \mapsto 1$
    - $HT \mapsto 2$
    - $TH \mapsto 3$
    - $TT \mapsto$ 기각. 두 번 더 던져 다시 시도한다

    기각되지 않았다는 조건 아래에서 받아들여진 세 결과는 같은 정도로 일어나며 각각 조건부확률이 $1/3$ 이다. 받아들여진 결과가 $1$ 일 때 그리고 오직 그때만 성공이라고 선언한다. $P(\text{기각})^k = (1/4)^k \to 0$ 이므로 이 절차는 확률 $1$ 로 끝난다.

    **(c) $p = 1/\pi$ (이진 전개 + 문턱값).** 요령은 동전 던지기를 $[0, 1]$ 위의 균등확률변수로 바꾼 뒤 문턱값과 견주는 것이다.

    *1단계: 동전 던지기로 $U \sim U(0, 1)$ 만들기.* 동전을 되풀이해 던져 $X_n \in \{0, 1\}$ 인 독립 비트 $X_1, X_2, X_3, \ldots$ 를 만든다(앞면 $= 1$, 뒷면 $= 0$). 그리고 다음과 같이 놓는다.

    $$
    U = \sum_{n=1}^{\infty} \frac{X_n}{2^n} = 0.X_1 X_2 X_3 \cdots \text{ (이진수)}
    $$

    잘 알려진 사실(모든 $u \in [0, 1]$ 은 이진 전개를 갖고, 자릿수가 균등하면 $U$ 도 균등하다)에 따라 $U \sim U(0, 1)$ 이다.

    *2단계: $1/\pi$ 를 이진수로 적기.* 각 $b_n \in \{0, 1\}$ 에 대하여 $1/\pi = 0.b_1 b_2 b_3 \cdots$ 이라 하자. 이 비트들은 고정되어 있고 무작위가 아니다.

    *3단계: 게으른 비교.* $X_n$ 을 하나씩 만들면서 $b_n$ 과 견준다. $X_n \neq b_n$ 이 되는 첫 번째 자리 $n$ 에서 멈춘다.

    - $X_n < b_n$ 이면(곧 $X_n = 0$, $b_n = 1$) **성공**이라고 선언한다. 이때 $U < 1/\pi$ 가 보장된다.
    - $X_n > b_n$ 이면(곧 $X_n = 1$, $b_n = 0$) **실패**라고 선언한다. 이때 $U > 1/\pi$ 가 보장된다.

    이진 전개의 사전식 순서에 따라, 처음으로 어긋나는 자리에서 $X_n < b_n$ 인 것이 곧 $\{U < 1/\pi\}$ 이다. $U \sim U(0, 1)$ 이므로 다음이 성립한다.

    $$
    P(\text{성공}) = P\!\left(U < \tfrac{1}{\pi}\right) = \tfrac{1}{\pi}
    $$

    $P(\text{모든 } n \text{ 에 대하여 } X_n = b_n) = P(U = 1/\pi) = 0$ 이므로 이 절차는 거의 확실하게 멈춘다.

    **교훈.** 공정한 동전 던지기만으로 계산 가능한 *어떤* 확률 $p \in [0, 1]$ 도 실현할 수 있다. $U \sim U(0, 1)$ 을 한 자리씩 만들면서 $p$ 와 견주면 된다. 균등분포는 보편적인 무작위성의 원천이며, 이는 위 절의 내용을 이제 구성적으로 보인 것이다. $\square$

---

**연습문제 3.** *두 균등확률변수의 최솟값과 최댓값.* $U_1, U_2 \sim U(0, 1)$ 이 독립이라 하자. $M = \min(U_1, U_2)$ 와 $X = \max(U_1, U_2)$ 의 누적분포함수와 확률밀도함수를 구하고, $E[M] + E[X] = 1$ 임을 확인하여라.

??? success "연습문제 3 풀이"
    $x \in [0, 1]$ 에 대하여 독립성을 쓰면 다음을 얻는다.

    $$
    P(X \leq x) = P(U_1 \leq x,\, U_2 \leq x) = P(U_1 \leq x)\,P(U_2 \leq x) = x^2
    $$

    따라서 $[0, 1]$ 위에서 $F_X(x) = x^2$ 이고 $f_X(x) = 2x$ 이다. 그러면 다음이 성립한다.

    $$
    E[X] = \int_0^1 2x^2 \, dx = \tfrac{2}{3}
    $$

    $M = \min(U_1, U_2)$ 에 대해서는 여사건을 쓴다.

    $$
    P(M > m) = P(U_1 > m,\, U_2 > m) = (1 - m)^2
    $$

    따라서 $[0, 1]$ 위에서 $F_M(m) = 1 - (1 - m)^2$ 이고 $f_M(m) = 2(1 - m)$ 이다. 그러면 다음이 성립한다.

    $$
    E[M] = \int_0^1 2m(1 - m) \, dm = \tfrac{1}{3}
    $$

    확인: $E[M] + E[X] = 1/3 + 2/3 = 1$ 이다. 이것은 사실 $E[U_1] + E[U_2] = E[\min] + E[\max]$ 라는 항등식을 달리 쓴 것이다. 최솟값과 최댓값을 더하면 무엇이든 그 합과 같기 때문이다. $\square$

---

**연습문제 4.** *확률적분변환.* $X$ 를 누적분포함수 $F$ 가 순증가하는 연속확률변수라 하자. $F(X) \sim U(0, 1)$ 임을 증명하여라.

??? success "연습문제 4 풀이"
    $Y = F(X)$ 라 하자. $F$ 가 순증가하고 연속이므로 $(0, 1)$ 위에서 역함수 $F^{-1}$ 을 갖는다. $y \in (0, 1)$ 에 대하여 다음이 성립한다.

    $$
    P(Y \leq y) = P(F(X) \leq y) = P(X \leq F^{-1}(y)) = F(F^{-1}(y)) = y
    $$

    따라서 $(0, 1)$ 위에서 $F_Y(y) = y$ 이고, 이것은 $U(0, 1)$ 의 누적분포함수이다. 그러므로 $Y \sim U(0, 1)$ 이다.

    **따라 나오는 결과.**

    - **역변환 표집.** 거꾸로 $U \sim U(0, 1)$ 이고 $X = F^{-1}(U)$ 이면 $X$ 의 누적분포함수는 $F$ 이다. 난수 생성기가 임의의 연속분포에서 표본을 만들어 내는 바탕이 바로 이것이다.
    - **균등한 잔차.** 가설검정에서 연속인 귀무분포를 제대로 잡았다면 그 아래에서 계산한 $p$-값은 그 자체가 $U(0, 1)$ 을 따른다. 확률적분변환에서 바로 따라 나오는 결과이다.
    - 순증가 가정은 일반화된 역함수 $F^{-1}(u) = \inf\{x : F(x) \geq u\}$ 를 써서 느슨하게 할 수 있고, 이로써 확률적분변환은 일반적인 연속 누적분포함수로 넓혀진다. $\square$
