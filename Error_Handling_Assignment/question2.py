#!/usr/bin/python3
#Question  3 : Dictionary Lookup
data = {"name":"Alice" , "age":"25" ,"country":"Wounderland"}
key = input("Enter the key you want to look up :")
try:
    print("Value:" , data[key]) 
except KeyError:
    print("please this key is not in the dictionary.please enter new key")
