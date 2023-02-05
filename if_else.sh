#! /bin/bash

printf "Where do you live?: "
read home

if [[ "$home" = "ankara" ]]
then
        echo "no way, my home is not in cold city"
elif [[ "$home" = "antalya" ]]
then
        echo "ohh, there is so hot..."
elif [[ "$home" = "istanbul" ]]
then
        echo "yes you find it!!"
else
        echo "try again."
fi
             