#Question 5: Age Validator
try:
 age = int(input("Enter your age: "))
except ValueError:
 print ("The value you entered is invalid please try again")
if age <0:
    print("Age cannot be negative ! ")
elif age >120:
    print("That age is unlikely ! ")
else:
    print("Your age is: age")
