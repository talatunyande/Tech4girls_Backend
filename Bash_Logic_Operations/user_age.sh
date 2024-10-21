#!/bin/bash
# this script is to prompt the user of their age
echo "How old are you ?:"
read=age
if [ $age -lt 18 ]; 
then 
echo "you are a minor"
else if [ $age -ge 18 && $age -le 64 ] ;
then 
echo "you are an adult "
else 
echo " you are a senior "
fi
fi