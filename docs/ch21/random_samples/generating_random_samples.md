# 확률표본을 어떻게 만드는가

## 개요

모의실험은 확률과 통계에서 힘이 센 도구이다. 알고 있는 분포에서 확률표본을 만들어 내면 확률적인 현상을 살펴보고, 이론적인 결과를 확인하고, 해석적으로 풀기 어려운 문제를 풀 수 있다.

대부분의 프로그래밍 환경은 난수를 만드는 함수를 갖추고 있다. MATLAB에서 가장 기본이 되는 난수 발생기는 다음과 같다.

| 함수 | 설명 |
|----------|-------------|
| `rand` | $[0, 1]$ 위의 균등분포 — $U(0,1)$ 표본을 만든다 |
| `randn` | 표준정규분포 — $N(0,1)$ 표본을 만든다 |
| `randi` | $\{1, 2, \ldots, N\}$ 위의 균등분포 |
| `randperm` | $\{1, 2, \ldots, N\}$ 의 무작위 순열 |

## `random` 함수

더 일반적인 분포를 위해 MATLAB은 `random` 함수를 제공한다.

```matlab
x = random('Dist', Pa1*ones(n,m), Pa2*ones(n,m))
```

이는 모수가 `Pa1`, `Pa2` 인 주어진 분포에서 $n \times m$ 크기의 표본 행렬을 만든다. 분포 이름과 그에 맞는 모수는 `help random` 으로 자세히 볼 수 있다.

## 난수 발생기 다루기

같은 결과를 다시 얻으려면 난수 발생기(RNG)의 상태를 다루는 일이 중요하다.

| 명령 | 설명 |
|---------|-------------|
| `rng('default')` | 난수 발생기를 기본 초기 상태로 되돌린다 |
| `rng(n)` | 씨앗값 `n` 으로 난수 발생기를 되돌린다 |

씨앗값을 정해 두면 언제 돌리든 똑같은 "무작위" 수열이 만들어지며, 이는 오류를 찾거나 실험을 그대로 되풀이할 때 꼭 필요하다.

## 파이썬에서는

파이썬(NumPy)에서 이에 대응하는 함수들은 다음과 같다.

```python
import numpy as np

# 같은 결과를 다시 얻기 위해 씨앗값을 정한다
np.random.seed(0)
# 또는 더 새로운 Generator API 를 쓴다:
rng = np.random.default_rng(seed=0)

# [0, 1] 위의 균등분포
U = np.random.rand(n, m)        # 또는 rng.random((n, m))

# 표준정규분포 N(0, 1)
Z = np.random.randn(n, m)       # 또는 rng.standard_normal((n, m))

# {1, 2, ..., N} 위의 균등분포
X = np.random.randint(1, N+1, size=(n, m))  # 또는 rng.integers(1, N+1, size=(n, m))

# {0, 1, ..., N-1} 의 무작위 순열
perm = np.random.permutation(N)  # 또는 rng.permutation(N)
```

일반적인 분포를 위해 NumPy는 `np.random.binomial`, `np.random.poisson`, `np.random.exponential` 을 비롯한 여러 함수를 제공한다.

## 연습문제

**연습문제 1.**
**기각법**은 모든 $x$ 에 대하여 $f(x) \leq Mg(x)$ 가 되는 제안밀도 $g(x)$ 와 상수 $M$ 을 써서 목표밀도 $f(x)$ 에서 표본을 만든다.

**(a)** $g(x) = \frac{1}{2}$ ($[-1,1]$ 위의 균등분포)을 써서 $[-1, 1]$ 위의 $f(x) = \frac{3}{2}(1 - x^2)$ 에서 표본을 만드는 기각 표집을 구현하여라. 가장 알맞은 $M$ 은 무엇인가?

**(b)** 표본 $10{,}000$ 개를 만들어 히스토그램을 참밀도와 함께 그려라.

**(c)** 제안된 값 가운데 받아들여지는 비율은 얼마인가? $1/M$ 과 견주어 보아라.

??? success "연습문제 1 풀이"
    ```python
    import numpy as np

    np.random.seed(42)

    def rejection_sampling(n_samples=10000):
        M = 1.5
        samples = []
        n_proposed = 0
        while len(samples) < n_samples:
            x = np.random.uniform(-1, 1)
            u = np.random.uniform()
            fx = 1.5 * (1 - x**2)
            gx = 0.5
            if u <= fx / (M * gx):
                samples.append(x)
            n_proposed += 1
        acceptance_rate = n_samples / n_proposed
        return np.array(samples), acceptance_rate

    samples_rej, acc_rate = rejection_sampling()
    print(f"Acceptance rate = {acc_rate:.4f} (theory 1/M = {1/1.5:.4f})")
    ```

---

**연습문제 2.**
**(a)** 역누적분포함수 방법을 써서 $x \geq 0$ 에서 누적분포함수가 $F(x) = 1 - e^{-x^2}$ 인 분포에서 표본을 만들어라.

