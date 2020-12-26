# ex input 14-15 d: dzjgbdwdkdhdddh

# spit in to sections

# min = 14
# max = 15
# char = d
# password = dzjgbdwdkdhdddh

# get lines to array
file = open('input1.txt', 'r')

Lines = file.read().splitlines()

numberOfLines = 0

for line in Lines:
    min = int(line.split(' ')[0].split('-')[0])
    max = int(line.split(' ')[0].split('-')[1])
    char = line.split(' ')[1].split(':')[0]
    password = line.split(' ')[2]

    count = 0

    for c in password:
        if (c == char):
            count = count + 1

    if count >= min and count <= max: 
        numberOfLines = numberOfLines + 1

print(numberOfLines)
