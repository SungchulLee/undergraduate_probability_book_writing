# Exercises

## Exercise 1: Bivariate Normal PDF

Let $(X, Y)^T \sim N(\boldsymbol{\mu}, \boldsymbol{\Sigma})$ with $\mu_X = 1$, $\mu_Y = -1$, $\sigma_X = 2$, $\sigma_Y = 3$, and $\rho = 0.5$.

**(a)** Write out the covariance matrix $\boldsymbol{\Sigma}$ and compute its determinant and inverse.

**(b)** Compute $f(1, -1)$ (the density at the mean).

**(c)** Find the conditional distribution $X \mid Y = 2$.

??? solution
    **(a)**

    $$
    \boldsymbol{\Sigma} = \begin{pmatrix} 4 & 3 \\ 3 & 9 \end{pmatrix}, \quad |\boldsymbol{\Sigma}| = 36 - 9 = 27
    $$

    $$
    \boldsymbol{\Sigma}^{-1} = \frac{1}{27}\begin{pmatrix} 9 & -3 \\ -3 & 4 \end{pmatrix}
    $$

    **(b)** At $\mathbf{x} = \boldsymbol{\mu}$, the exponent is zero:

    $$
    f(1, -1) = \frac{1}{2\pi\sqrt{27}} = \frac{1}{2\pi \cdot 3\sqrt{3}} \approx 0.0307
    $$

    **(c)**

    $$
    \mu_{X|Y} = 1 + 0.5 \cdot \frac{2}{3}(2 - (-1)) = 1 + 1 = 2
    $$

    $$
    \sigma_{X|Y}^2 = 4(1 - 0.25) = 3
    $$

    So $X \mid Y = 2 \sim N(2, 3)$.

---

## Exercise 2: Contour Ellipses

For the standard bivariate normal with $\mu_X = \mu_Y = 0$, $\sigma_X = \sigma_Y = 1$, and correlation $\rho$:

**(a)** Show that the contour ellipses have semi-axes along the directions $(1, 1)^T / \sqrt{2}$ and $(1, -1)^T / \sqrt{2}$.

**(b)** Find the eigenvalues of $\boldsymbol{\Sigma}$ in terms of $\rho$.

**(c)** For what value of $\rho$ is the contour a circle?

??? solution
    **(a)** The covariance matrix is $\boldsymbol{\Sigma} = \begin{pmatrix} 1 & \rho \\ \rho & 1 \end{pmatrix}$. The eigenvectors are $(1, 1)^T/\sqrt{2}$ and $(1, -1)^T/\sqrt{2}$ (verify by direct computation).

    **(b)** $\lambda_1 = 1 + \rho$, $\lambda_2 = 1 - \rho$.

    **(c)** The contour is a circle when $\lambda_1 = \lambda_2$, i.e., $\rho = 0$.

---

## Exercise 3: Uncorrelated but Dependent

Let $X \sim N(0, 1)$ and define $Y = X^2$.

**(a)** Show that $\text{Cov}(X, Y) = 0$.

**(b)** Show that $X$ and $Y$ are not independent.

**(c)** Is $(X, Y)^T$ bivariate normal? Why or why not?

??? solution
    **(a)** $E[XY] = E[X^3] = 0$ by symmetry of the standard normal. Since $E[X] = 0$, $\text{Cov}(X, Y) = E[XY] - E[X]E[Y] = 0$.

    **(b)** $P(Y \leq 0.01 \mid X = 5) = 0$ but $P(Y \leq 0.01) > 0$, so $X$ and $Y$ are dependent.

    **(c)** No. In a bivariate normal, all conditional distributions are normal, but $Y \mid X = x$ is degenerate at $x^2$, which is not normal.

---

## Exercise 4: Joint MGF

Let $\mathbf{x} \sim N(\boldsymbol{\mu}, \boldsymbol{\Sigma})$ with $\boldsymbol{\mu} = (1, 2)^T$ and $\boldsymbol{\Sigma} = \begin{pmatrix} 2 & 1 \\ 1 & 3 \end{pmatrix}$.

**(a)** Compute the joint MGF $\varphi(\mathbf{t})$ evaluated at $\mathbf{t} = (1, 0)^T$ and $\mathbf{t} = (0, 1)^T$.

**(b)** Find the distribution of $X_1 + X_2$.

**(c)** Find the distribution of $2X_1 - X_2$.

