# aoc day 01

# get lines to array
file = open('input1.txt', 'r')
Lines = file.read().splitlines()

for line1 in Lines:
    for line2 in Lines:
        for line3 in Lines:
            sum = int(line1) + int(line2) + int(line3)
            
            if sum == 2020:
                print(int(line1) * int(line2) * int(line3))
                exit()