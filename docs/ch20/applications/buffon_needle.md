# 뷔퐁의 바늘

## 문제 설정

종이 위에 **1만큼 떨어진** 평행한 가로줄들을 긋는다. **길이가 1**인 바늘을 그 위에 무작위로 떨어뜨린다. 바늘의 위치는 다음 둘로 정해진다.

- $Y$: 아래쪽 끝의 높이로 $[0, 1]$ 위에서 균등분포를 따른다.
- $\Theta$: 바늘이 가로 방향과 이루는 각으로 $[0, \pi]$ 위에서 균등분포를 따른다.

위쪽 끝의 높이는 $Y + \sin\Theta$ 이다.

바늘이 ($y = 1$ 에 있는) **선을 가로지를** 필요충분조건은 $Y + \sin\Theta \geq 1$ 이다.

## 가로지를 확률

다음 지시확률변수를 정의하자.

$$
R_i = \begin{cases} 1 & i\text{ 번째 떨어뜨림에서 바늘이 선을 가로지를 때} \\ 0 & \text{그 밖의 경우} \end{cases}
$$

그러면 $R_i \overset{iid}{\sim} \text{Bernoulli}(p)$ 이고 여기에서 $p$ 는 다음과 같다.

$$
p = P(Y + \sin\Theta \geq 1)
$$

$p$ 를 셈하면 다음과 같다.

$$
p = \int_0^{\pi} \int_0^1 \mathbf{1}(y + \sin\theta \geq 1)\, dy\, \frac{d\theta}{\pi}
$$

$\theta$ 를 고정하면 $y$ 에 대한 적분은 $\min(\sin\theta, 1)$ 이 된다. 간격이 1인 줄 위에 길이 1인 바늘을 떨어뜨리는 경우에는 이것이 다음과 같이 간단해진다.

$$
p = \frac{1}{\pi}\int_0^{\pi} \sin\theta\, d\theta = \frac{2}{\pi}
$$

## 원주율 어림하기

큰수의 법칙에 따라 $n$ 번 떨어뜨린 뒤 다음이 성립한다.

$$
\frac{1}{n}\sum_{i=1}^n R_i \xrightarrow{a.s.} \frac{2}{\pi}
$$

따라서 다음을 얻는다.

$$
\pi \approx \frac{2n}{\sum_{i=1}^n R_i} = \frac{2}{\text{가로지른 비율}}
$$

## 파이썬 구현

```python
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
n = 5000

# 아래쪽 끝 높이 Y ~ Uniform(0, 1) 과 각 Theta ~ Uniform(0, pi) 를 무작위로 만든다
y = np.random.rand(n)           # 아래쪽 끝의 높이
theta = np.random.rand(n)       # 각을 pi 로 나눈 값 (실제 각은 theta*pi)

# 위쪽 끝의 높이
h = y + np.sin(np.pi * theta)

# 바늘이 y = 1 에 있는 선을 가로지르는가?
crosses = h >= 1

# 원주율을 어림한다
estimated_pi = 2 * n / np.sum(crosses)
print(f"Estimated pi: {estimated_pi:.4f}")

# 그때까지의 어림값
cumulative_crosses = np.cumsum(crosses)
running_pi = 2 * np.arange(1, n + 1) / cumulative_crosses

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# 그때까지의 어림값
axes[0].plot(range(1, n + 1), running_pi, 'r-', alpha=0.7)
axes[0].axhline(y=np.pi, color='k', linestyle='-', label='True π')
axes[0].set_xlabel('Number of drops')
axes[0].set_ylabel('Estimate of π')
axes[0].set_ylim([2, 4])
axes[0].set_title("Buffon's Needle: Running Estimate")
axes[0].legend()
axes[0].grid(True)

# 실험을 되풀이한 결과의 히스토그램
m = 1000
n_each = 100
estimates = []
for _ in range(m):
    y_exp = np.random.rand(n_each)
    theta_exp = np.random.rand(n_each)
    h_exp = y_exp + np.sin(np.pi * theta_exp)
    n_crosses = np.sum(h_exp >= 1)
    if n_crosses > 0:
        estimates.append(2 * n_each / n_crosses)
estimates = np.array(estimates)

axes[1].hist(estimates, bins=30, edgecolor='black')
axes[1].axvline(x=np.pi, color='r', linestyle='--', label='True π')
axes[1].set_xlabel('Estimate of π')
axes[1].set_ylabel('Frequency')
axes[1].set_title(f'Histogram ({m} experiments, {n_each} drops each)')
axes[1].legend()

plt.tight_layout()
plt.savefig('buffon_needle.png', dpi=150, bbox_inches='tight')
plt.show()
```

