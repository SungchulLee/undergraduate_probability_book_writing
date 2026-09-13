# t분포와의 관계

## T² ~ F₁,d

$F$ 분포와 $t$ 분포를 잇는 가장 중요한 관계는 다음과 같다.

**$T \sim t_d$ 이면 $T^2 \sim F_{1,d}$ 이다.**

### 증명

정의에 따라 독립인 $Z \sim N(0,1)$ 과 $V \sim \chi^2_d$ 에 대하여 $T = Z / \sqrt{V/d}$ 이다.

$$T^2 = \frac{Z^2}{V/d} = \frac{Z^2/1}{V/d} = \frac{\chi^2_1/1}{\chi^2_d/d} \sim F_{1,d}$$

### 가설검정에서의 뜻

검정통계량이 $T$ 이고 자유도가 $d$ 인 양쪽꼬리 $t$ 검정은 $|T| > t_{\alpha/2, d}$ 일 때 기각하는데, 이는 $T^2 > t_{\alpha/2,d}^2 = F_{\alpha, 1, d}$ 일 때 기각하는 것과 같다.

곧 다음이 성립한다.

$$\text{양쪽꼬리 } t\text{ 검정} \iff (1, d) \text{ 자유도의 } F\text{ 검정}$$

## 관계 정리

세 분포는 모두 정규분포에서 비롯한다.

| 분포 | 만드는 법 | 모수 |
|-------------|-------------|------------|
| $\chi^2_d$ | $\sum_{i=1}^d Z_i^2$ | $d$ = 제곱한 정규확률변수의 개수 |
| $t_d$ | $\frac{Z}{\sqrt{\chi^2_d / d}}$ | $d$ = 분모의 자유도 |
| $F_{d_1, d_2}$ | $\frac{\chi^2_{d_1}/d_1}{\chi^2_{d_2}/d_2}$ | $d_1, d_2$ = 분자와 분모의 자유도 |

**서로 사이의 관계:**

- $\chi^2_d = \Gamma(d/2, 1/2)$ (감마분포의 특별한 경우)
- $t_d^2 = F_{1,d}$ ($t$ 를 제곱하면 $F$ 가 된다)
- $\frac{1}{F_{d_1,d_2}} = F_{d_2, d_1}$ (역수를 취하면 자유도가 맞바뀐다)
- $d \to \infty$ 일 때 $t_d \to N(0,1)$
- $d_2 \to \infty$ 일 때 $d_1 \cdot F_{d_1, d_2} \to \chi^2_{d_1}$

## 파이썬으로 확인하기

```python
import numpy as np
from scipy import stats

np.random.seed(42)
d = 10
n_sim = 200_000

# t 표본을 만들어 제곱한다
t_samples = np.random.standard_t(d, n_sim)
t_squared = t_samples**2

# F(1, d) 와 견준다
ks_stat, p_value = stats.kstest(t_squared, 'f', args=(1, d))
print(f"KS test (T^2 vs F(1,{d})): stat={ks_stat:.4f}, p={p_value:.4f}")

# 역수 성질을 확인한다
f_samples = np.random.f(5, 10, n_sim)
reciprocal = 1.0 / f_samples
ks_stat2, p_value2 = stats.kstest(reciprocal, 'f', args=(10, 5))
print(f"KS test (1/F(5,10) vs F(10,5)): stat={ks_stat2:.4f}, p={p_value2:.4f}")
```

**실행 결과:**
```
KS test (T^2 vs F(1,10)): stat=0.0025, p=0.9812
KS test (1/F(5,10) vs F(10,5)): stat=0.0031, p=0.9534
```

## 연습문제

**연습문제 1.**
$T \sim t_{15}$ 일 때 $P(T^2 > 4.54)$ 를 구하여라.

??? success "연습문제 1 풀이"
    $T^2 \sim F_{1, 15}$ 이다.

    ```python
    from scipy import stats
    print(f"{stats.f(1, 15).sf(4.54):.4f}")  # 0.0500
    ```

    이는 $P(|T| > \sqrt{4.54}) = P(|T| > 2.131) \approx 0.05$ 와 같으며, 양쪽꼬리 $t$ 검정의 임곗값에 해당한다.

---

**연습문제 2.**
$X_1, \ldots, X_9$ 가 i.i.d. $N(5, 4)$ 이고, 이와 독립으로 $Y_1, \ldots, Y_{13}$ 이 i.i.d. $N(5, 9)$ 라고 하자.
각각의 표본분산을 $S_X^2$ 과 $S_Y^2$ 이라고 하자.

(a) $\frac{8 S_X^2}{4}$ 의 분포를 구하고 그 평균과 분산을 말하여라.

