import numpy as np
import submission;

def test_bibonacci():
    assert submission.bibonacci(0) == [1]
    assert submission.bibonacci(1) == [1, 1]
    assert submission.bibonacci(2) == [1, 1, 1]
    assert submission.bibonacci(12) == [1, 1, 1, 3, 5, 9, 17, 31, 57, 105, 193, 355, 653]

def test_not_bibonacci():
    assert submission.not_bibonacci(0) == [0]
    assert submission.not_bibonacci(1) == [0]
    assert submission.not_bibonacci(2) == [0, 2]
    assert submission.not_bibonacci(19) == [0, 2, 4, 6, 7, 8, 10, 11, 12, 13, 14, 15, 16, 18, 19]
    

def test_dict_of_lists():
    example = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
    assert submission.dict_of_lists(example) == {'yellow': [1, 3], 'blue': [2, 4], 'red': [1]}


def test_Rectangle():
    myrectangle = submission.Rectangle(length=4, width=3)
    assert myrectangle.get_area() == 12
    myrectangle2 = submission.Rectangle(length=10, width=.4)
    assert myrectangle2.get_area() == 4


def test_checker():
    assert np.all(submission.checker(n=1) == np.array([[0]]))
    assert np.all(submission.checker(n=2) == np.array([[0, 1], [1, 0]]))
    assert np.all(submission.checker(n=3) == np.array([[0, 1, 0], [1, 0, 1], [0, 1, 0]]))


def test_selector():
    input = np.array([[0,0,0], [1e-6, 0, 0], [1,-1,0], [1e-10, 0, 0], [2e-6, -1e-6, -1e-6]])
    output = np.array([[ 0.e+00,  0.e+00,  0.e+00],
                    [ 1.e+00, -1.e+00,  0.e+00],
                    [ 1.e-10,  0.e+00,  0.e+00],
                    [ 2.e-06, -1.e-06, -1.e-06]])
    assert np.all(submission.selector(input) == output)


def test_covariance():
    np.random.seed(42)
    example_data = np.random.rand(10, 4)
    C = submission.covariance(example_data)
    C_np = np.cov(example_data.T) # Numpy function expects data in DxN orientation.
    assert np.all(np.isclose(C, C_np))


def test_nearest_neighbor_predict():
    # Generate some example data.
    X = np.array([[0,1.5], [1.5,0], [1,1]])
    y = np.array([0, 0, 1]) 
    X_test = np.array([[0,0], [0.1, 0.1], [0,1], [1, 0], [1,1], [4,-2], [4,2]])

    # Test with euclid metric.
    y_pred = nearest_neighbor_predict(X, y, X_test, metric='euclidean')
    assert np.all(y_pred == np.array([1, 1, 0, 0, 1, 0, 1,]))
    # Test with taxicab metric.
    y_pred = nearest_neighbor_predict(X, y, X_test, metric='taxicab')
    assert np.all(y_pred == np.array([0, 0, 0, 0, 1, 0, 1,]))
