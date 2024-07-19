#!/bin/bash
FILEPATH="../demo_files/demo.txt"
if [[ -f $FILEPATH ]]; then
    echo "$(basename $FILEPATH) File exists"
else
    echo "File does not exist"
    exit 1
fi
