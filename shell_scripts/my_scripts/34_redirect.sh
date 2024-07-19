#!/bin/bash
ping -c 1 www.google.com > redirect.log

# dev/null
<<comment
in case if we dont want to print the output
of a command on terminal or write in a file,
we can redirect the output to /dev/null
example
#cd /root &> /dev/null
comment

