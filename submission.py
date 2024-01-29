import numpy as np
from typing import List


def bibonacci(n: int) -> List[int]:
    seq=[]
    for i in range(0,n):
        if i==0 or i==1 or i==2:
            iseq=1
        else:
            iseq=seq[i-3]+seq[i-2]+seq[i-1]
        seq.append(iseq)
    return(seq)
    """Write a function that computes the first n+1 elements of the Bibonacci Sequence.
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
    yes_bibonacci=bibonacci(n)
    seq=[]
    for i in range(0,n):
        breaker=0
        for iyes in yes_bibonacci:
            if i==iyes:
                breaker=1
        if breaker==0:
            seq.append(i)
    return(seq)
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
    Dict = {}
    i=-1
    for ilist in mylist:            
        label=ilist[0]
        value=ilist[1]
        breaker=0
        for checker in Dict.keys():
            if checker==label:
                breaker=1
        if breaker==0:
            i=i+1
            Dict[label]=[value]
        elif breaker==1:
            oldlist=Dict[label]
            newlist=[]
            for ioldlist in oldlist:
                newlist.append(ioldlist)
            newlist.append(value)
            Dict[label]=newlist
    return(Dict)
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
        self.length=length
        self.width=width
        pass # IMPLEMENT ME
    
    def get_area(self):
        return(self.length*self.width)
        pass # IMPLEMENT ME

def checker(n: int):
    array=[]
    switcher=1
    for i in range(0,n*n):
        if i==0:
            iarray=[]
        elif i%n==0:
            array.append(iarray)
            iarray=[]
            if switcher==1:
                switcher=0
            elif switcher==0:
                switcher=1
        if switcher==1:
            iarray.append(i%2)
        else:
            iarray.append((i+1)%2)
    """Write a Numpy function that takes int n and returns an nxn numpy array
    filled with a checkerboard pattern, with zero in the top left corner.
    For example, for n=8, the function should return: 
    [[0 1 0 1 0 1 0 1]
     ..........
     [0 1 0 1 0 1 0 1]
     [1 0 1 0 1 0 1 0]]
    Hint: Use numpy array slicing.
    """
    return(array)
    pass # IMPLEMENT ME

def selector(X):
    newX=[]
    for iX in X:
        sum=iX[0]+iX[1]
        input(sum)
        if np.isclose(sum,0):
            input(sum)
            newX.append(iX)
    return(newX)
    """Take in 2-dimensional array X, and remove any row for which the 
    sum of the row is not zero. Use the numpy function np.isclose() to test 
    whether the sum is zero, since floating point arithmetic can be imprecise.
    """
    pass # IMPLEMENT ME

def covariance(X):
    N, D = X.shape

    shape=np.shape(X)
    colsize=shape[0]
    rowsize=shape[1]
    covmax=np.zeros((colsize,colsize))
    for irow in range(0,colsize):
        irowavg=np.mean(X[irow,:])
        for jrow in range(0,colsize):
            jrowavg=np.mean(X[jrow,:])
            tempval=0
            for icol in range(0,rowsize):
                tempval2=(X[irow,icol]-irowavg)*(X[jrow,icol]-jrowavg)
                tempval=tempval+tempval2
            tempval=tempval/(rowsize-1)
            covmax[irow][jrow]=tempval

    return(covmax)

    """Compute sample covariance matrix of NxD feature matrix.

    Args:
        X: NxD numpy array, where N is number of samples and D the number of features.
    Returns:
        C: DxD numpy array, where C_ij is cov(X[:,i], X[:,j]) = Sum_k((Xki - Xi_mean)(Xkj - Xk_mean))/(N-1)
    Warning: 
        The sample covariance is an estimate of the true covariance of the random variables. 
        There are other ways to estimate the variance from a finite dataset; use this definition.
        It should match the version computed in numpy with numpy.cov(). 
        In your function, you can use np.mean() and np.dot(), but don't use np.cov().
    """
    pass # IMPLEMENT ME

def nearest_neighbor_predict(X, y, X_test, metric):
    returnval=[]
    for iX_test in X_test:
        dist=-1
        counter=-1
        newy='A'
        for iX in X:
            counter=counter+1
            findy=y[counter]
            if metric=='euclidean':
                newdist=np.sqrt((iX_test[0]-iX[0])**2+(iX_test[1]-iX[1])**2)
            elif metric=='taxicab':
                newdist=np.abs(iX_test[0]-iX[0])+np.abs(iX_test[1]-iX[1])
            if dist==-1:
                dist=newdist
                newy=findy
            else:
                if newdist<dist:
                    dist=newdist
                    newy=findy
        returnval.append(newy)
    return(returnval)
    

  
    """
    Classify the examples in X_test using the nearest neighbor algorithm. 
    Args:
    X: 2D numpy array containing the feature matrix with N rows and D columns, 
        where N is number of examples and D is the number of features.
    y: 1D numpy array containing the N labels. 
    X_test: 2D numpy array containing the feature matrix of the test data. 
            Shape is MxD, where M is the number of test points.
    metric: "euclidean" or "taxicab", string indicating distance metric to use.
    Returns: 
    y_test: 1D numpy array containing the M labels of the test data.
    """
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
