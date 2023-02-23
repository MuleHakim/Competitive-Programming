def serejaDima():
    n = int(input())
    arr = list(map(int,input().split(None,n)[:n]))
    i = 0
    j = len(arr) - 1
    turn = 0
    ans = [0]*2
    
    while i <= j:
        cur_max = 0
        if arr[i] > arr[j]:
            cur_max = arr[i]
            i += 1
        else:
            cur_max = arr[j]
            j -= 1
        if turn % 2 == 0:
            ans[0] += cur_max
        else:
            ans[1] += cur_max
        turn += 1
    
    print(*ans)
 
if __name__ == '__main__':
    serejaDima()
