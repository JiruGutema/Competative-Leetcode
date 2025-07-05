class Solution:
    def findLucky(self, arr: List[int]) -> int:
        count = Counter(arr)
        lucky = -1
        for v, k in count.items():
            if v == k:
                if lucky < v:
                    lucky =  v

        return lucky
