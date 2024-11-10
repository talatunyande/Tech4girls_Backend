#!/usr/bin/python3
#Question 4: Integer Conversion
#ISSUES: invalid input
user_input =input("Enter a number : ")
try:
   converted_number = int(user_input)
except ValueError:
    print("Invalid input .please try again")
else :
    print("The number you entered is :" , converted_number)
    