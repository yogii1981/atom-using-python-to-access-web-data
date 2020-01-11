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

""" Looping and counting"""
word = 'banana'
count = 0
for letter in word:
    if letter == 'a':
        count = count + 1
print(count)


"""
Exercise 3:  this code in a function named count, and generalize
it so that it accepts the string and letter as arguments
"""

'a' in 'banana'

"""String comparison"""
word = 'banana'
if word == 'banana':
    print('your word,' + word + ', 'comes before banana.')
elif word > 'banana':
    print('your word,' + word + ', come after banana')
else:
    print('All right, bananas.')

""" String methods """
stuff = "hello world"
type(stuff)

dir(stuff)


word = 'banana'
word.upper()
new_word = word.upper()
print(new_word)



word = 'banana'
index = word.find('a')
print(index)


word = 'banana'
index1 = word.find('na')
print(index1)

word = 'banana'
index2 = word.find('na', 3)
print(index2)

line = '   here we go '
line.strip()  # remove space, tabs or newsline
print(line)


""" You will see "startswith" requires case to match """

line = "Have a good day"
line.startswith('h')
print(line.startswith('h'))


line = "Have a good day"
line.lower()
print(line.lower().startswith('h'))  #lower case "h" startswith "have a good day"


"""
Exercise 4: There is a string method called count.
Use it to write an invocation that counts the number of
times the letter "a" occues in "banana".
"""

word = "banana"
substring = "a"   #define a substring prior to search
print(word.count(substring,0,6))  # substring, starting point for search , end point of search


""" Parsing Strings"""

data = 'From stephen.marquand@uct.ac.za Sat Jan 9 09:45:14 2019'
atpos = data.find('@')   #find the location of @ sign
print (atpos)

sppos = data.find( ' ', atpos)   # find the location of fisr space after @sign
print(sppos)

host = data[atpos+1:sppos]    #display from the fist text after @ till the space sign appearance
print(host)



""" Format operator"""
#Format operator, % allows us to construct
# strings, replacing part of tstrings with data stored
# in variables
# % act as modulus when appolied to integer and act as
# format when applied to Strings


camels = 42
'%d' % camels
print(camels)
print(type(camels))


camels = 42
test = 'I have spotted %d camels.' %camels  # replace the %d with value of camels
print(test)

""" %d is used to format integer and %g is used to format a floating point number """

sentence = 'In %d years, I have spotted %g %s.' % (3, 0.1,'camels')
print(sentence)

a = ' %d %d %d % (1,2)'
print(a)
