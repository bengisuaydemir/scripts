#! /bin/bash

printf "what is your name?: "
read name

printf "When is your birthday?: "

read birthday

#get date:
let year=$(date +"%Y")
#birthday
let age=year-birthday
#

printf "so your age is "$age" \n " .
                                     