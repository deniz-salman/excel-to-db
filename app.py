import json
import os
import pandas as pd

with open('headers_mapping.json', 'r') as f:
    header_mapping = json.load(f)

files_dir = 'excel_files/'
excel_files = [os.path.join(files_dir, file) for file in os.listdir(files_dir) if file.endswith('.xlsx')]
insert_data_file = 'insert.sql'


open(insert_data_file, 'w').close()

def escape_sql_value(value):
    if pd.isna(value):
        return 'NULL'
    elif isinstance(value, str):
        return f"""'{value.replace("'", "''")}'"""
    elif isinstance(value, (int, float)):
        return str(value)
    else:
        return f"""'{value}'"""

for excel_file in excel_files:
    df = pd.read_excel(excel_file, engine='openpyxl')

    new_columns = {}
    for column in df.columns:
        for key, values in header_mapping.items():
            if column in values:
                new_columns[column] = key
                break
    df.rename(columns=new_columns, inplace=True)

    table_name = "delivery"
    columns = ", ".join([f"`{col}`" for col in df.columns])

    with open(insert_data_file, 'a') as f:
        for _, row in df.iterrows():
            values = ", ".join([escape_sql_value(val) for val in row.values])
            sql_statement = f"INSERT INTO {table_name} ({columns}) VALUES ({values});"
            f.write(sql_statement + '\n')

    print(f"Extracted data from {excel_file}.")