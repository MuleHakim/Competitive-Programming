def beautifulPaper(t):
    for _ in range(t):
        a, b = list(map(int,input().split()))
        c, d = list(map(int,input().split()))
        maxAB = max(a,b)
        minAB = min(a,b)
        maxCD = max(c,d)
        minCD = min(c,d)
        if maxAB == maxCD and minAB + minCD == maxAB:
            print("Yes")
        else:
            print("No")
if __name__ == '__main__':
    testCase = int(input())
    beautifulPaper(testCase)
