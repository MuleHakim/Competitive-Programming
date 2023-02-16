def smaller():
    n, m = map(int,input().split())
    arr1 = list(map(int,input().split()))
    arr2 = list(map(int,input().split()))

    pointer1 = 0
    pointer2 = 0
    ans = []
    
    while pointer1 < n and pointer2 < m:
        if arr2[pointer2] > arr1[pointer1]:
            pointer1 += 1
        else:
            ans.append(pointer1)
            pointer2 += 1

    while pointer2 < m:
        ans.append(pointer1)
        pointer2 += 1
        
    print(*ans)

if __name__ == '__main__':
    smaller()
