# 수렴들 사이의 관계

## 수렴의 층계

세 가지 수렴 사이에는 다음 함의 관계가 성립한다.

$$
X_n \xrightarrow{a.s.} X \implies X_n \xrightarrow{p} X \implies X_n \xrightarrow{d} X
$$

그 역들은 일반적으로 하나도 성립하지 않는다.

## 거의 확실한 수렴이 확률수렴을 함의하는 까닭

$P(\lim X_n = X) = 1$ 이면 임의의 $\varepsilon > 0$ 에 대하여 $|X_n - X| > \varepsilon$ 이 되는 결과들의 모임은 줄어들 수밖에 없다. 좀 더 정확히 말하면, 거의 확실한 수렴은 "나쁜" 사건 $\{|X_n - X| > \varepsilon\}$ 이 (확률 1로) 유한 번만 일어날 수 있음을 뜻하므로 그 확률은 0으로 가야 한다.

$$
P(|X_n - X| > \varepsilon) \to 0
$$

이것이 바로 확률수렴이다.

## 확률수렴이 분포수렴을 함의하는 까닭

모든 $\varepsilon > 0$ 에 대하여 $P(|X_n - X| > \varepsilon) \to 0$ 이면, $F_X$ 의 임의의 연속점 $x$ 에서 누적분포함수의 차이를 벗어날 확률로 눌러 줌으로써 $F_{X_n}(x) \to F_X(x)$ 임을 보일 수 있다.

## 역은 성립하지 않는다

??? example "확률수렴하지만 거의 확실하게 수렴하지는 않는 경우"
    균등분포를 준 $\Omega = [0,1]$ 을 생각하자. $X_n = \mathbf{1}_{I_n}$ 으로 두되, 구간 $I_n$ 은 길이를 줄여 가며 $[0,1]$ 을 돌아다니게 한다. 곧 $I_1 = [0,1]$, $I_2 = [0,1/2]$, $I_3 = [1/2,1]$, $I_4 = [0,1/3]$, $I_5 = [1/3,2/3]$, $I_6 = [2/3,1]$, 이런 식이다.

    그러면 $P(X_n = 1) \to 0$ 이므로 $X_n \xrightarrow{p} 0$ 이다. 그러나 모든 $\omega \in [0,1]$ 에 대하여 수열 $X_n(\omega)$ 는 값 1을 무한히 자주 가지므로 어떤 $\omega$ 에 대해서도 $X_n(\omega) \not\to 0$ 이다. 따라서 $X_n$ 은 거의 확실하게 수렴하지 **않는다**.

??? example "분포수렴하지만 확률수렴하지는 않는 경우"
    $X \sim N(0,1)$ 이라 하고 모든 $n$ 에 대하여 $X_n = -X$ 로 정의하자. 그러면 모든 $n$ 에 대하여 $X_n \sim N(0,1)$ 이므로 $X_n \xrightarrow{d} X$ 이다. 그러나 $|X_n - X| = 2|X|$ 이므로 모든 $\varepsilon > 0$ 과 모든 $n$ 에 대하여 $P(|X_n - X| > \varepsilon) = P(2|X| > \varepsilon) > 0$ 이다. 따라서 $X_n$ 은 $X$ 로 확률수렴하지 **않는다**.

## 특별한 경우: 상수로 수렴할 때

극한이 **상수** $c$ 일 때에는 분포수렴과 확률수렴이 동치이다.

$$
X_n \xrightarrow{d} c \iff X_n \xrightarrow{p} c
$$

큰수의 법칙이 상수 $\mu$ 로의 수렴을 주장하므로 이 사실은 특히 중요하다.

## 요약 표

| 수렴 | 기호 | 정의 |
|------|----------|------------|
| 거의 확실한 수렴(강) | $X_n \xrightarrow{a.s.} X$ | $P(\lim X_n = X) = 1$ |
| 확률수렴(약) | $X_n \xrightarrow{p} X$ | 모든 $\varepsilon > 0$ 에 대하여 $P(\|X_n - X\| > \varepsilon) \to 0$ |
| 분포수렴 | $X_n \xrightarrow{d} X$ | 연속점에서 $F_{X_n}(x) \to F_X(x)$ |

## 각 수렴이 나타나는 곳

| 정리 | 수렴의 뜻 |
|---------|---------------------|
| 중심극한정리 | 분포수렴 |
| 큰수의 약법칙 | 확률수렴 |
| 큰수의 강법칙 | 거의 확실한 수렴 |

