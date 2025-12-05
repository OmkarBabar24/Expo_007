import duckdb as db
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
#

# file1=pd.read_json("C:\\Users\\prati\\Downloads\\archive\\salaries.json")
# print(file1)

file=pd.read_csv("C:\\Users\\prati\\Downloads\\archive\\salaries.csv")
# print(file)
#
# print(file2.describe())
# print(file2.info)
# print(file2.dtypes)
# print(file.isnull().sum())


import pandas as pd
from typing import Optional, List, Tuple, Dict, Union

def validate_dataframe(df: pd.DataFrame,
                       n_cols: Optional[int] = None,
                       n_rows: Optional[Tuple[int, int]] = None,
                       columns: Optional[List[str]] = None,
                       column_types: Optional[Dict[str, type]] = None,
                       check_duplicates: bool = False,
                       check_null_values: bool = False,
                       unique_columns: Optional[List[str]] = None,
                       column_ranges: Optional[Dict[str, Tuple[Union[int, float], Union[int, float]]]] = None,
                       date_columns: Optional[List[str]] = None,
                       categorical_columns: Optional[Dict[str, List[Union[str, int, float]]]] = None
                       ) -> Tuple[bool, str]:
    """
    Validates a Pandas DataFrame based on specified criteria.

    Parameters:
    - df (pd.DataFrame): The DataFrame to be validated.
    - n_cols (int, optional): Number of expected columns in the DataFrame.
    - n_rows (tuple, optional): Tuple (min_rows, max_rows) specifying the expected range of rows.
    - columns (list, optional): List of column names that should be present in the DataFrame.
    - column_types (dict, optional): Dictionary mapping column names to the expected data types.
    - check_duplicates (bool, optional): Check for the presence of duplicate rows in the DataFrame.
    - check_null_values (bool, optional): Check for the presence of null values in the DataFrame.
    - unique_columns (list, optional): List of columns that should have only unique values.
    - column_ranges (dict, optional): Dictionary mapping numeric columns to the allowed ranges.
    - date_columns (list, optional): List of columns containing date values to validate the format.
    - categorical_columns (dict, optional): Dictionary mapping categorical columns to allowed values.

    Returns:
    - tuple: (bool, str) indicating success or failure, and an optional description of the problem.
    """

    # Validate number of columns
    if n_cols is not None and len(df.columns) != n_cols:
        return False, f"Error: Expected {n_cols} columns, but found {len(df.columns)} columns."

    # Validate row range
    if n_rows is not None:
        min_rows, max_rows = n_rows
        if not (min_rows <= len(df) <= max_rows):
            return False, f"Error: Number of rows should be between {min_rows} and {max_rows}."

    # Validate columns
    if columns is not None and not set(columns).issubset(df.columns):
        missing_columns = set(columns) - set(df.columns)
        return False, f"Error: Missing columns: {missing_columns}."

    # Validate column types
    if column_types is not None:
        for col, expected_type in column_types.items():
            if col not in df.columns:
                return False, f"Error: Column '{col}' not found."
            if not df[col].dtype == expected_type:
                return False, f"Error: Column '{col}' should have type {expected_type}."

    # Validate duplicates in specific columns
    if check_duplicates and df.duplicated().any():
        return False, "Duplicates found in the DataFrame."

    # Validate null values in specific columns
    if check_null_values and df.isnull().any().any():
        return False, "DataFrame contains null values."

    # Validate unique values in specific columns
    if unique_columns is not None:
        for col in unique_columns:
            if col in df.columns and df[col].duplicated().any():
                return False, f"Column '{col}' should have only unique values."

    # Validate values in a specific range
    if column_ranges is not None:
        for col, value_range in column_ranges.items():
            if col in df.columns and not df[col].between(*value_range).all():
                return False, f"Values in '{col}' should be between {value_range[0]} and {value_range[1]}."

    # Validate date format (assuming 'date_columns' are date columns)
    if date_columns is not None:
        for col in date_columns:
            if col in df.columns:
                try:
                    pd.to_datetime(df[col], errors='raise')
                except ValueError:
                    return False, f"'{col}' should be in a valid date format."

    # Validate categorical values
    if categorical_columns is not None:
        for col, allowed_values in categorical_columns.items():
            if col in df.columns and not df[col].isin(allowed_values).all():
                return False, f"Values in '{col}' should be {allowed_values}."

    # If all validations pass, return True
    return True, "DataFrame has passed all validations."

