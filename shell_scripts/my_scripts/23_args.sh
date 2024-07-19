#!/bin/bash
if [[ $# -eq 0 ]]
then
    echo "No Arguments"
    exit 1
fi

echo "First Argument is $1"
echo "Second Argument is $2"
echo "all the args are: $@"
echo "Number of args are: $#"

#for loop to access the values from arguments

for arg in $@
do
    echo "Argument is $arg"
done

# to run this script
# bash 23_args.sh bhawesh mehta