**(b)** 표본 $10{,}000$ 개를 만들어 모의실험으로 평균과 분산을 확인하여라. $E[X]$ 와 $\text{Var}(X)$ 를 수치로 구하여라.

**(c)** 히스토그램을 참확률밀도함수 $f(x) = 2xe^{-x^2}$ 과 함께 그려라.

??? success "연습문제 2 풀이"
    $U \sim U(0,1)$ 일 때 $X = F^{-1}(U)$ 가 누적분포함수 $F$ 를 따른다는 것이 역변환 표집의 뼈대이다. 여기에서는 $u = 1 - e^{-x^2}$ 을 $x$ 에 대하여 풀면 된다.

    $$
    e^{-x^2} = 1 - u \quad \Longrightarrow \quad x^2 = -\ln(1-u) \quad \Longrightarrow \quad F^{-1}(u) = \sqrt{-\ln(1-u)}
    $$

    이 분포는 $\sigma = 1/\sqrt{2}$ 인 레일리분포이다. 밀도는 $f(x) = F'(x) = 2xe^{-x^2}$ 이고, 적률은 $t = x^2$ 로 바꾸면 감마함수로 바로 나온다.

    $$
    E[X] = \int_0^\infty 2x^2 e^{-x^2}\,dx = \frac{\sqrt{\pi}}{2} \approx 0.8862, \qquad E[X^2] = \int_0^\infty 2x^3 e^{-x^2}\,dx = 1
    $$

    따라서 $\text{Var}(X) = 1 - \pi/4 \approx 0.2146$ 이다.

    ```python
    import numpy as np

    np.random.seed(42)

    # (a) F(x) = 1 - exp(-x^2) 의 역함수: F^{-1}(u) = sqrt(-ln(1-u))
    def inverse_cdf_sample(n_samples=10000):
        u = np.random.uniform(size=n_samples)
        return np.sqrt(-np.log(1 - u))

    # (b) 표본 10,000 개로 평균과 분산을 확인한다
    samples = inverse_cdf_sample(10000)
    mean_exact = np.sqrt(np.pi) / 2          # E[X] = sqrt(pi)/2
    var_exact = 1 - np.pi / 4                # Var(X) = 1 - pi/4
    print(f"Sample mean     = {samples.mean():.4f}   (exact {mean_exact:.4f})")
    print(f"Sample variance = {samples.var(ddof=1):.4f}   (exact {var_exact:.4f})")

    # 수치적분으로 E[X], E[X^2] 를 다시 확인한다
    from scipy.integrate import quad
    m1, _ = quad(lambda x: x * 2 * x * np.exp(-x**2), 0, np.inf)
    m2, _ = quad(lambda x: x**2 * 2 * x * np.exp(-x**2), 0, np.inf)
    print(f"Numerical E[X]  = {m1:.4f},  E[X^2] = {m2:.4f},  Var = {m2 - m1**2:.4f}")

    # (c) 히스토그램과 참밀도 f(x) = 2x exp(-x^2)
    import matplotlib.pyplot as plt
    xs = np.linspace(0, 3, 300)
    plt.figure(figsize=(7, 5))
    plt.hist(samples, bins=50, density=True, edgecolor='black', alpha=0.7,
             label='Samples')
    plt.plot(xs, 2 * xs * np.exp(-xs**2), '-r', linewidth=2, label='True pdf')
    plt.xlabel('x'); plt.ylabel('density'); plt.legend(); plt.grid(True)
    plt.show()
    ```

    **실행 결과:**
    ```
    Sample mean     = 0.8763   (exact 0.8862)
    Sample variance = 0.2097   (exact 0.2146)
    Numerical E[X]  = 0.8862,  E[X^2] = 1.0000,  Var = 0.2146
    ```

    표본평균 $0.8763$ 은 참값 $\sqrt{\pi}/2 = 0.8862$ 와, 표본분산 $0.2097$ 은 참값 $1 - \pi/4 = 0.2146$ 과 잘 맞는다. 표본평균의 표준오차가 $\sqrt{0.2146/10000} \approx 0.0046$ 이므로 $0.01$ 정도의 차이는 표집오차의 범위 안에 있다. 수치적분으로 얻은 $E[X] = 0.8862$, $E[X^2] = 1.0000$ 은 위에서 손으로 구한 값과 소수점 네 자리까지 일치한다.

    히스토그램은 $x = 1/\sqrt{2} \approx 0.707$ 에서 봉우리를 이루고 오른쪽으로 꼬리를 끄는 모양이 되며, 빨간 곡선으로 겹쳐 그린 참밀도 $f(x) = 2xe^{-x^2}$ 와 거의 포개진다. 균등난수 하나만 있으면 이렇게 꼬리가 있는 분포도 닫힌 꼴의 역함수 한 줄로 만들어 낼 수 있다. $\square$
