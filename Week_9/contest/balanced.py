def balanced():
    n = int(input())
    arr = list(map(int,input().split()))
    arr.sort()
    ans = 0
    i = 0
    j = 0
    while j < n:
        if arr[j] - arr[i] <= 5:
            ans = max(ans,j-i+1)
            j += 1
        else:
            i += 1
    return ans
 
if __name__ == '__main__':
    print(balanced())
