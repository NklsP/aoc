import math

# get lines to array
file = open('05/input1.txt', 'r')
Lines = file.read().splitlines()

# Lines = ["BFFFBBFRRR", "FFFBBBFRRR", "BBFFBBFRLL"]

seatIds = []

for line in Lines:
    high = 127
    low = 0
    left = 0
    right = 7
    for c in line:
        if c == "F":            
            low = low
            high = low + math.floor((high - low) / 2)
        elif c == "B":
            high = high
            low = low + math.ceil((high - low) / 2)
        elif c == "L":
            left = left
            right = left + math.floor((right - left) / 2)
        elif c == "R":
            left = left + math.ceil((right - left) / 2)
            right = right

    seatId = low * 8 + left  
    seatIds.append(seatId)   

print(max(seatIds))
