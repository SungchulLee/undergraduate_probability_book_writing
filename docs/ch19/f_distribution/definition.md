# 카이제곱분포의 비로서의 정의

## 정의

$V_1 \sim \chi^2_{d_1}$ 과 $V_2 \sim \chi^2_{d_2}$ 가 **독립**이면 다음이 성립한다.

$$F = \frac{V_1 / d_1}{V_2 / d_2} \sim F_{d_1, d_2}$$

여기에서 $d_1$ 과 $d_2$ 를 각각 **분자의 자유도**와 **분모의 자유도**라고 한다.

## 야코비안을 이용한 밀도함수 유도

### 문제 설정

$X \sim \chi^2_{d_1}$ 과 $Y \sim \chi^2_{d_2}$ 가 독립일 때 $F = \frac{X/d_1}{Y/d_2}$, $Z = Y$ 로 두자.

역변환은 $x = f \cdot d_1 \cdot z / d_2$, $y = z$ 이다.

### 야코비안

$$\left|\frac{\partial(x, y)}{\partial(f, z)}\right| = \left|\frac{\partial(f, z)}{\partial(x, y)}\right|^{-1} = \left|\det \begin{pmatrix} \frac{1/d_1}{z/d_2} & * \\ 0 & 1 \end{pmatrix}\right|^{-1} = \frac{z/d_2}{1/d_1} = \frac{d_1 z}{d_2}$$

### 결합밀도함수

$$f_{F,Z}(f, z) = f_{X,Y}(x, y) \left|\frac{\partial(x,y)}{\partial(f,z)}\right|$$

$$= \frac{(1/2)^{d_1/2}}{\Gamma(d_1/2)} x^{d_1/2-1} e^{-x/2} \cdot \frac{(1/2)^{d_2/2}}{\Gamma(d_2/2)} y^{d_2/2-1} e^{-y/2} \cdot \frac{d_1 z}{d_2}$$

여기에 $x = f \cdot d_1 z / d_2$ 와 $y = z$ 를 넣고 $\lambda = \frac{1}{2}\!\left(1 + \frac{d_1}{d_2}f\right)$ 로 두면 다음과 같다.

$$f_{F,Z}(f, z) = \frac{1}{B(d_1/2, \, d_2/2) \cdot f} \sqrt{\frac{(d_1 f)^{d_1} \cdot d_2^{d_2}}{(d_1 f + d_2)^{d_1+d_2}}} \cdot \underbrace{\frac{\lambda\,(\lambda z)^{(d_1+d_2)/2 - 1} e^{-\lambda z}}{\Gamma\!\left(\frac{d_1+d_2}{2}\right)}}_{\text{Gamma}\!\left(\frac{d_1+d_2}{2}, \, \lambda\right) \text{ 의 } z \text{ 에 대한 밀도함수}}$$

### F 의 주변밀도함수

$z$ 에 대하여 적분하면(감마밀도함수의 적분이 $1$ 이므로) 다음을 얻는다.

$$\boxed{f_F(f) = \frac{1}{B\!\left(\frac{d_1}{2}, \frac{d_2}{2}\right) \cdot f} \sqrt{\frac{(d_1 f)^{d_1} \cdot d_2^{d_2}}{(d_1 f + d_2)^{d_1 + d_2}}}, \quad f > 0}$$

## 파이썬으로 확인하기

```python
import numpy as np
from scipy import stats, special
import matplotlib.pyplot as plt

d1, d2 = 5, 10
x = np.linspace(0.01, 5, 500)

# 공식으로 구한 값
B = special.beta(d1/2, d2/2)
pdf_formula = (1 / (B * x)) * np.sqrt((d1*x)**d1 * d2**d2 / (d1*x + d2)**(d1+d2))

# scipy 로 구한 값
pdf_scipy = stats.f.pdf(x, d1, d2)

print(f"Max difference: {np.max(np.abs(pdf_formula - pdf_scipy)):.2e}")

# 모의실험
np.random.seed(42)
v1 = np.random.chisquare(d1, 100_000)
v2 = np.random.chisquare(d2, 100_000)
f_samples = (v1 / d1) / (v2 / d2)

fig, ax = plt.subplots(figsize=(8, 5))
ax.hist(f_samples, bins=100, density=True, alpha=0.5, range=(0, 6), label='Simulation')
ax.plot(x, pdf_scipy, 'r-', lw=2, label=f'$F_{{{d1},{d2}}}$ PDF')
ax.set_xlabel('$f$')
ax.set_ylabel('Density')
ax.set_title(f'$F$ Distribution ($d_1={d1}, d_2={d2}$)')
ax.legend()
plt.tight_layout()
plt.show()
```

