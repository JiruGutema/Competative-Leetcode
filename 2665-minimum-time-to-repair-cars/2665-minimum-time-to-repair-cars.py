class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        def helper(t):
            count = 0
            for rank in ranks:
                count += int(sqrt(t/rank))
            return count

        l, r = 1, ranks[0]*(cars**2)
        res = -1
        while l <= r:
            mid = (l+r)//2
            if helper(mid) >= cars:
                res = mid
                r = mid -1
            else:
                l = mid + 1
        return res

