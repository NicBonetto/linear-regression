from numpy import std
from src.core import correlation_coefficient

def slope(x, y):
    r = correlation_coefficient(x, y) 
    return r * (std(y)/std(x))
