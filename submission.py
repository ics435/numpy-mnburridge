import numpy as np
from typing import List


def bibonacci(n: int) -> List[int]:
    """Write a function that computes the first n elements of the Bibonacci Sequence.
    This sequence is defined as: 
    B[0] = B[1] = B[2] = 1
    B[k] = B[k-1] + B[k-2] + B[k-3] for k>2.
    Args:
        n = integer
    Returns:
        seq = List of [B[0], B[1], ..., B[n]]
    """
    pass # IMPLEMENT ME


def not_bibonacci(n: int) -> List[int]:
    """Use list comprehensions to create a one-line python command that
    returns a list of the natural numbers in the range [0, n] inclusive 
    that are NOT Bibonacci numbers as computed in the previous function.
    Args:
        n = integer
    Returns:
        seq = List of integers.
    """
    pass # IMPLEMENT ME


def dict_of_lists(mylist):
    """Write a Python program to create a dictionary grouping
    a sequence of key-value pairs into a dictionary of lists.
    Example:
    Original list: [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 5), ('red', 1)]
    Grouping a sequence of key-value pairs into a dictionary of lists: {'yellow': [1, 3], 'blue': [2, 5], 'red': [1]}
    """
    pass # IMPLEMENT ME


class Rectangle():
    """
    Write a Python class named Rectangle constructed by a length and width,
    and a method print_area which will print the area of a rectangle.
    """
    def __init__(self, length, width):
        pass # IMPLEMENT ME
    
    def get_area(self):
        pass # IMPLEMENT ME


def checker(n: int):
    """Write a Numpy function that takes int n and returns an nxn numpy array
    filled with a checkerboard pattern, with zero in the top left corner.
    For example, for n=8, the function should return: 
    [[0 1 0 1 0 1 0 1]
     ..........
     [0 1 0 1 0 1 0 1]
     [1 0 1 0 1 0 1 0]]
    Hint: Use numpy array slicing.
    """
    pass # IMPLEMENT ME


def selector(X):
    """Take in 2-dimensional array X, and remove any row for which the 
    sum of the row is not zero. Use the numpy function np.isclose() to test 
    whether the sum is zero, since floating point arithmetic can be imprecise.
    """
    pass # IMPLEMENT ME

def covariance(X):
    """Compute sample covariance matrix of NxD feature matrix.


    Args:
        X: NxD numpy array, where N is number of samples and D the number of features.
    Returns:
        C: DxD numpy array, where C_ij is cov(X[:,i], X[:,j]) = Sum((xi - xmean)(yi - ymean))/(N-1)
    Warning: 
        The sample covariance is an estimate of the true covariance of the random variables. 
        There are other ways to estimate the variance from a finite dataset; use this definition.
        It should match the version computed in numpy with numpy.cov(). 
        In your function, you can use np.mean() and np.dot(), but don't use np.cov().
    """
    N, D = X.shape
    pass # IMPLEMENT ME


def nearest_neighbor_predict(X, y, X_test, metric):
  '''
  Classify the examples in X_test using the nearest neighbor algorithm. 
  Args:
    X: 2D numpy array containing the feature matrix with N rows and D columns, 
       where N is number of examples and D is the number of features.
    y: 1D numpy array containing the N labels. 
    X_test: 2D numpy array containing the feature matrix of the test data. 
            Shape is MxD, where M is the number of test points.
    metric: "euclidean" or "taxicab"
  Returns: 
    y_test: 1D numpy array containing the M labels of the test data.
  '''
  assert isinstance(X, np.ndarray)
  assert isinstance(y, np.ndarray)
  assert isinstance(X_test, np.ndarray)
  assert X.ndim == 2
  assert y.ndim == 1
  assert X_test.ndim == 2
  assert X.shape[0] == y.shape[0]
  N, D = X.shape
  M = X_test.shape[0]
  pass # IMPLEMENT ME
