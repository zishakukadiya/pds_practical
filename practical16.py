
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm, expon


# --------------------------------
# 1. NORMAL DISTRIBUTION
# --------------------------------

mean = 0
std = 1

x = np.linspace(-4, 4, 1000)

normal_pdf = norm.pdf(x, mean, std)

print("NORMAL DISTRIBUTION")
print("-------------------")
print("Mean =", mean)
print("Standard Deviation =", std)


plt.figure(figsize=(8, 5))

plt.plot(x, normal_pdf)

plt.title("Normal Distribution")
plt.xlabel("X")
plt.ylabel("Probability Density")

plt.grid()

plt.tight_layout()
plt.savefig("practical16_normal.png")
plt.close()


# --------------------------------
# 2. EXPONENTIAL DISTRIBUTION
# --------------------------------

lambda_value = 1

x_exp = np.linspace(0, 5, 1000)

exponential_pdf = expon.pdf(
    x_exp,
    scale=1 / lambda_value
)

print("\nEXPONENTIAL DISTRIBUTION")
print("-----------------------")
print("Lambda =", lambda_value)


plt.figure(figsize=(8, 5))

plt.plot(x_exp, exponential_pdf)

plt.title("Exponential Distribution")
plt.xlabel("X")
plt.ylabel("Probability Density")

plt.grid()

plt.tight_layout()
plt.savefig("practical16_exponential.png")
plt.close()


# --------------------------------
# 3. CENTRAL LIMIT THEOREM
# --------------------------------

population = np.random.normal(
    50,
    10,
    10000
)

num_samples = 1000
sample_size = 30

sample_means = []

for i in range(num_samples):

    sample = np.random.choice(
        population,
        sample_size
    )

    sample_means.append(
        np.mean(sample)
    )


print("\nCENTRAL LIMIT THEOREM")
print("---------------------")
print("Population Mean =", np.mean(population))
print("Mean of Sample Means =", np.mean(sample_means))
print("Sample Size =", sample_size)
print("Number of Samples =", num_samples)


plt.figure(figsize=(8, 5))

plt.hist(
    sample_means,
    bins=30,
    density=True
)

plt.title("Central Limit Theorem")
plt.xlabel("Sample Means")
plt.ylabel("Density")

plt.grid()

plt.tight_layout()
plt.savefig("practical16_clt.png")
plt.close()
