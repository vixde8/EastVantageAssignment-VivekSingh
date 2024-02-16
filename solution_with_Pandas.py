import pandas as pd
from sqlalchemy import create_engine


db_file = "xyz.db"     # Replace with a db with actual data and syntax Similar to xyz.db file attached

item_table = "items" 
order_table = "orders"
sales_table = "sales"
customer_table = "customer"

engine = create_engine(f'sqlite:///{db_file}')

# Reading tables in dataframes for transformations
item_df = pd.read_sql_table(item_table, con=engine)
order_df = pd.read_sql_table(order_table, con=engine)
sales_df = pd.read_sql_table(sales_table, con=engine)
customer_df = pd.read_sql_table(customer_table, con=engine)

# Joining DataFrames using merge
merged_df = pd.merge(customer_df, sales_df, on='customer_id')
merged_df = pd.merge(merged_df, order_df, on='sales_id')
merged_df = pd.merge(merged_df, item_df, on='item_id')

# Applying filters
result_df = merged_df[(merged_df['age'] >= 18) & (merged_df['age'] <= 35)]
print(result_df)
result_df = result_df.groupby(['customer_id', 'age', 'item_id']).agg({'quantity': 'sum'}).reset_index()
print(result_df)
result_df = result_df[result_df['quantity'] > 0]

# Renaming columns
result_df = result_df.rename(columns={'customer_id': 'Customer', 'age': 'Age', 'item_id': 'Item', 'quantity': 'Quantity'})

file_path = 'output.csv'
result_df.to_csv(file_path, index=False, sep=';')               # Writing the result to a ; delimited csv file

print("Write Successful...")