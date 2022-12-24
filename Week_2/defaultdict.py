# Enter your code here. Read input from STDIN. Print output to STDOUT
lst = list(map(int,input().split()))
from collections import defaultdict
charDict = defaultdict(list)
for pointer in range(1,lst[0]+1):
    groupA = input()
    charDict[groupA].append(str(pointer))
for pointer in range(lst[1]):
    groupB = input()
    if groupB not in charDict.keys():
        print("-1")
    else:
        print(" ".join(charDict[groupB]))
