#!/usr/bin/python3
#Creating class BankAccount
class BankAccount:
    bank_name="Tech4Girls Bank"

    def __init__(self,account_holder):
       self.account_holder=account_holder
       self.balance=0
    
# method for depositing amount
    def deposit(self,amount):
     if amount>=1:
      self.balance += amount
      print  ("amount deposited amount successfully")
    
    #method for withdrawing amount
    def withdraw(self,amount):
      if amount >=1:
        self.balance +=amount
        print (" you have withdraw  successfull")

        #using static method to display the bank policy 
@staticmethod
def bank_policy():
  return f"you are not allowed to withdraw more than amount deposited"

@classmethod
def get_bank_name(cls):
   return cls.bank_name


account= BankAccount("Talatu")
print (account.deposit(700))
print(account.withdraw(500))
print(bank_policy())







