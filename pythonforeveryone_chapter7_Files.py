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
print(inp1[:50

""" write a file in small chunk to fit a memory"""

raft = open('sample1.txt')
count = 0
for line in raft:
    if line.startswith('The'):
        print(line)

raft = open('sample1.txt')
for line in raft:
    line = line.rstrip()
    # skip 'uninteresting lines'
    if not line.startswith('A'):
        continue
        #Process our 'interesting' lines
        print(line)

fname = input('Enter the file name:')
raft = open(fname)
count = 0
for line in raft:
    if line.startswith('t'):
        count = count + 1
    print('There was', count, 'subject lines in', fname)
