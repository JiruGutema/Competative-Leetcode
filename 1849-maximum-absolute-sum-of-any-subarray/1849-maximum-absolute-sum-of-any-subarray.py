class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        m1 , m2= float("-inf") , float("inf")
        s1 = s2 = 0
        for num in nums:
            s1 = max(num, s1+num)
            m1 = max(s1, m1)
            s2 = min(num, s2+num)
            m2 = min(s2, m2)
        return max(abs(m2), m1)
        
        
