class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # selection

        def selection(nums):
            n = len(nums)
            for i in range(n):
                min_index = i
                for j in range(i+1, n):
                    if nums[j] < nums[min_index]:
                        min_index = j
                nums[i], nums[min_index] = nums[min_index], nums[i]
            return nums
        # return selection(nums)


        def bubble(nums):
            n = len(nums)
            for i in range(n):
                for j in range(0, n-i-1):
                    if nums[j] > nums[j+1]:
                        nums[j], nums[j+1] = nums[j+1], nums[j]
            return nums
        # return bubble(nums)


        def insertion(nums):
            for i in range(1, len(nums)):
                key = nums[i]
                j = i - 1

                while j >=0 and nums[j] > key:
                    nums[j+1] = nums[j]
                    j -= 1
                nums[j+1] = key
            return nums
        # return insertion(nums)

        def mergeSort(nums):
            if len(nums) <=1:
                return nums
            
            mid = len(nums)//2

            left = mergeSort(nums[:mid])
            right = mergeSort(nums[mid:])

            return merge(left, right)

        def merge(left, right):
            sorted_arr = []

            i=j = 0

            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    sorted_arr.append(left[i])
                    i += 1
                else:
                    sorted_arr.append(right[j])
                    j += 1

            sorted_arr.extend(left[i:])
            sorted_arr.extend(right[j:])
            
            return sorted_arr
        
            

        return mergeSort(nums)



            
