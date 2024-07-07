import json
import os
import pandas as pd

header_mapping = open('headers_mapping.json', 'r').read()
header_mapping = json.loads(header_mapping)

files_dir = 'excel_files/'
excel_files = [os.path.join(files_dir, file) for file in os.listdir(files_dir) if file.endswith('.xlsx')]

all_sql_statements = []

for excel_file in excel_files:
    df = pd.read_excel(excel_file)
    
    new_columns = {}
    for column in df.columns:
        for key, values in header_mapping.items():
            if column in values:
                new_columns[column] = key
                break
    
    df.rename(columns=new_columns, inplace=True)

    table_name = "delivery" 
    columns = ", ".join(df.columns)
    
    for _, row in df.iterrows():
        values = ", ".join([f"'{str(val)}'" for val in row.values])
        sql_statement = f"INSERT INTO {table_name} ({columns}) VALUES ({values});"
        all_sql_statements.append(sql_statement)
    print(f"SQL statements created for {excel_file}")
    
output_file = "all_inserts.sql"
with open(output_file, 'w', encoding='utf-8') as f:

    f.write("\n".join(all_sql_statements))