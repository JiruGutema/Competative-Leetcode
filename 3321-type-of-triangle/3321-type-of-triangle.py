class Solution:
    def triangleType(self, nums: List[int]) -> str:
        ln = len(set(nums))

        if ln == 1:
            return "equilateral"
        elif ln == 2:
            a = 0 
            b = 0
            for num in nums:
                if Counter(nums)[num] == 2:
                    a = num
                else:
                    b = num

            if 2*a > b:
                return "isosceles"
            else:
                return 'none'

            return "isosceles"
        else:
            if nums[0] + nums[1] > nums[2] and nums[2] + nums[1] > nums[0] and nums[0] + nums[2] > nums[1]:
                return "scalene"
            else:
                return "none"
    
