import pandas as pd
from typing import Optional, List, Tuple, Dict, Union
import openpyxl


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

# Usage example:
model_config = pd.read_csv(r"C:\omkar\project\FRS\model_config.csv")
is_valid, message = validate_dataframe(model_config, n_cols=4, check_duplicates=True)
#print(is_valid, message)

# Usage example:
model_collateral = pd.read_csv(r"C:\omkar\project\FRS\model_collateral.csv")
is_valid, message = validate_dataframe(model_collateral, n_cols=14, check_duplicates=True)

#print(is_valid, message)
#print(model_collateral)

#reading all files in one dataframes

import os

path =r"C:\omkar\project\FRS\model_auth_Rep"
ssv = [f for f in os.listdir(path) if f.endswith('.csv')]
#print(ssv)
dfs = []
# Read CSV files and append dataframes to the list
for file in ssv:
    model_auth_rep = pd.read_csv(os.path.join(path, file))
    dfs.append(model_auth_rep)

# Validate each dataframe in the list
for df in dfs:
    is_valid, message = validate_dataframe(df, n_cols=14, check_duplicates=True)
#print(is_valid, message)

# #join

# df1=pd.concat([model_config,model_collateral],ignore_index=True)
# print(df1)

df2=pd.concat([df],ignore_index=True)
# print(df2)
print(df2.columns)

#ECL report:-
stage1ecl=df2['EAD']*df2['PD12']*df2['LGD']
# print(stage1ecl)
#
stage2ecl = df2['EAD']*df2['PDLT']*df2['LGD']
#print(stage2ecl)

stage3ecl=df2['EAD']*df2['LGD']
#print(stage3ecl)
#
# ecl_dataframe=EAD,PD12,LGD,PDLT,stage1ecl,stage2ecl,stage3ecl
EAD=df['EAD']
PD12=df['PD12']
LGD=df['LGD']
PDLT=df['PDLT']

# ecl_dataframe=[EAD,PD12,LGD,PDLT,stage1ecl,stage2ecl,stage3ecl]
# print(ecl_dataframe)

ecl_dataframe=pd.DataFrame({
    'EAD':EAD,
    'PD12':PD12,
    'LGD':LGD,
    'PDLT':PDLT,
    'stage1ecl':stage1ecl,
    'stage2ecl':stage2ecl,
    'stage3ecl':stage3ecl
})
print(ecl_dataframe)

file_name='ecl_dataframe.xlsx'

path=os.path.join(os.path.expanduser("~"), "Desktop")
print(path)
xl_path=os.path.join(path,file_name)
print(xl_path)
ecl_dataframe.to_excel(xl_path, index=False)


Previous_EAD=df2['Previous EAD']
#ead variation reports:-
change_EAD=EAD-Previous_EAD
print(change_EAD)

percentage_change_EAD=((EAD-Previous_EAD)/Previous_EAD)*100
#print(percentage_change_EAD)

# EAD_DF=EAD,Previous EAD,change_ead,percentage in ead
EAD_DF=[EAD,Previous_EAD,change_EAD,percentage_change_EAD]
#print(EAD_DF)

EAD_DF=pd.DataFrame({
        'EAD':EAD,
        'Previous_EAD':Previous_EAD,
        'change_EAD':change_EAD,
        'percentage_change_EAD':percentage_change_EAD
})
print(EAD_DF)
file_name='EAD_DF.xlsx'
path=os.path.join(os.path.expanduser("~"), "Desktop")

print(path)
xl_path=os.path.join(path,file_name)
print(xl_path)
EAD_DF.to_excel(xl_path, index=False)

Previous_LGD=df2['Previous LGD']
#LGD variation reports:-
change_LGD=LGD-Previous_LGD
print(change_LGD)
percentage_change_LGD=((LGD-Previous_LGD)/Previous_LGD)*100
print(percentage_change_LGD)
LGD_DF=[LGD,Previous_LGD,change_LGD,percentage_change_LGD]
print(LGD_DF)

LGD_DF=pd.DataFrame({
    'LGD':LGD,
    'Previous_LGD':Previous_LGD,
    'change_LGD':change_LGD,
    'percentage_change_LGD':percentage_change_LGD
})
print(LGD_DF)

file_name='LGD_DF.xlsx'
path=os.path.join(os.path.expanduser("~"), "Desktop")
print(path)
xl_path=os.path.join(path,file_name)
print(xl_path)
LGD_DF.to_excel(xl_path,index=False)