df1=pd.read_csv("C:\\Users\\prati\\Downloads\\archive\\salaries.csv")
# df=df.duplicated().sum()
df=df1.drop_duplicates()
# print(df)
aa=validate_dataframe(df,n_cols=11,categorical_columns=None,check_duplicates=True,n_rows=(10000, 140000),)
print(df1.columns)



# पगारानुसार टॉप 5 जॉब्स कोणते आहेत?
ab=duckdb.query("select job_title,salary from df order by salary desc limit 5").df()
# print(ab)

# देशनिहाय (country-wise) सरासरी पगार किती आहे?
#
ac=duckdb.query("select company_location,avg(salary) as avg_salary from df group by company_location order by avg_salary desc limit 10").df()
# print(ac)
# जास्त पगार कोणत्या अनुभव पातळीवर मिळतो?
cd=duckdb.query("select experience_level ,salary from df order by salary desc limit 1").df()
# print(cd)
# Remote (घरून काम) vs Office मध्ये कोणाला जास्त पगार आहे?
#
ba=duckdb.query("select remote_ratio,ANY_VALUE(salary) as T from df group by remote_ratio  order by T desc ").df()
# print(ba)

# Entry Level मध्ये कोणत्या जॉब्सना जास्त पगार मिळतो?

aa=duckdb.query("select experience_level,max(salary) from df group by experience_level having experience_level='EN'").df()
# print(aa)
zz=duckdb.query(" select experience_level, salary from df  where experience_level = 'EN' order by salary desc limit 1").df()
# print(zz)

# 📈 Visualization (Visualization) सुचना:
# Pie Chart: कंपनी साईजचे प्रमाण


az=duckdb.query("select distinct company_size from df ").df()
# print(az)
ax=duckdb.query("select company_size, count(work_year) as year from df group by company_size").df()
# print(ax)
# fx=ax['company_size'].to_numpy()
# fy=ax['year'].to_numpy()
# plt.bar(fx,fy)
# plt.show()
# fx=ax['company_size'].to_numpy()
# fy=ax['year'].to_numpy()
# plt.title("Size of company ")
# plt.xlabel("company size")
# plt.ylabel("year")
# plt.bar(fx,fy,color="red")
# plt.plot(fx,fy)
# plt.scatter(fx,fy)
# plt.fill_between(fx,fy)
# # plt.show()
# plt.pie(ax['year'], labels=ax['company_size'])
# # plt.pie(fy,labels=fx)
# plt.show()


# Bar Chart: जॉब टायटलनुसार सरासरी पगार

bb=duckdb.query("select job_title,avg(salary) as salary from df group by job_title order by salary desc limit 10  ").df()

# plt.bar(bb["job_title"],bb["salary"])
# plt.xticks(rotation=90)
# plt.show()

# =ax['company_size'].to_numpy()
# fy=ax['year'].to_numpy()
# plt.title("Size of company ")
# plt.xlabel("company size")
# plt.ylabel("year")
# plt.bar(fx,fy,color="red")
# plt.plot(fx,fy)
# plt.scatter(fx,fy)
# plt.fill_between(fx,fy)
# # plt.show()
# plt.pie(bb['salary'], labels=bb['job_title'],autopct='%1.1f%%')
# plt.pie(bb,labels=bb)
# plt.show()


# Line Graph: वर्षानुसार पगारातील बदल
#
yy=duckdb.query("select work_year,avg(salary_in_usd) as salary from df group by work_year ").df()
print(yy)
plt.pie(yy['salary'], labels=yy['work_year'],autopct='%1.1f%%')
plt.show()


