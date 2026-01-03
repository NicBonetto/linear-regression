from numpy import mean
from src.core import slope

def intercept(x, y): 
    return mean(y) - slope(x, y) * mean(x)
