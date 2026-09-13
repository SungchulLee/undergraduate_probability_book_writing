# 박스–뮐러 변환

**박스–뮐러 변환**은 균등분포 표본에서 표준정규분포 표본을 만들어 낸다. 모의실험과 몬테카를로 방법에서 바탕이 되는 기법이다.

## 방법 1: 기본 박스–뮐러

**1단계.** i.i.d. $U_1, U_2 \sim U(0, 1)$ 두 개를 만든다.

**2단계.** 다음과 같이 놓는다.

$$\Theta = 2\pi U_1, \qquad R^2 = -2\log U_2$$

**3단계.** 다음과 같이 놓는다.

$$Z_1 = R\cos\Theta, \qquad Z_2 = R\sin\Theta$$

그러면 $Z_1$ 과 $Z_2$ 는 **i.i.d.** $N(0, 1)$ 이다.

### 왜 통하는가

이 유도는 두 가지 배경 사실에 기댄다.

**사실 1:** $U \sim U(0, 1)$ 이면 $V = -2\log U \sim \text{Exp}(1/2)$ 이다.

*증명:*

$$P(V \leq v) = P(-2\log U \leq v) = P\left(\log U \geq -\frac{v}{2}\right) = P\left(U \geq e^{-v/2}\right) = 1 - e^{-v/2}$$

따라서 $f_V(v) = \frac{1}{2}e^{-v/2}$ 이고, 이는 $\text{Exp}(1/2)$ 의 확률밀도함수이다.

**사실 2:** $X, Y \sim N(0,1)$ 이 i.i.d. 일 때 $S = X^2 + Y^2$ 와 $\Theta = \tan^{-1}(Y/X)$ 로 놓자. 그러면 다음이 성립한다.

- $\Theta \sim U(0, 2\pi)$
- $S \sim \text{Exp}(1/2)$
- $S$ 와 $\Theta$ 는 독립이다

*증명:* $X = \sqrt{S}\cos\Theta$, $Y = \sqrt{S}\sin\Theta$, $S = R^2$ 인 극좌표 $(S, \Theta)$ 로 $(X, Y)$ 를 옮긴다. 야코비안은 다음과 같다.

$$\left|\frac{\partial(x,y)}{\partial(s,\theta)}\right| = \begin{vmatrix} \frac{1}{2\sqrt{s}}\cos\theta & -\sqrt{s}\sin\theta \\ \frac{1}{2\sqrt{s}}\sin\theta & \sqrt{s}\cos\theta \end{vmatrix} = \frac{1}{2}$$

결합밀도는 다음과 같이 변한다.

$$f_{S,\Theta}(s, \theta) = f_X(x)f_Y(y) \cdot \left|\frac{\partial(x,y)}{\partial(s,\theta)}\right|$$

$$= \frac{1}{\sqrt{2\pi}}e^{-x^2/2} \cdot \frac{1}{\sqrt{2\pi}}e^{-y^2/2} \cdot \frac{1}{2} = \frac{1}{4\pi}e^{-(x^2+y^2)/2} = \underbrace{\frac{1}{2\pi}}_{\Theta \sim U(0,2\pi)} \cdot \underbrace{\frac{1}{2}e^{-s/2}}_{S \sim \text{Exp}(1/2)}$$

결합밀도가 곱으로 갈라지므로 독립성과 각각의 주변분포가 확인된다.

**박스–뮐러 변환은 이 관계를 거꾸로 돌린 것이다.** $R^2 = -2\log U_2 \sim \text{Exp}(1/2)$ 와 $\Theta = 2\pi U_1 \sim U(0, 2\pi)$ 가 독립이므로, 직교좌표 $Z_1 = R\cos\Theta$ 와 $Z_2 = R\sin\Theta$ 는 i.i.d. $N(0,1)$ 일 수밖에 없다.

## 방법 2: 마살리아 극좌표 방법

**1단계.** i.i.d. $U_1, U_2 \sim U(0, 1)$ 두 개를 만든다.

**2단계.** $V_i = 2U_i - 1$ 로 놓는다(그러면 $V_i \sim U(-1, 1)$ 이다).

**3단계.** $r^2 = V_1^2 + V_2^2$ 을 계산한다. $r^2 > 1$ 이면(곧 $(V_1, V_2)$ 가 단위원 바깥에 있으면) **기각**하고 되풀이한다.

**4단계.** 다음과 같이 놓는다.

$$Z_i = V_i \sqrt{\frac{-2\log r^2}{r^2}}$$

그러면 $Z_1, Z_2$ 는 i.i.d. $N(0, 1)$ 이다.

마살리아 방법은 삼각함수(sin, cos) 계산을 피하는 대신 기각 단계를 치른다. 받아들여질 확률은 $\pi/4 \approx 78.5\%$ 이다.

## 파이썬 구현

```python
import numpy as np

def box_muller(n):
    """박스-뮐러 방법으로 표준정규분포 표본 n 개를 만든다."""
    U1 = np.random.uniform(0, 1, (n + 1) // 2)
    U2 = np.random.uniform(0, 1, (n + 1) // 2)
    
    R = np.sqrt(-2 * np.log(U2))
    Theta = 2 * np.pi * U1
    
    Z1 = R * np.cos(Theta)
    Z2 = R * np.sin(Theta)
    
    samples = np.concatenate([Z1, Z2])
    return samples[:n]

# 만들어서 확인하기
np.random.seed(42)
Z = box_muller(100000)
print(f"Box-Muller samples (n=100000):")
print(f"  Mean: {Z.mean():.4f}  (expected: 0)")
print(f"  Var:  {Z.var():.4f}  (expected: 1)")
print(f"  Skew: {float(np.mean(((Z - Z.mean())/Z.std())**3)):.4f}  (expected: 0)")
```

**실행 결과:**
```
Box-Muller samples (n=100000):
  Mean: -0.0014  (expected: 0)
  Var:  1.0012  (expected: 1)
  Skew: -0.0068  (expected: 0)
```

## 연습문제

**연습문제 1.**
$U_1, U_2 \overset{\text{iid}}{\sim} U(0, 1)$ 이라 하자. $Z_1 = \sqrt{-2\ln U_1}\cos(2\pi U_2)$ 와 $Z_2 = \sqrt{-2\ln U_1}\sin(2\pi U_2)$ 로 정의한다.

(a) $Z_1$ 과 $Z_2$ 의 분포는 무엇인가?

(b) $Z_1$ 과 $Z_2$ 는 독립인가?

??? success "연습문제 1 풀이"
    (a) $Z_1 \sim N(0, 1)$ 이고 $Z_2 \sim N(0, 1)$ 이다.

    (b) 그렇다. $Z_1$ 과 $Z_2$ 는 독립인 표준정규확률변수이다. 박스–뮐러 변환에서 따라 나온다. $R^2 = -2\ln U_1 \sim \text{Exp}(1/2)$ 와 $\Theta = 2\pi U_2 \sim U(0, 2\pi)$ 가 독립이면 $(R\cos\Theta, R\sin\Theta)$ 는 i.i.d. $N(0,1)$ 확률변수의 짝이 된다.