뒤로 갈수록 표본평균이 어떻게 움직이는지에 대하여 더 강한 주장을 한다.

## 연습문제

**연습문제 1.**
$c$ 가 상수이고 $X_n \xrightarrow{d} c$ 라고 하자. $X_n \xrightarrow{p} c$ 임을 증명하여라.

*힌트: 임의의 $\varepsilon > 0$ 에 대하여 $P(|X_n - c| > \varepsilon)$ 을 $F_{X_n}$ 으로 나타내고, 연속점 $c - \varepsilon$ 과 $c + \varepsilon$ 에서의 누적분포함수 수렴을 써라.*

??? success "연습문제 1 풀이"
    $F_n$ 을 $X_n$ 의 누적분포함수라고 하고, 상수 $c$ 를 확률변수로 보았을 때의 누적분포함수를 $F$ 라고 하자. 정의 $F(x) = P(c \leq x)$ 를 그대로 셈하면 다음과 같다.

    $$
    F(x) = \begin{cases} 0 & x < c \\ 1 & x \geq c \end{cases}
    $$

    이를 **퇴화분포**라고 한다.

    **1단계: 연속점을 파악한다.** $F$ 는 $x = c$ 에서만 뛴다($0$ 에서 $1$ 로). 그러므로 $x \neq c$ 인 모든 $x$ 가 $F$ 의 연속점이다. 특히 $\varepsilon > 0$ 을 아무렇게나 고정하면 $c - \varepsilon$ 과 $c + \varepsilon$ 은 둘 다 연속점이다. 가정 $X_n \xrightarrow{d} c$ 는 연속점에서의 수렴만 보장하므로, 이 점들을 고른 것이 결정적이다. (문제의 점 $x = c$ 에서는 $F_n(c) \to F(c) = 1$ 이 성립하지 않을 수도 있고, 실제로 필요하지도 않다.)

    **2단계: 나쁜 사건을 누적분포함수로 눌러 준다.** 사건 $\{|X_n - c| > \varepsilon\}$ 은 서로소인 두 조각으로 갈린다.

    $$
    \{|X_n - c| > \varepsilon\} = \{X_n > c + \varepsilon\} \cup \{X_n < c - \varepsilon\}
    $$

    각 조각을 누적분포함수로 적는다. 첫 번째는 정확히 다음과 같다.

    $$
    P(X_n > c + \varepsilon) = 1 - P(X_n \leq c + \varepsilon) = 1 - F_n(c + \varepsilon)
    $$

    두 번째는 $\{X_n < c - \varepsilon\} \subset \{X_n \leq c - \varepsilon\}$ 이므로 부등식이 된다(열린 부등호와 닫힌 부등호의 차이는 한 점의 확률뿐이다).

    $$
    P(X_n < c - \varepsilon) \leq P(X_n \leq c - \varepsilon) = F_n(c - \varepsilon)
    $$

    두 조각의 확률을 더하면 다음을 얻는다.

    $$
    0 \leq P(|X_n - c| > \varepsilon) \leq 1 - F_n(c + \varepsilon) + F_n(c - \varepsilon)
    $$

    **3단계: 극한을 취한다.** $c + \varepsilon > c$ 이므로 $F(c + \varepsilon) = 1$ 이고, $c - \varepsilon < c$ 이므로 $F(c - \varepsilon) = 0$ 이다. 두 점 모두 연속점이므로 분포수렴의 정의에서 다음이 성립한다.

    $$
    F_n(c + \varepsilon) \to F(c + \varepsilon) = 1, \qquad F_n(c - \varepsilon) \to F(c - \varepsilon) = 0
    $$

    따라서 2단계 오른쪽 값의 극한은 다음과 같다.

    $$
    \lim_{n \to \infty}\big[1 - F_n(c + \varepsilon) + F_n(c - \varepsilon)\big] = 1 - 1 + 0 = 0
    $$

    **4단계: 결론.** 조임 정리(샌드위치 정리)에 따라 다음을 얻는다.

    $$
    \lim_{n \to \infty} P(|X_n - c| > \varepsilon) = 0
    $$

    $\varepsilon > 0$ 은 아무렇게나 고른 것이었으므로 이는 곧 $X_n \xrightarrow{p} c$ 를 뜻한다.

    **뜻풀이.** 일반적으로 분포수렴은 확률수렴을 함의하지 않는다. 분포수렴은 $X_n$ 과 $X$ 를 **같은 표본공간 위에서 견주지 않고** 각자의 분포만 견주기 때문이다. 그런데 극한이 상수이면 사정이 다르다. "$X_n$ 의 분포가 점 $c$ 한 곳으로 몰린다"는 말이 곧 "$X_n$ 의 값이 $c$ 가까이에 있을 확률이 1로 간다"는 말이 되어, 견줄 상대인 $c$ 가 무작위가 아니므로 분포에 대한 정보가 그대로 값에 대한 정보가 된다.

    페이지에 나온 반례 $X \sim N(0,1)$, $X_n = -X$ 가 바로 이 자리에서 무너진다. 거기에서는 극한 $X$ 가 무작위여서 $X_n$ 과 $X$ 가 같은 분포를 가져도 값이 서로 멀리 떨어져 있을 수 있다. 큰수의 법칙이 주장하는 것은 상수 $\mu$ 로의 수렴이므로 이 정리가 바로 쓰인다. $\square$

