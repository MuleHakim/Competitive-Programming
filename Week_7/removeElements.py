def removeElements(t):
    for _ in range(t):
        n = int(input())
        arr = list(map(int,input().split(None,n)[:n]))
        arr.sort()
        for i in range(1,len(arr)):
            if arr[i] - arr[i -1] > 1:
                print("NO")
                break
        else:
            print("YES")

if __name__ == '__main__':
    testCase = int(input())
    removeElements(testCase)
