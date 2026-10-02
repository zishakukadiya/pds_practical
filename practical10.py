
import numpy as np

# Array creation
arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

print("Original Array:")
print(arr)

# Indexing
print("\nIndexing:")
print("Element at row 1, column 2:", arr[1, 2])

# Slicing
print("\nSlicing:")
print(arr[0:2, 1:3])

# Reshaping
print("\nReshaping:")
new_arr = np.arange(1, 13).reshape(3, 4)
print(new_arr)

# Broadcasting
print("\nBroadcasting:")
print(new_arr + 10)

# Mathematical operations
print("\nMathematical Operations:")
print("Addition:")
print(arr + 2)

print("Subtraction:")
print(arr - 2)

print("Multiplication:")
print(arr * 2)

print("Division:")
print(arr / 2)

print("Square:")
print(arr ** 2)

# Mathematical functions
print("\nMathematical Functions:")
print("Square Root:")
print(np.sqrt(arr))

print("Sum:", np.sum(arr))
print("Mean:", np.mean(arr))
print("Maximum:", np.max(arr))
print("Minimum:", np.min(arr))
