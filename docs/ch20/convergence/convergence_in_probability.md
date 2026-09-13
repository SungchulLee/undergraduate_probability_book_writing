# 확률수렴

## 정의

확률변수열 $X_1, X_2, \ldots$ 가 모든 $\varepsilon > 0$ 에 대하여 다음을 만족하면 확률변수 $X$ 로 **확률수렴한다**고 한다.

$$
\lim_{n \to \infty} P(|X_n - X| > \varepsilon) = 0
$$

이를 다음과 같이 적는다.

$$
X_n \xrightarrow{p} X
$$

## 뜻풀이

확률수렴은 허용오차 $\varepsilon > 0$ 을 아무리 작게 잡아도 $X_n$ 이 $X$ 에서 $\varepsilon$ 보다 더 벗어날 확률이 $n \to \infty$ 일 때 사라진다는 뜻이다. 달리 말하면 크게 벗어나는 일이 점점 더 일어나기 어려워진다는 것이지, 유한한 $n$ 에 대하여 그런 일이 아예 없다는 뜻은 아니다.

## 예: 표본평균

$X_1, X_2, \ldots$ 가 평균 $\mu$, 분산 $\sigma^2 < \infty$ 인 i.i.d. 확률변수라고 하자. 표본평균 $\bar{X}_n = \frac{1}{n}\sum_{i=1}^n X_i$ 는 다음을 만족한다.

$$
\bar{X}_n \xrightarrow{p} \mu
$$

이것이 바로 **큰수의 약법칙**의 서술이다.

## 분포수렴과의 관계

확률수렴은 분포수렴을 함의한다.

$$
X_n \xrightarrow{p} X \implies X_n \xrightarrow{d} X
$$

그 역은 일반적으로 거짓이지만, 극한이 **상수** $c$ 인 경우에는 참이다.

$$
X_n \xrightarrow{d} c \iff X_n \xrightarrow{p} c
$$

## 연습문제

**연습문제 1.** $X_n \sim \text{Uniform}(0, 1/n)$ 이라고 하자. $X_n \xrightarrow{p} 0$ 임을 보여라.

??? success "연습문제 1 풀이"
    임의의 $\varepsilon > 0$ 에 대하여 $P(|X_n| > \varepsilon) = P(X_n > \varepsilon) = \max(0, 1 - n\varepsilon)$ 이고, $n \to \infty$ 일 때 이 값은 0으로 간다($n > 1/\varepsilon$ 이 되는 순간부터 0이다).

    따라서 $X_n \xrightarrow{p} 0$ 이다. $\square$

---

**연습문제 2.** 확률수렴이 분포수렴을 함의함을 증명하여라.

??? success "연습문제 2 풀이"
    $X_n \xrightarrow{p} X$ 이고 $x$ 가 $F_X$ 의 연속점이라고 하자. 임의의 $\varepsilon > 0$ 에 대하여 다음이 성립한다.

    $$
    P(X_n \leq x) \leq P(X \leq x + \varepsilon) + P(|X_n - X| > \varepsilon)
    $$

    $$
    P(X_n \leq x) \geq P(X \leq x - \varepsilon) - P(|X_n - X| > \varepsilon)
    $$

    $n \to \infty$ 로 보내면 $P(|X_n - X| > \varepsilon) \to 0$ 이므로 $F_X(x - \varepsilon) \leq \liminf F_{X_n}(x) \leq \limsup F_{X_n}(x) \leq F_X(x + \varepsilon)$ 을 얻는다. 연속점에서 $\varepsilon \to 0$ 으로 보내면 $F_{X_n}(x) \to F_X(x)$ 이다. $\square$

---

**연습문제 3.** $X_n \xrightarrow{p} 0$ 이지만 $X_n$ 이 0으로 거의 확실하게 수렴하지는 **않는** 예를 들어라.

??? success "연습문제 3 풀이"
    $X_n = \mathbf{1}_{A_n}$ 이라 하고, 사건 $A_n$ 을 $P(A_n) = 1/\lceil\log_2 n\rceil$ 이면서 $A_n$ 이 $\Omega$ 의 여러 부분을 돌아가며 훑도록 잡는다. 좀 더 구체적으로는 $[0,1]$ 을 여러 덩어리로 나누고 지시함수가 그 덩어리들을 차례로 돌게 만든다. 그러면 $P(|X_n| > 0.5) = P(A_n) \to 0$ 이므로 확률수렴하지만, 거의 모든 $\omega$ 에 대하여 $X_n(\omega) = 1$ 이 무한히 자주 일어나므로 $X_n \not\to 0$ (a.s.)이다.

    구체적인 만듦새는 다음과 같다. 르베그 측도를 준 $[0,1]$ 위에서, $n$ 을 $n = k(k-1)/2 + j$ 로 쪼갠 뒤 $A_n$ 을 $j/k$ 에서 시작하는 길이 $1/k$ 의 구간으로 잡으면, 구간이 점점 더 빠르게 돌아간다.

---

**연습문제 4.** $X_1, X_2, \ldots$ 가 $E[X_i] = \mu$, $\text{Var}(X_i) = \sigma^2$ 인 i.i.d. 확률변수라고 하자. 체비쇼프 부등식을 써서 $\bar{X}_n \xrightarrow{p} \mu$ 임을 증명하여라.

??? success "연습문제 4 풀이"
    $E[\bar{X}_n] = \mu$ 이고 $\text{Var}(\bar{X}_n) = \sigma^2/n$ 이다. 체비쇼프 부등식에 따라 다음이 성립한다.

    $$
    P(|\bar{X}_n - \mu| > \varepsilon) \leq \frac{\sigma^2}{n\varepsilon^2} \to 0
    $$

    이는 $n \to \infty$ 일 때의 결과이다. 이것이 바로 큰수의 약법칙의 증명이다. $\square$

---

**연습문제 5.** $X_n \xrightarrow{p} X$ 이고 $g$ 가 연속함수이면 $g(X_n) \xrightarrow{p} g(X)$ 임을 증명하여라.

??? success "연습문제 5 풀이"
    임의의 $\varepsilon > 0$ 과 $\delta > 0$ 에 대하여, $g$ 가 $X(\omega)$ 에서 연속이므로 $|x - X(\omega)| < \eta \implies |g(x) - g(X(\omega))| < \varepsilon$ 을 만족하는 $\eta > 0$ 이 있다. 그러면 다음이 성립한다.

    $$
    P(|g(X_n) - g(X)| > \varepsilon) \leq P(|X_n - X| > \eta) + P(g \text{ 가 해당 집합에서 균등연속이 아님})
    $$

    첫째 항은 확률수렴에 따라 $\to 0$ 이다. 엄밀한 증명에서는 임의의 $\delta > 0$ 에 대하여 $M$ 이 크면 $P(|X| > M) < \delta$ 라는 사실과, $g$ 가 $[-M, M]$ 위에서 균등연속이라는 사실을 쓴다. $\square$
