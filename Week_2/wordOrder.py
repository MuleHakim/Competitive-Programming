from collections import Counter
tmp = []
n = int(input())
for i in range(n):
    word = input()
    tmp.append(word)
counter = Counter(tmp)
print(len(counter))
for i in counter.values():
    print(i,end=" ")
