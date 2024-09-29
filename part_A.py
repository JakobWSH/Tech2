import numpy as np
from math import sqrt
def std_loops(x):
    """
    Compute standard deviation of x using loops.
    Parameters
    ----------
    x: Sequence of numbers
    Returns
    -------
    sd : float
    Standard deviation of the list of numbers.
    """
    N = len(x)
    
    # Calculate the mean
    mean = sum(x[i] for i in range(N)) / N
    
    # Calculate the mean of squares
    mean_of_squares = sum(x[i] ** 2 for i in range(N)) / N
    
    # Calculate the variance
    variance = mean_of_squares - mean ** 2
    
    # Calculate the standard deviation
    standard_deviation = sqrt(variance)
    
    return standard_deviation

def std_builtin(x):
    """
    Compute standard deviation of x using the built-in functions sum() and len().
    Parameters
    ----------
    x: Sequence of numbers
    Returns
    -------
    sd : float
    Standard deviation of the list of numbers.
    """
    N = len(x)
    
    # Calculate the mean using sum() and len()
    mean = sum(x) / N
    
    # Calculate the mean of squares using sum() and len()
    mean_of_squares = sum(i ** 2 for i in x) / N
    
    # Calculate the variance
    variance = mean_of_squares - mean ** 2
    
    # Calculate the standard deviation
    standard_deviation = sqrt(variance)
    
    return standard_deviation

if __name__ == "__main__":
    num_lst = [1, 2, 3, 4, 5]
    
    # Compute standard deviation using loops
    std_loop_result = std_loops(num_lst)
    print(f"Standard Deviation using loops: {std_loop_result}")
    
    # Compute standard deviation using built-in functions
    std_builtin_result = std_builtin(num_lst)
    print(f"Standard Deviation using built-in functions: {std_builtin_result}")
    
    # Compute standard deviation using NumPy
    std_numpy_result = np.std(num_lst)
    print(f"Standard Deviation using NumPy: {std_numpy_result}")