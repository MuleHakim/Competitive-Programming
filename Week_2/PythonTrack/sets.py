# Enter your code here. Read input from STDIN. Print output to STDOUT
n,m = input().split()
arr = list(map(int, input().split()))
A = set(map(int, input().split()))
B = set(map(int, input().split()))
hap = 0
for i in arr:
    if i in A: hap += 1
    elif i in B: hap -= 1
print(hap)
