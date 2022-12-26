# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
t = tuple(map(int,input().split(None,n)[:n]))
print(t)
print(hash(t))
