class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # brute force

        # nums = Counter(nums)
        # nums = sorted(nums.items(), key=lambda key: key[1], reverse=True)
        # return [num[0] for num in nums[:k]]

        # using bucket sort

        count = {}
        freq = [[] for _ in range(len(nums)+1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for n,c in count.items():
            freq[c].append(n)
        
        res = []
        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                res.append(n)
            if len(res) == k:
                return res
   

























        