## 연습문제

**연습문제 1.** $V_1 \sim \chi^2_5$ 와 $V_2 \sim \chi^2_{10}$ 이 독립이라고 하자. $F = (V_1/5)/(V_2/10)$ 일 때 $E[F]$ 를 구하여라.

??? success "연습문제 1 풀이"
    $d_2 > 2$ 인 $F \sim F_{d_1, d_2}$ 에 대하여 $E[F] = \frac{d_2}{d_2 - 2} = \frac{10}{8} = 1.25$ 이다.

---

**연습문제 2.** $T \sim t_d$ 이면 $T^2 \sim F_{1, d}$ 임을 보여라.

??? success "연습문제 2 풀이"
    독립인 $Z \sim N(0,1)$ 과 $V \sim \chi^2_d$ 에 대하여 $T = Z/\sqrt{V/d}$ 이다. 그러면

    $$
    T^2 = \frac{Z^2}{V/d} = \frac{Z^2/1}{V/d}
    $$

    이다. $Z^2 \sim \chi^2_1$ 이고 분자와 분모가 독립이므로 이는 $\chi^2_1/1$ 과 $\chi^2_d/d$ 의 비이다. 정의에 따라 $T^2 \sim F_{1,d}$ 이다. $\square$

---

**연습문제 3.** $F \sim F_{d_1, d_2}$ 이면 $1/F$ 의 분포는 무엇인가?

??? success "연습문제 3 풀이"
    $F = \frac{V_1/d_1}{V_2/d_2}$ 이므로 $1/F = \frac{V_2/d_2}{V_1/d_1} \sim F_{d_2, d_1}$ 이다.

    곧 $F_{d_1, d_2}$ 의 역수는 자유도를 맞바꾼 $F_{d_2, d_1}$ 이다.

---

**연습문제 4.** $F \sim F_{5, 20}$ 일 때 $\text{Var}(F)$ 를 구하여라.

??? success "연습문제 4 풀이"
    $d_2 > 4$ 인 $F_{d_1, d_2}$ 에 대하여 다음이 성립한다.

    $$
    \text{Var}(F) = \frac{2d_2^2(d_1 + d_2 - 2)}{d_1(d_2-2)^2(d_2-4)} = \frac{2 \times 400 \times 23}{5 \times 324 \times 16} = \frac{18400}{25920} \approx 0.710
    $$

---

**연습문제 5.** $d_2 > 2$ 일 때 모든 $F_{d_1, d_2}$ 분포에서 $E[F] > 1$ 인 까닭과, $d_2 \to \infty$ 일 때 이 평균이 $1$ 로 다가가는 까닭을 직관적으로 설명하여라.

??? success "연습문제 5 풀이"
    $E[F] = d_2/(d_2 - 2)$ 이다. 이 값이 $1$ 보다 큰 까닭은 이러하다. 분모 $V_2/d_2$ 는 $\chi^2_1$ 확률변수들의 표본평균이므로 큰수의 법칙에 따라 $1$ 언저리에 몰리지만, 그 역수를 취하면 옌센 부등식에 따라 $E[1/(V_2/d_2)] > 1/E[V_2/d_2]$ 가 된다(역수 함수는 볼록하다). $d_2 \to \infty$ 이면 $V_2/d_2 \xrightarrow{p} 1$ 이므로 비가 $V_1/d_1$ 을 $1$ 로 나눈 것에 가까워지고 $E[F] \to 1$ 이 된다.
