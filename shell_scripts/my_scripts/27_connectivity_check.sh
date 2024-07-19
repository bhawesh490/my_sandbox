#!/bin/bash
read -p "which site you want to check?" site
ping -c 1 $site
# echo $? to check the status of last command
if [ $? -eq 0 ]
then
    echo "$site is up"
else
    echo "$site is down"
fi

