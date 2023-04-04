l,r = map(int, input().split())
xor = l ^ r
pos = 0
while xor:
    xor >>= 1
    pos += 1
print(2**pos - 1)