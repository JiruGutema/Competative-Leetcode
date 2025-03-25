class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # if not nums:
        #     return -1  

        # mid = len(nums) // 2

        # if nums[mid] == target:
        #     return mid
        # elif nums[mid] < target:
        #     return self.search(nums[mid + 1:], target) if self.search(nums[mid + 1:], target) == -1 else self.search(nums[mid + 1:], target) + mid + 1
        # else:
        #     return self.search(nums[:mid], target)


        i, j = 0, len(nums)-1

        while i <= j:
            mid = (j+i) //2 
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                j = mid-1
            else:
                i = mid+1
        return -1
        

        
