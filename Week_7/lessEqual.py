def lessEqual():
    n, k = map(int,input().split())
    arr = list(map(int,input().split(None,n)[:n]))
    arr.sort()

    # k = 0
    if k == 0:
        if arr[0] == 1:
            return -1
        return arr[0] - 1
    # k = n
    if k == len(arr):
        return arr[-1]
    # k = 1 ... n - 1
    if arr[k - 1] == arr[k]:
        return -1
    return arr[k] - 1

    
if __name__ == '__main__':
    print(lessEqual())
