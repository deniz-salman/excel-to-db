#!/bin/bash

mysql --max_allowed_packet=1073741824 -h 127.0.0.1 -u deniz -p'dnzpss' --force delivery_db < "insert.sql"