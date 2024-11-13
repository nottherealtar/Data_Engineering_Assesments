import pandas as pd
import os

# Define the directories
input_dir = 'data'
output_dir = 'output'

# Create the output directory if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# 1 Load the three datasets
weather_data = pd.read_csv('weather_data.csv')
solar_panel_output = pd.read_csv('solar_panel_output.csv')
energy_consumption = pd.read_csv('energy_consumption.csv')

# 2 Display the first few rows of each dataset to understand their structure
# 2.1 Why do we display the first few rows of each dataset?
print("Weather Data:")
print(weather_data.head())

print("\nSolar Panel Output:")
print(solar_panel_output.head())

print("\nEnergy Consumption:")
print(energy_consumption.head())

# 3 Integrate the datasets
# 4 Merge weather_data and solar_panel_output on 'inverter_serial'
integrated_data = pd.merge(weather_data, solar_panel_output, on='inverter_serial')

# 5 How do we Merge the result with energy_consumption based on 'inverter_serial' ?
# 5.1 

# 6 How do we Display the first few rows of the integrated dataset
# 6.1 

# 6.2 


# 7 How do we Save the integrated dataset to a CSV file
output_file = os.path.join(output_dir, 'integrated_data.csv')
# 7.1 


print("Integration complete. The integrated dataset is saved as 'integrated_data.csv'.")

# Additional steps (optional):
# - Ensure data consistency and handle any discrepancies
# - Create a data model to store the integrated data
# - Document the integration process and any challenges encountered