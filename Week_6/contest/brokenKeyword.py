def brokenKeyword(t):
    for _ in range(t):
        string = input()
        if len(string) == 1:
            print(string)
            continue
        ans = set()
        i = 0
        while i < len(string):
            j = i + 1
            count = 1
            while j < len(string) and string[j] == string[j-1]:
                count += 1
                j += 1
                i += 1
            if count % 2 == 1 and string[i] not in ans:
                ans.add(string[i])
            i += 1
 
        print("".join(sorted(list(ans))))
 
if __name__ == '__main__':
    testCase = int(input())
    brokenKeyword(testCase)
