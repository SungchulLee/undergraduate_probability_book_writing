# Beta Distribution Definition


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

## The Beta Function

!!! info "Beta Function"
    For $\alpha > 0$ and $\beta > 0$, the **Beta function** is:

    $$B(\alpha, \beta) = \int_0^1 x^{\alpha - 1}(1 - x)^{\beta - 1} \, dx$$

    It is related to the Gamma function by:

    $$B(\alpha, \beta) = \frac{\Gamma(\alpha)\,\Gamma(\beta)}{\Gamma(\alpha + \beta)}$$

## Definition

!!! info "Beta Distribution"
    A continuous random variable $X$ has the **Beta distribution** with parameters $\alpha > 0$ and $\beta > 0$, written $X \sim \text{Beta}(\alpha, \beta)$, if its PDF is:

    $$f(x) = \frac{x^{\alpha - 1}(1 - x)^{\beta - 1}}{B(\alpha, \beta)}, \quad 0 < x < 1$$

    Equivalently, since the PDF is proportional to $x^{\alpha-1}(1-x)^{\beta-1}$:

    $$f(x) \propto x^{\alpha - 1}(1 - x)^{\beta - 1}$$

    and the Beta function $B(\alpha, \beta)$ is the normalizing constant that ensures the PDF integrates to 1.

## Mean and Variance

!!! info "Moments of Beta(α, β)"

    $$E[X] = \frac{\alpha}{\alpha + \beta}, \qquad \text{Var}(X) = \frac{\alpha\beta}{(\alpha + \beta)^2(\alpha + \beta + 1)}$$

The mean $\frac{\alpha}{\alpha + \beta}$ is the ratio of $\alpha$ to the total $\alpha + \beta$, which has a natural interpretation as a "fraction" or "proportion."

## Intuition: Fraction of Waiting Time

The Beta distribution arises naturally from the Gamma distribution. If $X \sim \Gamma(\alpha, \lambda)$ and $Y \sim \Gamma(\beta, \lambda)$ are **independent**, then:

1. The total $T = X + Y \sim \Gamma(\alpha + \beta, \lambda)$
2. The fraction $F = \dfrac{X}{X + Y} \sim \text{Beta}(\alpha, \beta)$
3. $T$ and $F$ are **independent**
4. The Beta function identity $B(\alpha, \beta) = \dfrac{\Gamma(\alpha)\,\Gamma(\beta)}{\Gamma(\alpha + \beta)}$ follows as a byproduct

### Proof via Jacobian

Let $X \sim \Gamma(\alpha, \lambda)$ and $Y \sim \Gamma(\beta, \lambda)$ be independent. Define:

$$t = x + y, \qquad f = \frac{x}{x + y}$$

so $x = tf$ and $y = t(1-f)$.

**Jacobian computation:**

$$\frac{\partial(t, f)}{\partial(x, y)} = \det \begin{pmatrix} 1 & 1 \\ \frac{t - x}{t^2} & -\frac{x}{t^2} \end{pmatrix} = -\frac{1}{t}$$

Therefore $\left|\frac{\partial(x, y)}{\partial(t, f)}\right| = t$.

**Joint density transformation:**

$$f_{T,F}(t, f) = f_{X,Y}(x, y) \left|\frac{\partial(x, y)}{\partial(t, f)}\right|$$

$$= \frac{\lambda(\lambda x)^{\alpha-1} e^{-\lambda x}}{\Gamma(\alpha)} \cdot \frac{\lambda(\lambda y)^{\beta-1} e^{-\lambda y}}{\Gamma(\beta)} \cdot t$$

Substituting $x = tf$, $y = t(1-f)$ and simplifying:

$$f_{T,F}(t, f) = \underbrace{\frac{f^{\alpha-1}(1-f)^{\beta-1}}{\Gamma(\alpha)\Gamma(\beta)/\Gamma(\alpha+\beta)}}_{\text{function of } f \text{ only}} \cdot \underbrace{\frac{\lambda(\lambda t)^{(\alpha+\beta)-1} e^{-\lambda t}}{\Gamma(\alpha + \beta)}}_{\text{function of } t \text{ only}}$$

