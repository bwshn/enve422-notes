import numpy as np

# Define the models


def linear_model(x, a, b):
    return a + x * b


def exponential_model(x, a, b):
    return a * np.exp(b * x)


def logarithmic_model(x, a, b):
    return a * np.log(x) + b


def power_series_model(x, a, b):
    return a * (x ** b)

# Define R2 calculation function


def calculate_r2(y_true, y_pred):
    corr = np.corrcoef(y_true, y_pred)[0, 1]
    r2 = corr ** 2
    return r2

while True:

    # Get input values
    x_input = input("Enter the x values separated by commas: ").split(',')
    y_input = input("Enter the y values separated by commas: ").split(',')

    # Convert input values to float
    x = np.array([float(val) for val in x_input])
    y = np.array([float(val) for val in y_input])

    # Fit linear model
    linear_params = np.polyfit(x, y, deg=1)
    linear_slope, linear_intercept = linear_params
    linear_y_pred = linear_model(x, linear_intercept, linear_slope)
    linear_r2 = calculate_r2(y, linear_y_pred)

    # Fit exponential model
    exp_params = np.polyfit(x, np.log(y), deg=1)
    exp_intercept, exp_slope = np.exp(exp_params[1]), exp_params[0]
    exp_y_pred = exponential_model(x, exp_intercept, exp_slope)
    exp_r2 = calculate_r2(y, exp_y_pred)

    # Fit logarithmic model
    log_params = np.polyfit(np.log(x), y, deg=1)
    log_intercept, log_slope = log_params[1], log_params[0]
    log_y_pred = logarithmic_model(x, log_intercept, log_slope)
    log_r2 = calculate_r2(y, log_y_pred)

    # Fit power series model
    power_params = np.polyfit(np.log(x), np.log(y), deg=1)
    power_intercept, power_slope = np.exp(power_params[1]), power_params[0]
    power_y_pred = power_series_model(x, power_intercept, power_slope)
    power_r2 = calculate_r2(y, power_y_pred)

    # Print the results
    print("\nLinear Model:")
    print("Intercept:", linear_intercept)
    print("Slope:", linear_slope)
    print("R2:", linear_r2)

    print("\nExponential Model:")
    print("Intercept:", exp_intercept)
    print("Slope:", exp_slope)
    print("R2:", exp_r2)

    print("\nLogarithmic Model:")
    print("Intercept:", log_intercept)
    print("Slope:", log_slope)
    print("R2:", log_r2)

    print("\nPower Series Model:")
    print("Intercept:", power_intercept)
    print("Slope:", power_slope)
    print("R2:", power_r2)
