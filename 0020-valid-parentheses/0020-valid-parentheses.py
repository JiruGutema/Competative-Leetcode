class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        brackets = {
            '(': ')',
            '[': ']',
            '{': '}'
        }

        for char in s:
            if char in brackets:
                stack.append(char)
            else:
                if not stack:
                    return False
                top = stack.pop()
                if brackets[top] != char:
                    return False

        return len(stack) == 0