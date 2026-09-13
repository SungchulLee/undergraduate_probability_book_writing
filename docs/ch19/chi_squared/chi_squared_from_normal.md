# 정규확률변수의 제곱합에서 얻는 카이제곱분포: 모의실험

자유도가 $d$ 인 카이제곱분포는 독립인 표준정규확률변수 $d$ 개를 제곱하여 더한 것으로 정의된다. 이 절에서는 $\chi^2_d$ 에서 바로 뽑은 표본과 $N(0,1)$ 에서 뽑아 제곱하여 더한 표본을 견주어 이 정의를 모의실험으로 확인한다.

## 배경

$Z_1, Z_2, \ldots, Z_d$ 를 서로 독립인 표준정규확률변수라고 하자. 그러면 다음이 성립한다.

$$
Q = Z_1^2 + Z_2^2 + \cdots + Z_d^2 \sim \chi^2_d
$$

여기에서 $\chi^2_d$ 는 자유도가 $d$ 인 카이제곱분포이다. 같은 말로 $\chi^2_d \stackrel{d}{=} \Gamma(d/2, 1/2)$ 이므로 밀도함수는 다음과 같다.

$$
f_{\chi^2_d}(x) = \frac{(1/2)^{d/2}}{\Gamma(d/2)}\, x^{d/2 - 1}\, e^{-x/2}, \quad x > 0
$$

평균은 $E[\chi^2_d] = d$ 이고 분산은 $\text{Var}(\chi^2_d) = 2d$ 이다. 아래 모의실험은 $\chi^2_5$ 표본을 두 가지 방법으로 만들어 정의를 확인한다. (1) `scipy.stats.chi2` 에서 바로 뽑는 방법과 (2) 표본 하나마다 $N(0,1)$ 에서 다섯 번 뽑아 제곱하여 더하는 방법이다. 정의가 옳다면 두 히스토그램이 모두 이론적인 밀도함수와 맞아떨어져야 한다.

## 코드

```python
"""표준정규확률변수의 제곱합으로서의 카이제곱분포: 두 표집 방법 견주기."""
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

np.random.seed(42)
df = 5

data_direct = stats.chi2(df=df).rvs(10_000)
data_from_norm = np.sum(stats.norm.rvs(size=(df, 10_000)) ** 2, axis=0)

fig, (ax0, ax1) = plt.subplots(1, 2, figsize=(12, 4))

_, bins, _ = ax0.hist(data_direct, bins=100, density=True, alpha=0.7, color="steelblue")
y = stats.chi2(df=df).pdf(bins)
ax0.plot(bins, y, "--r", lw=2)
ax0.set_title("Direct χ² sampling")

ax1.hist(data_from_norm, bins=bins, density=True, alpha=0.7, color="steelblue")
ax1.plot(bins, y, "--r", lw=2)
ax1.set_title("Sum of squared N(0,1)")

for ax in (ax0, ax1):
    ax.grid(True, alpha=0.3)

plt.suptitle(f"χ²({df}) = Z₁² + Z₂² + ··· + Z_{df}²", fontsize=14, fontweight="bold")
plt.tight_layout()
plt.savefig("chi_squared_from_normal.png", dpi=150, bbox_inches="tight")
plt.show()
```

## 실행 결과

이 코드는 각각 10 000개의 표본에 바탕을 둔 히스토그램 두 개를 나란히 그려 준다.

- **왼쪽("Direct $\chi^2$ sampling")**: `scipy.stats.chi2` 를 써서 $\chi^2_5$ 에서 바로 뽑은 표본의 히스토그램이며, 그 위에 이론적인 $\chi^2_5$ 밀도함수(빨간 점선)를 얹었다.
- **오른쪽("Sum of squared $N(0,1)$")**: $N(0,1)$ 에서 다섯 개를 독립으로 뽑아 각각 제곱하여 더해 얻은 표본의 히스토그램이며, 마찬가지로 같은 이론적 밀도함수를 얹었다.

두 히스토그램 모두 오른쪽으로 치우쳐 있고 최빈값이 $x = 3$ 언저리, 최고 밀도가 약 $0.15$ 이며 오른쪽 꼬리가 $x = 20$ 너머까지 길게 뻗는다.

## 뜻풀이

두 히스토그램은 사실상 구별되지 않으며 둘 다 이론적인 $\chi^2_5$ 밀도함수를 잘 따라간다. $\chi^2_d$ 에서 뽑는 것과 독립인 표준정규확률변수 $d$ 개를 제곱하여 더하는 것이 같다는 정의가 확인된 것이다. 이 모의실험은 카이제곱분포의 주요 특징도 함께 보여 준다. 받침이 $(0, \infty)$ 이고, 오른쪽으로 치우쳐 있으며, $d = 5$ 일 때 최빈값이 $d - 2 = 3$ 에 놓인다.

## 연습문제

**연습문제 1.**
코드를 고쳐 $d = 1$ 과 $d = 30$ 으로 실행하여라. $d$ 가 커질 때 히스토그램의 모양이 어떻게 달라지는지 말하여라.

