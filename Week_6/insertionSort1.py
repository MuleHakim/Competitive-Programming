#!/bin/python3

import math
import os
import random
import re
import sys

def insertionSort1(n, arr):
    target = arr[-1]
    index = n - 2

    while (target < arr[index]) and (index >= 0):
        arr[index + 1] = arr[index]
        print(*arr)
        index -= 1

    arr[index+1] = target
    print(*arr)

def main():
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
main()

