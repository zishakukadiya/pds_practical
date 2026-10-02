
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom, poisson


# -------------------------------
# 1. BINOMIAL DISTRIBUTION
# -------------------------------

n = 10
p = 0.5

x = np.arange(0, n + 1)

binomial_probability = binom.pmf(x, n, p)

print("BINOMIAL DISTRIBUTION")
print("---------------------")

for i in range(len(x)):
    print(
        "P(X =", x[i], ") =",
        binomial_probability[i]
    )


plt.figure(figsize=(8, 5))

plt.bar(x, binomial_probability)

plt.title("Binomial Distribution")
plt.xlabel("Number of Successes")
plt.ylabel("Probability")

plt.grid(axis="y")

plt.tight_layout()
plt.savefig("practical15_binomial.png")
plt.close()


# -------------------------------
# 2. POISSON DISTRIBUTION
# -------------------------------

lambda_value = 4

x_poisson = np.arange(0, 15)

poisson_probability = poisson.pmf(
    x_poisson,
    lambda_value
)

print("\nPOISSON DISTRIBUTION")
print("--------------------")

for i in range(len(x_poisson)):
    print(
        "P(X =", x_poisson[i], ") =",
        poisson_probability[i]
    )


plt.figure(figsize=(8, 5))

plt.bar(x_poisson, poisson_probability)

plt.title("Poisson Distribution")
plt.xlabel("Number of Events")
plt.ylabel("Probability")

plt.grid(axis="y")

plt.tight_layout()
plt.savefig("practical15_poisson.png")
plt.close()
