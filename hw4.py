import numpy as np

from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split


X , y = load_boston(return_X_y=True)

# Add a vector of ones to the data matrix to absorb the bias term
# (Recall slide #7 from the lecture)
X = np.hstack([np.ones([X.shape[0], 1]), X])
# From now on, D refers to the number of features in the AUGMENTED dataset
#  (i.e. including the dummy '1' feature for the absorbed bias term)

# Split into train and test
test_size = 0.2
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size)


def fit_least_squares(X, y):
    """Fit ordinary least squares model to the data.

    Parameters
    ----------
    X : array, shape [N, D]
        (Augmented) feature matrix.
    y : array, shape [N]
        Regression targets.

    Returns
    -------
    w : array, shape [D]
        Optimal regression coefficients (w[0] is the bias term).

    """
    psi = np.linalg.pinv(X)
    return np.dot(psi, y)


def fit_ridge(X, y, reg_strength):
    """Fit ridge regression model to the data.

    Parameters
    ----------
    X : array, shape [N, D]
        (Augmented) feature matrix.
    y : array, shape [N]
        Regression targets.
    reg_strength : float
        L2 regularization strength (denoted by lambda in the lecture)

    Returns
    -------
    w : array, shape [D]
        Optimal regression coefficients (w[0] is the bias term).

    """
    # TODO
    return None


# Load the data
np.random.seed(1234)
X , y = load_boston(return_X_y=True)
X = np.hstack([np.ones([X.shape[0], 1]), X])
test_size = 0.2
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size)

# Ordinary least squares regression
w_ls = fit_least_squares(X_train, y_train)

# print(w_ls)
#y_pred_ls = predict_linear_model(X_test, w_ls)
#mse_ls = mean_squared_error(y_test, y_pred_ls)
#print('MSE for Least squares = {0}'.format(mse_ls))

# Ridge regression
#reg_strength = 1
#w_ridge = fit_ridge(X_train, y_train, reg_strength)
#y_pred_ridge = predict_linear_model(X_test, w_ridge)
#mse_ridge = mean_squared_error(y_test, y_pred_ridge)
#print('MSE for Ridge regression = {0}'.format(mse_ridge))