# 카이제곱분포와의 관계

## 감마분포의 특별한 경우인 카이제곱분포

!!! info "카이제곱분포와 감마분포의 연결"
    자유도가 $d$ 인 **카이제곱분포**는 감마분포의 특별한 경우이다.

    $$\chi^2_d \stackrel{d}{=} \Gamma\!\left(\frac{d}{2}, \frac{1}{2}\right)$$

    특히 다음이 성립한다.

    $$\chi^2_1 \stackrel{d}{=} \Gamma\!\left(\frac{1}{2}, \frac{1}{2}\right)$$

## 유도: Z² ~ χ²₁

$Z \sim N(0, 1)$ 이면 $X = Z^2 \sim \chi^2_1 = \Gamma(1/2, 1/2)$ 이다.

누적분포함수 방법을 쓰면 $x > 0$ 에 대하여 다음이 성립한다.

$$P(X \leq x) = P(Z^2 \leq x) = P(-\sqrt{x} \leq Z \leq \sqrt{x}) = 2\mathcal{N}(\sqrt{x}) - 1$$

미분하면 다음을 얻는다.

$$f_X(x) = 2\phi(\sqrt{x}) \cdot \frac{1}{2\sqrt{x}} = \frac{1}{\sqrt{2\pi}} x^{-1/2} e^{-x/2}$$

이것은 다음과 같이 고쳐 쓸 수 있다.

$$f_X(x) = \frac{(x/2)^{1/2 - 1} e^{-x/2}}{2 \, \Gamma(1/2)} \cdot \frac{1}{1} = \frac{\frac{1}{2}\left(\frac{1}{2}x\right)^{1/2-1} e^{-x/2}}{\Gamma(1/2)}$$

이것이 바로 $\Gamma(1/2, 1/2)$ 의 확률밀도함수이므로 $\chi^2_1 = \Gamma(1/2, 1/2)$ 임이 확인된다.

## 정규확률변수 제곱의 합

$Z_1, Z_2, \ldots, Z_d$ 가 i.i.d. $N(0,1)$ 이면 감마분포의 덧셈 성질에 따라 다음이 성립한다.

$$Z_1^2 + Z_2^2 + \cdots + Z_d^2 \sim \Gamma\!\left(\frac{1}{2}, \frac{1}{2}\right) * \cdots * \Gamma\!\left(\frac{1}{2}, \frac{1}{2}\right) = \Gamma\!\left(\frac{d}{2}, \frac{1}{2}\right) = \chi^2_d$$

## 감마분포에서 얻는 적률

$\chi^2_d = \Gamma(d/2, 1/2)$ 이므로 적률은 감마분포의 공식에서 바로 나온다.

$$E[\chi^2_d] = \frac{d/2}{1/2} = d$$

$$\text{Var}(\chi^2_d) = \frac{d/2}{(1/2)^2} = 2d$$

## 카이제곱분포의 덧셈 성질

카이제곱분포는 비율이 $\lambda = 1/2$ 인 감마분포이므로, 감마분포의 덧셈 성질에서 다음을 얻는다.

$$\chi^2_{d_1} + \chi^2_{d_2} \sim \chi^2_{d_1 + d_2}$$

단, 두 카이제곱확률변수가 독립일 때이다.

## 특별한 경우 요약

| 분포 | 감마분포의 모수 | 모양 $\alpha$ | 비율 $\lambda$ |
|:---:|:---:|:---:|:---:|
| $\text{Exp}(\lambda)$ | $\Gamma(1, \lambda)$ | $1$ | $\lambda$ |
| 얼랑$(k, \lambda)$ | $\Gamma(k, \lambda)$ | $k$ (정수) | $\lambda$ |
| $\chi^2_1$ | $\Gamma(1/2, 1/2)$ | $1/2$ | $1/2$ |
| $\chi^2_d$ | $\Gamma(d/2, 1/2)$ | $d/2$ | $1/2$ |

## 역감마분포

**역감마분포** $\text{IG}(\alpha, \lambda)$ 는 $X \sim \Gamma(\alpha, \lambda)$ 일 때 $1/X$ 의 분포이다. 베이즈 통계에서 분산모수의 켤레사전분포로 쓰인다.

## 파이썬 구현

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

np.random.seed(42)
n_sim = 100000

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# 카이제곱분포 = Gamma(d/2, 1/2) 확인
x = np.linspace(0, 20, 300)
for d in [1, 2, 5, 10]:
    chi2_pdf = stats.chi2.pdf(x, df=d)
    gamma_pdf = stats.gamma.pdf(x, a=d/2, scale=2)  # scale = 1/rate = 2
    axes[0].plot(x, chi2_pdf, '-', lw=2, label=f'χ²({d})')
    axes[0].plot(x, gamma_pdf, '--', lw=1, alpha=0.7)

axes[0].set_title('χ² PDFs (solid) vs Γ(d/2, 1/2) (dashed)')
axes[0].set_xlabel('x')
axes[0].set_ylabel('f(x)')
axes[0].legend()
axes[0].grid(True, alpha=0.3)
axes[0].set_ylim(0, 0.5)

# Z^2 ~ χ²_1 보이기
Z = np.random.standard_normal(n_sim)
X = Z ** 2

axes[1].hist(X, bins=100, density=True, alpha=0.5, range=(0, 8),
             color='blue', label='Z² (simulated)')
x_theory = np.linspace(0.01, 8, 300)
pdf_theory = stats.chi2.pdf(x_theory, df=1)
axes[1].plot(x_theory, pdf_theory, 'r-', lw=2, label='χ²(1) PDF')
axes[1].set_title('Z² ~ χ²(1) = Γ(1/2, 1/2)')
axes[1].set_xlabel('x')
axes[1].set_ylim(0, 2)
axes[1].legend()
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('chi_squared_gamma.png', dpi=150, bbox_inches='tight')
plt.show()

# 덧셈 성질 확인
print("=== Chi-Squared Additivity ===")
for d1, d2 in [(3, 5), (2, 8), (1, 1)]:
    X1 = np.random.chisquare(d1, n_sim)
    X2 = np.random.chisquare(d2, n_sim)
    S = X1 + X2
    print(f"χ²({d1}) + χ²({d2}): mean={np.mean(S):.3f} "
          f"(theory {d1+d2}), var={np.var(S):.3f} (theory {2*(d1+d2)})")
```

## 연습문제

**연습문제 1.**
$Z_1, Z_2, \ldots, Z_8$ 이 i.i.d. $N(0,1)$ 일 때 $W = Z_1^2 + Z_2^2 + \cdots + Z_8^2$ 의 분포와 평균, 분산을 구하여라.

??? success "연습문제 1 풀이"
    $W \sim \chi^2_8 = \Gamma(4, 1/2)$ 이다.

    $E[W] = 8$, $\text{Var}(W) = 16$ 이다.
