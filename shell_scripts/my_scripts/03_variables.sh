#!/bin/bash
#script to define variables

name="Bhawesh"
age=20
task="learn"

echo "name is $name and age is $age"
name="Prashant"
echo "name is $name"

#variable to store the output of the command
HOSTNAME=$(hostname)
PWD=$(pwd)
echo "Name of this machine is $HOSTNAME"
echo "The path of this file is $PWD"
