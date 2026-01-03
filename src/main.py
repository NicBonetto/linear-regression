from numpy import mean, std, array
from src.core import standard, slope, intercept

def fit(x, y, standardize=False):
    x = array(x)
    y = array(y)

    if standardize:
        x = standard(x)
        y = standard(y)

    m = slope(x, y)
    b = intercept(x, y)

    def predict(val):
        if standardize:
            val = (val - mean(x)) / std(x)

        return (m * val + b).item()

    return predict

