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
