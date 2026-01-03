from numpy import mean, std

def standard(x):
    return (x - mean(x)) / std(x)
