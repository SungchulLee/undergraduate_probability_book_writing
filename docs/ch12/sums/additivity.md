# 독립인 푸아송확률변수의 가법성

## 정리의 서술

!!! info "푸아송분포의 가법성"
    $X \sim \text{Po}(\lambda_1)$ 과 $Y \sim \text{Po}(\lambda_2)$ 가 **독립**이면 다음이 성립한다.

    $$
    X + Y \sim \text{Po}(\lambda_1 + \lambda_2)
    $$

    더 일반적으로 $X_1, X_2, \ldots, X_n$ 이 독립이고 $X_i \sim \text{Po}(\lambda_i)$ 이면 다음이 성립한다.

    $$
    \sum_{i=1}^{n} X_i \sim \text{Po}\!\left(\sum_{i=1}^{n} \lambda_i\right)
    $$

이것은 푸아송분포를 모형으로 삼거나 계산하는 데 특히 편리하게 만들어 주는 근본적인 성질이다.

---

## 합성곱을 쓴 증명

독립인 $X \sim \text{Po}(\lambda_1)$ 과 $Y \sim \text{Po}(\lambda_2)$ 에 대하여 합성곱 공식으로 $Z = X + Y$ 의 확률질량함수를 계산한다.

$$
P(Z = k) = \sum_{j=0}^{k} P(X = j) \, P(Y = k - j)
$$

푸아송분포의 확률질량함수를 대입하면 다음과 같다.

$$
P(Z = k) = \sum_{j=0}^{k} \frac{e^{-\lambda_1} \lambda_1^j}{j!} \cdot \frac{e^{-\lambda_2} \lambda_2^{k-j}}{(k-j)!}
$$

$$
= e^{-(\lambda_1 + \lambda_2)} \sum_{j=0}^{k} \frac{\lambda_1^j \lambda_2^{k-j}}{j!(k-j)!}
$$

$$
= \frac{e^{-(\lambda_1 + \lambda_2)}}{k!} \sum_{j=0}^{k} \binom{k}{j} \lambda_1^j \lambda_2^{k-j}
$$

이항정리에 따라 $\sum_{j=0}^{k} \binom{k}{j} \lambda_1^j \lambda_2^{k-j} = (\lambda_1 + \lambda_2)^k$ 이므로 다음을 얻는다.

$$
P(Z = k) = \frac{e^{-(\lambda_1 + \lambda_2)} (\lambda_1 + \lambda_2)^k}{k!}
$$

이것은 $\text{Po}(\lambda_1 + \lambda_2)$ 의 확률질량함수이다.

---

## 적률생성함수를 쓴 증명

$X \sim \text{Po}(\lambda)$ 의 적률생성함수는 다음과 같다.

$$
M_X(t) = E[e^{tX}] = e^{\lambda(e^t - 1)}
$$

독립인 $X \sim \text{Po}(\lambda_1)$ 과 $Y \sim \text{Po}(\lambda_2)$ 에 대하여 다음이 성립한다.

$$
M_{X+Y}(t) = M_X(t) \cdot M_Y(t) = e^{\lambda_1(e^t - 1)} \cdot e^{\lambda_2(e^t - 1)} = e^{(\lambda_1 + \lambda_2)(e^t - 1)}
$$

적률생성함수의 유일성 정리에 따라 $X + Y \sim \text{Po}(\lambda_1 + \lambda_2)$ 이다.

---

## 푸아송 과정과의 관계: 합침

가법성은 **푸아송 과정**(13장에서 다룬다)으로 자연스럽게 풀이할 수 있다.

강도가 $\lambda_1$ 과 $\lambda_2$ 인 독립인 푸아송 과정 둘이 있을 때, 이 둘을 합치면 강도가 $\lambda_1 + \lambda_2$ 인 푸아송 과정이 된다. 어떤 구간에서 일어난 사건의 개수는 각 과정에서 일어난 개수의 합이며, 이것이 바로 가법성이다.

---

## 중요: 독립성이 반드시 필요하다

가법성에는 독립성이 필요하다. $X$ 와 $Y$ 가 종속인 푸아송확률변수라면 그 합은 일반적으로 푸아송분포를 따르지 **않는다**.

```python
import numpy as np
from scipy.stats import poisson, kstest

np.random.seed(42)
n = 100_000
la1, la2 = 3, 5

# 독립인 경우: 합은 푸아송분포를 따른다
X_ind = np.random.poisson(la1, n)
Y_ind = np.random.poisson(la2, n)
Z_ind = X_ind + Y_ind

# 종속인 경우: 합은 푸아송분포를 따르지 않는다
# (예: Y = X + Poisson(2)로 두면 서로 종속이 된다)
X_dep = np.random.poisson(la1, n)
Y_dep = X_dep + np.random.poisson(la2 - la1, n)  # Y가 X에 기대고 있다
Z_dep = X_dep + Y_dep

print("Independent case:")
print(f"  Z mean = {Z_ind.mean():.3f}, var = {Z_ind.var():.3f}")
print(f"  Expected: mean = {la1+la2}, var = {la1+la2}")

print("\nDependent case:")
print(f"  Z mean = {Z_dep.mean():.3f}, var = {Z_dep.var():.3f}")
print(f"  Note: var ≠ mean, so Z is NOT Poisson")
```

