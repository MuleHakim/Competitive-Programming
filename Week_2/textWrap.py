import textwrap
import math
def wrap(string, max_width):
    cur = 0
    length = len(string)
    numOfiteration = math.ceil(length/max_width)
    result = ""
    for pointer in range(1,numOfiteration):
        if pointer == numOfiteration - 1:
            result += string[cur:cur + max_width] + "\n" + string[cur + max_width:]
        else:
            result += string[cur:cur + max_width] + "\n"
        cur = pointer * max_width
        
    return result

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
