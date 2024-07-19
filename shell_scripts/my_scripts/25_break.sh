#!/bin/bash
#we need to confirm if the given number is present or not
no=6

for i in 1 2 3 4 5 6 7 8 9
do
    if [[ $no -eq $i ]]
    then
        echo "$no Number is present"
        break
    fi
    echo "Number is $i"
done
