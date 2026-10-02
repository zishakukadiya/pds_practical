
import numpy as np
from scipy import stats

# Dataset
data = [12, 15, 14, 10, 18, 20, 16, 15, 14, 19]

print("Dataset:")
print(data)

# Statistical measures
print("\nStatistical Measures:")

print("Mean:", np.mean(data))
print("Median:", np.median(data))
print("Mode:", stats.mode(data, keepdims=True).mode[0])
print("Variance:", np.var(data))
print("Standard Deviation:", np.std(data))
print("Minimum:", np.min(data))
print("Maximum:", np.max(data))

# Statistical test
# One-sample t-test
test_value = 15

t_statistic, p_value = stats.ttest_1samp(data, test_value)

print("\nOne Sample T-Test:")
print("T-statistic:", t_statistic)
print("P-value:", p_value)

# Interpretation
alpha = 0.05

if p_value < alpha:
    print("Result: Reject the null hypothesis.")
    print("There is a significant difference.")
else:
    print("Result: Fail to reject the null hypothesis.")
    print("There is no significant difference.")
