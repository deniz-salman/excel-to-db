#!/bin/bash

successful_inserts=0
failed_inserts=0

mysql -h 127.0.0.1 -u deniz -p'dnzpss' --force delivery_db < "insert.sql" 2>&1 | \
while IFS= read -r line
do
    echo "$line" 
    if [[ "$line" == *"Query OK"* ]]; then
        successful_inserts=$((successful_inserts + 1))
    elif [[ "$line" == *"ERROR"* ]]; then
        failed_inserts=$((failed_inserts + 1))
    fi
    echo "Successful inserts: $successful_inserts"
    echo "Failed inserts: $failed_inserts"
done