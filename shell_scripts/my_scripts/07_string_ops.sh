#!/bin/bash
myVar="Hey Buddy, how are you?"
length=${#myVar}
echo "Length of my string is $length"
echo "Length of my string is ${#myVar}"
echo "Upper case is ${myVar^^}"
echo "lower case is ${myVar,,}"
#to replace a string
myNewVar=${myVar/Hey/Hello}
echo "New string is $myNewVar"
#to slice a string
echo "Sliced string is ${myVar:4}"

