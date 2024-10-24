#!/bin/bash
Firstnumber=$1
Secondnumber=$2
if  [  $1 -gt 10  -a $2 -gt 10  ] ;then
 echo " Both numbers are greater than 10" 
elif [  $1  -gt 10  -o $2 -gt 10 ]; then 
 echo "Atleast one number is greater than  10 "
else 
 echo  "none of the numbers are greater than  10" 
 fi