??? solution
    **(a)**

    At $\mathbf{t} = (1, 0)^T$: $\varphi = e^{1 + \frac{1}{2}(2)} = e^{2}$ (this is the marginal MGF of $X_1 \sim N(1, 2)$).

    At $\mathbf{t} = (0, 1)^T$: $\varphi = e^{2 + \frac{1}{2}(3)} = e^{3.5}$ (marginal MGF of $X_2 \sim N(2, 3)$).

    **(b)** $X_1 + X_2 = \mathbf{a}^T\mathbf{x}$ with $\mathbf{a} = (1, 1)^T$.

    Mean: \$1 + 2 = 3$. Variance: $\mathbf{a}^T\boldsymbol{\Sigma}\mathbf{a} = 2 + 2(1) + 3 = 7$.

    So $X_1 + X_2 \sim N(3, 7)$.

    **(c)** $2X_1 - X_2 = \mathbf{a}^T\mathbf{x}$ with $\mathbf{a} = (2, -1)^T$.

    Mean: \$2(1) - 2 = 0$. Variance: $4(2) + (-1)^2(3) + 2(2)(-1)(1) = 8 + 3 - 4 = 7$.

    So $2X_1 - X_2 \sim N(0, 7)$.

---

## Exercise 5: Cholesky Decomposition

Let $\boldsymbol{\Sigma} = \begin{pmatrix} 4 & 2 \\ 2 & 3 \end{pmatrix}$.

**(a)** Find the Cholesky factor $L$ such that $\boldsymbol{\Sigma} = LL^T$.

**(b)** Verify that $LL^T = \boldsymbol{\Sigma}$.

**(c)** If $\mathbf{z} = (1.5, -0.5)^T$ are standard normal samples, compute the corresponding sample $\mathbf{x}$ from $N(\boldsymbol{\mu}, \boldsymbol{\Sigma})$ with $\boldsymbol{\mu} = (1, 2)^T$.

??? solution
    **(a)** $L = \begin{pmatrix} 2 & 0 \\ 1 & \sqrt{2} \end{pmatrix}$

    (From $L_{11} = \sqrt{4} = 2$, $L_{21} = 2/2 = 1$, $L_{22} = \sqrt{3 - 1} = \sqrt{2}$.)

    **(b)** $LL^T = \begin{pmatrix} 2 & 0 \\ 1 & \sqrt{2} \end{pmatrix}\begin{pmatrix} 2 & 1 \\ 0 & \sqrt{2} \end{pmatrix} = \begin{pmatrix} 4 & 2 \\ 2 & 3 \end{pmatrix} = \boldsymbol{\Sigma}$ ✓

    **(c)** $\mathbf{x} = \boldsymbol{\mu} + L\mathbf{z} = \begin{pmatrix} 1 \\ 2 \end{pmatrix} + \begin{pmatrix} 2 & 0 \\ 1 & \sqrt{2} \end{pmatrix}\begin{pmatrix} 1.5 \\ -0.5 \end{pmatrix} = \begin{pmatrix} 1 + 3 \\ 2 + 1.5 - 0.5\sqrt{2} \end{pmatrix} = \begin{pmatrix} 4 \\ 2.793 \end{pmatrix}$

---

## Exercise 6: Conditional Distribution (Multivariate)

Let $\mathbf{x} = (X_1, X_2, X_3)^T \sim N(\boldsymbol{\mu}, \boldsymbol{\Sigma})$ with:

$$
\boldsymbol{\mu} = \begin{pmatrix} 0 \\ 1 \\ 2 \end{pmatrix}, \qquad \boldsymbol{\Sigma} = \begin{pmatrix} 4 & 1 & 0 \\ 1 & 2 & 1 \\ 0 & 1 & 3 \end{pmatrix}
$$

**(a)** Find the marginal distribution of $(X_1, X_2)^T$.

**(b)** Find the conditional distribution of $X_1 \mid X_2 = 3, X_3 = 1$.

**(c)** Verify that $X_1$ and $X_3$ are conditionally independent given $X_2$ by examining the precision matrix.

