#!/bin/bash
read -p "Enter your Marks: " marks
#we could have used single bracket also
#Notice the space between [[ and $marks
if [[ $marks -ge 80 ]]
then
    echo "1st Division"
elif [[ $marks -ge 60 ]]
then
    echo "2nd Division"
elif [[ $marks -ge 40 ]]
then
    echo "3rd Division"
else
    echo "You have failed the exam"
fi