---

**연습문제 2.**
다음 각각이 참인지 거짓인지 밝히고 간단히 근거를 대어라.

(a) 거의 확실한 수렴은 확률수렴을 함의한다.

(b) 분포수렴은 확률수렴을 함의한다.

(c) $X_n \xrightarrow{p} X$ 이고 $Y_n \xrightarrow{p} Y$ 이면 $X_n + Y_n \xrightarrow{p} X + Y$ 이다.

(d) $X_n \xrightarrow{d} X$ 이고 $Y_n \xrightarrow{d} Y$ 이면 $X_n + Y_n \xrightarrow{d} X + Y$ 이다.

??? success "연습문제 2 풀이"
    **(a) 참.** 이것이 수렴의 층계에서 첫 번째 화살표이다.

    $\varepsilon > 0$ 을 고정하고 $A = \{\omega : X_n(\omega) \to X(\omega)\}$ 라고 하자. 가정에서 $P(A) = 1$ 이다. $\omega \in A$ 이면 수렴의 정의에 따라 어떤 $N(\omega)$ 가 있어서 $n \geq N(\omega)$ 일 때 $|X_n(\omega) - X(\omega)| \leq \varepsilon$ 이다. 곧 $\omega$ 는 나쁜 사건 $B_n = \{|X_n - X| > \varepsilon\}$ 에 유한 번만 걸린다. 이를 사건으로 적으면 다음과 같다.

    $$
    P\left(\limsup_{n \to \infty} B_n\right) = P(B_n \text{ 이 무한히 자주 일어남}) = 0
    $$

    그런데 $B_n \subset \bigcup_{m \geq n} B_m$ 이고 이 합집합은 $n$ 에 대하여 줄어드는 집합열이므로 확률의 연속성에서 다음을 얻는다.

    $$
    P(B_n) \leq P\left(\bigcup_{m \geq n} B_m\right) \downarrow P\left(\limsup_{m} B_m\right) = 0
    $$

    따라서 $P(|X_n - X| > \varepsilon) \to 0$ 이며, 이것이 확률수렴이다.

    **(b) 거짓.** 화살표의 방향이 반대이다. 페이지에 있는 반례를 그대로 쓸 수 있다. $X \sim N(0,1)$ 에 대하여 모든 $n$ 에 대해 $X_n = -X$ 로 두면 대칭성에서 $X_n \sim N(0,1)$ 이므로 $X_n \xrightarrow{d} X$ 이다. 그러나 다음과 같다.

    $$
    P(|X_n - X| > \varepsilon) = P(2|X| > \varepsilon) = P\left(|X| > \frac{\varepsilon}{2}\right) > 0 \qquad \text{모든 } n
    $$

    이 값은 $n$ 에 전혀 기대지 않는 양수이므로 $0$ 으로 가지 않는다.

    **다만 극한이 상수이면 참이다.** 연습문제 1에서 보았듯이 $c$ 가 상수일 때에는 다음이 성립한다.

    $$
    X_n \xrightarrow{d} c \implies X_n \xrightarrow{p} c
    $$

    반례가 통했던 까닭은 극한 $X$ 가 **무작위**여서 분포가 같아도 값이 멀리 떨어질 수 있었기 때문이다. 극한이 한 점으로 퇴화하면 그런 여지가 없어진다.

    **(c) 참.** 핵심은 삼각부등식으로 얻는 다음 포함 관계이다. $|X_n + Y_n - (X+Y)| \leq |X_n - X| + |Y_n - Y|$ 이므로, 왼쪽이 $\varepsilon$ 보다 크려면 오른쪽 두 항 가운데 적어도 하나가 $\varepsilon/2$ 보다 커야 한다.

    $$
    \{|X_n + Y_n - (X + Y)| > \varepsilon\} \subset \left\{|X_n - X| > \frac{\varepsilon}{2}\right\} \cup \left\{|Y_n - Y| > \frac{\varepsilon}{2}\right\}
    $$

    합집합의 확률은 각 확률의 합을 넘지 않으므로 다음을 얻는다.

    $$
    P(|X_n + Y_n - (X+Y)| > \varepsilon) \leq P\left(|X_n - X| > \frac{\varepsilon}{2}\right) + P\left(|Y_n - Y| > \frac{\varepsilon}{2}\right) \to 0 + 0 = 0
    $$

    $X_n$ 과 $Y_n$ 사이의 독립성은 **전혀 필요하지 않다**. 확률수렴이 같은 표본공간 위에서 값끼리 견주는 수렴이기 때문에 이런 덧셈이 자유롭게 된다.

    **(d) 거짓.** (c)와 겉모습이 똑같은데 결론이 갈리는 것이 이 문제의 핵심이다.

    분포수렴은 $X_n$ 과 $Y_n$ 각각의 **주변분포**에 대한 정보만 준다. 그런데 합 $X_n + Y_n$ 의 분포는 주변분포만으로 정해지지 않고 둘의 **결합분포**에 달려 있다. 그러므로 주변분포의 극한만 알고서는 합의 극한을 말할 수 없다.

    **반례.** $Z \sim N(0,1)$ 이라 하고 모든 $n$ 에 대하여 다음과 같이 두자.

    $$
    X_n = Z, \qquad Y_n = -Z
    $$

    대칭성에서 $-Z \sim N(0,1)$ 이므로 두 수열 모두 $N(0,1)$ 로 분포수렴한다. 극한 확률변수로는 서로 **독립인** $X \sim N(0,1)$ 과 $Y \sim N(0,1)$ 을 잡자. 그러면 $X_n \xrightarrow{d} X$ 이고 $Y_n \xrightarrow{d} Y$ 이다. 그러나 합은 다음과 같다.

    $$
    X_n + Y_n = Z - Z = 0 \qquad \text{모든 } n
    $$

    곧 $X_n + Y_n \xrightarrow{d} 0$ 으로 한 점에 퇴화한다. 반면 극한끼리의 합은 독립인 정규확률변수의 합이므로 다음과 같다.

    $$
    X + Y \sim N(0, 2)
    $$

    $N(0,2)$ 는 퇴화분포가 아니므로 $X_n + Y_n \not\xrightarrow{d} X + Y$ 이다.

    **언제 참이 되는가.** 다음 가운데 하나가 더해지면 (d)도 성립한다.

    - 각 $n$ 에 대하여 $X_n$ 과 $Y_n$ 이 독립이고 $X$ 와 $Y$ 도 독립일 때. 이때에는 특성함수가 곱으로 갈라져 $\varphi_{X_n}(t)\varphi_{Y_n}(t) \to \varphi_X(t)\varphi_Y(t)$ 가 되고, 레비의 연속성 정리가 결론을 준다.
    - 한쪽 극한이 **상수**일 때, 곧 $Y_n \xrightarrow{p} c$ 일 때. 이것이 **슬러츠키 정리**이며 $X_n + Y_n \xrightarrow{d} X + c$ 를 준다. (c)와 (d)를 잇는 다리가 바로 여기이다. 연습문제 1에 따라 상수로의 분포수렴은 확률수렴과 같으므로, 상수 극한에서는 분포수렴도 (c)처럼 덧셈을 견뎌 낸다.

    **요약.**

    | | 주장 | 참·거짓 | 까닭 |
    |---|---|---|---|
    | (a) | a.s. $\implies$ p | 참 | 나쁜 사건이 유한 번만 일어남 |
    | (b) | d $\implies$ p | 거짓 | $X_n = -X$ (극한이 상수이면 참) |
    | (c) | p 는 덧셈에 닫혀 있음 | 참 | 삼각부등식 |
    | (d) | d 는 덧셈에 닫혀 있음 | 거짓 | 주변분포가 결합분포를 정하지 못함 |

    $\square$
