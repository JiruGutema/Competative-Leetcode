class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        sortedToHashMap = {}
        
        for i in strs:
            sortedd = "".join(sorted(i))
            if sortedd in sortedToHashMap:
                sortedToHashMap[sortedd].append(i)
            else:
                sortedToHashMap[sortedd] = [i]
        return list(sortedToHashMap.values())