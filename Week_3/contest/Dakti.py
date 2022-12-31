def Dakti(n):
    while n > 0:
        dict_ = {}
        st = list(input().split())
        for i in st:
            for j in i:
                if j.isdigit():
                    i = i.replace(j, "")
                    dict_[i] = int(j)
        dict_ = dict(sorted(dict_.items(), key=lambda item: item[1]))
        print(" ".join(dict_.keys()))
        
        n -= 1
def main():
    n = int(input())
    Dakti(n)
main()
