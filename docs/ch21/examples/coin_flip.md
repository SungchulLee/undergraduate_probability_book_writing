# 균등표본으로 동전 던지기

## 균등분포에서 베르누이분포로

가장 기본이 되는 모의실험 기법 가운데 하나는 균등확률변수에서 베르누이확률변수를 만들어 내는 것이다. $U \sim U(0,1)$ 과 성공확률 $p \in [0,1]$ 이 주어졌을 때 다음과 같이 정의한다.

$$
B = \begin{cases} 1 & U > 1 - p \text{ 일 때} \\ 0 & U \leq 1 - p \text{ 일 때} \end{cases}
$$

$P(B = 1) = P(U > 1-p) = p$ 이므로 $B \sim \text{Bernoulli}(p)$ 이다.

## 예

$[0,1]$ 에서 균등표본 $U_i$ 를 5개 만들고, 성공률 $p = 0.499$ 인 베르누이표본 $B_i$ 로 바꾸어 보자.

**MATLAB:**

```matlab
clear all; close all; clc; rng('default')

n = 5; p = 0.499;

% 균등표본 n 개
U = rand(1, n)

% 베르누이표본 B(p) n 개
B = U; B(U <= 1-p) = 0; B(U > 1-p) = 1
```

**실행 결과:**

```
U =
    0.8147    0.9058    0.1270    0.9134    0.6324

B =
    1    1    0    1    1
```

$1 - p = 0.501$ 이므로 $U_3 = 0.1270$ 만이 문턱값 아래에 놓이고, 그래서 $B_3 = 0$ 이며 나머지는 모두 1이다.

**파이썬:**

```python
import numpy as np

np.random.seed(0)

n = 5
p = 0.499

# 균등표본 n 개
U = np.random.rand(n)
print("U =", U)

# 베르누이표본 n 개
B = (U > 1 - p).astype(int)
print("B =", B)
```

## 왜 이렇게 되는가

이 기법은 **역변환 방법**의 한 예이다. 베르누이($p$) 확률변수의 누적분포함수는 다음과 같다.

$$
F(x) = \begin{cases} 0 & x < 0 \\ 1 - p & 0 \leq x < 1 \\ 1 & x \geq 1 \end{cases}
$$

$B = \mathbf{1}(U > 1 - p)$ 로 두는 것은 $U$ 에 $F$ 의 일반화된 역함수를 적용하는 것과 같다. 이 원리는 그대로 일반화된다. 어떤 분포든 역누적분포함수를 거치면 균등확률변수에서 표본을 뽑을 수 있다(확률적분변환을 보아라).

## 연습문제

**연습문제 1.**
$U_1, U_2, \ldots$ 를 i.i.d. $\text{Uniform}(0, 1)$ 이라고 하자. $N = \min\{n : U_1 + U_2 + \cdots + U_n > 1\}$ 로 정의한다. $E[N] = e$ 임이 알려져 있다.

**(a)** $10{,}000$ 번의 시행으로 $E[N]$ 을 어림하는 모의실험을 짜라.

**(b)** 어림값과 그 표준오차를 보고하여라. $e \approx 2.71828$ 과 견주어 보아라.

**(c)** 그때까지의 어림값 $\hat{e}_k = \frac{1}{k}\sum_{i=1}^{k} N_i$ 를 $k$ 에 대한 함수로 그려라.

??? success "연습문제 1 풀이"
    ```python
    import numpy as np

    np.random.seed(42)

    def estimate_e(n_trials=10000):
        Ns = []
        for _ in range(n_trials):
            total, n = 0, 0
            while total <= 1:
                total += np.random.uniform()
                n += 1
            Ns.append(n)
        return np.array(Ns)

    Ns = estimate_e()
    print(f"E[N] approx {np.mean(Ns):.5f} (true e = {np.e:.5f})")
    print(f"SE = {np.std(Ns)/np.sqrt(len(Ns)):.5f}")
    ```
