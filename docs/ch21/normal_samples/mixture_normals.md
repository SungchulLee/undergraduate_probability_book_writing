# 서로 다른 두 정규분포에서 뽑은 표본

## 정규분포 표본 만들기

$N(\mu, \sigma^2)$ 에서 표본을 만들려면 표준적인 변환을 쓴다. $Z \sim N(0,1)$ 이면 다음이 성립한다.

$$
X = \mu + \sigma Z \sim N(\mu, \sigma^2)
$$

MATLAB에서 `randn(1, n)` 은 표준정규분포 표본 $n$ 개를 만드므로, `mu + sigma * randn(1, n)` 은 $N(\mu, \sigma^2)$ 에서 표본을 만든다.

## 예: 두 정규분포의 혼합

$N(1, 1)$ 에서 표본 600개를, $N(4, 1)$ 에서 표본 400개를 만든 뒤 이를 한데 모아 1000개짜리 자료를 만들어 보자.

**MATLAB:**

```matlab
clear all; close all; clc; rng('default')

% N(mu1, si1) 에서 표본 n1 개
n1 = 600;
mu1 = 1; si1 = 1;
x1 = mu1 + si1 * randn(1, n1);
subplot(131)
hist(x1)

% N(mu2, si2) 에서 표본 n2 개
n2 = 400;
mu2 = 4; si2 = 1;
x2 = mu2 + si2 * randn(1, n2);
subplot(132)
hist(x2)

% 서로 다른 두 정규분포에서 뽑은 표본
x = [x1 x2];
subplot(133)
hist(x)
```

**파이썬:**

```python
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)

# N(1, 1) 에서 표본 600 개
n1 = 600; mu1 = 1; si1 = 1
x1 = mu1 + si1 * np.random.randn(n1)

# N(4, 1) 에서 표본 400 개
n2 = 400; mu2 = 4; si2 = 1
x2 = mu2 + si2 * np.random.randn(n2)

# 한데 모은 표본
x = np.concatenate([x1, x2])

fig, axes = plt.subplots(1, 3, figsize=(14, 4))

axes[0].hist(x1, bins=20, edgecolor='black')
axes[0].set_title(f'600 samples from $N({mu1}, {si1}^2)$')

axes[1].hist(x2, bins=20, edgecolor='black')
axes[1].set_title(f'400 samples from $N({mu2}, {si2}^2)$')

axes[2].hist(x, bins=20, edgecolor='black')
axes[2].set_title('Combined 1000 samples')

plt.tight_layout()
plt.show()
```

## 혼합분포

한데 모은 히스토그램은 **혼합분포**의 한 예이다. 혼합분포의 밀도는 다음과 같다.

$$
f(x) = w_1 \, f_1(x) + w_2 \, f_2(x)
$$

여기에서 $w_1 = \frac{n_1}{n_1 + n_2} = 0.6$, $w_2 = 0.4$ 이고 $f_i$ 는 $N(\mu_i, \sigma_i^2)$ 의 밀도이다.

이렇게 얻은 히스토그램은 봉우리가 둘인 모양을 띤다. 이는 성분들의 평균이 표준편차에 견주어 충분히 떨어져 있을 때 혼합분포가 보이는 특징적인 모습이다.

## 연습문제

**연습문제 1.**
**메트로폴리스 알고리즘**은 무작위로 옮겨 갈 곳을 제안하고 이를 받아들이거나 물리치는 방식으로 어떤 분포에서 표본을 만든다.

**(a)** $N(x_{\text{현재}}, \sigma^2)$ 을 제안분포로 써서 $\mathbb{R}$ 위의 $f(x) \propto e^{-|x|^3}$ 에서 표본을 뽑는 메트로폴리스 알고리즘을 구현하여라.

**(b)** 길이 $50{,}000$ 의 사슬을 만들어라. 자취 그림과 히스토그램을 그려라.

**(c)** $\sigma = 0.1, 1, 5$ 로 바꾸어 실험하여라. 제안의 눈금이 섞임에 어떤 영향을 주는가?

