class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
            '(': ')',
            '{': '}',
            '[': ']'
        }

        for i in s:
            if i in pairs:  # If it's an opening bracket
                stack.append(i)
            else:  # If it's a closing bracket
                if not stack or pairs[stack.pop()] != i:
                    return False

        return not stack  # True if stack is empty, False otherwise
