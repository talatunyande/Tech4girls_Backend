#!/bin/bash
if [ $#  -ne 2 ]; then
num1=$1
num2=$2
if [  "$num1" -gt  "num2"  ]; then
echo "num1 is grester than $num2"
else 
if [  "$num1" -it "$num2" ];
then
echo "$num1 is less than $num2"
else
 echo "$num1 and $num2 are equal"
fi