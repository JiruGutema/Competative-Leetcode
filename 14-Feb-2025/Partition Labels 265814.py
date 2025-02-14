# Problem: Partition Labels - https://leetcode.com/problems/partition-labels/

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        n = len(s)
        i = 0
        j = 0
        res = []
        seen = defaultdict(int)
        check = set()

        for k in range(n):
            seen[s[k]] = seen.get(s[k], 0) + 1

        while i < n and i <= j:

            seen[s[j]] = seen[s[j]] - 1
            check.add(s[j])

            if seen[s[j]] == 0:
                check.remove(s[j])
            
            if len(check) == 0:
                res.append(j-i+1)
                j += 1
                i = j
            else:
                j += 1

        return res


        
        