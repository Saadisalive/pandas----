import pandas as pd

data = {
    'Id': [1, 2, 3, 4],
    'Name': ['Pankaj', 'Meghna', 'David', 'Lisa'],
    'Role': ['CEO', None, None, None],
    'Salary': [100, 200, None, None]
}
df = pd.DataFrame(data)
print("Initial DataFrame:")
print(df)
print("\nInitial 2 values:")
print(df.head(2))
print("\nLast 2 values:")
print(df.tail(2))

print("\nTotal null values:")
print(df.isnull().sum().sum())

print("\nDataFrame Info:")
df.info()

df_rows_dropped = df.dropna(how='any')
print("\nDataFrame after dropping rows with null values:")
print(df_rows_dropped)

df_cols_dropped = df.dropna(axis=1, how='any')
print("\nDataFrame after dropping columns with null values:")
print(df_cols_dropped)


df_filled_salary = df.copy()
df_filled_salary['Salary'] = df_filled_salary['Salary'].fillna(300)
print("\nDataFrame after filling null Salary values:")
print(df_filled_salary)

df_filled_CEO = df.copy()
df_filled_CEO['Role'] = df_filled_CEO['Role'].fillna("CEO")
print("\nDataFrame after filling null CEO values:")
print(df_filled_CEO)