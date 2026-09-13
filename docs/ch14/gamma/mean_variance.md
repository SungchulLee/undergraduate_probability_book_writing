# 평균과 분산

## 평균

!!! info "Γ(α, λ) 의 평균"
    $X \sim \Gamma(\alpha, \lambda)$ 이면 다음이 성립한다.

    $$E[X] = \frac{\alpha}{\lambda}$$

### 유도

$$E[X] = \int_0^\infty x \cdot \frac{\lambda(\lambda x)^{\alpha - 1} e^{-\lambda x}}{\Gamma(\alpha)} \, dx$$

핵심 요령은 **적분 안에서 감마분포의 확률밀도함수를 알아보는 것**이다. 적당히 곱하고 나누어 $\Gamma(\alpha + 1, \lambda)$ 의 확률밀도함수를 만든다.

$$E[X] = \frac{\Gamma(\alpha + 1)}{\lambda \, \Gamma(\alpha)} \int_0^\infty \underbrace{\frac{\lambda(\lambda x)^{(\alpha+1)-1} e^{-\lambda x}}{\Gamma(\alpha + 1)}}_{\Gamma(\alpha+1, \lambda) \text{ 의 확률밀도함수}} \, dx = \frac{\alpha \, \Gamma(\alpha)}{\lambda \, \Gamma(\alpha)} = \frac{\alpha}{\lambda}$$

적분하는 대상이 올바른 확률밀도함수이므로 적분값은 $1$ 이고, $\Gamma(\alpha + 1) = \alpha \, \Gamma(\alpha)$ 를 썼다.

## 이차 적률

$$E[X^2] = \int_0^\infty x^2 \cdot \frac{\lambda(\lambda x)^{\alpha - 1} e^{-\lambda x}}{\Gamma(\alpha)} \, dx$$

마찬가지로 $\Gamma(\alpha + 2, \lambda)$ 의 확률밀도함수를 만든다.

$$E[X^2] = \frac{\Gamma(\alpha + 2)}{\lambda^2 \, \Gamma(\alpha)} \int_0^\infty \underbrace{\frac{\lambda(\lambda x)^{(\alpha+2)-1} e^{-\lambda x}}{\Gamma(\alpha + 2)}}_{\Gamma(\alpha+2, \lambda) \text{ 의 확률밀도함수}} \, dx = \frac{(\alpha + 1)\alpha \, \Gamma(\alpha)}{\lambda^2 \, \Gamma(\alpha)} = \frac{\alpha(\alpha + 1)}{\lambda^2}$$

여기서는 $\Gamma(\alpha + 2) = (\alpha + 1) \alpha \, \Gamma(\alpha)$ 를 썼다.

## 분산

!!! info "Γ(α, λ) 의 분산"
    $X \sim \Gamma(\alpha, \lambda)$ 이면 다음이 성립한다.

    $$\text{Var}(X) = \frac{\alpha}{\lambda^2}$$

### 유도

$$\text{Var}(X) = E[X^2] - (E[X])^2 = \frac{\alpha(\alpha + 1)}{\lambda^2} - \frac{\alpha^2}{\lambda^2} = \frac{\alpha}{\lambda^2}$$

## 적률을 구하는 일반적인 방법

위의 유도는 쓸모 있는 요령 하나를 보여 준다. 감마확률변수의 $E[X^k]$ 를 구하려면 **피적분함수를 모수가 옮겨진 감마분포의 확률밀도함수 꼴로 다시 빚은 뒤**, 확률밀도함수의 적분이 1이라는 사실을 쓰면 된다.

일반적으로 $X \sim \Gamma(\alpha, \lambda)$ 에 대하여 다음이 성립한다.

$$E[X^k] = \frac{\Gamma(\alpha + k)}{\lambda^k \, \Gamma(\alpha)}$$

## 정리하며: 이산과 연속의 대응

