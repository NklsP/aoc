# get lines to array
file = open('06/input1.txt', 'r')
Lines = file.read().splitlines()

lastElemCoutner = 1
newLines = []
entry = ""

yeses = 0

for line in Lines:
    if lastElemCoutner >= len(Lines):
        entry = entry + line
        entry = entry.replace(" ", "")
        newLines.append(set(entry))
        yeses = yeses + len(set(entry))      
        continue

    if line != "":
        entry = entry + " " + line
    else:        
        entry = entry.replace(" ", "")
        newLines.append(set(entry)) 
        yeses = yeses + len(set(entry))  
        entry = ""

    lastElemCoutner = lastElemCoutner + 1

print(yeses)