import pandas as pd

aa=pd.read_excel("C:\\Users\\prati\\Desktop\\ecl_dataframe3.xlsx")
# print(aa)

import pandas as pd
import numpy as np

# 1. Creating DataFrames (Different Methods)


# From dictionary
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [25, 30, 35, 40, 45],
    'City': ['NY', 'LA', 'Chicago', 'Houston', 'Miami'],
    'Salary': [70000, 80000, 90000, 100000, 110000]
}
df = pd.DataFrame(data)

# From list of lists
data_list = [
    ['Alice', 25, 'NY', 70000],
    ['Bob', 30, 'LA', 80000],
    ['Charlie', 35, 'Chicago', 90000],
    ['David', 40, 'Houston', 100000],
    ['Eva', 45, 'Miami', 110000]
]
df_list = pd.DataFrame(data_list, columns=['Name', 'Age', 'City', 'Salary'])

# From CSV
# df_csv = pd.read_csv('data.csv')

# From Excel
# df_excel = pd.read_excel('data.xlsx')

# From numpy array
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
df_arr = pd.DataFrame(arr, columns=['A', 'B', 'C'])

print("Original DataFrame:")
print(df)
print("\n")

# =============================================
# 2. Basic DataFrame Operations
# =============================================

# Display first n rows
print("First 2 rows:")
print(df.head(2))
print("\n")

# Display last n rows
print("Last 2 rows:")
print(df.tail(2))
print("\n")

# DataFrame info
print("DataFrame info:")
print(df.info())
print("\n")

# DataFrame description
print("DataFrame description:")
print(df.describe())
print("\n")

# DataFrame shape
print("DataFrame shape:", df.shape)
print("\n")

# DataFrame columns
print("DataFrame columns:", df.columns.tolist())
print("\n")

# DataFrame index
print("DataFrame index:", df.index)
print("\n")

# =============================================
# 3. Selecting Data
# =============================================

# Select column
print("Name column:")
print(df['Name'])
print("\n")

# Select multiple columns
print("Name and Age columns:")
print(df[['Name', 'Age']])
print("\n")

# Select rows by index
print("Row at index 2:")
print(df.iloc[2])
print("\n")

# Select rows by condition
print("People older than 30:")
print(df[df['Age'] > 30])
print("\n")

# Select rows and columns
print("Name of people older than 30:")
print(df.loc[df['Age'] > 30, 'Name'])
print("\n")

# =============================================
# 4. Data Manipulation
# =============================================

# Add new column
df['Senior'] = df['Age'] > 35
print("DataFrame with Senior column:")
print(df)
print("\n")

# Modify column
df['Salary'] = df['Salary'] * 1.1  # 10% raise
print("DataFrame with updated Salary:")
print(df)
print("\n")

# Delete column
df.drop('Senior', axis=1, inplace=True)
print("DataFrame after dropping Senior column:")
print(df)
print("\n")

# Rename columns
df.rename(columns={'City': 'Location'}, inplace=True)
print("DataFrame with renamed columns:")
print(df)
print("\n")

# Sort values
df_sorted = df.sort_values('Age', ascending=False)
print("DataFrame sorted by Age:")
print(df_sorted)
print("\n")

# =============================================
# 5. Handling Missing Data
# =============================================

# Create DataFrame with missing values
df_missing = pd.DataFrame({
    'A': [1, 2, np.nan, 4],
    'B': [5, np.nan, np.nan, 8],
    'C': [10, 20, 30, 40]
})

print("DataFrame with missing values:")
print(df_missing)
print("\n")

# Check for missing values
print("Missing values:")
print(df_missing.isna())
print("\n")

# Fill missing values
df_filled = df_missing.fillna(value={'A': 0, 'B': 99})
print("DataFrame with filled missing values:")
print(df_filled)
print("\n")

# Drop rows with missing values
df_dropped = df_missing.dropna()
print("DataFrame after dropping rows with missing values:")
print(df_dropped)
print("\n")

# =============================================
# 6. Grouping and Aggregation
# =============================================

# Create DataFrame for grouping
df_group = pd.DataFrame({
    'Department': ['HR', 'Tech', 'HR', 'Tech', 'Finance', 'Finance'],
    'Employee': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank'],
    'Salary': [70000, 80000, 90000, 100000, 110000, 120000]
})

print("Grouping DataFrame:")
print(df_group)
print("\n")

# Group by department
grouped = df_group.groupby('Department')

# Aggregate functions
print("Average salary by department:")
print(grouped['Salary'].mean())
print("\n")

print("Salary statistics by department:")
print(grouped['Salary'].describe())
print("\n")

# Multiple aggregations
print("Multiple aggregations:")
print(grouped['Salary'].agg(['mean', 'sum', 'count', 'max', 'min']))
print("\n")

# =============================================
# 7. Merging, Joining, and Concatenating
# =============================================

# Create DataFrames to merge
df1 = pd.DataFrame({
    'ID': [1, 2, 3],
    'Name': ['Alice', 'Bob', 'Charlie']
})

df2 = pd.DataFrame({
    'ID': [2, 3, 4],
    'Salary': [80000, 90000, 100000]
})

# Inner join
print("Inner join:")
print(pd.merge(df1, df2, on='ID', how='inner'))
print("\n")

# Left join
print("Left join:")
print(pd.merge(df1, df2, on='ID', how='left'))
print("\n")

