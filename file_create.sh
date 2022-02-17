#!/bin/bash
read -p "Enter file name =" file
if [ -e $file ]; then
echo "$file you have"
else
echo "$file you do not have"
sleep 0.5
echo  "$file is going to be ready"
touch $file
sleep 0.5
echo "$file is ready"
echo hello > $file
sleep 0.5
echo "see file:"
cat $file
fi