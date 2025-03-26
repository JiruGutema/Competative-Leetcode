# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 0
        right = n-1

        while left <= right:
            mid = (left + right) // 2
            if isBadVersion(mid) and isBadVersion(right):
                right = mid - 1
            elif not isBadVersion(mid) and not isBadVersion(left):
                left = mid + 1
        return left
