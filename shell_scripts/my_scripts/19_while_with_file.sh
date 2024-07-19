#!/bin/bash
# while loop with file

while read myvar
do
    echo "Value from file is $myvar"
done < ../demo_files/demo.txt

