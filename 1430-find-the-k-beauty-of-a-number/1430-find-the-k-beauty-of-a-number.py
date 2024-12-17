class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        nums = str(num)
        ans = 0
        i = 0
        j = k

        while j < len(nums)+1:
            if int(nums[i:j]) != 0 and num%(int(nums[i:j])) == 0:
                ans += 1
            i += 1
            j += 1
        return ans