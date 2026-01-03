# linear-regression
Linear regression from scratch.

## Description
This module implements linear regression using nothing but NumPy. The design is intentionally minimal: pass in `x` and `y` (optionally `standardize` as a bool), and the module fits a line by evaluating the parameters. A predictor function is returned that can be applied to new values.

Concepts and formulas closely frame ideas taught in **Data 8: Foundations of Data Science** at UC Berkeley.

## API
```
fit(x, y)
```
**Parameters**
- `x`: 1D list of explanatory variable values
- `y`: 1D list of response variable values

**Returns**
- `predict(new_val)`: a function that takes a new `x` value and returns a predicted `y` value.

Ex.
```
predict = fit([1, 2, 3, 4, 5], [3. 5. 7. 9. 11])
y_hat = predict(5)
```



