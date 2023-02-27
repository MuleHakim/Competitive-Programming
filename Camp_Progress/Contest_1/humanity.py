def humanity(t):
    for _ in range(t):
        n, m = map(int,input().split())
        string = list(input())
        left = 0
        right = 0
        for right in range(n):
            if string[right] == "1" and string[left] == "1":
                index1 = left + 1
                index2 = right - 1
                temp = m
                while index1 < index2 and temp > 0:
                    string[index1] = "1"
                    string[index2] = "1"
                    index1 += 1
                    index2 -= 1
                    temp -= 1
                left = right
            elif string[right] == "1" and string[left] == "0":
                index2 = right - 1
                temp = m
                while index2 >= 0 and temp > 0:
                    string[index2] = "1"
                    index2 -= 1
                    temp -= 1
                left = right
        if string[left] == "1":
            index1 = left + 1
            temp = m
            while index1 < n and temp > 0:
                string[index1] = "1"
                index1 += 1
                temp -= 1
            
        print("".join(string))
                

if __name__ == '__main__':
    testCase = int(input())
    humanity(testCase)