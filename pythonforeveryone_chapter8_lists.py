"""Lists"""

a1 = ['spam', 2.0, 5,[10,20]]
len(a1) # show the length of the list
print(a1[1:3]) #show the elements at position 1, 2
print(a1[-1])   #show the last element of the list
print(a1[-1][-1]) #show the last element present within the last element of the list

cheeses = ['Cheddar','Edam','Gouda']
print(cheeses[-1])

"""Lists are mutable"""
cheeses = ['Cheddar','Edam','Gouda']
print(cheeses[0])

numbers = [17,123]
numbers[1] = 5
print(numbers)

cheeses = ['Cheddar','Edam','Gouda']
print('Edam' in cheeses)
print('Adam' in cheeses)


"""
This loop transverses the list and
updates each element. 'len' returns  the number
of elements in the list. range returns a list of indices
from 0 to n-1,where "n" in the length of list
"""

numbers = [17,21,223,34111,2,121]
for number in range(len(numbers)):
    numbers[number] = numbers[number] * 2
print(numbers)

empty = []
for x in empty:
    print('This never happens')

"""List operations"""
a = [1,2,3]
b = [4,5,6]
c = a + b
print(c)

a =[0] * 4 # operator repeat a list a given number of times
print(a)

b = [1,2,3] * 3
print(b)


""" Slice operators also works on list """
t = ['a','b','c','d']
print(t[0:2])

print(t[:])


t = ['a','b','c','d','e','f','g']
t.append('gg') # appending the list t with "gg" value adding extra element
print(t)

t1 = ['a','b','c']
t2 = ['d','e','f']
t1.extend(t2) # extend takes a list as an arguement and append of the elements
print(t1)
""" only t1 is updated not t2 """

""" Sort operations """
t = ['d','s', 'a', 'b', 'c','i']
print(t.sort()) # list is modified but print(t.sort() will be none)
print(t)

"""deleting elements"""
t = ['a','b','c','d']
x = t.pop(2)
print(t)

""" if user don't want to the remove value but know the index"""
t = ['a', 'b', 'c']
del t[1]
print(t)

""" if user knows the value to be remove then use remove function"""
t = ['a','b','c']
t.remove('b')
print(t)


""" Lists and Functions"""
nums = [3, 41, 12, 9, 74, 15]
print(len(nums))
print(max(nums))
print(min(nums))
print(sum(nums))
print(sum(nums)/len(nums))

"""Write a program to compute
an average without a list:"""

total = 0
count = 0
while(True):
    inp = input('Enter a number:')
    if inp == 'done': break
    value = float(inp)
    total = total + value
    count = count + 1
    average = total / count
print('Average:', average)

"""Use built-in functions to compute sum and count"""
numlist = list()
while(True):
    inp = input('Enter a number:')
    if input == 'done': break
    value = float(inp)
    numlist.append(value)
average =sum(numlist) / len(numlist)
print('Average:', average)

"""Lists and Strings"""
s = 'spam'
t = list(s) # to covert from string to list of characters
print(t)


# to convert a string into a word
s = 'pining for the fjords'
t = s.split()
print(t)

# once you have used the split function,
# you can use the delimiter to use a
# particular word as a boundary

s = 'spam-spam-spam'
delimiter = "-"
print(s.split(delimiter))

# Join the inverse of the split

t = ['I', 'am', 'a', 'boy']
delimiter = ' '
delimiter.join(t)
print(delimiter.join(t))

"""Parsing lines"""
"""
we can use a split a function to look for a line where
line starts from "the" and then print out the third word
in the line"""
fhand = open('sample1.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('The'):continue
    words = line.split()
    print(words[2])

x = " this is a champion of the east"
print(x.strip())

""" Objects and values"""
a = 'banana'
b = 'banana' # banana is object and system only created one object
print(a is b)


# system creates two list even though look similar and they are different even
# though they look similar
a = [1,2,3]
b = [1,2,3]
print(a is b)

""" IMPORTANT NOTE: a and b are equivalent because
they have idential elements but no same elements"""

a = [1,2,3]
b = [1,2,3]
print( a == b)

""" How to assign same elemenets to different variable - ALIASING"""
a = [1, 2, 3]
b = a
print(b)

b[0] = 17
print(b)
print(a)
"""This is error prone since chaning the element of b also changed
the element of a"""

""" List Arguments"""

def delete_head(t):
    del t[0]
#defining the function
# delete_head which removes the first elements

letters = ['a', 'b', 'c']
delete_head(letters)
print(letters)

t1 = [1,2]
t2 = t1.append(3)
print(t1)
print(t2)



def bad_delete_head(t):
    t=t[1:] #this function doesn't delete the head of a list

def tail(t):
    return t[1:] # function returns all but first element

letters = ['a', 'c','f','g','t']
rest = tail(letters)
print(rest)

"""
Write a function "chop" that
takes a list and modifies it,
removing the first and last elemenets
and returns "None"

Then write a "middle" function that takes a list and returns a new
list that contains all but first and last elements
"""

def chop(list):
    """ Take a list"""
    del list[0] #delete first element from list
    del list[-1]    #delete last element from List

def middle(list):
    new = list[1:]
    del new[-1]
    return new


letters = ['a', 'c','f','g','t']
rest = chop(letters)
print(letters)
print(rest)

test = middle(letters)
print(test)
