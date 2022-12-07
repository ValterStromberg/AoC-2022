import numpy as np

def to_array_from_file(path):
    Data = np.genfromtxt(path, dtype=str, encoding=None, delimiter=",")
    return Data
dataPath = r'C:\code\AoC_22\AoC-2022\Day_4\input.txt'

array = to_array_from_file(dataPath)


score=0
for i in array:
    temp  = list(i[0])
    a = temp.index('-')
    temp2 = list(i[1])
    b = temp2.index('-')
    set1 = set(range(int("".join(temp[0:a])) , int("".join(temp[(a+1):len(temp)]))+1)) 
    set2 = set(range(int("".join(temp2[0:b])) , int("".join(temp2[(b+1):len(temp2)]))+1))
    if set1.issubset(set2) or set2.issubset(set1):
        score +=1

print (score)

###### part2 ######
score = 0
for i in array:
    temp  = list(i[0])
    a = temp.index('-')
    temp2 = list(i[1])
    b = temp2.index('-')
    incommon =  set(range(int("".join(temp[0:a])) , int("".join(temp[(a+1):len(temp)]))+1)) &  set(range(int("".join(temp2[0:b])) , int("".join(temp2[(b+1):len(temp2)]))+1))
    if incommon == set():
        print('HELLO')
        score += 1
print(len(array) - score)
