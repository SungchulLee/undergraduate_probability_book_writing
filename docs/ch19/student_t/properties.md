# 성질과 정규분포와의 비교

## 성질 요약

| 성질 | 값 |
|----------|-------|
| 밀도함수 | $\frac{1}{\sqrt{d}\,B(1/2, d/2)}\left(1 + \frac{t^2}{d}\right)^{-(d+1)/2}$ |
| 평균 | $d > 1$ 일 때 $0$ |
| 분산 | $d > 2$ 일 때 $\frac{d}{d - 2}$ |
| 대칭성 | $0$ 에 대하여 대칭 |
| 받침 | $(-\infty, \infty)$ |

## 평균과 분산

**평균.** 밀도함수가 대칭이므로($f_T(t) = f_T(-t)$) $d > 1$ 일 때 $E[T] = 0$ 이다.

!!! warning "$d = 1$ 일 때는 평균이 없다"
    $d = 1$ 이면 t분포는 **코시분포**가 되며, 코시분포에는 유한한 평균이 없다. 적분 $\int_{-\infty}^{\infty} t \cdot f_T(t)\,dt$ 가 발산하기 때문이다.

**분산.** $d > 2$ 일 때 다음이 성립한다.

$$\text{Var}(T) = \frac{d}{d - 2}$$

분산은 언제나 표준정규분포의 분산인 $1$ 보다 크며, 이는 꼬리가 더 두껍다는 사실을 반영한다. $d \to \infty$ 이면 $\text{Var}(T) \to 1$ 이다.

## 표준정규분포와 견주기

t분포는 표준정규분포보다 **꼬리가 두껍다**.

$$f_T(t) \propto \left(1 + \frac{t^2}{d}\right)^{-(d+1)/2} \quad \text{대} \quad \phi(t) \propto e^{-t^2/2}$$

t분포의 밀도함수는 $|t|^{-(d+1)}$ 처럼 **다항식꼴로** 줄어들지만 정규분포의 밀도함수는 $e^{-t^2/2}$ 처럼 **지수적으로** 줄어든다. 이는 다음을 뜻한다.

- $N(0,1)$ 보다 $t_d$ 의 꼬리 쪽에 확률이 더 많다
- 둘 다 적분값이 $1$ 이어야 하므로, 그만큼 $N(0,1)$ 은 가운데 쪽에 확률이 더 많다
- 극단적인 값은 $N(0,1)$ 보다 $t_d$ 에서 더 자주 나온다

## 특별한 경우: 코시분포 (d = 1)

$d = 1$ 이면 다음과 같다.

$$f_T(t) \propto \frac{1}{1 + t^2} \quad \Rightarrow \quad f_T(t) = \frac{1}{\pi} \cdot \frac{1}{1 + t^2}$$

코시분포는 다음과 같은 성질을 지닌다.

- 유한한 평균이 없다(적분이 발산한다)
- 유한한 분산이 없다
- 적률생성함수가 없다
- i.i.d. 코시확률변수 $n$ 개의 표본평균이 코시확률변수 하나와 **같은** 분포를 따른다. 중심극한정리가 적용되지 않는다

## 파이썬으로 견주기

```python
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

x = np.linspace(-4, 4, 500)

fig, ax = plt.subplots(figsize=(8, 5))
ax.plot(x, stats.norm.pdf(x), 'r-', lw=2, label='$N(0,1)$')
for d in [1, 2, 5, 10, 30]:
    ax.plot(x, stats.t.pdf(x, d), '--', label=f'$t_{{{d}}}$')

ax.set_xlabel('$x$')
ax.set_ylabel('Density')
ax.set_title("Student's $t$ vs. Standard Normal")
ax.legend()
plt.tight_layout()
plt.show()
```

## 연습문제

**연습문제 1.**
$T \sim t_1$(코시분포)일 때 $E[T]$ 가 존재하지 않음을 보여라.

??? success "연습문제 1 풀이"
    밀도함수는 $f(t) = \frac{1}{\pi(1 + t^2)}$ 이다. 다음을 따져 보면 된다.

    $$E[|T|] = \frac{2}{\pi} \int_0^{\infty} \frac{t}{1+t^2}\,dt = \frac{2}{\pi} \left[\frac{1}{2}\ln(1+t^2)\right]_0^{\infty} = \infty$$

    $E[|T|] = \infty$ 이므로 평균은 존재하지 않는다.
