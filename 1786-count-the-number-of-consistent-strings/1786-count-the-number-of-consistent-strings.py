class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed = Counter(allowed)
        ans = 0
        for word in words:
            consistent = True
            for char in word:
                if char not in allowed:
                    consistent = False
                    break
            if consistent:
                ans += 1
        return ans


            