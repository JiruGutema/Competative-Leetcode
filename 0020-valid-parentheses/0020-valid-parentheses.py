class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
            '(': ')','{': '}','[': ']'}

        for i in s:
            if i in pairs:
                stack.append(i)
            else: 
                if not stack or pairs[stack.pop()] != i:
                    return False

        return not stack