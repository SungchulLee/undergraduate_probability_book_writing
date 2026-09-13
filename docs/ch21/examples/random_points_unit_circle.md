# 임의의 점과 단위원

## [0,1]² 안의 임의의 점 100개

단위정사각형 안에서 고르게 임의의 점을 만드는 일은 간단하다. $x$ 좌표와 $y$ 좌표로 쓸 독립인 $U(0,1)$ 표본을 두 개 만들면 된다.

**MATLAB:**

```matlab
clear all; close all; clc; rng('default')

n = 100;
x = rand(2, n);

plot(x(1,:), x(2,:), 'o')
```

**파이썬:**

```python
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)

n = 100
x = np.random.rand(2, n)

plt.figure()
plt.plot(x[0, :], x[1, :], 'o')
plt.xlabel('x'); plt.ylabel('y')
plt.title('100 random points in $[0,1]^2$')
plt.show()
```

이렇게 얻은 산점도는 고르게 흩어진 점들의 특징적인 모습을 보여 준다. 대체로 고르게 퍼져 있지만 자연스럽게 뭉친 곳과 빈 곳이 함께 나타난다.

## 단위원 안에 든 점

한 걸음 더 나아가 보자. $[-1, 1]^2$ 위에서 고르게 임의의 점 100개를 만들고, 단위원 $x^2 + y^2 = 1$ 의 안에 있는지 밖에 있는지 가른다.

**MATLAB:**

```matlab
clear all; close all; clc; rng('default')

n = 100;
x = 2*rand(2, n) - 1;

plot(x(1,:), x(2,:), 'o'); grid on; hold on

r2 = x(1,:).^2 + x(2,:).^2;
i = find(r2 <= 1);
plot(x(1,i), x(2,i), 'or')

xp = -1:0.01:1;
yp = sqrt(1 - xp.^2);
plot(xp, yp, '-r', xp, -yp, '-r')
```

**파이썬:**

```python
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)

n = 100
x = 2 * np.random.rand(2, n) - 1

r2 = x[0, :]**2 + x[1, :]**2
inside = r2 <= 1
outside = ~inside

plt.figure(figsize=(6, 6))
plt.plot(x[0, outside], x[1, outside], 'ob', label='Outside')
plt.plot(x[0, inside], x[1, inside], 'or', label='Inside')

theta = np.linspace(0, 2*np.pi, 200)
plt.plot(np.cos(theta), np.sin(theta), '-r')

plt.axis('equal'); plt.grid(True)
plt.title('Points inside the unit circle')
plt.legend()
plt.show()
```

## 몬테카를로로 원주율 구하기와의 관계

원 안에 떨어지는 점의 비율은 넓이의 비에 가까워진다.

$$
\frac{\text{원의 넓이}}{\text{정사각형의 넓이}} = \frac{\pi \cdot 1^2}{(2)^2} = \frac{\pi}{4}
$$

따라서 점 $n$ 개 가운데 $k$ 개가 원 안에 떨어지면 다음 값이

$$
\hat{\pi} = \frac{4k}{n}
$$

$\pi$ 의 몬테카를로 어림값이 된다. 큰수의 법칙에 따라 $n \to \infty$ 일 때 $\hat{\pi} \to \pi$ 이다.

## 연습문제

**연습문제 1.**
**(a)** 모임의 크기가 $n = 2, 3, \ldots, 60$ 일 때 $P(\text{적어도 두 사람의 생일이 같다})$ 를 어림하는 모의실험을 짜라. 각 크기마다 $10{,}000$ 번씩 시행하여라. (생일 365가지가 모두 같은 정도로 일어난다고 하자.)

**(b)** 모의실험으로 얻은 확률을 정확한 공식과 함께 그려라. $n$ 이 얼마일 때 이 확률이 처음으로 0.5를 넘어서는가?

**(c)** "세 사람 생일 문제"에 맞게 모의실험을 고쳐라. 곧 $P(\text{적어도 세 사람의 생일이 같다})$ 를 구하여라. $n = 2, \ldots, 100$ 에 대하여 그려라.

---

**연습문제 2.**
뷔퐁의 바늘 실험을 모의실험하여라. 길이가 $\ell$ 인 바늘을 간격이 $d \geq \ell$ 인 평행선 위에 떨어뜨린다. 선을 가로지를 확률은 $\frac{2\ell}{\pi d}$ 이다. 이를 써서 $\ell = d = 1$ 로 $100{,}000$ 번 떨어뜨려 $\pi$ 를 어림하여라.

??? success "연습문제 2 풀이"
    ```python
    import numpy as np

    np.random.seed(42)

    def buffon_needle(n_drops=100000, ell=1, d=1):
        theta = np.random.uniform(0, np.pi, n_drops)
        x = np.random.uniform(0, d / 2, n_drops)
        crosses = x <= (ell / 2) * np.sin(theta)
        p_cross = np.cumsum(crosses) / np.arange(1, n_drops + 1)
        pi_est = (2 * ell) / (d * p_cross)
        return pi_est

    pi_estimates = buffon_needle()
    print(f"pi estimate = {pi_estimates[-1]:.5f}")
    ```
