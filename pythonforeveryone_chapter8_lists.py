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

numbers = [17,21,223,34111,2,121]
for number in range(len(numbers)):
    numbers[number] = numbers[number] * 2
print(numbers)
