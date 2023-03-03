def team():
    a,b = map(int,input().split())
    min_val = min(a,b)
    temp = (a + b) // 4
    return min(min_val,temp)
 
 
if __name__ == '__main__':
    testCase = int(input())
    for _ in range(testCase):
        print(team())