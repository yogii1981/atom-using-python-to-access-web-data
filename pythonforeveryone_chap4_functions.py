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
from random import random

for i in random(10):
    x = random.random()
    print(x)

# using unifrom method
from random import random
x = random.uniform(0.0, 1.0) in range(10)
print(x)

# randomly selecting grretings

from random import random

greetings = ["Namaste", "Ola", "Hello", "Wie gehts"]
value = random.choice(greetings)
print(value + ' , Monica!')

#to choose any element from a squence at randon ,
# you can use choice
import random
t = [1,2,3]
random.choice(t)

# Math functions
import math
print(math)

import math
radians = 0.7
height = math.sin(-radians)

import math
degrees = 45
radians = degrees / 360.0 * 2 * math.pi
print(math.sin(radians))

import math 
print(math.sqrt(2)/ 2.0)
