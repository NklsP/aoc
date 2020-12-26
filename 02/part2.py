# ex input 14-15 d: dzjgbdwdkdhdddh

# spit in to sections

# min = 14
# max = 15
# char = d
# password = dzjgbdwdkdhdddh

# get lines to array
file = open('input2.txt', 'r')

Lines = file.read().splitlines()

numberOfLines = 0

for line in Lines:
    first = int(line.split(' ')[0].split('-')[0])
    second = int(line.split(' ')[0].split('-')[1])
    char = line.split(' ')[1].split(':')[0]
    password = line.split(' ')[2]

    if password[first - 1] == char and password[second - 1] != char:
        numberOfLines = numberOfLines + 1

    if password[first - 1] != char and password[second - 1] == char:
        numberOfLines = numberOfLines + 1

print(numberOfLines)
