def merging():
    n,m = map(int,input().split())
    arr1 = list(map(int,input().split()))
    arr2 = list(map(int,input().split()))
    i = 0
    j = 0
    ans = ""
    while i < n and j < m:

        if arr1[i] <= arr2[j]:
            ans += str(arr1[i]) + " "
            i += 1
        else:
            ans += str(arr2[j]) + " "
            j += 1
    while i < n:
        ans += str(arr1[i]) + " "
        i += 1
    while j < m:
        ans += str(arr2[j]) + " "
        j += 1

    return ans.rstrip()
print(merging())
