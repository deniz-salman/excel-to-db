import json
import os
import pandas as pd
import sys

batch_size_limit = 15 * 1024 * 1024  

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
        return "'{}'".format(value.replace("'", "''").replace("\\", "\\\\").replace("\n", "\\n"))
    elif isinstance(value, (int, float)):
        return str(value)
    else:
        return "'{}'".format(value)

def get_batch_size_in_bytes(batch):
    return sys.getsizeof(", ".join(batch))

all_values = []
table_name = "delivery"
columns = None

row_data_count = 0

for excel_file in excel_files:
    print(f"\rReading data from {excel_file}.", end='')
    df = pd.read_excel(excel_file, engine='openpyxl')
    print(f"\rExtracting data from {excel_file}.")

    new_columns = {}
    for column in df.columns:
        for key, values in header_mapping.items():
            if column in values:
                new_columns[column] = key
                break
        else:
            new_columns[column] = column  

    df.rename(columns=new_columns, inplace=True)

    if columns is None:
        columns = ", ".join([f"`{col}`" for col in df.columns])

    for _, row in df.iterrows():
        row_data_count += 1
        print(f"\rTotal rows processed: {row_data_count}", end='')
        values = ", ".join([escape_sql_value(val) for val in row.values])
        all_values.append(f"({values})")

        if get_batch_size_in_bytes(all_values) >= batch_size_limit:
            sql_statement = f"INSERT INTO {table_name} ({columns}) VALUES {', '.join(all_values)};"
            with open(insert_data_file, 'a') as f:
                f.write(sql_statement + '\n')
                print(f"\rAdded insert query to {insert_data_file} for {len(all_values)} rows.")
            all_values = []

    print(f"\rExtracted data from {excel_file}.")

if all_values:
    sql_statement = f"INSERT INTO {table_name} ({columns}) VALUES {', '.join(all_values)};"
    with open(insert_data_file, 'a') as f:
        f.write(sql_statement + '\n')
        print(f"Added insert query to {insert_data_file} for {len(all_values)} rows.")

print(f"Total rows processed: {row_data_count}")
print("SQL generation completed.")