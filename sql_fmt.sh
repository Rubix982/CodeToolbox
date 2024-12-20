#!/bin/bash

# Ensure that two arguments are provided
if [ "$#" -ne 2 ]; then
  echo "Usage: $0 <SQL_QUERY> <PARAMS>"
  exit 1
fi

query=$1
params=$2

# Replace placeholders in the SQL query with values from the params array
for i in $(seq 1 $(echo $params | jq length)); do 
  query=$(echo $query | sed "s/\\\$$i/$(echo $params | jq -r .[$((i-1))])/")
done

# Output the final SQL query
echo "$query"

