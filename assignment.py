import numpy as np

def hello_world() -> str:
    """
    Implement a function that returns Hello World!
    """
    return "Hello World!"


def add_two(number: int) -> int:
    """
    Adds two to `number`
    """
    return number + 2


def zero_array(N: int) -> np.ndarray:
    """
    Returns a double type ndarray of length N filled with zeros 
    """
    zeros_array = np.zeros(N*2, dtype=np.float64)
    return zeros_array

# print(zero_array(3))