import pandas as pd
import os

#1 Define the directories
input_dir = 'data'
output_dir = 'output'

#2 Create the output directory if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

#3 Load the datasets
customer_orders = pd.read_csv(os.path.join(input_dir, 'customer_orders.csv'))
customer_details = pd.read_csv(os.path.join(input_dir, 'customer_details.csv'))

#4 Display the first few rows of each dataset to understand their structure
print("Customer Orders:")
print(customer_orders.head())

print("\nCustomer Details:")
print(customer_details.head())

#5 Integrate the datasets
#5.1 Merge customer_orders and customer_details on 'customer_id' and 'email'
integrated_data = pd.merge(customer_orders, customer_details, on=['customer_id', 'email'], how='left')

# Display the first few rows of the integrated dataset
print("\nIntegrated Data:")
print(integrated_data.head())

#7 Save the integrated dataset to a CSV file
output_file = os.path.join(output_dir, 'integrated_customer_data.csv')
#7.1
integrated_data.to_csv(output_file, index=False)

print(f"Integration complete. The integrated dataset is saved as '{output_file}'.")

