import pandas as pd
from typing import Optional, List, Tuple, Dict, Union
import openpyxl
from openpyxl.utils.datetime import to_excel


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
    return True, "DataFrame has passed all validations."

 # uses exmple
model_confing=pd.read_csv(r"C:\omkar\project\FRS\model_config.csv")
model_1=validate_dataframe(model_confing,n_cols=4,check_duplicates=True)
print(model_1)
# print(model_confing)

model_collateral=pd.read_csv(r"C:\omkar\project\FRS\model_collateral.csv")
# print(model_collateral)
model_2=validate_dataframe(model_collateral,n_cols=78,check_duplicates=True)
print(model_2)

import os
path =r"C:\omkar\project\FRS\model_auth_Rep"
ssv = [f for f in os.listdir(path) if f.endswith('.csv')]
#print(ssv)
dfs = []
# Read CSV files and append dataframes to the list
for file in ssv:
    model_auth_rep = pd.read_csv(os.path.join(path, file))
    dfs.append(model_auth_rep)
#print(dfs)


for df in dfs:
    model_auth_rep=validate_dataframe(df,n_cols=14,check_duplicates=True)
    print(model_auth_rep)
new=pd.concat(dfs,ignore_index=True)
print(new)

import duckdb

stage1=duckdb.query("select EAD*PD12*LGD as ECL_report1 from new").df()
print(stage1)

stage2=duckdb.query("select EAD*PDLT*LGD as ECL_report2 from new").df()
print(stage2)

stage3=duckdb.query("select EAD*LGD as ECL_report3 from new").df()
print(stage3)

ecl_dataframe=duckdb.query("select EAD,PD12,LGD,PDLT from new").df()
print(ecl_dataframe)

new2=pd.concat([ecl_dataframe,stage1,stage2,stage3],axis=1)
print(new2)
file_name="ECL_dataframe.xlsx"
path=r"C:\Users\prati\Desktop"
x1_path=os.path.join(path,file_name)
print(xl_path)
new2.to_excel(xl_path,index=false)




# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
#
# # Dataset लोड करा (CSV ची path द्या)
# df = pd.read_csv("salaries.csv")  # Replace with correct filename
#
# # जॉब टायटलनुसार सरासरी पगार काढा (USD मध्ये)
# avg_salary = df.groupby("job_title")["salary_in_usd"].mean().sort_values(ascending=False)
#
# # Chart तयार करा
# plt.figure(figsize=(12, 8))
# sns.barplot(x=avg_salary.values, y=avg_salary.index, palette="viridis")
#
# plt.title("जॉब टायटलनुसार सरासरी पगार (USD मध्ये)", fontsize=16)
# plt.xlabel("सरासरी पगार (USD)", fontsize=14)
# plt.ylabel("जॉब टायटल", fontsize=14)
# plt.tight_layout()
# plt.show()




# import pandas as pd
# import matplotlib.pyplot as plt
#
# # CSV फाईल लोड करा (फाईलचे नाव योग्य ठेवा)
# df = pd.read_csv("salaries.csv")  # Replace with correct file name
#
# # वर्षानुसार सरासरी पगार (USD) काढा
# yearly_avg_salary = df.groupby("work_year")["salary_in_usd"].mean().reset_index()
#
# # Line Graph तयार करा
# plt.figure(figsize=(10, 6))
# plt.plot(yearly_avg_salary["work_year"], yearly_avg_salary["salary_in_usd"], marker='o', linestyle='-', color='teal')
#
# plt.title("वर्षानुसार सरासरी पगारातील बदल (USD मध्ये)", fontsize=16)
# plt.xlabel("वर्ष (Year)", fontsize=14)
# plt.ylabel("सरासरी पगार (USD)", fontsize=14)
# plt.grid(True)
# plt.tight_layout()
# plt.show()
