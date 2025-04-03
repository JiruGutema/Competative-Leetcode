class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        def quick(nums, left, right):
            if left >= right:  
                return
            pivot = partition(nums, left, right)

            quick(nums, left, pivot - 1)
            quick(nums, pivot + 1, right)

        def partition(nums, left, right):
            random_index = randint(left, right)
            nums[left], nums[random_index] = nums[random_index], nums[left]
            pivot = left

            holder = left + 1

            for seeker in range(holder, right + 1):
                if nums[seeker] <= nums[pivot]:
                    nums[seeker], nums[holder] = nums[holder], nums[seeker]
                    holder += 1

            nums[pivot], nums[holder - 1] = nums[holder - 1], nums[pivot]

            return holder - 1

     
        quick(nums, 0, len(nums) - 1)
        return nums
