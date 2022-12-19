def swap_case(s):
    res = ""
    for i in range(len(s)):
        if s[i].isalpha() and 65<=ord(s[i])<=90:
            res += s[i].lower()
        elif s[i].isalpha() and 97<=ord(s[i])<=122:
            res += s[i].upper()
        else:
            res += s[i]
    return res
if __name__ == '__main__':
