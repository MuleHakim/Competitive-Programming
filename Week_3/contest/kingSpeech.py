def king(n):
    while n > 0:
        word = input()
        listW = word[:2] + "... "  + word + "?" 
        print("".join(listW))
        n -= 1
def main():
    n = int(input())
    king(n)
main()
