
class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed) % 2 != 0:
            return []  
        count = defaultdict(int)
        for num in changed:
            count[num] += 1

        original = []
        for num in sorted(changed):
            if count[num] == 0:
                continue
            if count[2 * num] == 0:
                return []
            original.append(num)
            count[num] -= 1
            count[2 * num] -= 1

        return original