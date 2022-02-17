#!/bin/bash
read -p "Enter directory name= " dir
if [ -e directory ]; then
echo "$dir you have"
else
echo "$dir you do not have"
sleep 0.5
echo  "$dir is going to be ready"
mkdir $dir
sleep 0.5
echo "$dir is ready"
fi
