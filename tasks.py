import numpy as np

# Follow the tasks below to practice basic Python concepts.
# Write your code in between the dashed lines.
# Don't import additional packages. Numpy suffices.

# Task 1: 
# Instructions:
#Write a function that takes one numeric argument as input. 
#If the number is larger than zero, the function should return 1, otherwise is should return -1.
#The name of the function should be step

# Your code here:
# -----------------------------------------------

def step (num):
    if num > 0:
        return 1
    else:
        return -1


# -----------------------------------------------


# Task 2:
# Instructions:
#Write a function that takes in two arguments: a numpy array, and an integer (call argument "cutoff" and set default to 0).
#The function should return a numpy array of the same length, with all elements smaller than the cutoff being set to cutoff).
#The name of the function should be ReLu


# Your code here:
# -----------------------------------------------
def ReLu (arr, cutoff = 0):
    return np.maximum(arr, cutoff)

def test_relu_default_cutoff():
    array = np.array([-5, 0, 3, -2, 4])
    expected_output = np.array([0, 0, 3, 0, 4])
    np.testing.assert_array_equal(ReLu(array.copy()), expected_output, "Failed on default cutoff")

def test_relu_custom_cutoff():
    array = np.array([-5, 0, 3, -2, 4])
    expected_output = np.array([2, 2, 3, 2, 4])
    np.testing.assert_array_equal(ReLu(array.copy(), 2), expected_output, "Failed on custom cutoff")

def test_relu_empty_array():
    array = np.array([])
    expected_output = np.array([])
    np.testing.assert_array_equal(ReLu(array.copy()), expected_output, "Failed on empty array")
# -----------------------------------------------


# Task 3:
# Instructions:
#Write a function that takes in a two-dimensional numpy array of size (n, p) and a one-dimensional numpy array of size p.
#The function should start by multiplying the two numpy arrays (matrix multiplication).
#Next, apply the ReLu function from above to the resulting matrix and return the result.
#Name the function neural_net_layer

# Your code here:
# -----------------------------------------------

def neural_net_layer(n, p):
    product = n @ p
    result = ReLu(product)
    return result
    

# ------------------------------------------