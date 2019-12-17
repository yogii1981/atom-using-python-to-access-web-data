print(4)

type('Hello, World!')


type(3.2)

type('17')

print(1,000,000)

#variables



n = 17
print(n)

message = "and now for something different"
type(message)


#statements
print(1)

y1 = 4
print(y1)

a = 2 + 3
print (a)

#operators and operands

minute = 59
print(float(minute/60))

b = 'test1'
print(b)

minute = 59
minute // 60

#expression
x = 2
y= x + 17
print(y)

#exercise 1
5
x = 5
x + 1

#order of operations
#PEDMADS

y = (4 + 3 ** 2 + 4 - 2 * 6 / 2)
print (y)

#Modulus operator

quotient = 7 // 3
print(quotient)

remainder = 7 % 3
print(remainder)

#string operations

first = 10
second = 15
print(first + second)

first1 = '100'
second1 = '200'
print(first1 + second1)


#asking for the input
input = input()
print(input)

name = input('What is your name? \n') #newline
print(name)

prompt = 'What ....is airspeed velocity of unladen swallow? \n '
speed = input(prompt)

int(speed)
int(speed) + 5

#comments
#anything typed after # is considered comments
v = 5 # assiged velocity v is 5 mter/ second


a = 10
b = 20
c = a * b
print(c)

p = 100 # in dollars
r = 4 # 4 % rate
t = 12 # number of years = 12
SI = (p * r * t ) /100
print(SI)


words = "this is a sentence"
for word in words:
    print(word)

#debugging

#exercise 2: write a program
# that uses 'input' to prompt a user
# for their name and then welcome them

name = input('Enter your name: ')
print("Welcome", name)


#exercise 3 : Write a program to propmpt
# the user for hours and rate per hours
# to computer gross pay

Enter_hours = input("Enter your hours: ")
Enter_rate = input("Enter rate: ")
pay = (int(Enter_hours) * int(Enter_rate))
print(pay)

#Exercise 4: Assume that we execute the following assignement

width = 17
height = 12.0

print(width // 2)
print(type(width // 2))

print(width // 2.0)
print(type(width // 2.0))

print(height // 3)
print(type(height// 3))

# exercise 5: wite a program which the user for a celcius
# tempatture , convert the temperature to fahrenheit and print
# out the converted temperature

celcius_temp =  input("Enter a temperature: ")
fahrenheit_temp = (float(celcius_temp) * (9/5)) + 32
print(fahrenheit_temp,"F")
