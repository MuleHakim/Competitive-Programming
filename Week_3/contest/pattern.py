def Pattern(n):
    listOfString = []
    while n > 0:
        string = input()
        listOfString.append(string)
        n -= 1

    ans = ""
    for i in range(len(listOfString[0])):
        tmp = ""
        for j in range(len(listOfString)):
            tmp += listOfString[j][i]
        tmp = set(tmp)
        if len(tmp) > 2 or (len(tmp) == 2 and "?" not in tmp) :
            ans += "?"
        elif len(tmp) == 2:
            letter = list(tmp.difference({"?"}))[0]
            ans += letter
        elif len(tmp) == 1:
            tmp = list(tmp)
            if "?" in tmp:
                ans += "m"
            else:
                ans += tmp[0]

    return ans
if __name__ == '__main__':
    n = int(input())
    answer = Pattern(n)
    print(answer)
