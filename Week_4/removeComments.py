class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
            
        newSource = []
        commenting = False
        modified = ''

        for line in source:
            idx = 0
            while idx < len(line):
                if idx + 1 == len(line):
                    if not commenting:
                        modified += line[idx]
                    idx += 1
                    break
                twoChars = line[idx:idx + 2]
                if twoChars == '/*' and not commenting:
                    commenting = True
                    idx += 2
                elif twoChars == '*/' and commenting:
                    commenting = False
                    idx += 2
                elif twoChars == '//':
                    if not commenting:
                        break
                    else:
                        idx += 2
                else:
                    if not commenting:
                        modified += line[idx]
                    idx += 1

            if modified and not commenting:
                newSource.append(modified)
                modified = ''

        return newSource