---

## 수치로 확인하기

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson

np.random.seed(42)
la1, la2 = 3, 7
la_sum = la1 + la2
n_samples = 100_000

# 독립인 푸아송확률변수의 합을 모의실험한다
X = np.random.poisson(la1, n_samples)
Y = np.random.poisson(la2, n_samples)
Z = X + Y

# 경험적 분포를 Po(λ1 + λ2)와 견주어 본다
k = np.arange(0, 30)
empirical_pmf = np.array([(Z == ki).mean() for ki in k])
theoretical_pmf = poisson.pmf(k, la_sum)

fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# 확률질량함수 비교
axes[0].bar(k - 0.2, empirical_pmf, width=0.4, alpha=0.7,
            label=f'Empirical X+Y', color='steelblue')
axes[0].bar(k + 0.2, theoretical_pmf, width=0.4, alpha=0.7,
            label=f'Po({la_sum})', color='coral')
axes[0].set_title(f'Po({la1}) + Po({la2}) = Po({la_sum})')
axes[0].set_xlabel('k')
axes[0].set_ylabel('P(Z = k)')
axes[0].legend()
axes[0].grid(True, alpha=0.3)

# 차이 그림
axes[1].bar(k, empirical_pmf - theoretical_pmf, color='gray', alpha=0.7)
axes[1].axhline(y=0, color='black', linewidth=0.5)
axes[1].set_title('Difference (Empirical − Theoretical)')
axes[1].set_xlabel('k')
axes[1].set_ylabel('PMF difference')
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('poisson_additivity.png', dpi=150, bbox_inches='tight')
plt.show()

print(f"Sample mean:  {Z.mean():.3f}  (theoretical: {la_sum})")
print(f"Sample var:   {Z.var(ddof=1):.3f}  (theoretical: {la_sum})")
```

---

## 응용: 여러 원천에서 온 개수를 합치기

실제로 서로 독립인 여러 원천에서 오는 사건이 각각 푸아송분포를 따르면 전체 개수도 푸아송분포를 따른다. 예를 들면 다음과 같다.

- **콜센터**: A 지역에서 시간당 $\lambda_1 = 5$ 의 비율로, B 지역에서 시간당 $\lambda_2 = 3$ 의 비율로 전화가 걸려 온다. 시간당 전체 전화 건수는 $\text{Po}(8)$ 을 따른다.

- **보험**: 자동차 보험의 청구($\lambda_1$)와 주택 보험의 청구($\lambda_2$)가 독립이면, 전체 청구 건수는 $\text{Po}(\lambda_1 + \lambda_2)$ 를 따른다.

- **금융**: 비율이 $\lambda_1, \lambda_2, \ldots, \lambda_n$ 인 독립된 신용 포트폴리오들에서 일어나는 부도 사건의 전체 개수는 $\text{Po}(\sum \lambda_i)$ 를 따른다.


## 연습문제

**연습문제 1.**
어떤 가게에 서로 독립인 세 가지 경로로 손님이 들어온다.

- 걸어 들어오는 손님: 시간당 $X_1 \sim \text{Po}(8)$
- 온라인으로 주문하고 찾아가는 손님: 시간당 $X_2 \sim \text{Po}(5)$
- 전화로 주문하는 손님: 시간당 $X_3 \sim \text{Po}(2)$

**(a)** 시간당 전체 손님 수의 분포는 무엇인가?

**(b)** $P(\text{전체} > 20)$ 과 $P(\text{전체} = 15)$ 를 계산하여라.

**(c)** 10,000시간을 모의실험하여 이론적인 분포를 확인하여라.

??? success "연습문제 1 풀이"

    **(a)** 가법성에 따라 $X_1 + X_2 + X_3 \sim \text{Po}(8 + 5 + 2) = \text{Po}(15)$ 이다.

    **(b)**

    ```python
    from scipy.stats import poisson

    la = 15
    print(f"P(total > 20) = {1 - poisson.cdf(20, la):.6f}")
    print(f"P(total = 15) = {poisson.pmf(15, la):.6f}")
    ```

    **(c)**

    ```python
    import numpy as np

    np.random.seed(42)
    n_sim = 10_000

    X1 = np.random.poisson(8, n_sim)
    X2 = np.random.poisson(5, n_sim)
    X3 = np.random.poisson(2, n_sim)
    total = X1 + X2 + X3

    print(f"Sample mean: {total.mean():.3f} (theoretical: 15)")
    print(f"Sample var:  {total.var(ddof=1):.3f} (theoretical: 15)")
    ```
