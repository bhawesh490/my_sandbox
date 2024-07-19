#!/bin/bash
#Arithmetic Operations
#Approach 1
x=10
y=20
let mul=$x*$y
echo "Multiplication of $x and $y is $mul"
let sum=$x+$y
echo "Sum of $x and $y is $sum"

#Approach 2
read -p "Enter First Number:" x
read -p "Enter Second Number:" y
let mul=$x*$y
echo "Multiplication of $x and $y is $mul"

#Approach 3
#use of double case brackets
read -p "Enter the first Number" x
read -p "Enter the second Number" y
echo "Subtraction values is $((x-y))"