# Right join
print("Right join:")
print(pd.merge(df1, df2, on='ID', how='right'))
print("\n")

# Outer join
print("Outer join:")
print(pd.merge(df1, df2, on='ID', how='outer'))
print("\n")

# Concatenation
df3 = pd.DataFrame({
    'ID': [4, 5],
    'Name': ['David', 'Eva']
})

print("Concatenated DataFrames:")
print(pd.concat([df1, df3], ignore_index=True))
print("\n")

# =============================================
# 8. Pivot Tables
# =============================================

# Create DataFrame for pivot
df_pivot = pd.DataFrame({
    'Date': ['2023-01-01', '2023-01-01', '2023-01-02', '2023-01-02'],
    'City': ['NY', 'LA', 'NY', 'LA'],
    'Temperature': [32, 75, 30, 72],
    'Humidity': [80, 50, 85, 55]
})

print("Pivot table - mean temperature by city and date:")
print(pd.pivot_table(df_pivot, values='Temperature', index='Date', columns='City', aggfunc='mean'))
print("\n")

# =============================================
# 9. Time Series Operations
# =============================================

# Create time series data
dates = pd.date_range('20230101', periods=6)
df_time = pd.DataFrame({
    'Date': dates,
    'Value': np.random.randn(6)
})

print("Time series DataFrame:")
print(df_time)
print("\n")

# Set date as index
df_time.set_index('Date', inplace=True)

# Resample (monthly mean)
print("Resampled data (monthly mean):")
print(df_time.resample('M').mean())
print("\n")

# =============================================
# 10. Applying Functions
# =============================================

# Apply function to column
df['Salary'] = df['Salary'].apply(lambda x: x * 1.05)  # 5% raise
print("DataFrame after salary raise:")
print(df)
print("\n")

# Apply function to each element
print("Formatted salary:")
print(df['Salary'].apply(lambda x: f"${x:,.2f}"))
print("\n")


# Apply function to multiple columns
def age_salary_ratio(row):
    return row['Salary'] / row['Age']


df['Salary/Age'] = df.apply(age_salary_ratio, axis=1)
print("DataFrame with Salary/Age ratio:")
print(df)
print("\n")

# =============================================
# 11. String Operations
# =============================================

# String operations on Name column
df['Name_Upper'] = df['Name'].str.upper()
df['Name_Length'] = df['Name'].str.len()
print("DataFrame with string operations:")
print(df)
print("\n")

# =============================================
# 12. Input/Output Operations
# =============================================

# Save to CSV
df.to_csv('output.csv', index=False)

# Save to Excel
df.to_excel('output.xlsx', index=False)

# Save to JSON
df.to_json('output.json')

print("Data saved to output.csv, output.xlsx, and output.json")
print("\n")

# =============================================
# 13. Advanced Operations
# =============================================

# Multi-indexing
arrays = [
    ['A', 'A', 'B', 'B'],
    [1, 2, 1, 2]
]
index = pd.MultiIndex.from_arrays(arrays, names=('Letter', 'Number'))
df_multi = pd.DataFrame({'Value': [10, 20, 30, 40]}, index=index)

print("Multi-index DataFrame:")
print(df_multi)
print("\n")

# Cross-tabulation
print("Cross-tabulation example:")
print(pd.crosstab(df['Name'], df['Location']))
print("\n")

# Binning
print("Age bins:")
print(pd.cut(df['Age'], bins=[20, 30, 40, 50]))
print("\n")

# =============================================
# 14. Visualization (requires matplotlib)
# =============================================
try:
    import matplotlib.pyplot as plt

    # Plot histogram of ages
    df['Age'].plot(kind='hist', title='Age Distribution')
    plt.show()

    # Plot bar chart of salaries
    df.plot(x='Name', y='Salary', kind='bar', title='Salary by Name')
    plt.show()

    # Scatter plot
    df.plot(x='Age', y='Salary', kind='scatter', title='Age vs Salary')
    plt.show()
except ImportError:
    print("Matplotlib not installed. Visualization skipped.")
print("\n")

# =============================================
# 15. Other Useful Functions
# =============================================

# Unique values
print("Unique cities:", df['Location'].unique())
print("\n")

# Value counts
print("City value counts:")
print(df['Location'].value_counts())
print("\n")

# Correlation
print("Correlation matrix:")
print(df.corr())
print("\n")

# Memory usage
print("Memory usage:")
print(df.memory_usage())
print("\n")

# Replace values
print("Replace values example:")
print(df['Location'].replace({'NY': 'New York', 'LA': 'Los Angeles'}))
print("\n")

# Query
print("Query example (Age > 30):")
print(df.query('Age > 30'))
print("\n")

# Duplicates
print("Check for duplicates:")
print(df.duplicated())
print("\n")

# Sample rows
print("Random sample of 2 rows:")
print(df.sample(2))
print("\n")

# Iterate over rows
print("Iterating over rows:")
for index, row in df.iterrows():
    print(f"{row['Name']} is {row['Age']} years old")
print("\n")

# =============================================
# 16. Working with Large DataFrames
# =============================================

# Chunk processing (for large files)
# for chunk in pd.read_csv('large_file.csv', chunksize=10000):
#     process(chunk)

# Dask can be used for out-of-core DataFrames
# import dask.dataframe as dd
# ddf = dd.read_csv('very_large_file.csv')