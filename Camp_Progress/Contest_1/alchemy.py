def alchemy(n):
    arr = list(map(int,input().split()))
    edw = 0
    edwCount = 0
    alp = 0
    alpCount = 0
    left = 0
    right = n-1
    while left <= right:
        if edw <= alp:
            edw += arr[left]
            edwCount += 1
            left += 1
        else:
            alp += arr[right]
            alpCount += 1
            right -= 1
    print(edwCount,alpCount)
if __name__ == '__main__':
    n = int(input())
    alchemy(n)