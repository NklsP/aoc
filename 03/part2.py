import math

# get lines to array
file = open('input1.txt', 'r')
Lines = file.read().splitlines()

print(len(Lines))

# Create correct string lenghts
right = [1,3,5,7,1]
down = [1,1,1,1,2]

print("Max value =", max(right))
minNumCharPerLine = len(Lines) * max(right)

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

counter = 0
treeCounter = 0

results = []

for slope in range(len(right)):
    for index in range(len(newLines)):
        if index % down[slope] == 0:
            if counter < len(newLines[index]):
                if newLines[index][counter] == str("#"):
                    treeCounter = treeCounter + 1
                
            counter = counter + right[slope]

    results.append(treeCounter)
    counter = 0
    treeCounter = 0

value = 1

for r in results:
    value = value * r


print(value)