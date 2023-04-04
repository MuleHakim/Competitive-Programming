def xor():
    n = int(input())
    arr = list(map(int,input().split()))
    for i in range(len(arr)):
        res = 0
        for j in range(len(arr)):
            if i != j:
                res ^= arr[j]
        if res == arr[i]:
            return res
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        print(xor())