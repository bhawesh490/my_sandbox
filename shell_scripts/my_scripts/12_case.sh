#!/bin/bash
#Case statement
echo "Provide an Option"
echo "a for print date"
echo "b for list of scripts"
echo "c to check current locations"

read choice
case $choice in
    a)date;;
    b)ls;;
    c)pwd;;
    *)echo "Invalid Option";;
esac

echo "Provide an Option Again"
echo "a for print date"
echo "b for list of scripts"
echo "c to check current locations"

read choice
case $choice in
    a)
        echo "current date is "
        date
        ;;
    b)
        echo "List of scripts"
        ls;;
    c)
        echo "Current location is "
        pwd;;
    *)echo "Invalid Option";;
esac
