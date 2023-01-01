from collections import Counter
def planets(t):
    while t > 0:
        n, c = input().split()
        n = int(n)
        c = int(c)
        plantes = list(map(int,input().split(None,n)[:n]))
        counter = Counter(plantes)
        countValues = list(counter.values())
        res = 0
        for i in range(len(countValues)):
            res += min(c,countValues[i])
        print(res)
        t -= 1

if __name__=='__main__':
    testCase = int(input())
    planets(testCase)
