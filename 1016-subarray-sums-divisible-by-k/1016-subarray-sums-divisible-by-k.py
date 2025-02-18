class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        dictionary = Counter()
        dictionary[0] = 1
        count = 0
        prefix_sum = 0  

        for num in nums:
            prefix_sum += num
            remainder = prefix_sum % k

            if remainder < 0:
                remainder += k

            count += dictionary[remainder]
            dictionary[remainder] += 1
            
        return count
