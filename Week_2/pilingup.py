# Enter your code here. Read input from STDIN. Print output to STDOUT
T = int(input())
for _ in range(T):
    n = int(input())
    block = list(map(int,input().split(None,n)[:n]))
    i = 1
    j = len(block)-2
    while i<=j:
        if block[i]>block[i-1] and block[j]>block[j+1]:
            print("No")
            break
        else:
            i += 1
            j -= 1
    else:
        print("Yes")
