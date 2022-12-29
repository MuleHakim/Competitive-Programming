class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:

        pathDict = defaultdict(int)
        output = []
        delimiter = " "
        lengthOfPaths = len(paths)

        for pointer1 in range(lengthOfPaths):
            splitted_list = paths[pointer1].split()
            lengthOfSplittedList = len(splitted_list)
            
            for pointer2 in range(1,lengthOfSplittedList):
                root = splitted_list[0] + "/"
                idx = splitted_list[pointer2].index("(")

                if splitted_list[pointer2][idx + 1:-1] in pathDict.keys():
                    pathDict[splitted_list[pointer2][idx + 1:-1]] +=  delimiter + root + splitted_list[pointer2][:idx]
                else:
                    pathDict[splitted_list[pointer2][idx + 1:-1]] = root + splitted_list[pointer2][:idx]

        for path in pathDict.values():
            if delimiter in path:
                output.append(path.split(delimiter))

        return output
