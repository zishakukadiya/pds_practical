
import numpy as np
from scipy import stats

# ==========================================
# ONE SAMPLE T-TEST
# ==========================================

# Sample data
data = [52, 48, 51, 49, 53, 50, 47, 54, 52, 51]

# Hypothesized population mean
population_mean = 50

# Significance level
alpha = 0.05

print("ONE SAMPLE T-TEST")
print("-----------------")

print("Sample Data:", data)
print("Hypothesized Population Mean:", population_mean)
print("Significance Level:", alpha)

# Perform one sample t-test
t_statistic, p_value = stats.ttest_1samp(data, population_mean)

print("\nT-Statistic:", t_statistic)
print("P-Value:", p_value)

# ==========================================
# HYPOTHESIS TESTING
# ==========================================

print("\nHYPOTHESIS TESTING")
print("------------------")

print("Null Hypothesis (H0): Population mean = 50")
print("Alternative Hypothesis (H1): Population mean != 50")

if p_value < alpha:
    print("\nResult: Reject the Null Hypothesis (H0).")
    print("There is significant evidence that the population mean is different from 50.")
else:
    print("\nResult: Fail to Reject the Null Hypothesis (H0).")
    print("There is not enough evidence to conclude that the population mean is different from 50.")
