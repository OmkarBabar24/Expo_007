import duckdb
import duckdb as db
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import duckdb as db
from typing import Optional, List, Tuple, Dict, Union

customer_feedback=pd.read_csv("C:\\omkar\\project\\study project\\project 2 blinkit\\blinkit_customer_feedback.csv")
print('customer_feedback',customer_feedback)


customers=pd.read_csv("C:\\omkar\\project\\study project\\project 2 blinkit\\blinkit_customers.csv")
print('customers',customers)

marketing_performance=pd.read_csv("C:\\omkar\\project\\study project\\project 2 blinkit\\blinkit_marketing_performance.csv")
print('marketing_performance',marketing_performance)

order_items=pd.read_csv("C:\\omkar\\project\\study project\\project 2 blinkit\\blinkit_order_items.csv")
print('order_items',order_items)

orders=pd.read_csv("C:\\omkar\\project\\study project\\project 2 blinkit\\blinkit_orders.csv")
print('orders',orders)

product=pd.read_csv("C:\\omkar\\project\\study project\\project 2 blinkit\\blinkit_products.csv")
print('product',product)



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

customer_feedback=pd.read_csv("C:\\omkar\\project\\study project\\project 2 blinkit\\blinkit_customer_feedback.csv")
aa = validate_dataframe(customer_feedback, n_cols=8, check_duplicates=True, )
print('customer_feedback',aa)


customers=pd.read_csv("C:\\omkar\\project\\study project\\project 2 blinkit\\blinkit_customers.csv")
aa=validate_dataframe(customers,n_cols=11,check_duplicates=True,)
print("customers",aa)
#
marketing_performance=pd.read_csv("C:\\omkar\\project\\study project\\project 2 blinkit\\blinkit_marketing_performance.csv")
aa=validate_dataframe(marketing_performance,n_cols=11,check_duplicates=True,)
print('marketing_performance',aa)

order_items=pd.read_csv("C:\\omkar\\project\\study project\\project 2 blinkit\\blinkit_order_items.csv")
aa=validate_dataframe(order_items,n_cols=4,check_duplicates=True,)
print('order_items',aa)

orders=pd.read_csv("C:\\omkar\\project\\study project\\project 2 blinkit\\blinkit_orders.csv")
aa=validate_dataframe(orders,n_cols=10,check_duplicates=True,)
print('orders',aa)

product=pd.read_csv("C:\\omkar\\project\\study project\\project 2 blinkit\\blinkit_products.csv")
aa=validate_dataframe(product,n_cols=10,check_duplicates=True,)
print('product',aa)


print('customer_feedback')
print(customer_feedback.columns)

print('customers')
print(customers.columns)

print('marketing_performance')
print(marketing_performance.columns)

print('order_items')
print(order_items.columns)

print('orders')
print(orders.columns)

print('product')
print(product.columns)
#

# df=pd.concat([blinkit_customer_feedback,blinkit_customers])
# print(df)

# Data Quality Questions
# Are there any missing values in critical fields like customer ID, order dates, or product categories?
# a=orders[['customer_id','order_date']]
# print(a.tail())
# print(a.isnull().sum())

# Do all dates fall within a reasonable timeframe (no future dates or extremely old dates)?

# aa=duckdb.query("select order_date from orders where order_date between '2024-01-15' and '2024-02-15' ")
# print(aa)

# Are numeric fields like prices, quantities, and discounts within expected ranges?
# aa=duckdb.query("select a.price,a.margin_percentage,b.quantity  from product a inner join order_items b on a.product_id=b.product_id where a.price between 500 and 1000 ")
# print(aa)

# Are there any duplicate records in the dataset?
# aa=duckdb.query("with omkar as (select product_id,count(*) from product group by product_id having count(*)>1) select * from omkar "))
# print(aa)
#
# Business Logic Validation
# Do all order totals match the sum of their line items (including discounts)?
# aa=duckdb.query("select a.product_name,count(a.product_id) as total_product ,sum(b.quantity) as quantity from  product a inner join order_items b on a.product_id = b.product_id  group by a.product_name  ")
# print(aa)
# Are there any negative values in quantity or price fields where they shouldn't exist?
# aa=duckdb.query("select order_id,product_id,quantity,unit_price,CASE WHEN quantity < 0 THEN 'Invalid: Negative Quantity' WHEN unit_price< 0 THEN 'Invalid: Negative Price' ELSE 'Valid' END AS validation_status FROM order_items WHERE quantity < 0 OR unit_price < 0")
# print(aa)

# Do customer acquisition dates align with their first purchase dates?

# aa=duckdb.query("select order_date as date from orders order by order_date LIMIT 1 ")
# print(aa)

# Are there products with unusually high or low purchase frequencies that might indicate data errors?

aa=duckdb.query("select a.product_name,max(b.quantity),min(b.quantity) from product a inner join order_items b on a.product_id=b.product_id group by a.product_name")
print(aa)
#
# Consistency Checks
# Are product IDs consistent across different tables (if multiple tables exist)?

#
# Do customer demographics (age, location) follow expected distributions?
#
# Are there any timezone inconsistencies in the timestamp data?
#
# Do marketing campaign dates align with corresponding sales spikes?
#
# Completeness Questions
# Are all expected product categories represented in the data?
#
# Are there any gaps in the time series data (missing days/weeks)?
#
# Does the dataset cover the full geographic scope claimed?
#
# Are all expected customer segments represented?
#
# Relationship Validation
# Do all orders have corresponding customer records?
#
# Are there any products in orders that don't exist in the product catalog?
#
# Do referral codes match existing customer IDs where applicable?
#
# Are customer lifetime values calculated consistently across the dataset?