(b) $\frac{S_X^2 / 4}{S_Y^2 / 9}$ 의 분포를 구하고 $P\!\left(\frac{S_X^2 / 4}{S_Y^2 / 9} > 1\right)$ 을 $F$ 분포의 누적분포함수로 나타내어라.

(c) $T = \frac{\bar{X} - 5}{S_X / \sqrt{9}}$ 은 $t$ 분포를 따른다. 그 자유도를 말하고, $T^2$ 이 따르는 $F$ 분포의 두 자유도를 밝혀 확인하여라.

??? success "연습문제 2 풀이"
    (a) $X_i \sim N(5, 4)$ 이고 $n = 9$ 이므로

    $$\frac{(n-1)S_X^2}{\sigma_X^2} = \frac{8 S_X^2}{4} \sim \chi^2_8$$

    이다. 평균은 $8$ 이고 분산은 $2 \cdot 8 = 16$ 이다.

    (b) 각각의 표본분산에 알맞은 상수를 곱한 것이 카이제곱분포를 따르므로

    $$\frac{S_X^2/4}{S_Y^2/9} = \frac{\chi^2_8 / 8}{\chi^2_{12}/12} \sim F_{8, 12}$$

    이다. 따라서 $F_{8,12}$ 분포의 누적분포함수를 $F_{F_{8,12}}$ 라고 하면 $P\!\left(\frac{S_X^2/4}{S_Y^2/9} > 1\right) = 1 - F_{F_{8,12}}(1)$ 이다. 수치로는 대략 $0.488$ 이다.

    (c) $T = \frac{\bar{X} - 5}{S_X / 3} \sim t_8$ 이다(자유도는 $n - 1 = 8$). 그러면

    $$T^2 = \frac{(\bar{X} - 5)^2}{S_X^2 / 9} = \frac{Z^2/1}{\chi^2_8/8} \sim F_{1, 8}$$

    이다. 여기에서 $Z = \frac{\bar{X} - 5}{\sigma_X / 3} \sim N(0,1)$ 이고 $Z^2 \sim \chi^2_1$ 이다.

---

**연습문제 3.**
$F \sim F_{d_1, d_2}$ 일 때 $d_2 \to \infty$ 이면 $d_1 F \xrightarrow{d} \chi^2_{d_1}$ 임을 증명하여라.

*힌트:* 독립인 $V_1 \sim \chi^2_{d_1}$ 과 $V_2 \sim \chi^2_{d_2}$ 에 대하여 $F = \frac{V_1/d_1}{V_2/d_2}$ 로 쓰고 $V_2/d_2$ 에 큰수의 법칙을 적용하여라.

??? success "연습문제 3 풀이"
    독립인 $V_1 \sim \chi^2_{d_1}$ 과 $V_2 \sim \chi^2_{d_2}$ 에 대하여 $F = \frac{V_1/d_1}{V_2/d_2}$ 로 쓴다. 그러면

    $$d_1 F = \frac{V_1}{V_2/d_2}$$

    이다. $W_i \overset{\text{iid}}{\sim} N(0,1)$ 에 대하여 $V_2 = W_1^2 + \cdots + W_{d_2}^2$ 이므로 큰수의 법칙에 따라 다음이 성립한다.

    $$\frac{V_2}{d_2} = \frac{1}{d_2}\sum_{i=1}^{d_2} W_i^2 \xrightarrow{p} E[W_1^2] = 1$$

    $V_1$ 은 $d_2$ 에 의존하지 않고 $V_2/d_2 \xrightarrow{p} 1$ 이므로 슬루츠키 정리에 따라 다음을 얻는다.

    $$d_1 F = \frac{V_1}{V_2/d_2} \xrightarrow{d} \frac{V_1}{1} = V_1 \sim \chi^2_{d_1}$$

    이는 $t_d \to N(0,1)$ 이라는 수렴과 나란한 이야기이다. 둘 다 자유도가 커질수록 분모의 카이제곱 평균이 $1$ 언저리에 몰린다는 사실에서 나온다. $\square$

---

**연습문제 4.**
두 모수를 모두 모르는 정규모집단 $N(\mu, \sigma^2)$ 에 대한 추론의 흐름 전체를 생각해 보자. $X_1, \ldots, X_n$ 을 관측했다고 하자.

(a) $\frac{\bar{X} - \mu}{\sigma/\sqrt{n}}$ 을 $\mu$ 에 대한 피벗으로 바로 쓸 수 없는 까닭과, $\sigma$ 를 $S$ 로 바꾸면 분포가 $N(0,1)$ 에서 $t_{n-1}$ 로 바뀌는 까닭을 설명하여라. 답에는 $\bar{X}$ 과 $S^2$ 의 독립성, 그리고 $(n-1)S^2/\sigma^2$ 의 카이제곱분포가 들어가야 한다.

