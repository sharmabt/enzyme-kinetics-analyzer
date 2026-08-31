# Enzyme Kinetics Analyzer

## Description
This Python script allows the user to analyze noisy enzyme assay data and judge the quality of an enzyme. It reads data provided by the user through a CSV file and uses the `curve_fit` function to find the closest theoretical fit for the experimental data. This saves a significant amount of time, as fitting such curves manually would require lengthy mathematical calculations.

## Why I Built This
This is my first project utilizing more advanced Python libraries, and I wanted to gain practical exposure to them. I specifically chose the Michaelis-Menten equation because its graph is relatively simple to understand and analyze. It also stems from a core biological process that is widely used in industry to evaluate and compare the efficiency of enzymes.

## Scientific Background
This script calculates two important kinetic constants: **Km** and **Vmax**.

- **Vmax** is the maximum speed a reaction can theoretically reach.
- **Km** is the substrate concentration at which the reaction reaches half of its Vmax.

These two values allow us to compare different enzymes. A low Km and a high Vmax is the ideal case, but it is rare. In practice, Km helps us understand how much raw material (substrate) is needed to run a reaction efficiently, while Vmax tells us the maximum possible rate.

## How This Works
1. First, we import the required libraries.
2. We define a function called `load_data`, which reads the CSV file and extracts the experimental data.
3. Next, we define the Michaelis-Menten equation. This tells Python the expected shape of the graph.
4. The core of the project uses `curve_fit` to find the curve that best fits the imported data.

To understand why this is important, it helps to know what happens under the hood. The script runs simulations because real data is noisy—if the data were perfect, the curve would be obvious. `curve_fit` performs many iterations, trying to minimize the error landscape and find the best curve that passes closest to all the data points. It returns the most compatible **Vmax** and **Km** values, along with a covariance matrix that describes the uncertainty in those values.

The covariance matrix is saved in the `covariance` variable. While we do not print it in this project, it can be used to examine the error in the fit and the relationship between Vmax and Km.

## How to Run This Project

1. Clone this repository or download the files to your computer.

2. Install the required libraries:

   `pip install -r requirements.txt`

3. Run the main Python script:

   `python enzyme_analysis.py`

4. The script will generate a plot called `enzyme_kinetics_result.png` in the same folder.

## Sample Output

![Km and Vmax Plot](enzyme_kinetics_result.png)

## Requirements
All required libraries are listed in `requirements.txt` and can be installed with:

`pip install -r requirements.txt`