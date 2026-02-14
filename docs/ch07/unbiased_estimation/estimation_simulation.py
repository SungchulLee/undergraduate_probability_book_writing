"""Estimation Simulation: demonstrate unbiased estimation of mean and variance."""
import numpy as np
import matplotlib.pyplot as plt


def main():
    np.random.seed(42)

    true_mu = 2.0
    true_sigma = 2.0
    n_samples = 1000

    # generate normal samples
    x = np.random.normal(true_mu, true_sigma, size=n_samples)

    # unbiased estimators
    mu_hat = np.mean(x)
    sigma2_hat_unbiased = np.sum((x - mu_hat) ** 2) / (n_samples - 1)
    sigma2_hat_biased = np.sum((x - mu_hat) ** 2) / n_samples

    # PDF for overlay
    xp = np.linspace(mu_hat - 4 * np.sqrt(sigma2_hat_unbiased),
                     mu_hat + 4 * np.sqrt(sigma2_hat_unbiased), 200)
    pdf_estimated = (np.exp(-(xp - mu_hat) ** 2 / (2 * sigma2_hat_unbiased))
                     / np.sqrt(2 * np.pi * sigma2_hat_unbiased))
    pdf_true = (np.exp(-(xp - true_mu) ** 2 / (2 * true_sigma ** 2))
                / np.sqrt(2 * np.pi * true_sigma ** 2))

    fig, axes = plt.subplots(1, 2, figsize=(13, 5))

    # Left panel: histogram with estimated and true PDF overlay
    axes[0].hist(x, bins=30, density=True, color="steelblue",
                 edgecolor="white", alpha=0.7, label="Samples")
    axes[0].plot(xp, pdf_estimated, "--r", linewidth=2,
                 label=f"Estimated: N({mu_hat:.2f}, {sigma2_hat_unbiased:.2f})")
    axes[0].plot(xp, pdf_true, "-k", linewidth=1.5, alpha=0.5,
                 label=f"True: N({true_mu}, {true_sigma ** 2})")
    axes[0].set_xlabel("x")
    axes[0].set_ylabel("Density")
    axes[0].set_title("Sample Histogram with Estimated Normal PDF")
    axes[0].legend(fontsize=9)
    axes[0].grid(True, alpha=0.3)

    # Right panel: convergence of sample variance estimators
    n_range = np.arange(2, n_samples + 1)
    biased_variances = np.array([np.sum((x[:n] - np.mean(x[:n])) ** 2) / n
                                 for n in n_range])
    unbiased_variances = np.array([np.sum((x[:n] - np.mean(x[:n])) ** 2) / (n - 1)
                                   for n in n_range])

    axes[1].plot(n_range, biased_variances, linewidth=0.8, alpha=0.7,
                 label="Biased ($\\div n$)")
    axes[1].plot(n_range, unbiased_variances, linewidth=0.8, alpha=0.7,
                 label="Unbiased ($\\div (n-1)$)")
    axes[1].axhline(true_sigma ** 2, color="red", linestyle="--", linewidth=1.5,
                    label=f"True $\\sigma^2$ = {true_sigma ** 2}")
    axes[1].set_xlabel("Sample Size n")
    axes[1].set_ylabel("Estimated Variance")
    axes[1].set_title("Biased vs Unbiased Variance Estimators")
    axes[1].legend()
    axes[1].grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig("estimation_simulation.png", dpi=150, bbox_inches="tight")
    plt.show()

    print(f"True parameters:     mu = {true_mu}, sigma^2 = {true_sigma ** 2}")
    print(f"Estimated (unbiased): mu_hat = {mu_hat:.4f}, sigma^2_hat = {sigma2_hat_unbiased:.4f}")
    print(f"Estimated (biased):   sigma^2_hat = {sigma2_hat_biased:.4f}")


if __name__ == "__main__":
    main()
