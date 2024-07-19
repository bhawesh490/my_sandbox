#!/bin/bash
#example of using continue in loop
#suppose we need to print only odd no

for i in 1 2 3 4 5 6 7 8 9 10
do
    if [[ $i%2 -eq 0 ]]
    then
        continue
    fi
    echo $i

done
