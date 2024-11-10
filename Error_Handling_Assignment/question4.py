#!/usr/bin/python3
#Question4:List Index Access
items=["apple","banana","cherry"]
try:
    index = int(input("Enter the index of the item you want to access :"))
except ValueError:
    print("please invalid index. please try again")
except IndexError:
    print("please ypu entered a wrong index .try again with a different index")
else:
   print("You selected ", items[index])