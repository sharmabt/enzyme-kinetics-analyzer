import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.optimize import curve_fit

def load_data(filepath):
    df = pd.read_csv(filepath)

    x_data = df["substrate_concentration"].values

    y_data = df["reaction_rate"].values

    return x_data, y_data

def michaelis_menten(S, Vmax, Km):
    V = (Vmax * S) / (Km + S)
    return V

def find_kinetic_constants(x_data, y_data):
    params, covariance = curve_fit(michaelis_menten, x_data, y_data, p0=[1.0, 0.5])
    
    Vmax = params[0]  
    Km = params[1]    
    
    return Vmax, Km

def plot_results(x_data, y_data, Vmax, Km):

    plt.scatter(x_data, y_data, label="Experimental Data", color="blue")

    x_smooth = np.linspace(0, max(x_data), 100)
    y_smooth = (Vmax * x_smooth) / (Km + x_smooth)

    plt.plot(x_smooth, y_smooth, 'r-', label="Fitted Michaelis-Menten Curve")

    plt.xlabel("Substrate Concentration (mM)")
    plt.ylabel("Reaction Rate (µM/min)")
    plt.title("Enzyme Kinetics: Michaelis-Menten Fit")
    plt.legend()
    plt.grid(True)

    plt.savefig("enzyme_kinetics_result.png")
    print("Graph saved as enzyme_kinetics_result.png")

    plt.show()

if __name__ == "__main__":
    x, y = load_data("enzyme_data.csv")
    print("Data loaded successfully!")

    Vmax, Km = find_kinetic_constants(x, y)
    print(f"Calculated Vmax: {Vmax:.2f}")
    print(f"Calculated Km: {Km:.2f}")

    plot_results(x, y, Vmax, Km)