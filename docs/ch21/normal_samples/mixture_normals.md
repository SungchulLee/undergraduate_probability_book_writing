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
x2 = mu2 + si1 * randn(1, n2);
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
