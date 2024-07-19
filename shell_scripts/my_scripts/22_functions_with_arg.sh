#!/bin/bash
welcome()
{
echo "hi $1 how are you?"
echo "hi $2 how are you?"
echo "Adding $1+$2"

}

welcome bhawesh saumya
welcome Yogesh Ankit

read -p "Enter First Number:" x
read -p "Enter Second Number:" y

add()
{

echo "addition of $x and $y is $((x+y))"

}

add
