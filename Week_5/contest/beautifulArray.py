def beautifulArray():
    
    n = int(input())
    a = list(map(int,input().split(None,n)[:n]))
    pos = []
    neg = []
    zero = []
    for i in a:
        if i > 0: pos.append(i)
        elif i < 0: neg.append(i)
        else: zero.append(i)
    if len(pos) == 0:
        for _ in range(2):
            pos.append(neg.pop())
    if len(neg) % 2 == 0:
        zero.append(neg.pop())
    

    negResult = str(len(neg)) + " "
    for i in neg:
        negResult += str(i) + " "
    print(negResult.rstrip())
    posResult = str(len(pos)) + " "
    for i in pos:
        posResult += str(i) + " "
    print(posResult.rstrip())
    zeroesResult = str(len(zero)) + " "
    for i in zero:
        zeroesResult += str(i) + " "
    print(zeroesResult.rstrip())

if __name__ == '__main__':
    beautifulArray()
