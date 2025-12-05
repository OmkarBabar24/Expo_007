import numpy as np
# Numpy is python library which is used to perform the numeric operations on data
#Array is a collection of homogeneous type of element
#Types of Array
#1D array,2D array,3D array,N_dimensional array

# Print NumPy version
# print("NumPy version:", np.version)

# # Create arrays
arr1 = np.array([1, 2, 3, 4, 5])  # 1D array
print("1D Array:", arr1)

arr2 = np.array([[1, 2, 3], [4, 5, 6]])  # 2D array
print("2D Array:\n", arr2)

arr3 = np.array([[1, 2, 3], [4, 5, 6],[7,8,9]])  # 3D array
print("3D Array:\n", arr3)
#print(arr3[1,1])

arr = np.array([
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
    [[10, 11, 12], [13, 14, 15], [16, 17, 18]],
    [[19, 20, 21], [22, 23, 24], [25, 26, 27]]
])
print(arr)
#print(arr.shape)
print(arr[2,:,2])
# # Array attributes
# print("Array shape:", arr2.shape)
# print("Array dimensions:", arr2.ndim)
# print("Number of elements:", arr2.size)
# print("Data type:", arr2.dtype)
# print("Item size (bytes):", arr2.itemsize)
# print("Array data:\n", arr2.data)
#
# # Indexing and slicing
#print("Element at (0,1):", arr3[0, 0])
# print("First row:", arr2[0, :])
# print("Second column:", arr2[:, 1])
# print("Subarray:\n", arr2[0:2, 1:3])
#
#print(arr3[1:,1:])
#
# arr3 = np.zeros((3, 3))  # Array of zeros
# print("Zeros array:\n", arr3)
#
# arr4 = np.ones((2, 4))  # Array of ones
# print("Ones array:\n", arr4)
#
arr5 = np.full((3, 3), 7)  # Constant array
print("Full array:\n", arr5)
arr6 = np.eye(4)  # Identity matrix
print("Identity matrix:\n", arr6)
#
#
# arr7 = np.random.random((2,2))  # Random array
# print("Random array:\n", arr7)
# # #
# arr8 = np.arange(0, 10, 2)  # Array with range
# print("Arange array:", arr8)
# #
# arr9 = np.linspace(1, 6, 5)  # Evenly spaced numbers
# print("Linspace array:", arr9)
#
#
#
#
#
# # Boolean indexing
# bool_arr = arr1 > 2
# print("Boolean mask:", bool_arr)
# print("Filtered array:", arr1[bool_arr])
#
#
# # Basic math operations
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print("Addition:", a + b)
# print("Subtraction:", a - b)
# print("Multiplication:", a * b)
# print("Division:", b / a)
# print("Exponentiation:", a ** 2)
# print("Dot product:", np.dot(a, b))
# print("Square root:", np.sqrt(a))
# print("Exponential:", np.exp(a))
# print("Logarithm:", np.log(a))
# print("Trigonometric sine:", np.sin(a))
#
# # Aggregation functions
# arr = np.array([[1, 2, 3], [4, 5, 6]])
# #
# print("Sum:", np.sum(arr))
# print("Sum along axis 0:", np.sum(arr, axis=0))
# print("Sum along axis 1:", np.sum(arr, axis=1))
# print("Mean:", np.mean(arr))
# print("Standard deviation:", np.std(arr))
# print("Variance:", np.var(arr))
# print("Minimum:", np.min(arr))
# print("Maximum:", np.max(arr))
# print("Index of min:", np.argmin(arr))
# print("Index of max:", np.argmax(arr))
#
# # Array manipulation
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
#
# # Reshaping
print("Reshaped array:\n", a.reshape(4, 1))
#
# # Concatenation
print("Vertical concatenation:\n", np.vstack((a, b)))
print("Horizontal concatenation:\n", np.hstack((a, b)))
#
# # Splitting
print("Vertical split:\n", np.vsplit(a, 2))
print("Horizontal split:\n", np.hsplit(a, 2))
#
# # Transpose
print("Transpose:\n", a.T)
#
# # Flatten
# print("Flattened array:", a.flatten())
#
# # Adding/removing dimensions
# print("Expanded dimensions:", np.expand_dims(a, axis=0))
# print("Squeezed array:", np.squeeze(np.expand_dims(a, axis=0)))
#
# # Broadcasting example
# a = np.array([[1, 2, 3], [4, 5, 6]])
# b = np.array([10, 20, 30])
#
# print("Broadcasted addition:\n", a + b)
# # Linear algebra
# a = np.array([[1, 2], [3, 4]])
# b = np.array([[5, 6], [7, 8]])
#
# print("Matrix multiplication:\n", np.matmul(a, b))
# print("Determinant:", np.linalg.det(a))
# print("Inverse:\n", np.linalg.inv(a))
# print("Eigenvalues:", np.linalg.eigvals(a))
# print("Matrix rank:", np.linalg.matrix_rank(a))
# print("Solve linear equations:", np.linalg.solve(a, np.array([1, 2])))
#
# # Statistical operations
# data = np.random.normal(0, 1, 1000)  # Normal distribution
#
# print("Mean:", np.mean(data))
# print("Median:", np.median(data))
# print("Percentiles:", np.percentile(data, [25, 50, 75]))
# print("Histogram counts:", np.histogram(data, bins=10)[0])
# print("Correlation coefficient:", np.corrcoef(data[:500], data[500:]))
#
# # Sorting and searching
# arr = np.array([3, 1, 4, 2, 5])
#
# print("Sorted array:", np.sort(arr))
# print("Indices of sorted array:", np.argsort(arr))
# print("Partitioned array:", np.partition(arr, 2))
# print("Where condition:", np.where(arr > 2))
# print("Non-zero elements:", np.nonzero(arr))
#
# # File I/O
# arr = np.arange(10)
#
# # Save and load
# np.save('my_array.npy', arr)
# loaded_arr = np.load('my_array.npy')
# print("Loaded array:", loaded_arr)
#
# # Text files
# np.savetxt('array.txt', arr)
# loaded_txt = np.loadtxt('array.txt')
# print("Loaded from text:", loaded_txt)
#
#
# # Advanced operations
# arr = np.array([[1, 2, 3], [4, 5, 6]])
#
# # Vectorized operations
# print("Vectorized operation:", arr * 2 + 1)
#
# # Masked arrays
# masked_arr = np.ma.masked_where(arr > 3, arr)
# print("Masked array:\n", masked_arr)
#
# # Universal functions
# arr = np.array([1.1, 2.2, 3.3])

# print("Floor:", np.floor(arr))
# print("Ceil:", np.ceil(arr))
# print("Round:", np.round(arr))
# print("Absolute:", np.abs(np.array([-1, -2])))
#print("Sign:", np.sign(np.array([-5, 0, 5])))
#
# ## 14. Set Operations

# a = np.array([1, 2, 3, 4, 5])
# b = np.array([3, 4, 5, 6, 7])

# print("Unique elements:", np.unique(a))
# print("Intersection:", np.intersect1d(a, b))
# print("Union:", np.union1d(a, b))
# print("Set difference:", np.setdiff1d(a, b))
# print("Set XOR:", np.setxor1d(a, b))
#
# # Random number generation
# print("Random float:", np.random.rand())
# print("Random array:\n", np.random.rand(2, 3))
# print("Random integers:", np.random.randint(0, 10, 5))
# print("Normal distribution:", np.random.normal(0, 1, 5))
# print("Shuffled array:", np.random.permutation([1, 2, 3, 4, 5]))