class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k,t) -> bool:
       n = len(nums)
       print(k,t)
       from sortedcontainers import SortedSet
       s=SortedSet()
       for i in range(n):
           p=s.bisect_left(nums[i]-t)
           if  p<len(s) and abs(s[p]-nums[i])<=t :
               return True
           s.add(nums[i]) 
           if len(s)>k:
               s.remove(nums[i-k])
          
       return False          
        