class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        path = path.split("/")

        for component in path:
            if component == "" or component == ".":
                continue
            elif component == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(component)

        canonical_path = "/" + "/".join(stack)

        return canonical_path