## 역사적 뜻

뷔퐁의 바늘 문제는 1777년 조르주루이 르클레르, 곧 뷔퐁 백작이 내놓은 것으로 기하학적 확률의 가장 이른 문제 가운데 하나이다. 이 문제는 기하($\pi$)와 확률을 아름답게 이어 주며, 몬테카를로라는 말이 생기기 훨씬 전에 나온 몬테카를로 어림의 고전적인 예이다.

## 연습문제

**연습문제 1.** 가로지를 확률 $P = 2/\pi$ 를 셈하고 $2/P \approx \pi$ 임을 수치로 확인하여라.

??? success "연습문제 1 풀이"
    $$
    P = \frac{2}{\pi} \approx 0.6366
    $$

    $$
    \frac{2}{P} = \frac{2}{2/\pi} = \pi \approx 3.14159
    $$

---

**연습문제 2.** 줄 사이의 거리를 $d$ 라고 할 때 길이가 $\ell < d$ 인 바늘을 떨어뜨리면 가로지를 확률이 $2\ell/(\pi d)$ 임을 보여라.

??? success "연습문제 2 풀이"
    $Y \sim \text{Uniform}(0, d)$, $\Theta \sim \text{Uniform}(0, \pi)$ 일 때 바늘이 선을 가로지를 필요충분조건은 $Y + \ell \sin\Theta \geq d$ 이다. 가로지를 확률은 다음과 같다.

    $$
    P = \frac{1}{\pi d}\int_0^{\pi}\ell\sin\theta\,d\theta = \frac{\ell}{\pi d}\left[-\cos\theta\right]_0^{\pi} = \frac{2\ell}{\pi d}
    $$

    $\square$

---

**연습문제 3.** 바늘을 10,000번 떨어뜨려 6,380번 가로지르는 것을 보았다. 이 실험에서 $\pi$ 를 어림하여라.

??? success "연습문제 3 풀이"
    $\hat{P} = 6380/10000 = 0.638$ 이다. 따라서 $\hat{\pi} = 2/\hat{P} = 2/0.638 \approx 3.135$ 이다.

---

**연습문제 4.** 큰수의 법칙을 써서 뷔퐁의 바늘 추정량 $\hat{\pi}_n = 2n / (\sum R_i)$ 이 $\pi$ 에 대하여 일치추정량인 까닭을 설명하여라.

??? success "연습문제 4 풀이"
    강법칙에 따라 $\frac{1}{n}\sum R_i \xrightarrow{a.s.} E[R_i] = 2/\pi$ 이다. $\hat{\pi}_n = 2/(\frac{1}{n}\sum R_i)$ 이고 $g(x) = 2/x$ 가 $x = 2/\pi > 0$ 에서 연속이므로, 연속사상정리에 따라 $\hat{\pi}_n \xrightarrow{a.s.} 2/(2/\pi) = \pi$ 이다. $\square$

---

**연습문제 5.** $n$ 번 떨어뜨린 뒤 가로지를 확률 추정량의 표준오차는 $\sqrt{P(1-P)/n}$ 이다. $n = 10{,}000$ 일 때 $\pi$ 의 대략적인 95% 신뢰구간을 셈하여라.

??? success "연습문제 5 풀이"
    $\text{SE}(\hat{P}) = \sqrt{(2/\pi)(1-2/\pi)/10000} \approx \sqrt{0.6366 \times 0.3634/10000} \approx 0.00481$ 이다.

    $P$ 의 95% 신뢰구간은 $0.6366 \pm 1.96 \times 0.00481 = (0.6272, 0.6460)$ 이다.

    이를 $\pi = 2/P$ 로 옮기면 $(2/0.6460, 2/0.6272) = (3.096, 3.189)$ 이다. 참값 $\pi \approx 3.1416$ 이 이 구간 안에 들어 있다.
