import pandas as pd

# Sample data (you can replace this with your actual dataset)
data = {
    'Transaction_ID': [1, 2, 3, 4, 5],
    'Amount': [100.0, 50.0, 200.0, 75.0, 300.0],
    'Customer_ID': ['A123', 'B456', 'A123', 'C789', 'D101'],
    'Transaction_Date': ['2023-01-15', '2023-01-16', '2023-01-17', '2023-01-18', '2023-01-19'],
}

# Create a Pandas DataFrame
df = pd.DataFrame(data)

# Step 3: Data Profiling
# Profile the data to understand its characteristics
data_profile = df.describe()

# Display the data profiling results
print("Data Profiling:")
print(data_profile)

# Step 4: Feature Engineering
# Let's create a new feature 'Weekday' from 'Transaction_Date'
df['Transaction_Date'] = pd.to_datetime(df['Transaction_Date'])
df['Weekday'] = df['Transaction_Date'].dt.weekday_name

# Display the updated DataFrame with the new 'Weekday' feature
print("\nDataFrame with Feature Engineering:")
print(df)
