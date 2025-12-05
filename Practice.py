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
# print(df)

# From list of lists
data_list = [
    ['Alice', 25, 'NY', 70000],
    ['Bob', 30, 'LA', 80000],
    ['Charlie', 35, 'Chicago', 90000],
    ['David', 40, 'Houston', 100000],
    ['Eva', 45, 'Miami', 110000]
]
df_list = pd.DataFrame(data_list, columns=['Name', 'Age', 'City', 'Salary'])
# print("Data_List:")
# print(df_list)
# print("\n")
# From numpy array
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
df_arr = pd.DataFrame(arr, columns=['A', 'B', 'C'])
# print("Original DataFrame:")
# print(df_arr)
# print("\n")

data=pd.read_csv(r"C:\\omkar\\project\\PIZZA Project\\pizza_sales.csv")
print(data)

# print(data.info)
# check missing value
# print(data.isna())
# print(data_missing)
# print(data.column.tolist)
print(data[['pizza_id']])

# data1=pd.read_excel(r"C:\Users\\prati\\Desktop\\ecl_dataframe3.xlsx")
# # print(data1)
# print(df.head(2))
# print("Last Data:")
# print(df.tail(2))

# print(df.info)
# print(df.describe())
# print("to sahpe:",df.shape)

# print(df.columns.tolist)

# =============================================
# 3. Selecting Data
# =============================================
# print(df[['Name', 'Age']])
# print(df['Name'])
# print(df.iloc[2])

# print(df[df['Age'] > 30])

