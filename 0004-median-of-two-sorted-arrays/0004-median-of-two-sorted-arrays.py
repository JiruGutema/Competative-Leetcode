class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i, j = 0, 0
        ans = []

        while i < len(nums1) and j < len(nums2):
            if nums1[i] > nums2[j]:
                ans.append(nums2[j])
                j += 1
            else:
                ans.append(nums1[i])
                i += 1
        ans.extend(nums1[i:])
        ans.extend(nums2[j:])
 
        if len(ans)%2 == 1:
            return ans[len(ans)//2]

        else:

            mid = ans[(len(ans)//2 - 1)]

            mid_plus_one = ans[(len(ans)//2)]

            return (mid + mid_plus_one)/2
