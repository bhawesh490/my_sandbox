#!/bin/bash
myArray=(1 2 3 4 5 bhawesh prashant)
for i in ${myArray[@]}
do
    echo "Number is $i"
done

echo "---------------------------------"
myArraynew=(using the different approach)
length=${#myArraynew[@]}
for (( i=0; i<$length; i++ )) #remember double parenthesis in arithmetic operations
do
    echo "Implentation is ${myArraynew[$i]}"
done