| 분포 | 평균 | 분산 |
|:---:|:---:|:---:|
| $\text{Geo}(p)$ | $\dfrac{1}{p}$ | $\dfrac{q}{p^2}$ |
| $\text{NegBin}(n, p)$ | $\dfrac{n}{p}$ | $\dfrac{nq}{p^2}$ |
| $\text{Exp}(\lambda)$ | $\dfrac{1}{\lambda}$ | $\dfrac{1}{\lambda^2}$ |
| $\Gamma(n, \lambda)$ | $\dfrac{n}{\lambda}$ | $\dfrac{n}{\lambda^2}$ |
| $\Gamma(\alpha, \lambda)$ | $\dfrac{\alpha}{\lambda}$ | $\dfrac{\alpha}{\lambda^2}$ |

규칙이 뚜렷하다. 모양모수 $\alpha$ 는 평균과 분산을 모두 일차로 키우고, 비율모수 $\lambda$ 는 분모에 나타난다(평균에는 한 번, 분산에는 제곱으로).

## 파이썬 구현

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

np.random.seed(42)
n_sim = 100000

# 여러 (alpha, lambda) 짝에 대해 평균과 분산을 확인한다
print("=== Mean and Variance Verification ===")
print(f"{'α':>5} {'λ':>5} | {'E[X] theory':>12} {'E[X] sim':>10} | "
      f"{'Var theory':>12} {'Var sim':>10}")
print("-" * 70)

params = [(1, 1), (2, 1), (3, 2), (5, 2), (0.5, 0.5), (10, 3)]
for alpha, lam in params:
    X = np.random.gamma(shape=alpha, scale=1/lam, size=n_sim)
    mean_theory = alpha / lam
    var_theory = alpha / lam**2
    print(f"{alpha:5.1f} {lam:5.1f} | {mean_theory:12.4f} {np.mean(X):10.4f} | "
          f"{var_theory:12.4f} {np.var(X):10.4f}")

# alpha 가 커질 때 평균과 분산이 어떻게 달라지는지 본다
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

lam = 2.0
alphas = np.linspace(0.5, 10, 20)
x = np.linspace(0, 10, 300)

# 평균을 표시한 확률밀도함수
for alpha in [1, 2, 4, 8]:
    pdf = stats.gamma.pdf(x, a=alpha, scale=1/lam)
    mean = alpha / lam
    axes[0].plot(x, pdf, lw=2, label=f'α={alpha}, E[X]={mean:.1f}')
    axes[0].axvline(mean, linestyle=':', alpha=0.4)

axes[0].set_title(f'Gamma PDFs with Means (λ={lam})')
axes[0].set_xlabel('x')
axes[0].set_ylabel('f(x)')
axes[0].legend()
axes[0].grid(True, alpha=0.3)

# alpha 의 함수로 본 평균과 분산
means = alphas / lam
variances = alphas / lam**2
sds = np.sqrt(variances)

axes[1].plot(alphas, means, 'b-', lw=2, label='E[X] = α/λ')
axes[1].plot(alphas, variances, 'r-', lw=2, label='Var(X) = α/λ²')
axes[1].plot(alphas, sds, 'g--', lw=2, label='SD(X) = √α/λ')
axes[1].set_title(f'Moments vs Shape Parameter (λ={lam})')
axes[1].set_xlabel('α')
axes[1].set_ylabel('Value')
axes[1].legend()
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('gamma_mean_variance.png', dpi=150, bbox_inches='tight')
plt.show()
```


## 연습문제

**연습문제 1.**
$X \sim \Gamma(3, 2)$ 라 하자. $E[X]$, $\text{Var}(X)$, $E[X^2]$ 을 구하여라.

??? success "연습문제 1 풀이"
    $E[X] = \alpha/\lambda = 3/2 = 1.5$

    $\text{Var}(X) = \alpha/\lambda^2 = 3/4 = 0.75$

    $E[X^2] = \text{Var}(X) + (E[X])^2 = 0.75 + 2.25 = 3.0$

    다른 방법으로는 $E[X^2] = \alpha(\alpha+1)/\lambda^2 = 3 \cdot 4 / 4 = 3.0$ 이다.
