class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []

        path = path.split("/")

        for i in path:
            if i == ".." and stack:
                stack.pop()
            elif i != "..":
                if i != "" and i != ".":
                    stack.append(i)

        return "/"+"/".join([dir for dir in stack ])