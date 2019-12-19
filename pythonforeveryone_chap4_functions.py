type(32)

max("hello world")
print(max("hellow world")) # find the largest character
print(min("hello world")) # find the minimum character
print(len("Hello World"))  #length of hello World

int('32')
int('Hello')

# type conversion functions
int(3.999)
int(-2.3)

int('Hello')  #valueError: invalid internal

float(32)   #converting to float
print(float(32))

print(str(32))  #convert its arguement to a string

#random numbers
#write a program to generate random numbers between 0.0 and 1.0
import random

for i in random(10):
    x = random.random()
    print(x)
