#!/bin/bash
#And Operator
read -p "Enter Your Name: " name
read -p "Enter Your Age: " age
read -p "Enter Your Code: " code
read -p "What is your country? " country

# in case of string use == sign
if [[ $age -gt 18 && $age -lt 30 && $country == "India" && $code -eq 123 ]]
then
    echo "$name having age $age from country $country is eligible for the job"
else
    echo "$name having age $age from country $country is not eligible for the job because code is $code"
fi
