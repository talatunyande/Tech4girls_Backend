#!/usr/bin/python3
#looping through numbers
x=1
while x < 51 :
    print (x)
    x +=1

number=int(input('Enter number:'))

if number%3 == 0 :
    print('Fizz')
elif number%5==0 :
 print('Buzz')
elif number%3==0 and number%5 ==0:
    print('FizzBuzz')
else:
   print ('number')