import math

# get lines to array
file = open('input1.txt', 'r')
Lines = file.read().splitlines()

print(len(Lines))

# Create correct string lenghts
minNumCharPerLine = len(Lines) * 3

multiplier = math.ceil(minNumCharPerLine / len(Lines[0]))
print(multiplier)

newLines = []
for line in Lines:
    x = 0
    newLine = ""
    while x < multiplier:
        newLine = newLine + line
        x = x + 1

    newLines.append(newLine)

# print(newLines)

counter = 0
treeCounter = 0

for line in newLines:
    if counter <= len(line):
        if line[counter] == str("#"):
            print(counter, line)
            treeCounter = treeCounter + 1
        
        counter = counter + 3

print(treeCounter)

