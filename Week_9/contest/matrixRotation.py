def matrixRotation(t):
    for _ in range(t):
        a,b = map(int,input().split())
        c,d = map(int,input().split())
        for _ in range(4):
            if a < b and a < c and c < d and b < d:
                print("YES")
                break
            else:
                tmp = a
                a = c
                c = d
                d = b
                b = tmp
        else:
            print("NO")
 
if __name__ == '__main__':
    testCase = int(input())
    matrixRotation(testCase)
