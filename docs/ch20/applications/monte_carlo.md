# 몬테카를로 모의실험

## 생각의 얼개

몬테카를로 방법은 해석적으로 셈하기 어려운 값을 **무작위 표집**으로 어림한다. 표본평균이 기댓값으로 수렴한다는 큰수의 법칙이 그 이론적 바탕이다.

분포를 아는 확률변수 $X$ 에 대하여 $\theta = \mathbb{E}[g(X)]$ 를 셈하고 싶다면 다음과 같이 하면 된다.

1. $X$ 의 분포에서 i.i.d. 표본 $X_1, \ldots, X_n$ 을 뽑는다.
2. 표본평균 $\hat{\theta}_n = \frac{1}{n}\sum_{i=1}^n g(X_i)$ 를 셈한다.
3. 큰수의 법칙에 따라 $n \to \infty$ 일 때 $\hat{\theta}_n \to \theta$ 이다.

## 몬테카를로로 원주율 어림하기

### 문제 설정

정사각형 $[-1, 1]^2$ 에서 고르게 무작위로 점 $X_i$ 를 $n$ 개 뽑는다. 다음과 같이 정의하자.

$$
R_i = \begin{cases} 1 & X_i \text{ 가 단위원 안에 있을 때} \\ 0 & \text{그 밖의 경우} \end{cases}
$$

그러면 $R_i \overset{iid}{\sim} \text{Bernoulli}(p)$ 이고 여기에서 $p$ 는 다음과 같다.

$$
p = \frac{\text{단위원의 넓이}}{\text{정사각형의 넓이}} = \frac{\pi}{4}
$$

### 어림하기

큰수의 법칙에 따라 다음이 성립한다.

$$
\frac{1}{n}\sum_{i=1}^n R_i \xrightarrow{a.s.} \frac{\pi}{4}
$$

따라서 다음을 얻는다.

$$
\pi \approx \frac{4}{n}\sum_{i=1}^n R_i = 4 \times \frac{\text{원 안에 든 점의 수}}{n}
$$

### 파이썬 구현

```python
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
n = 5000

# [-1, 1]^2 안에서 무작위로 점을 만든다
x = 2 * np.random.rand(2, n) - 1

# 단위원 안에 있는지 확인한다
r2 = x[0]**2 + x[1]**2
inside = r2 <= 1

# 원주율을 어림한다
estimated_pi = 4 * np.sum(inside) / n
print(f"Estimated pi: {estimated_pi:.4f}")

# 그림 그리기
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

# 산점도
axes[0].scatter(x[0, inside], x[1, inside], c='red', s=1, label='Inside')
axes[0].scatter(x[0, ~inside], x[1, ~inside], c='blue', s=1, label='Outside')
axes[0].set_aspect('equal')
axes[0].set_title(f'{n} Random Darts')
axes[0].legend()

# 그때까지의 어림값
running_pi = 4 * np.cumsum(inside) / np.arange(1, n + 1)
axes[1].plot(range(1, n + 1), running_pi, 'r-', alpha=0.7)
axes[1].axhline(y=np.pi, color='k', linestyle='-', label='True π')
axes[1].set_xlabel('Number of darts')
axes[1].set_ylabel('Estimate of π')
axes[1].set_title('Running Estimate (Strong Law)')
axes[1].legend()

# 실험을 되풀이한 결과의 히스토그램
m = 1000  # 실험 횟수
n_each = 100  # 실험 한 번에 던지는 다트 수
estimates = np.array([
    4 * np.sum(np.sum((2*np.random.rand(2, n_each)-1)**2, axis=0) <= 1) / n_each
    for _ in range(m)
])
axes[2].hist(estimates, bins=30, edgecolor='black')
axes[2].axvline(x=np.pi, color='r', linestyle='--', label='True π')
axes[2].set_xlabel('Estimate of π')
axes[2].set_ylabel('Frequency')
axes[2].set_title(f'Histogram ({m} experiments, {n_each} darts each)')
axes[2].legend()

plt.tight_layout()
plt.savefig('monte_carlo_pi.png', dpi=150, bbox_inches='tight')
plt.show()
```

### 관찰

- **왼쪽 그림**(한 줄기의 그때까지의 어림값)은 **강법칙**을 보여 준다. 표본경로 하나가 $\pi$ 로 수렴한다.
- **오른쪽 그림**(여러 어림값의 히스토그램)은 **약법칙**을 보여 준다. 표본평균의 분포가 $\pi$ 주위로 몰린다.
- 다트를 더 많이 던질수록 $\Rightarrow$ 더 좋은 어림값을 얻는다. 표준오차는 $\sigma/\sqrt{n}$ 이며 $1/\sqrt{n}$ 의 속도로 줄어든다.

## 연습문제

**연습문제 1.**
$\theta = \int_0^1 e^{-x^2} \, dx$ 를 어림하는 몬테카를로 모의실험을 설계하여라. $U \sim U(0,1)$ 에 대하여 $\theta = E[g(U)]$ 로 적고, $g(U_1), \ldots, g(U_n)$ 의 표본평균을 셈한 뒤, 중심극한정리를 써서 $n = 10{,}000$ 일 때 $\theta$ 의 95% 신뢰구간을 만들어라.
