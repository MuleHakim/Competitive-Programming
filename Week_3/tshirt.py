def tshirt(t):
    while t > 0:
        a_size, b_size = input().split()

        if a_size == b_size:
            print("=")
        else:
            a_size = a_size[::-1]
            b_size = b_size[::-1]

            if a_size[0] == b_size[0]:
                if a_size.count("X") > b_size.count("X") and a_size[0] == "S":
                    print("<")
                elif a_size.count("X") < b_size.count("X") and a_size[0] == "S":
                    print(">")
                elif a_size.count("X") > b_size.count("X") and a_size[0] == "L":
                    print(">")
                elif a_size.count("X") < b_size.count("X") and a_size[0] == "L":
                    print("<")
            elif a_size[0] != b_size[0]:
                if ord(a_size[0]) > ord(b_size[0]):
                    print("<")
                else:
                    print(">")
        t -= 1

if __name__ == '__main__':
    testCase = int(input())
    tshirt(testCase)
    
