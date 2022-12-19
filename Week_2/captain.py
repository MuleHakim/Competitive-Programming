from collections import Counter
k = int(input())
room = list(map(int, input().split()))
counter = Counter(room)
print(list(counter.keys())[-1])
