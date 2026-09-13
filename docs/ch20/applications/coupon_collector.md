# 쿠폰 모으기 문제

## 문제 설정

서로 다른 종류의 쿠폰이 $n$ 가지 있다고 하자(이를테면 어린이 세트에 들어 있는 장난감). 세트를 하나 살 때마다 쿠폰 하나를 고르게 무작위로 받는다. $T_n$ 을 $n$ 가지를 **모두** 모으는 데 필요한 전체 구매 횟수라고 하자.

**주장**: $n \to \infty$ 일 때 다음이 성립한다.

$$
\frac{T_n}{n \log n} \xrightarrow{p} 1
$$

## 쪼개기

서로 다른 쿠폰을 $i-1$ 가지 모은 뒤 $i$ 번째 **새로운** 쿠폰을 얻는 데 더 필요한 구매 횟수를 $\tau_i$ 라고 하자. 그러면 다음과 같다.

**1. 쪼개기:**

$$
T_n = \sum_{i=1}^n \tau_i
$$

**2. 분포:** 서로 다른 쿠폰을 $i-1$ 가지 가지고 있을 때 새 쿠폰을 얻을 확률은 $\frac{n-(i-1)}{n}$ 이다. 그러므로 다음이 성립한다.

$$
\tau_i \sim \text{Geo}\left(\frac{n-(i-1)}{n}\right)
$$

**3. 독립성:** $\tau_i$ 들은 독립이다(새 쿠폰을 얻는 순간 각 단계가 새로 시작한다).

## 1단계: 평균 구하기

$$
\mathbb{E}T_n = \sum_{i=1}^n \mathbb{E}\tau_i = \sum_{i=1}^n \frac{n}{n-(i-1)} = n\left(1 + \frac{1}{2} + \frac{1}{3} + \cdots + \frac{1}{n}\right) = nH_n
$$

여기에서 $H_n = \sum_{k=1}^n \frac{1}{k}$ 은 $n$ 번째 조화수이다. $H_n \sim \log n$ 이므로 다음이 성립한다.

$$
\mathbb{E}T_n \sim n \log n
$$

## 2단계: 분산 구하기

$$
Var(T_n) = \sum_{i=1}^n Var(\tau_i) = \sum_{i=1}^n \frac{1 - p_i}{p_i^2} \leq \sum_{i=1}^n \frac{n^2}{(n-i+1)^2} = n^2 \sum_{k=1}^n \frac{1}{k^2} \leq Cn^2
$$

$\sum_{k=1}^{\infty} 1/k^2 = \pi^2/6 < \infty$ 이기 때문이다.

## 3단계: 체비쇼프 부등식 적용하기

$a_n = n\log n$ 으로 고르자. 그러면 임의의 $\varepsilon > 0$ 에 대하여 다음이 성립한다.

$$
P\left(\left|\frac{T_n - \mathbb{E}T_n}{a_n}\right| > \varepsilon\right) \leq \frac{Var(T_n)}{\varepsilon^2 a_n^2} \leq \frac{Cn^2}{\varepsilon^2 (n\log n)^2} = \frac{C}{\varepsilon^2 (\log n)^2} \to 0
$$

또한 $\mathbb{E}T_n / a_n \to 1$ 임도 필요하다.

$$
\frac{\mathbb{E}T_n}{n\log n} = \frac{nH_n}{n\log n} = \frac{H_n}{\log n} \to 1
$$

이 두 사실을 합치면 다음을 얻는다.

$$
\frac{T_n}{n\log n} = \frac{T_n - \mathbb{E}T_n}{n\log n} + \frac{\mathbb{E}T_n}{n\log n} \xrightarrow{p} 0 + 1 = 1
$$

## 뜻풀이

쿠폰 $n$ 가지를 모두 모으려면 대략 $n\ln n$ 번을 사야 한다. 이를테면 쿠폰이 $n = 100$ 가지라면 모두 모으는 데 약 $100 \times \ln(100) \approx 461$ 번 사야 하리라고 기대한다.

## 연습문제

**연습문제 1.**
쿠폰이 $n = 50$ 가지인 쿠폰 모으기 문제에서 기댓값 $E[T_{50}]$ 을 정확히 셈하고, 체비쇼프 부등식을 써서 $P(|T_{50} - E[T_{50}]| > 100)$ 의 상계를 구하여라.
