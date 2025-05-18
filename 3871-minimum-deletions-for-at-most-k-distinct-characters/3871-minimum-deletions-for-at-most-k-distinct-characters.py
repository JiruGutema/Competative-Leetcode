
class Solution:
    def minDeletion(self, s: str, k: int) -> int:
        count = Counter(s)
        frequencies = sorted(count.values(), reverse=True)

        delete = 0

        while len(frequencies) > k:
            delete += frequencies.pop()
        
        return delete
