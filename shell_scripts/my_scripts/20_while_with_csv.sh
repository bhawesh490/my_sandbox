#!/bin/bash
# read data from csv file
while IFS="," read -r id name
do
    echo "Id is $id"
    echo "Name is $name"
done < ../demo_files/demo.csv
