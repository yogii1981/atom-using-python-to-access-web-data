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

# add new functions
# def ia key word which which defines
# new function and name of the function
# is print_lyrics
def print_lyrics():
    print("I'm a lumbejack, and I'm okay.")
    print("I work all day and I sleep all night")

print_lyrics()


#once you have defined the function ,
# you can use it inside another functions
# and we call it as repeat_lyrics

def repeat_lyrics():
    print_lyrics()
    print_lyrics()
def print_lyrics():
        print("I'm a lumbejack, and I'm okay.")
        print("I work all day and I sleep all night")
repeat_lyrics()

#parameters and arguement
# math.sin()  anything writtten in the bracket is the
# arguement passed to sin
# sin is a function

def print_twice(bruce):
    print(bruce)
    print(bruce)
# this function assigns the arguement to a parameter


# parameters are part of the function body and arguments are passed
# to parameters

def ref_demo(x):
    print("x=", x, " id = ", id(x))
    x = 42
    print("x=", x, " id = ", id(x))
# in above example id() function is used, which takes an object as
# a parameter. id(obj) returns the identity of the object "obj" . This
# identity , the return value of the function, is an integer
# which is unique and constant for this object during lifetime

def no_side_effects(cities):
     print(cities)
     cities = cities + ["Birmingham", "Bradford"]
     print(cities)

locations = ["London", "Leeds", "Glasgow", "Sheffield"]
no_side_effects(locations)
print(locations)


#### This changes drastically, if we increment the list by using
# augmented assigment operator +1 =.



#
def square(number):          #name of the function is square
    """Calculate the square of the number."""  #docstring which explains the p
        # of the fucntion#
    return number ** 2

square(7)      # 7 is an argument  and (number) is parameter

# functions with multiple parameters

def maximum(value1, value2,value3):
    """return the maxiumum value of three values."""
    max_value = value1
    if value2 > max_value:
        max_value = value2
        if value3 > max_value:
            max_value = value3
            return max_value

maximum(12,36,48)
print(maximum(12,36,48))

maximum("yellow","red","pink")

import random
for roll in range(10):
    print(random.randrange(2,8), end = ' ')

print("test")

def multiplytwo(a,b):
    multiply = a * b
    return multiply


x = multiplytwo(77,81)
print(x)

def average1(a,b,c,d):
    average = (a+b+c+d)/4
    return average

y = average1(8911,8711,9811,1111)
print(y)
