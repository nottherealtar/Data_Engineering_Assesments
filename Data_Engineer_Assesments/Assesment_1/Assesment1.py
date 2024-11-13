import pandas as pd
import os

# Define the directories
input_dir = 'data'
output_dir = 'output'

# Create the output directory if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Load the datasets
customer_orders = pd.read_csv(os.path.join(input_dir, 'customer_orders.csv'))
customer_details = pd.read_csv(os.path.join(input_dir, 'customer_details.csv'))

# Display the first few rows of each dataset to understand their structure
print("Customer Orders:")
print(customer_orders.head())

print("\nCustomer Details:")
print(customer_details.head())

# Integrate the datasets
# Merge customer_orders and customer_details on 'customer_id' and 'email'
integrated_data = pd.merge(customer_orders, customer_details, on=['customer_id', 'email'], how='left')

# Display the first few rows of the integrated dataset
print("\nIntegrated Data:")
print(integrated_data.head())

# Save the integrated dataset to a CSV file
output_file = os.path.join(output_dir, 'integrated_customer_data.csv')
integrated_data.to_csv(output_file, index=False)

print(f"Integration complete. The integrated dataset is saved as '{output_file}'.")

# Additional steps:
# - Handle missing email addresses and ensure data consistency
# - (optional)Perform an analysis to identify key insights about customer orders
# - Document the integration process, analysis, and any challenges encountered