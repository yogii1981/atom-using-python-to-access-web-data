#updating variable

x = x + 1 # gets current value of x , add 1 and update value of x

# print(x) will give NameError : Name
# 'x' is not defined\
x = 0
x = x + 1 # updating a value by incrementing the value by 1
print(x)


x = 5
x = x - 1  # updating a value by decrementing the value by 1
print(x)

# The While statement

n = 5
while n > 0:
    print(n)
    n = n - 1
    print('Blastoff')
# example of finite loop and n = 5 is an iteration variable
    """
        while n is greater than zero, display the value n ,
        and reduce the value of n by 1 and when you get to 0 then exit abd display
        the word "blastoff"
    """

# example of infinite loop using break

while True:
    line = input(' > ')
    if line == 'done':
        break
        print(line)
    print('Done!')

# example of infinite loop using "continue" to skip to next iteration

while True:
    line = input('> ')
    if line[0] == '#':
        continue
    if line == 'done':
        break
    print(line)
print('Done!')

# definite loops using "for"

friends = ['john', 'kelly', 'sunny'] # variable "friends" is a list1 of 3 strings
for friend in friends:       # "friend" is an iteration variable
    print('Happy New Year:', friend)
print('Done')

# counting and sunning loops

count = 0
for intervar in [3, 41, 12, 9, 74, 15]:     # "intervar" is an iteration variable
    count = count + 1
    print('count:', count)


total = 0
for intervar in [3, 41, 12, 9, 74, 15]:
    total = total + intervar
    print('Total:', total)
"""
 in the bove loop I didn't use the iteration variable.
 Instead simple adding to the count as in the previous
 loop.
 """

 """
 Neither the counting nor the summing loop are useful
 as there is built in function "len" and "sum" to
 take care of such tasks.
 """

 """ Maximum and minimum loops """
largest = None
print("Before: ", largest)
for intervar in [ 3, 41, 12, 9, 75, 15]:
     if largest is None or intervar > largest:
         largest = intervar
     print('Loop:', intervar, largest)
print('Largest:', largest)

smallest = None
print("Before:", smallest)
for intervar in [3, 14, 12,9, 75,15]:
    if smallest is None or intervar < smallest:
        smallest = intervar
    print("Loop:", intervar, smallest)
print("Smallest:", smallest)

def min(values):
    smallest = None
    for value in values:
        if smallest is None or value < smallest:
            smallest = value
        return smallest

"""
Execrise 5.1 write a program which repeatedly read numbers
until the user enters "done". Once "done" is entered,
print out the total, count, and average numbers. if the
user enters anything other than number, detect their mistake
using try and except and print an error message and skip to
the next number.

Enter a number: 4
Enter a number: 5
Enter a number: bad data
Invalid input
Enter a number: 7
Enter a number: done
"""

Number = input(Enter a number: )
count = 0
total = 0
try:
    score = float(Number)
except ValueError:
    print('Invalid input')
    quit()

for a number in Number:
    count = count + 1
    total = total + 1
    average = number / count
    print("Total:", total , "Count:", count, "Average: ", average)



def check_for_float(input1):
    """
    Checks if the type of "input1" is a float and returns the value if so.
    Input:    input1 -- variable to check
    Output: val -- value of float
    """
    try:
        val = float(input1)                   # Only allows input floats
        return val
    except ValueError:
        print('Error, please enter numeric input')
        quit()

# Check module name since check_for_float is being imported in the next
# exercise. See also, https://www.youtube.com/watch?v=sugvnHA7ElY (video)
# or https://www.tutorialspoint.com/python/python_modules.htm (text)
if __name__ == "__main__":
    count = 0                                 # Initializes values
    total = 0.0
    average = 0.0

    while True:                               # Stays in loop until break
        input_number = input('Enter a number: ')
        if input_number == 'done':
            break                             # Exits the while loop

        number = check_for_float(input_number)

        count += 1                            # Counter
        total = total + number                # Running total

    # Ensures count is not 0 which would cause division error
    if count:
        average = total / count               # Computes the average
    print(total, count, average)
