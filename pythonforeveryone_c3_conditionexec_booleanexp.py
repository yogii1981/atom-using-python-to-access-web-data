# Conditional executuion
# IF statement
x = 10
if x > 0 :
    print('x is positive')
if x < 0 :
    pass

x = 3
if x < 10 :
    print('Small')

# IF and Else statement
x = 10
if x % 2 == 0 :
    print("x is even")
else :
    print ("x is odd")

#Chained conditionals
x = 6
y = 8
if x > y :
    print("x is greater than y")
elif x > y  :
    print("x and y are equal")
else :
    print("y is greater than x")


choice = "d"
if choice == "a" :
    print("Excellent grades")
elif choice == "b" :
    print("Good grades")
elif choice == "c" :
    print("nice grades")
else :
    print("poor grades")

#nested conditionals
x = 10
y = 20
if x == y:
    print('x and y are equal')
else:
    if x < y:
        print('x is less than y')
    else:
        print('y is greater than x')

#another example of nested condition

x = 9
if 0 < x:
    if x < 10:
        print('x is positive single digit number.')

x = 9
if 0 < x and x > 10:
    print('x is positive single digit number.')

#catching exception using "Try and Except"
inp1 = input('Enter Fahrenheit Temp: ')
fahr = float(inp1)
cel = (fahr - 32.0) * 5.0 /9.0
print(cel)

inp1 = input('Enter Fahrenheit Temp: ')
try:
    fahr = float(inp1)
    cel = (fahr - 32.0) * 5.0 /9.0
    print(cel)
except:
    print('please enter number')

#short-circuit evaluation of logical expressions
x = 4
y = 5
z = (x >= 2 and (x/y) > 2)
print(z)

x = 1
y = 0
z = ( x >= 2 and y !=0  and (x/y) > 2)
print(z)

x = 6
y = 0
z = ( x >= 2 and y !=0  and (x/y) > 2)
print(z)

#exercise 1: rewrite your pay computation
# to give the employee 1.5 time the hour rate for hours worked
# above 40 hours

hourly_rate = 50
worked_hours = 44
if worked_hours > 40:
    pay = ((hourly_rate * 40) + (hourly_rate * 1.5) * (worked_hours - 40))
    print(pay)
else:
    pay = hourly_rate * worked_hours
    print(pay)

hourly_rate = 10
worked_hours = 45
if worked_hours > 40:
    pay = ((hourly_rate * 40) + (hourly_rate * 1.5) * (worked_hours - 40))
    print(pay)
else:
    pay = hourly_rate * worked_hours
    print(pay)

#exercise 2: Rewrite your pay program using try and except
# so that your program can gandles non-numeric input
# gracefully by printing a message and exit the program.

rate1 = input('Enter a hour rate:')
hours1 = input('Enter number of hours worked in a week: ')
try:
    hrate = float(rate1)
    whours = float(hours1)
    pay = hrate * whours
    print(pay)
except:
    print('Error, please enter numeric input')

# Exercise 3: write a program to prompt for a score between 0.0 and
# 1.0. If the score is out of range , print an error message
# IF the score is between 0.0 and 1.0, print a grade usingt he following table:
# Score  grade
# >= 0.9  A
# >= 0.8  B
# >= 0.7  C
# >= 0.6  D
# < 0.6   F

score = input('Enter the score:')
try:
    if score >= 0.9 and score < 1.0:
        print("Grade is A")
    else:
        if score >= 0.8 and score < 0.9:
            print("Grade is B")
        else:
            if score >= 0.7 and score < 0.8:
                print("Grade is C")
            else:
                if score >=0.6 and score < 0.7:
                    print("Grade is D")
                else:
                    if score <  0.6 and score <=0.0:
                        print("Grade is F")
except:
    print('bad score')

####################################################
score = 0.0                                # Initialize variables
grade = ""

input1 = input('Enter score: ')
try:
    score = float(input1)                  # Only allows input floats
except ValueError:
    print('Bad score')
    quit()

if 0.0 <= score <= 1.0:                    # Scores must be between 0.0 and 1.0
    if score >= 0.9:
        grade = 'A'
    elif score >= 0.8:
        grade = 'B'
    elif score >= 0.7:
        grade = 'C'
    elif score >= 0.6:
        grade = 'D'
    else:
        grade = 'F'
else:
    grade = 'Bad score'

print(grade)

#################################################

score = float(input('Enter score:') )
try:
    if score >= 0.9 and score < 1.0:
        print("Grade is A")
    else:
        if score >= 0.8 and score < 0.9:
            print("Grade is B")
        else:
            if score >= 0.7 and score < 0.8:
                print("Grade is C")
            else:
                if score >=0.6 and score < 0.7:
                    print("Grade is D")
                else:
                    if score < 0.6 and score <=0.0:
                        print("Grade is F")
except:
    print('bad score')
