#!/bin/bash
#script to check if it is a root user or not
if [ $UID -ne 0 ]
then
    echo "You are not a root user"
else
    echo "You are a root user"
fi
