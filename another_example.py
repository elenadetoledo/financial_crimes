import pandas as pd

# Creating a DataFrame with hardcoded data
data = {
    'Name': ['John', 'Alice', 'Bob', 'Eve'],
    'Age': [25, 28, 22, 30],
    'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']
}

df = pd.DataFrame(data)

# Displaying the DataFrame
print("DataFrame with hardcoded data:")
print(df)

# Accessing specific columns
print("\nColumn 'Name':")
print(df['Name'])

# Filtering data based on a condition
filtered_data = df[df['Age'] > 25]
print("\nFiltered data where 'Age' is greater than 25:")
print(filtered_data)

# Adding a new column with hardcoded values
df['Gender'] = ['Male', 'Female', 'Male', 'Female']
print("\nDataFrame with a new column 'Gender':")
print(df)
