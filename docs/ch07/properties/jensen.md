# 옌센 부등식

## 정리의 서술

$g$ 가 **볼록함수**이고 $X$ 가 $E[X]$ 와 $E[g(X)]$ 가 모두 유한한 확률변수이면 다음이 성립한다.

$$
E[g(X)] \geq g(E[X])
$$

$g$ 가 **오목함수**이면 부등호의 방향이 뒤집힌다.

$$
E[g(X)] \leq g(E[X])
$$

---

## 직관

볼록함수는 위로 휘어 있으므로 함숫값의 평균이 평균에서의 함숫값보다 작지 않다. 기하학적으로 보면 볼록함수의 현이 함수 위쪽에 놓인다는 뜻이다.

---

## 자주 쓰는 경우

| 함수 $g$ | 볼록/오목 | 옌센 부등식의 서술 |
|:---:|:---:|:---:|
| $g(x) = x^2$ | 볼록 | $E[X^2] \geq (E[X])^2$ |
| $g(x) = e^x$ | 볼록 | $E[e^X] \geq e^{E[X]}$ |
| $g(x) = \lvert x \rvert$ | 볼록 | $E[\lvert X\rvert] \geq \lvert E[X]\rvert$ |
| $g(x) = \log x$ | 오목 | $E[\log X] \leq \log E[X]$ |
| $g(x) = \sqrt{x}$ | 오목 | $E[\sqrt{X}] \leq \sqrt{E[X]}$ |

첫째 줄에서 $\text{Var}(X) = E[X^2] - (E[X])^2 \geq 0$ 임이 따라 나온다.

---

## 금융에서의 응용: 산술평균과 기하평균

양의 수익률 $R_1, \ldots, R_n$ 에 대하여 $\log$ 가 오목함수이므로 다음이 성립한다.

$$
\frac{1}{n}\sum \log R_i \leq \log\left(\frac{1}{n}\sum R_i\right)
$$

곧 **기하평균**은 언제나 **산술평균** 이하라는 뜻이다.

---

## 파이썬 구현

```python
import numpy as np

np.random.seed(42)
N = 1_000_000

X = np.random.exponential(1, N)

# E[X^2] >= (E[X])^2
print(f"E[X^2] = {np.mean(X**2):.4f}")
print(f"(E[X])^2 = {np.mean(X)**2:.4f}")
print(f"Jensen holds: {np.mean(X**2) >= np.mean(X)**2}")

# E[log(X)] <= log(E[X])
pos_X = X[X > 0]
print(f"\nE[log(X)] = {np.mean(np.log(pos_X)):.4f}")
print(f"log(E[X]) = {np.log(np.mean(pos_X)):.4f}")
print(f"Jensen holds: {np.mean(np.log(pos_X)) <= np.log(np.mean(pos_X))}")
```

## 연습문제

**연습문제 1.** 옌센 부등식을 써서 $X > 0$ 일 때 $E[1/X] \geq 1/E[X]$ 임을 보여라.

??? success "연습문제 1 풀이"
    함수 $\varphi(x) = 1/x$ 는 $(0, \infty)$ 에서 볼록하다(2계도함수가 $\varphi''(x) = 2/x^3 > 0$ 이다). 볼록한 $\varphi$ 에 대한 옌센 부등식에 따라 다음이 성립한다.

    $$
    E[\varphi(X)] \geq \varphi(E[X])
    $$

    대입하면 다음을 얻는다.

    $$
    E\!\left[\frac{1}{X}\right] \geq \frac{1}{E[X]}
    $$

    등호는 $X$ 가 거의 확실하게 상수일 때 그리고 오직 그때만 성립한다. $\square$
