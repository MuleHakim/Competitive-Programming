from collections import defaultdict
def replacement(testCase):
    while testCase > 0:

        n = int(input())
        listOfNumbers = list(map(int,input().split(None,n)[:n]))
        string = input()
        defDict = defaultdict(int)

        for i in range(len(listOfNumbers)):
            if listOfNumbers[i] in defDict:
                continue
            else:
                defDict[listOfNumbers[i]] = string[i]
        result = ""

        for j in listOfNumbers:
            result += defDict[j]
        
        if result == string:
            print("YES")
        else:
            print("NO")

        testCase -= 1

def main():
    t = int(input())
    replacement(t)
main()

