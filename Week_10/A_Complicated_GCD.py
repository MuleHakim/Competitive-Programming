def complicated():
    a,b = map(int,input().split())
    if a == b:
        return a
    return 1
print(complicated())