??? success "연습문제 1 풀이"
    현재 자리 $x$ 에서 $x' \sim N(x, \sigma^2)$ 을 제안한다. 제안분포가 대칭이어서 $q(x' \mid x) = q(x \mid x')$ 이므로 메트로폴리스–헤이스팅스 비는 목표밀도의 비만 남는다.

    $$
    \alpha(x, x') = \min\left(1, \frac{f(x')}{f(x)}\right) = \min\left(1, \, e^{-(|x'|^3 - |x|^3)}\right)
    $$

    여기에서 정규화상수는 약분되어 사라진다. 이것이 메트로폴리스 알고리즘의 힘이다. 밀도의 모양만 알면 $\int e^{-|x|^3}dx$ 를 구하지 않고도 표본을 만들 수 있다. 실제 구현에서는 넘침을 막으려고 로그를 취해 $\ln U < -(|x'|^3 - |x|^3)$ 을 견준다.

    ```python
    import numpy as np
    from math import gamma
    from scipy.integrate import quad

    np.random.seed(42)

    # (a) 목표밀도 f(x) ~ exp(-|x|^3), 제안분포는 N(x_current, sigma^2)
    def metropolis(sigma, n_chain=50000, x0=0.0):
        chain = np.empty(n_chain)
        x = x0
        n_accept = 0
        for t in range(n_chain):
            x_new = x + sigma * np.random.randn()
            # 제안분포가 대칭이므로 채택비는 f(x')/f(x) 뿐이다
            log_ratio = -(abs(x_new)**3 - abs(x)**3)
            if np.log(np.random.random()) < log_ratio:
                x = x_new
                n_accept += 1
            chain[t] = x
        return chain, n_accept / n_chain

    # (b) 길이 50,000 의 사슬 (앞의 5,000 개는 버린다)
    chain, acc = metropolis(sigma=1.5)
    burn = 5000
    x = chain[burn:]
    print(f"sigma = 1.5 : acceptance rate = {acc:.4f}")
    print(f"  chain mean = {x.mean():.4f},  chain sd = {x.std():.4f}")

    # 정규화상수 Z = int exp(-|x|^3) dx = 2*Gamma(4/3)
    Z, _ = quad(lambda t: np.exp(-abs(t)**3), -np.inf, np.inf)
    sd_exact = np.sqrt(quad(lambda t: t**2 * np.exp(-abs(t)**3), -np.inf, np.inf)[0] / Z)
    print(f"  Z = {Z:.6f}  (2*Gamma(4/3) = {2*gamma(4/3):.6f})")
    print(f"  target mean = 0.0000,  target sd = {sd_exact:.4f}")

    # (c) 제안의 눈금을 바꾸어 본다
    print()
    for s in [0.1, 1.0, 1.5, 5.0]:
        ch, a = metropolis(sigma=s)
        y = ch[burn:]
        # 1차 자기상관: 섞임이 좋을수록 0 에 가깝다
        r1 = np.corrcoef(y[:-1], y[1:])[0, 1]
        print(f"sigma = {s:4.1f} : acceptance = {a:.4f}, mean = {y.mean():7.4f}, "
              f"sd = {y.std():.4f}, lag-1 autocorr = {r1:.4f}")

    # (b) 그림: 자취 그림과 히스토그램
    import matplotlib.pyplot as plt
    xs = np.linspace(-2.5, 2.5, 400)
    fig, axes = plt.subplots(1, 2, figsize=(12, 4.5))
    axes[0].plot(chain[:2000], linewidth=0.7)
    axes[0].set_xlabel('iteration'); axes[0].set_ylabel('x')
    axes[0].set_title('Trace plot (sigma = 1.5, first 2000 steps)')
    axes[1].hist(x, bins=60, density=True, edgecolor='black', alpha=0.7,
                 label='Metropolis samples')
    axes[1].plot(xs, np.exp(-np.abs(xs)**3) / Z, '-r', linewidth=2, label='Target density')
    axes[1].set_xlabel('x'); axes[1].legend()
    axes[1].set_title('Histogram vs. target density')
    plt.tight_layout()
    plt.show()
    ```

    **실행 결과:**
    ```
    sigma = 1.5 : acceptance rate = 0.4571
      chain mean = 0.0008,  chain sd = 0.6145
      Z = 1.785959  (2*Gamma(4/3) = 1.785959)
      target mean = 0.0000,  target sd = 0.6110

    sigma =  0.1 : acceptance = 0.9567, mean = -0.0087, sd = 0.6018, lag-1 autocorr = 0.9875
    sigma =  1.0 : acceptance = 0.5893, mean =  0.0106, sd = 0.6116, lag-1 autocorr = 0.6445
    sigma =  1.5 : acceptance = 0.4562, mean =  0.0056, sd = 0.6114, lag-1 autocorr = 0.6233
    sigma =  5.0 : acceptance = 0.1576, mean = -0.0032, sd = 0.6111, lag-1 autocorr = 0.8248
    ```

    **(b)** $\sigma = 1.5$ 로 만든 사슬의 채택률은 $0.4571$ 이다. 표본평균 $0.0008$ 과 표준편차 $0.6145$ 는 목표분포의 참값 $0$ 과 $0.6110$ 에 잘 맞는다. 여기에서 참값을 구할 때 쓴 정규화상수는 $t = |x|^3$ 로 바꾸면 감마함수로 나온다.

    $$
    Z = \int_{-\infty}^{\infty} e^{-|x|^3}\,dx = 2\int_0^\infty e^{-x^3}\,dx = \frac{2}{3}\Gamma\!\left(\frac{1}{3}\right) = 2\,\Gamma\!\left(\frac{4}{3}\right) \approx 1.785959
    $$

    `scipy.integrate.quad` 로 구한 값도 소수점 여섯 자리까지 이와 같다. 자취 그림은 한자리에 오래 머무르거나 멀리 튀어 나가는 일 없이 $0$ 을 중심으로 고르게 오르내리며, 히스토그램은 $f(x)/Z$ 로 정규화한 목표밀도(빨간 곡선)와 거의 포개진다. 지수의 $|x|^3$ 때문에 꼬리가 정규분포보다 더 빨리 죽어 종 모양보다 어깨가 각지고 꼬리가 짧은 모습이 된다.

    **(c)** 제안의 눈금 $\sigma$ 는 채택률을 통해 섞임을 좌우한다.

    - $\sigma = 0.1$: 제안이 너무 작아 거의 다 받아들여지지만($0.9567$) 한 걸음의 폭이 작다. 1차 자기상관이 $0.9875$ 로 사슬이 제자리를 맴돈다.
    - $\sigma = 5$: 제안이 너무 커서 대부분 밀도가 거의 0인 곳으로 튀므로 $84\%$ 가 물리쳐진다. 받아들여지지 않으면 사슬은 같은 값에 머무르므로 자기상관이 다시 $0.8248$ 로 올라간다.
    - $\sigma = 1 \sim 1.5$: 채택률이 $0.45 \sim 0.59$ 로 알맞고 자기상관도 $0.62$ 안팎으로 가장 낮다. 곧 섞임이 가장 좋다.

    이처럼 채택률은 높을수록 좋은 것이 아니다. 너무 높으면 잘게 기고, 너무 낮으면 멈춰 선다. 1차원 문제에서 채택률이 대략 $0.2$ 에서 $0.5$ 사이에 들도록 $\sigma$ 를 맞추는 것이 경험에서 얻은 요령이며, 위의 표가 그 까닭을 보여 준다. 눈여겨볼 점은 세 경우 모두 표본평균과 표준편차는 옳은 값으로 모인다는 것이다. 사슬은 어느 눈금에서도 목표분포로 수렴한다. 다만 같은 정확도를 얻는 데 드는 반복 횟수가 달라질 뿐이다. $\square$
