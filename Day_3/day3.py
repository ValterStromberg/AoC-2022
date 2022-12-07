import numpy as np 

def to_array_from_file(path):
    Data = np.genfromtxt(path, dtype=str, encoding=None, delimiter="")
    return Data
dataPath = r'C:\code\Advent-of-Code_22\Day_3\input.txt'

array = to_array_from_file(dataPath)

score = 0
for i in (array):
    temp = list(i)
    length = len(i)
    middle_index = length // 2
    temp2 = set(temp[:middle_index]) & set(temp[middle_index:])
    temp2 = temp2.pop()
    if temp2.islower(): score += abs(ord(temp2) -96) 
    else:               score += abs(ord(temp2) -38)
print (score)


####### part 2 #######

score = 0
newarray = np.reshape(array,(np.size(array)//3,3))
for i in newarray:
    print(list(i[0]))
    temp2 = set(list(i[0])) & set( list(i[1])) & set( list(i[2]))
    temp2 = temp2.pop()
    if temp2.islower(): score += abs(ord(temp2) -96) 
    else:               score += abs(ord(temp2) -38)
print (score)    
