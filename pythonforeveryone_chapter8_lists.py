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
