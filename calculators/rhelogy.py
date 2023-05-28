import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from sklearn.metrics import r2_score

def fit_rheological_models():
    """
    Fit rheological models to input data and plot the best model.
    """
    # Define the rheological models

    # Newtonian fluid model
    def newtonian_model(x, viscosity):
        return viscosity * x

    # Bingham plastic fluid model
    def bingham_model(x, yield_stress, viscosity):
        return yield_stress + viscosity * x

    # Power-law (shear-thinning or shear-thickening) fluid model
    def power_law_model(x, consistency_index, flow_behavior_index):
        return consistency_index * x ** flow_behavior_index

    while True:
        # Get input values from the user
        shear_rate_values = input("Enter the shear rate values separated by commas (or 'q' to quit): ")
        if shear_rate_values.lower() == 'q':
            break

        shear_stress_values = input("Enter the shear stress values separated by commas: ")

        # Convert input values to numpy arrays
        try:
            shear_rate = np.array(list(map(float, shear_rate_values.split(","))))
            shear_stress = np.array(list(map(float, shear_stress_values.split(","))))
        except ValueError:
            print("Invalid input. Please enter numerical values separated by commas.")
            continue

        # Fit data to rheological models

        # Newtonian model fitting
        newtonian_params, _ = curve_fit(newtonian_model, shear_rate, shear_stress)
        newtonian_r2 = r2_score(shear_stress, newtonian_model(shear_rate, *newtonian_params))

        # Bingham plastic model fitting
        bingham_params, _ = curve_fit(bingham_model, shear_rate, shear_stress)
        bingham_r2 = r2_score(shear_stress, bingham_model(shear_rate, *bingham_params))

        # Power-law model fitting
        power_law_params, _ = curve_fit(power_law_model, shear_rate, shear_stress)
        power_law_r2 = r2_score(shear_stress, power_law_model(shear_rate, *power_law_params))

        # Determine the model with the highest R2 value
        model_r2_values = {'Newtonian': newtonian_r2, 'Bingham Plastic': bingham_r2, 'Power Law': power_law_r2}
        best_model = max(model_r2_values, key=model_r2_values.get)

        # Print model parameters and R2 values for all models
        print()
        print(f"Newtonian Model Parameters: {newtonian_params}")
        print(f"Newtonian Model R² Value: {newtonian_r2}")
        print()
        print(f"Bingham Plastic Model Parameters: {bingham_params}")
        print(f"Bingham Plastic Model R² Value: {bingham_r2}")
        print()
        print(f"Power-law Model Parameters: {power_law_params}")
        print(f"Power-law Model R² Value: {power_law_r2}")

        # Check if 'Bingham Plastic' R2 is very close to 'Newtonian' R2 and the intercept value is close to 0
        if best_model == 'Bingham Plastic' and abs(bingham_r2 - newtonian_r2) < np.exp(-5) and abs(bingham_params[0]) < 0.05:
            best_model = 'Newtonian'
            print("\nSince the R² values of Bingham Plastic and Newtonian models are so close (< e⁻⁵) and the intercept is close to 0, the model is likely to be a Newtonian model.")

        # Check the best model and print fluid type if 'Power Law'
        if best_model == 'Power Law':
            flow_behavior_index = power_law_params[1]
            if flow_behavior_index < 1:
                fluid_type = "Pseudoplastic Fluid"
            elif flow_behavior_index > 1:
                fluid_type = "Dilatant Fluid"
            else:
                fluid_type = "Newtonian Fluid"
            print("Fluid type: ", fluid_type)
        print()
        if best_model != 'Newtonian':
            print("The best model is", best_model, "model.")
            print()

        # Plot the data and best fitted model
        plt.scatter(shear_rate, shear_stress, label='Data')

        if best_model == 'Newtonian':
            plt.plot(shear_rate, newtonian_model(shear_rate, *newtonian_params), label='Newtonian')
        elif best_model == 'Bingham Plastic':
            plt.plot(shear_rate, bingham_model(shear_rate, *bingham_params), label='Bingham Plastic')
        elif best_model == 'Power Law':
            plt.plot(shear_rate, power_law_model(shear_rate, *power_law_params), label='Power Law')

        plt.xlabel('Shear Rate')
        plt.ylabel('Shear Stress')
        plt.title(f"Best Model: {best_model}")
        plt.legend()
        plt.grid(True)
        plt.show()

fit_rheological_models()
