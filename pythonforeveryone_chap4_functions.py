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
