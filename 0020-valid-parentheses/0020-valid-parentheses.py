class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapped = {"{":"}","[":']',"(":")"}
        n = len(s)

        for i in range(n):
            if s[i] in mapped.keys():
                stack.append(s[i])
            
            else:
                if not stack:
                    return False
                top = stack.pop()

                if mapped[top] != s[i]:
                    return False
        return not stack