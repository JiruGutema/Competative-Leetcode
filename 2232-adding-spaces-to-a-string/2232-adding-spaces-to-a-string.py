class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        newStr = ''
        i = 0
        for j in range(len(s)):
            if i < len(spaces) and j == spaces[i]:
                newStr += f" {s[j]}"
                i += 1
            else:
                newStr += s[j]
        return newStr

