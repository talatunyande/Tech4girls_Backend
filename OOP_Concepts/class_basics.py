#!/usr/bin/python3
#defining class called car
class Car:
    #Initializing variables make,model and year
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year

        #print car's details
    def display_info(self):
        return f' Our {self.make} car was modeled in {self.model} and made in year {self.year}'
    
    #ceating instance of the car
car1=Car("Toyota","Camry",2021)

#calling the function
print (car1.display_info())


