class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter1 = 0
        counter2 = 0

        num1 = 0
        num2 = 0

        for i in nums:
            while i in nums:
                counter1 += 1
                num1 = i
                nums.remove(i)
            if counter1 > counter2:
                counter2 = counter1
                counter1 = 0
                num2 = num1
        return num2
            