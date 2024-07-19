#!/bin/bash
#key value array
declare -A myArray
myArray=([name]=Bhawesh [age]=30 [city]=Almora)
echo "${myArray[name]}"
echo "${myArray[age]}"
echo "${myArray[city]}"
