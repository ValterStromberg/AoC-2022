import numpy as np

def to_array_from_file(path):
    Data = np.genfromtxt(path, dtype=str, encoding=None, delimiter=" ")
    return Data
dataPath = r'C:\code\Advent-of-Code_22\Day_2\input.txt'

array = to_array_from_file(dataPath)
print(array)
# X & A = rock
# Y & B = paper
# Z & C = scissors
win = 6
draw = 3
x = 1
y = 2
z = 3 
score = 0
for i in array:
    if i[1] == 'X':
        score +=1
        if i[0] == 'A':
            score += draw
        if i[0] == 'C':
            score += win
    if i[1] == 'Y':
        score +=2
        if i[0] == 'B':
            score += draw
        if i[0] == 'A':
            score += win
    if i[1] == 'Z':
        score +=3
        if i[0] == 'C':
            score += draw
        if i[0] == 'B':
            score += win
print(score)

## part 2
# X & A = rock
# Y & B = paper
# Z & C = scissors
score = 0
for i in array:
    if i[1] == 'X':
        if i[0] == 'A':
            score += z
        if i[0] == 'B':
            score += x
        if i[0] == 'C':
            score += y
    if i[1] == 'Y':
        score +=3
        if i[0] == 'A':
            score += x
        if i[0] == 'B':
            score += y
        if i[0] == 'C':
            score += z
    if i[1] == 'Z':
        score +=6
        if i[0] == 'A':
            score += y
        if i[0] == 'B':
            score += z
        if i[0] == 'C':
            score += x
print(score)