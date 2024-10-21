#!/bin/bash
# 
echo "enter three numbers :"
read number 
num1=$1
num2=$2
num3=$3
sum=$((num1 + num2))
product=$((sum * num3 ))
echo "The sum of $num1 and $num2 is :$sum"
echo "Tproduct :$product"