$$= \underbrace{\frac{f^{\alpha-1}(1-f)^{\beta-1}}{B(\alpha, \beta)}}_{\text{Beta}(\alpha, \beta) \text{ PDF}} \cdot \underbrace{\frac{\lambda(\lambda t)^{(\alpha+\beta)-1} e^{-\lambda t}}{\Gamma(\alpha + \beta)}}_{\Gamma(\alpha+\beta, \lambda) \text{ PDF}}$$

Since the joint PDF factors into a function of $f$ only times a function of $t$ only, $T$ and $F$ are **independent**, with:

- $F \sim \text{Beta}(\alpha, \beta)$
- $T \sim \Gamma(\alpha + \beta, \lambda)$

As a byproduct, comparing the normalizing constants gives $B(\alpha, \beta) = \frac{\Gamma(\alpha)\Gamma(\beta)}{\Gamma(\alpha + \beta)}$.

## Special Cases

| Parameters | Distribution | Shape |
|:---:|:---:|:---|
| $\text{Beta}(1, 1)$ | $U(0, 1)$ | Flat (uniform) |
| $\text{Beta}(\alpha, \alpha)$ | Symmetric | Symmetric about $1/2$ |
| $\text{Beta}(1, \beta)$ | — | Decreasing, concentrated near $0$ |
| $\text{Beta}(\alpha, 1)$ | — | Increasing, concentrated near $1$ |
| $\alpha, \beta > 1$ | — | Unimodal, bell-shaped |
| $\alpha, \beta < 1$ | — | U-shaped, concentrated at endpoints |

## Worked Example: Fraction of Waiting Time at Bank

??? example "Example: Bank and Post Office"
    When you enter a bank, one person is in line and there are 5 service desks with iid $\text{Exp}(\lambda_B)$ service times where $\lambda_B^{-1} = 10$ minutes. After the bank, you visit a post office where 2 people are in line, there are 2 service desks, and service times are iid $\text{Exp}(\lambda_P)$ where $\lambda_P^{-1} = 4$ minutes.

    Let $F$ be the fraction of total waiting time spent at the bank. Calculate $E[F]$ and $\text{Var}(F)$.

    **Bank waiting time:** With 5 desks, effective rate is $5\lambda_B = 0.5$/min. Two customers to serve:

    $$T_B = X_1 + X_2, \quad X_i \stackrel{\text{iid}}{\sim} \text{Exp}(0.5) \implies T_B \sim \Gamma(2, 0.5)$$

    **Post office waiting time:** With 2 desks, effective rate is $2\lambda_P = 0.5$/min. Three customers to serve:

    $$T_P = Y_1 + Y_2 + Y_3, \quad Y_j \stackrel{\text{iid}}{\sim} \text{Exp}(0.5) \implies T_P \sim \Gamma(3, 0.5)$$

    Since $T_B$ and $T_P$ are independent with the **same rate** $\lambda = 0.5$:

    $$F = \frac{T_B}{T_B + T_P} \sim \text{Beta}(2, 3)$$

    With $\alpha = 2$, $\beta = 3$:

    $$E[F] = \frac{2}{2 + 3} = \frac{2}{5} = 0.4$$

    $$\text{Var}(F) = \frac{2 \cdot 3}{5^2 \cdot 6} = \frac{6}{150} = \frac{1}{25} = 0.04$$

## Worked Example: Joint PDF with Beta Marginals

