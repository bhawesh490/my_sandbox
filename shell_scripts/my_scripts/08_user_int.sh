#!/bin/bash
#Approach 1
echo "What is Your Name?"
read Name
echo "Hello,My name is $Name"
echo "${Name,,}"
echo "${Name^^}"
echo "Approach2 Starting....."
#Approach 2
read -p "What is your name?" Name
echo "Hello,My name is $Name"
