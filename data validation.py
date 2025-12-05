import pandas as pd
from typing import Optional, List, Tuple, Dict, Union
from pyspark.sql import SparkSession
from openpyxl.workbook import Workbook
import os
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
model_config_raw = pd.read_csv(r'C:\Users\prati\Desktop\data\model_collateral.csv')
is_valid, message = validate_dataframe(model_config_raw, n_cols=4, check_duplicates=True)
#print(is_valid, message)
#model_config
# Usage example
model_collateral_raw = pd.read_csv(r'C:\Users\prati\Desktop\data\model_config.csv')
is_valid, message = validate_dataframe(model_collateral_raw, n_cols=78, check_duplicates=True)
print(is_valid, message)
import glob
import os

folder_path =r"C:\Users\prati\Desktop\data\model_auth_Rep"
csv_files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]
dfs = []
for csv_file in csv_files:
    model_authorrep_rep_raw = pd.read_csv(os.path.join(folder_path, csv_file))
    dfs.append(model_authorrep_rep_raw)
for df in dfs:
    is_valid, message = validate_dataframe(df, n_cols=14, check_duplicates=True)
    #print(is_valid, message)


df1 = pd.concat([model_config_raw, model_collateral_raw],ignore_index=True)
#print(df1)
#print(df1.columns)
df2 = pd.concat([df], ignore_index=True)
#print(df2)

#ECL report:-
#stage1ecl=EAD*PD12*LGD
#stage2ecl = EAD*PDLT*LGD
#stage3ecl=EAD*LGD
#ecl_dataframe=EAD,PD12,LGD,PDLT,stage1ecl,stage2ecl,stage3ecl
stage1ecl=df2['EAD']*df2['PD12']*df2['LGD']
#print(stage1ecl)
stage2ecl =df2['EAD']*df2['PDLT']*df2['LGD']
#print(stage2ecl)
stage3ecl=df2['EAD']*df2['LGD']
#print(stage3ecl)
EAD=df2['EAD']
PD12=df2['PD12']
LGD=df2['LGD']
PDLT=df2['PDLT']

ecl_dataframe=[EAD,PD12,LGD,PDLT,stage1ecl,stage2ecl,stage3ecl]
#print(ecl_dataframe)
ecl_dataframe= pd.DataFrame({
    'EAD': EAD,
    'PD12': PD12,
    'LGD': LGD,
    'PDLT': PDLT,
    'stage1ecl': stage1ecl,
    'stage2ecl': stage2ecl,
    'stage3ecl': stage3ecl
})
#print(ecl_dataframe)

# ead variation reports:-
# change_EAD= EAD-"Previous EAD"
# percentage change_EAD=((EAD-"Previous EAD")/"Previous EAD")*100
# EAD_DF=EAD,Previous EAD,change_ead,percentage in ead
# write this to excel (local) ---->load into hive internal table.
Previous_EAD=df2['Previous EAD']
change_EAD= EAD-Previous_EAD
#print(change_EAD)
percentage_change_EAD=((EAD-Previous_EAD)/Previous_EAD)*100
#print(percentage_change_EAD)

EAD_DF=[EAD,Previous_EAD,change_EAD,percentage_change_EAD]
#print(EAD_DF)
EAD_DF= pd.DataFrame({
    'EAD': EAD,
    'Previous_EAD':Previous_EAD,
    'change_EAD': change_EAD,
    'percentage_change_EAD': percentage_change_EAD,
})

#print(EAD_DF)

#LGD variation reports: -
#change_LGD = LGD - "Previous LGD"
#percentage change_LGD = ((LGD - "Previous LGD") / "Previous LGD") * 100
#LGD_DF = LGD, Previous LGD, change_LGD, percentage in LGD

#write this to excel(local) - --->load intohive internal table.
Previous_LGD=df2["Previous LGD"]
change_LGD = LGD - Previous_LGD
#print(change_LGD)
percentage_change_LGD = ((LGD - Previous_LGD) / Previous_LGD) * 100
#print(percentage_change_LGD)

LGD_DF =[ LGD,Previous_LGD,change_LGD,percentage_change_LGD ]
#print(LGD_DF)
LGD_DF =pd.DataFrame({
    'LGD' : LGD,
     'Previous_LGD': Previous_LGD,
     'change_LGD' : change_LGD,
     'percentage_change_LGD' : percentage_change_LGD,
})

#print(LGD_DF)
#1.ECL report:-ecl_dataframe
excel_file_name = 'ecl_dataframe1.xlsx'
ecl_dataframe.to_excel(excel_file_name, index=False)
#print(excel_file_name)
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
final_excel_path = os.path.join(desktop_path, excel_file_name)
os.rename(excel_file_name, final_excel_path)
print(final_excel_path)

#2.ead variation reports:-EAD_DF
excel_file_name = 'EAD_DF1.xlsx'
EAD_DF.to_excel(excel_file_name, index=False)
#print(excel_file_name)
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
final_excel_path = os.path.join(desktop_path, excel_file_name)
os.rename(excel_file_name, final_excel_path)
print(final_excel_path)

#LGD variation reports: -LGD_DF
excel_file_name = 'LGD_DF1.xlsx'
LGD_DF.to_excel(excel_file_name, index=False)
#print(excel_file_name)
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
final_excel_path = os.path.join(desktop_path, excel_file_name)
os.rename(excel_file_name, final_excel_path)
print(final_excel_path)