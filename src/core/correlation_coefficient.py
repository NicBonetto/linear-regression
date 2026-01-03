from numpy import cov, std

def correlation_coefficient(x, y):
    return cov(x, y, ddof=0)[0, 1] / (std(x) * std(y))
