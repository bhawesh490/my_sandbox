#!/bin/bash
#arrays
myArray=(1 2 3 4 5 "Hello bhawesh" bhawesh)
echo "Element is 6th index is ${myArray[6]}"
echo "All elements in the array are ${myArray[@]}"
echo "All elements in the array are ${myArray[*]}"

#how to find no of values in an array
echo "No of values in the array are ${#myArray[*]}"
#extract specific values from array
echo "Extracting values from array ${myArray[*]:6:2}"
#updating array with the new values
myArray+=("Prashant")
echo "All elements in the array are ${myArray[@]}"
