class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Selection Sort

        for i in range(len(nums)):
            minn = nums[i]
            indexx = i
            for j in range(i+1, len(nums)):
                if nums[j] <= minn:
                    minn = nums[j]
                    indexx = j
            nums[indexx] = nums[i]
            nums[i] = minn

        # #  Bubble sort

        for i in range(len(nums)):
            for j in range(len(nums)-1):
                if nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]

        # insertion sort

        for i in range(1, len(nums)):
            key = nums[i]
            j = i - 1
            while j >= 0 and nums[j] > key:
                nums[j + 1] = nums[j]
                j -= 1
            nums[j + 1] = key