??? success "연습문제 1 풀이"
    $d = 1$ 이면 히스토그램이 오른쪽으로 심하게 치우치고 최빈값이 $0$ 이다($x \to 0^+$ 일 때 밀도함수가 발산한다). $d = 30$ 이면 히스토그램이 거의 대칭인 종 모양이 되고 $x = 30$ 언저리를 중심으로 놓인다. $\chi^2_d$ 가 i.i.d. 확률변수 $d$ 개의 합이므로 $d \to \infty$ 일 때 중심극한정리에 따라 정규분포에 가까워지기 때문이다. 더 정확히 말하면 $d \to \infty$ 일 때 $({\chi^2_d - d})/{\sqrt{2d}} \xrightarrow{d} N(0,1)$ 이다.

---

**연습문제 2.**
$d = 5$ 로 두고 제곱합 방법으로 10 000개의 표본을 만들어 표본평균과 표본분산을 구하여라. 이론값 $E[\chi^2_5] = 5$ 및 $\text{Var}(\chi^2_5) = 10$ 과 견주어 보아라.

??? success "연습문제 2 풀이"
    ```python
    import numpy as np
    from scipy import stats

    np.random.seed(42)
    d = 5
    data = np.sum(stats.norm.rvs(size=(d, 10_000)) ** 2, axis=0)
    print(f"Sample mean: {data.mean():.3f}  (theoretical: {d})")
    print(f"Sample var:  {data.var(ddof=1):.3f}  (theoretical: {2*d})")
    ```

    보통 표본평균은 $\approx 5.00$, 표본분산은 $\approx 10.0$ 으로 나온다. 이론값 $E[\chi^2_d] = d = 5$, $\text{Var}(\chi^2_d) = 2d = 10$ 과 잘 맞는다.

---

**연습문제 3.**
$Z_1, \ldots, Z_d$ 가 i.i.d. $N(0,1)$ 이라고 하자. $E[Z_1^2 + \cdots + Z_d^2] = d$ 와 $\text{Var}(Z_1^2 + \cdots + Z_d^2) = 2d$ 를 증명하여라.

??? success "연습문제 3 풀이"
    $Z_i \sim N(0,1)$ 이므로 $E[Z_i^2] = \text{Var}(Z_i) + (E[Z_i])^2 = 1 + 0 = 1$ 이다. 기댓값의 선형성에 따라

    $$
    E\!\left[\sum_{i=1}^d Z_i^2\right] = \sum_{i=1}^d E[Z_i^2] = d
    $$

    이다. 분산을 구하려면 $\text{Var}(Z_i^2)$ 이 필요하다. 표준정규분포의 4차 적률이 $E[Z_i^4] = 3$ 이므로 $\text{Var}(Z_i^2) = E[Z_i^4] - (E[Z_i^2])^2 = 3 - 1 = 2$ 이다. 독립성에 따라

    $$
    \text{Var}\!\left(\sum_{i=1}^d Z_i^2\right) = \sum_{i=1}^d \text{Var}(Z_i^2) = 2d
    $$

    이다.

---

**연습문제 4.**
$X_1, \ldots, X_d$ 가 i.i.d. $N(\mu, \sigma^2)$ 이라고 하자. $\sum_{i=1}^d \left(\frac{X_i - \mu}{\sigma}\right)^2 \sim \chi^2_d$ 임을 보여라.

??? success "연습문제 4 풀이"
    $Z_i = (X_i - \mu)/\sigma$ 로 두자. $X_i \sim N(\mu, \sigma^2)$ 이므로 표준화에 따라 $Z_i \sim N(0,1)$ 이다. $X_i$ 들이 독립이므로 $Z_i$ 들도 독립이다. 따라서 카이제곱분포의 정의에 따라 다음이 성립한다.

    $$
    \sum_{i=1}^d \left(\frac{X_i - \mu}{\sigma}\right)^2 = \sum_{i=1}^d Z_i^2 \sim \chi^2_d
    $$

    $\square$

---

**연습문제 5.**
$d$ 가 유한할 때 카이제곱분포가 언제나 오른쪽으로 치우치는 까닭을 설명하고, $d \to \infty$ 일 때 왜도가 어떻게 되는지 말하여라.

??? success "연습문제 5 풀이"
    각 $Z_i^2$ 은 $[0, \infty)$ 의 값을 가지므로 $\chi^2_d = \sum Z_i^2$ 의 받침은 $(0, \infty)$ 이다. 아래로는 $0$ 으로 막혀 있지만 위로는 끝이 없기에 오른쪽으로 치우친다. 수치로 말하면 $\chi^2_d$ 의 왜도는 $\sqrt{8/d}$ 이다. 이는 $Z^2$ 의 3차 중심적률이 $E[(Z^2 - 1)^3] = 8$ 이라는 사실($E[Z^6] = 15$, $E[Z^4] = 3$, $E[Z^2] = 1$ 을 쓴다)과 i.i.d. 합에 대한 공식에서 따라 나온다. $d \to \infty$ 이면 왜도 $\sqrt{8/d} \to 0$ 이고, 중심극한정리에 따라 $(\chi^2_d - d)/\sqrt{2d} \xrightarrow{d} N(0,1)$ 이 되어 분포가 거의 대칭이 된다.
