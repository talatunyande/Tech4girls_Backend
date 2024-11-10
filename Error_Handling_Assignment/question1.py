#!/usr/bin/python3
# Question 1 Division Calculator
numerator = int(input("Enter the numerator : "))
denominator =int(input("Enter the denominator : "))
try:
    result= numerator /denominator
except ValueError:
   print("Enter valid number for numerator and denominator")
except ZeroDivisionError:
   print ("denomerator can not be zero . please enter a non- zero denomerator")
else:
   print("The result is " , result)
