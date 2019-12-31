""" String is a sequence of characters"""
fruit = 'banana'
letter = fruit[1]
print(fruit[1])

letter = fruit[0]
print(fruit[0])
print(letter)


fruit = 'banana'
len(fruit)
print(len(fruit))

last = fruit[length] # this will throw an error as index 6 is npt present in banana

last= fruit[length - 1]
print(last)

last1 = fruit[-2]

"""
Transveral through  a string with a loop
"""

index = 0
while index < len(fruit):
    letter = fruit[index]
    print(letter)
    index = index + 1
