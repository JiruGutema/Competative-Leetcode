class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n
        nums.reverse()
        nums[:k] = reversed(nums[:k])
        nums[k:] = reversed(nums[k:])


        # if k == 0 or len(nums) <= 1:
        #     return nums
        # curr = nums[0]
        # count = 0
        # idx = 0
        # start = 0

        # while count < len(nums):
        #     nxt_idx = (idx + k) % len(nums)
        #     temp = nums[nxt_idx]
        #     nums[nxt_idx] = curr
        #     curr = temp
        #     count += 1
        #     idx = nxt_idx
            
        #     if idx == start:
        #         start += 1
        #         idx = start
        #         curr = nums[idx]

        # return (nums)

        
