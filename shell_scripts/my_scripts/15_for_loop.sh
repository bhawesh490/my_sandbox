#!/bin/bash
for i in 1 2 3 4 5
do
    echo "Number is $i"
done

for name in bhawesh mehta
do
    echo "${name^^}"
    echo "length of name is ${#name}"
done

for i in {1..10}
do
    echo "Number is $i"
done

