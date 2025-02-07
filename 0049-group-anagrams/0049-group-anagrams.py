class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = defaultdict(list)
        ans = []

        for i in strs:
            arranged =str(sorted(i))

            if arranged in hashMap:
                ans[hashMap[arranged]].append(i)
            else:
                ans.append([i])
                hashMap[arranged] = len(ans)-1
        return ans
                
