class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        dec = collections.deque() 
        inc = collections.deque() 
        ans = 0
        left = 0

        for right, num in enumerate(nums):
            while dec and num > dec[-1]:
                dec.pop()

            dec.append(num)

            while inc and num < inc[-1]:
                inc.pop()

            inc.append(num)

            while dec[0] - inc[0] > limit:
                if dec[0] == nums[left]:
                    dec.popleft()

                if inc[0] == nums[left]:
                    inc.popleft()

                left += 1

            ans = max(ans, right - left + 1)

        return ans