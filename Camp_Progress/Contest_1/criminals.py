def criminals(t):
    n = int(input())
    arr = list(map(int,input().split()))
    count = 0
    for i in range(n-1):
        if arr[i] != 0:
            count += arr[i+1:-1].count(0)
            break
    ans = count + sum(arr[:-1])
    return ans
if __name__ == '__main__':
    testCase = int(input())
    for _ in range(testCase):
        print(criminals(testCase))