??? example "Example: Dependent Random Variables with Beta Marginals"
    The joint PDF of $X$ and $Y$ is given by:

    $$f(x, y) = cxy, \quad 0 \leq x \leq 1, \; 0 \leq y \leq 1, \; 0 \leq x + y \leq 1$$

    **(a) Find $c$.**

    $$\int_0^1 \int_0^{1-y} cxy \, dx \, dy = \frac{c}{2} \int_0^1 y(1-y)^2 \, dy = \frac{c}{2} B(2, 3)$$

    Recognizing the Beta integral: $\int_0^1 y^{2-1}(1-y)^{3-1} dy = B(2,3) = \frac{\Gamma(2)\Gamma(3)}{\Gamma(5)} = \frac{1! \cdot 2!}{4!} = \frac{1}{12}$

    So $\frac{c}{2} \cdot \frac{1}{12} = 1 \implies c = 24$.

    **(b) Find the marginal PDFs.**

    For $0 \leq x \leq 1$:

    $$f_X(x) = \int_0^{1-x} 24xy \, dy = 12x(1-x)^2 = \frac{x^{2-1}(1-x)^{3-1}}{B(2,3)}$$

    So $X \sim \text{Beta}(2, 3)$, and by symmetry $Y \sim \text{Beta}(2, 3)$.

    **(c) Are $X$ and $Y$ independent?**

    No. The constraint $x + y \leq 1$ prevents factorization:

    $$f(x,y) = 24xy \cdot \mathbf{1}(0 \leq x \leq 1) \cdot \mathbf{1}(0 \leq y \leq 1) \cdot \underbrace{\mathbf{1}(x + y \leq 1)}_{\text{cannot decompose}}$$

    If they were independent, $X + Y$ could range up to 2, but the joint PDF puts no mass on $x + y > 1$.

## Python Implementation

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Plot Beta PDFs
x = np.linspace(0.001, 0.999, 300)
params = [(1, 5), (2, 4), (3, 3), (4, 2), (5, 1)]
colors = ['blue', 'red', 'magenta', 'black', 'cyan']

for (a, b), color in zip(params, colors):
    pdf = stats.beta.pdf(x, a, b)
    axes[0].plot(x, pdf, color=color, lw=2,
                 label=f'α={a}, β={b}')

axes[0].set_title('PDF of Beta Distribution')
axes[0].set_xlabel('x')
axes[0].set_ylabel('f(x)')
axes[0].set_ylim(0, 6)
axes[0].legend()
axes[0].grid(True, alpha=0.3)

# Verify Gamma-Beta connection
np.random.seed(42)
n_sim = 100000
alpha, beta_param = 2, 3
lam = 0.5

X_gamma = np.random.gamma(shape=alpha, scale=1/lam, size=n_sim)
Y_gamma = np.random.gamma(shape=beta_param, scale=1/lam, size=n_sim)
F = X_gamma / (X_gamma + Y_gamma)

axes[1].hist(F, bins=60, density=True, alpha=0.5, color='steelblue',
             label='X/(X+Y) simulated')
x_theory = np.linspace(0.001, 0.999, 200)
pdf_theory = stats.beta.pdf(x_theory, alpha, beta_param)
axes[1].plot(x_theory, pdf_theory, 'r-', lw=2,
             label=f'Beta({alpha},{beta_param}) PDF')
axes[1].set_title(f'Γ({alpha},λ) / [Γ({alpha},λ)+Γ({beta_param},λ)] ~ Beta({alpha},{beta_param})')
axes[1].set_xlabel('f')
axes[1].legend()
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('beta_definition.png', dpi=150, bbox_inches='tight')
plt.show()

# Verify independence of T and F
T = X_gamma + Y_gamma
corr = np.corrcoef(T, F)[0, 1]
print(f"Correlation between T and F: {corr:.6f} (should be ≈ 0)")
print(f"E[F] = {np.mean(F):.4f} (theory {alpha/(alpha+beta_param):.4f})")
var_theory = alpha * beta_param / ((alpha+beta_param)**2 * (alpha+beta_param+1))
print(f"Var(F) = {np.var(F):.4f} (theory {var_theory:.4f})")
```