(b) 이제 크기가 $n_1$ 과 $n_2$ 인 독립인 두 정규표본이 $N(\mu_1, \sigma^2)$ 과 $N(\mu_2, \sigma^2)$ 에서 나왔다고 하자(같은 $\sigma^2$ 이며 그 값은 모른다). 합동표본분산은 다음과 같다.

$$S_p^2 = \frac{(n_1 - 1)S_1^2 + (n_2 - 1)S_2^2}{n_1 + n_2 - 2}$$

카이제곱분포의 가법성을 써서 $\frac{(n_1 + n_2 - 2)S_p^2}{\sigma^2} \sim \chi^2_{n_1 + n_2 - 2}$ 임을 보이고, 이어서 다음을 보여라.

$$\frac{(\bar{X}_1 - \bar{X}_2) - (\mu_1 - \mu_2)}{S_p\sqrt{1/n_1 + 1/n_2}} \sim t_{n_1 + n_2 - 2}$$

??? success "연습문제 4 풀이"
    (a) $\frac{\bar{X} - \mu}{\sigma/\sqrt{n}} \sim N(0,1)$ 에는 모르는 모수 $\sigma$ 가 들어 있으므로 피벗이 될 수 없다(피벗은 자료와 관심 있는 모수만으로 계산할 수 있어야 하며 다른 미지의 값이 끼어들면 안 된다).

    $\sigma$ 를 $S$ 로 바꾸면 $T = \frac{\bar{X} - \mu}{S/\sqrt{n}}$ 이 된다. $S$ 가 확률변수이고 같은 자료에 의존하기에 이 비는 더 이상 정규분포를 따르지 않는다. 고쳐 쓰면

    $$T = \frac{\bar{X} - \mu}{\sigma/\sqrt{n}} \bigg/ \frac{S}{\sigma} = \frac{Z}{\sqrt{V/(n-1)}}$$

    이고, 여기에서 $Z = \frac{\bar{X} - \mu}{\sigma/\sqrt{n}} \sim N(0,1)$ 이고 $V = \frac{(n-1)S^2}{\sigma^2} \sim \chi^2_{n-1}$ 이다. 결정적인 사실은 $\bar{X}$ 과 $S^2$ 이 독립이라는 것이다(다변량정규분포에서 공분산이 $0$ 이면 독립이라는 성질로 증명한다). 따라서 $Z$ 와 $V$ 가 독립이고, $t$ 분포의 정의에 따라 $T \sim t_{n-1}$ 이다.

    (b) 두 표본이 독립이므로 $\frac{(n_1 - 1)S_1^2}{\sigma^2} \sim \chi^2_{n_1 - 1}$ 과 $\frac{(n_2 - 1)S_2^2}{\sigma^2} \sim \chi^2_{n_2 - 1}$ 도 독립이다. 카이제곱분포의 가법성에 따라 다음을 얻는다.

    $$\frac{(n_1 - 1)S_1^2 + (n_2 - 1)S_2^2}{\sigma^2} = \frac{(n_1 + n_2 - 2)S_p^2}{\sigma^2} \sim \chi^2_{n_1 + n_2 - 2}$$

    이표본 $t$ 통계량을 보자. $\bar{X}_1 - \bar{X}_2 \sim N\!\left(\mu_1 - \mu_2, \, \sigma^2(1/n_1 + 1/n_2)\right)$ 이므로

    $$Z = \frac{(\bar{X}_1 - \bar{X}_2) - (\mu_1 - \mu_2)}{\sigma\sqrt{1/n_1 + 1/n_2}} \sim N(0, 1)$$

    이다. $V = \frac{(n_1 + n_2 - 2)S_p^2}{\sigma^2} \sim \chi^2_{n_1 + n_2 - 2}$ 로 두자. $S_p^2$ 은 표본 안의 편차 $X_{ij} - \bar{X}_i$ 에만 의존하고 $Z$ 는 표본평균 $\bar{X}_1$ 과 $\bar{X}_2$ 에만 의존하므로, 각 표본에 표본평균과 표본분산의 독립성을 적용하면 $Z$ 와 $V$ 가 독립임을 알 수 있다. 따라서 다음을 얻는다.

    $$\frac{Z}{\sqrt{V/(n_1 + n_2 - 2)}} = \frac{(\bar{X}_1 - \bar{X}_2) - (\mu_1 - \mu_2)}{\sigma\sqrt{1/n_1 + 1/n_2}} \bigg/ \frac{S_p}{\sigma} = \frac{(\bar{X}_1 - \bar{X}_2) - (\mu_1 - \mu_2)}{S_p\sqrt{1/n_1 + 1/n_2}} \sim t_{n_1+n_2-2}$$

    $\square$
