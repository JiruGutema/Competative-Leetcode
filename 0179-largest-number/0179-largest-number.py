class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def compare(a,b):
            if a+b > b + a:
                return -1
            else:
                return 1
    
        # nums = list(map(str, nums))
        nums = [str(i) for i in nums]
        nums.sort(key=cmp_to_key(compare))

        print(nums)
        result = "".join(nums)
        return result if result[0] != "0" else "0"



