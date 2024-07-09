#!/bin/bash

mysql -h 127.0.0.1 -u deniz -p'dnzpss' --force delivery_db < "insert.sql"