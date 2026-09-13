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

---

**연습문제 2.**
다음 각각이 참인지 거짓인지 밝히고 간단히 근거를 대어라.

(a) 거의 확실한 수렴은 확률수렴을 함의한다.

(b) 분포수렴은 확률수렴을 함의한다.

(c) $X_n \xrightarrow{p} X$ 이고 $Y_n \xrightarrow{p} Y$ 이면 $X_n + Y_n \xrightarrow{p} X + Y$ 이다.

(d) $X_n \xrightarrow{d} X$ 이고 $Y_n \xrightarrow{d} Y$ 이면 $X_n + Y_n \xrightarrow{d} X + Y$ 이다.
