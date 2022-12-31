def Amazing(n):
    listNum = list(map(int,input().split(None,n)[:n]))
    max_score = listNum[0]
    min_score = listNum[0]
    result = 0
    for i in range(1,len(listNum)):
        if listNum[i] < min_score:
            min_score = listNum[i]
            result += 1
        if listNum[i] > max_score:
            max_score = listNum[i]
            result += 1
    return result
 
def main():
    n = int(input())
    answer = Amazing(n)
    print(answer)
main()
