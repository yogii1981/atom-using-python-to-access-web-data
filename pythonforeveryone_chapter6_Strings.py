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

"""
this loop transverses the string and displays each letter
on a line by itself. The loop is condition is
index \< len (fruit), so when index is equal to length of the
string , the condition is false
"""


"""
Execrise 6.1 : write a while loop that starts at the last character
in the string and works its ways backward to first character in th string, printing
each letter on a separate line , except backwards.
"""

fruit = 'banana'
index = len(fruit)-1                    # Convert to index
while index >= 0:
    letter = fruit[index]
    print(letter)
    index -= 1                          # Update index



##########################################################
fruit = 'banana'
for char in fruit:
    print(char)


""" String Slices """
s = "Monthy python"
print (s[0:3])
print(s[:9]) ### from beggining till 8th character
print(s[3:]) ### from 3rd till the end


""" Exercise 2: Given that fruit is a string, What
does fruit[:] mean ?
"""

fruit = 'banana'
print(fruit[:])


######## Another way of transveral loop using for loop ###
fruit = 'banana'
for char in fruit:
    print(char)

"""
String Slices
"""

s = 'Monty Python'
print(s[0:4])


#######################################

greeting = 'Hello , test'
greeting[0] = 'J'   # Strings are immutable

greeting = 'Hello , test'
new_greeting = "j" + greeting[1:]
print(new_greeting)
