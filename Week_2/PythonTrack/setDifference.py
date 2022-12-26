# Enter your code here. Read input from STDIN. Print output to STDOUT
numOfEng = int(input())
EngNewsPaper = set(map(int,input().split(None,numOfEng)[:numOfEng]))
numOfFre = int(input())
FreNewsPaper = set(map(int,input().split(None,numOfFre)[:numOfFre]))
result = len(EngNewsPaper.difference(FreNewsPaper))
print(result)
