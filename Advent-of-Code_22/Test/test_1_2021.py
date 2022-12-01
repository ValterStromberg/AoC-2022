import numpy as np

def to_pointcloud_from_file(path):
    Data = np.genfromtxt(path, dtype=float, encoding=None, delimiter=",")
    return Data
dataPath = r'C:\code\Advent-of-Code\Test\data.txt'

array = to_pointcloud_from_file(dataPath)
prevValue = array[0]
tot = 0
for i in array:
    if i > prevValue:
        tot +=1
    prevValue = i
print(tot)

#-------------- part2 -------------------

curr = 0
tot2 = 0
prevValue = array[0] + array[1] + array[2]
for i in range(len(array)-3):
    curr = array[i+1] + array[i+2] + array[i+3]
    if curr > prevValue:
        tot2 +=1
    prevValue = curr
print(tot2)


