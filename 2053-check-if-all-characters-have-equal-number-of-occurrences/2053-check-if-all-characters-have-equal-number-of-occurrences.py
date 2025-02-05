class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        s = Counter(s)
        reference = list(s.values())[0]
        for value in s.values():
            if value != reference:
                return False
        return True
