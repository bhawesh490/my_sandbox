#!/bin/bash
FILE='../demo_files/demo.txt'
cat $FILE
echo "---------------------------------"
for i in $(cat $FILE)
do
    echo $i
done
