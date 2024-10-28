#!/usr/bin/python3
is_student=('you are a student')
is_employed=('you are employed')
print(bool(is_student))
print(bool(is_employed))
"""
if condition
"""
if is_student and  is_employed :
    print(' You are a working student ')
elif is_student - is_employed:
   print('you are a student')
elif is_employed - is_student :
   print('you are employed but not a student')
"""
if condition
"""
age =int(input("Enter  your age : "))
if age >=18:
   license=(input ("please do you have a driver's license ?:"))
   if license=='yes':
      print ('you are allowed to drive')
   elif license == 'no':
      print("You need a driver's license to drive")
   else:
      print("you are not old to drive")



