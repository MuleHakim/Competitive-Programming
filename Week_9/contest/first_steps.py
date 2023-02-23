def firstStep():
    n = int(input())
    arr = list(map(int,input().split()))
    ans = 1
    cur_idx = 0
    for i in range(1,n):
        if arr[i] >= arr[i-1]:
            ans = max(ans, i-cur_idx+1)
        else:
            cur_idx = i
    return ans
 
if __name__ == '__main__':
    print(firstStep())
