import numpy as np
import sys

np.set_printoptions(threshold=sys.maxsize)

dataPath = r'C:\code\Advent-of-Code\day_1\input.txt'

newlist=[]
with open(dataPath) as f:
    lines = f.readlines()

for i in range(len(lines)):
    newlist.append(lines[i].rstrip('\n'))
newlist = np.array(newlist)

for i in range(len(newlist)):
    if newlist[i] == "":
        newlist[i] = 0

newlist = newlist.astype(float)

tempval=0
winner = 0
for i in range(len(newlist)):
    tempval = tempval + newlist[i]
    if newlist[i] == 0:
        if tempval > winner:
            winner = tempval
        tempval = 0
print (winner)

#######part 2##############

tempval=0
winners = [0,0,0]
counter = 1
for i in range(len(newlist)):
    tempval = tempval + newlist[i]
    if newlist[i] == 0:
        if tempval > np.amin(winners):
            winners[np.argmin(winners)] = tempval
        tempval = 0
print(winners)
print (np.sum(winners))