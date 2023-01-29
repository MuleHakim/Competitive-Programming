def oddPerson():
    n = int(input())
    arr = list(map(int,input().split(None,n)[:n]))
    for i in range(len(arr)-1):
        if (arr[i] + arr[i+1]) % 2 != 0:
            arr.sort()
            break
    print(*arr)

if __name__ == '__main__':
    oddPerson()
