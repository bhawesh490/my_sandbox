#!/bin/bash
read -p "Enter your Marks: " marks
#we could have used single bracket also
if [[ $marks -gt 40 ]]
then
    echo "You have passed the exam"
else
    echo "You have failed the exam"
fi
