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
