class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        idx_value = set()
        i = 0
        max_lenght = 0

        for j in range(len(s)):
            while s[j] in idx_value:
                idx_value.remove(s[i])
                i += 1
           
            idx_value.add(s[j])
            max_lenght = max(max_lenght, j-i+1)
            
        return max_lenght
            
            
