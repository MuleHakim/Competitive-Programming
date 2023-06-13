class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        def getRep(node):
            if arr[node] != node:
                arr[node] = getRep(arr[node])

            return arr[node]

        def union(x,y):
            rep_x = getRep(x)
            rep_y = getRep(y)
            if rep_x != rep_y:
                arr[rep_y] = rep_x


        n = len(s)
        arr = [i for i in range(n)]
        for i, j in pairs:
            union(i,j)

        my_dict = defaultdict(list)
        for idx, val in enumerate(arr):
            my_dict[getRep(val)].append(idx)

        new_s = list(s)
        for key in my_dict.keys():
            index_list = my_dict[key]
            char_list = [s[i] for i in index_list]
            char_list.sort()


            for idx, char in zip(index_list,char_list):
                new_s[idx] = char

        return "".join(new_s)