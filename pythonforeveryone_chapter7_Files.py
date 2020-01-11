"""using secondary memory of the laptop"""

fhand = open('top50.csv')
print('fhand')

fhand

stuff = "Hello\nword!"
print(stuff)

fhand = open('top50.csv')
count = 0
for line in fhand:
    count = count + 1
print('Line Count:', count)

fhand = open('top50.csv')
inp = fhand.read()
print(len(imp))

raft = open('sample1.txt')
inp1 = raft.read()
print(len(inp1))
