#!/bin/bash
# this script is 
if [ -z "$1"] ; then 
echo "Please provide a number 'n' as an argument ."
exit 1
fi
n=$1
sum=0
for (( i=1; i<=n;i++  ))
do 
sum=$((sum = i))
done 
echo "The sum of number from 1 to $n is: $sum"