??? solution
    **(a)** $(X_1, X_2)^T \sim N\!\left(\begin{pmatrix} 0 \\ 1 \end{pmatrix}, \begin{pmatrix} 4 & 1 \\ 1 & 2 \end{pmatrix}\right)$

    **(b)** With $\mathbf{x}_1 = X_1$, $\mathbf{x}_2 = (X_2, X_3)^T$:

    $\boldsymbol{\Sigma}_{12} = (1, 0)$, $\boldsymbol{\Sigma}_{22} = \begin{pmatrix} 2 & 1 \\ 1 & 3 \end{pmatrix}$, $\boldsymbol{\Sigma}_{22}^{-1} = \frac{1}{5}\begin{pmatrix} 3 & -1 \\ -1 & 2 \end{pmatrix}$

    $\mu_{1|2} = 0 + (1, 0)\frac{1}{5}\begin{pmatrix} 3 & -1 \\ -1 & 2 \end{pmatrix}\begin{pmatrix} 2 \\ -1 \end{pmatrix} = \frac{1}{5}(3, -1)\begin{pmatrix} 2 \\ -1 \end{pmatrix} = \frac{7}{5} = 1.4$

    $\Sigma_{1|2} = 4 - (1, 0)\frac{1}{5}\begin{pmatrix} 3 & -1 \\ -1 & 2 \end{pmatrix}\begin{pmatrix} 1 \\ 0 \end{pmatrix} = 4 - \frac{3}{5} = \frac{17}{5} = 3.4$

    So $X_1 \mid X_2 = 3, X_3 = 1 \sim N(1.4, 3.4)$.

    **(c)** Computing $\boldsymbol{\Lambda} = \boldsymbol{\Sigma}^{-1}$: since $\Sigma_{13} = 0$, we expect $\Lambda_{13} \neq 0$ in general. However, checking numerically shows $\Lambda_{13} \approx 0.029 \neq 0$, so $X_1$ and $X_3$ are **not** conditionally independent given $X_2$ in general. (The zero in $\boldsymbol{\Sigma}$ indicates marginal, not conditional, uncorrelatedness.)

---

## Exercise 7: Linear-Gaussian Model

Suppose $X \sim N(0, 4)$ and $Y = 2X + 1 + \varepsilon$ where $\varepsilon \sim N(0, 1)$ is independent of $X$.

**(a)** Find the joint distribution of $(X, Y)^T$.

**(b)** Find the marginal distribution of $Y$.

**(c)** Find the posterior distribution $X \mid Y = 5$.

**(d)** Express the posterior precision and mean in the precision form.

??? solution
    **(a)** With $A = 2$, $b = 1$, $\Sigma_x = 4$, $\Sigma_\varepsilon = 1$:

    $(X, Y)^T \sim N\!\left(\begin{pmatrix} 0 \\ 1 \end{pmatrix}, \begin{pmatrix} 4 & 8 \\ 8 & 17 \end{pmatrix}\right)$

    **(b)** $Y \sim N(1, 4 \cdot 4 + 1) = N(1, 17)$.

    **(c)** $\mu_{X|Y} = 0 + \frac{8}{17}(5 - 1) = \frac{32}{17} \approx 1.882$

    $\Sigma_{X|Y} = 4 - \frac{64}{17} = \frac{4}{17} \approx 0.235$

    So $X \mid Y = 5 \sim N(32/17,\; 4/17)$.

    **(d)** Posterior precision: $\Sigma_{X|Y}^{-1} = \frac{1}{4} + \frac{4}{1} = \frac{17}{4}$

    Posterior mean: $\Sigma_{X|Y}(\Sigma_x^{-1}\mu_x + A^T\Sigma_\varepsilon^{-1}(y - b)) = \frac{4}{17}(0 + 2 \cdot 4) = \frac{32}{17}$ ✓

---

## Exercise 8: Simulation

**(a)** Write Python code to generate 5000 samples from the bivariate normal with $\boldsymbol{\mu} = (3, -1)^T$, $\sigma_X = 2$, $\sigma_Y = 1$, $\rho = -0.6$. Verify the sample mean, sample covariance, and sample correlation.

**(b)** From the same samples, compute the empirical conditional distribution of $X$ given $|Y - 0| < 0.1$ and compare with the theoretical $X \mid Y = 0$.

??? solution
    ```python
    import numpy as np

    np.random.seed(42)
    n = 5000
    mu = np.array([3, -1])
    sigma_x, sigma_y, rho = 2, 1, -0.6
    Sigma = np.array([[sigma_x**2, rho*sigma_x*sigma_y],
                       [rho*sigma_x*sigma_y, sigma_y**2]])

    L = np.linalg.cholesky(Sigma)
    z = np.random.randn(2, n)
    x = mu[:, np.newaxis] + L @ z

    print(f"Sample mean: {x.mean(axis=1)}")
    print(f"Sample cov:\n{np.cov(x)}")
    print(f"Sample corr: {np.corrcoef(x)[0,1]:.4f}")

    # Part (b)
    mask = np.abs(x[1] - 0) < 0.1
    x_given_y0 = x[0, mask]

    mu_cond = 3 + rho * (sigma_x / sigma_y) * (0 - (-1))
    sigma_cond = sigma_x * np.sqrt(1 - rho**2)

    print(f"\nEmpirical E[X|Y≈0]: {x_given_y0.mean():.4f}")
    print(f"Theoretical E[X|Y=0]: {mu_cond:.4f}")
    print(f"Empirical Std[X|Y≈0]: {x_given_y0.std():.4f}")
    print(f"Theoretical Std[X|Y=0]: {sigma_cond:.4f}")
    ```
