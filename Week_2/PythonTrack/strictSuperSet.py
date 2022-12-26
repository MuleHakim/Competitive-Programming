# Enter your code here. Read input from STDIN. Print output to STDOUT
elementA = set(map(int,input().split()))
n = int(input())
while n > 0:
    otherSet = set(map(int,input().split()))
    if not elementA.difference(otherSet) or otherSet.difference(elementA):
        print(False)
        break
    n -= 1
else:
    print(True)   
