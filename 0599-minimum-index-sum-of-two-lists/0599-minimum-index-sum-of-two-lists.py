class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        count = defaultdict(list)
        for i in list1:
            count[i].append(list1.index(i))
        for j in list2:
             count[j].append(list2.index(j))
        
        candidate = []
        reference = float('inf')
        for k, v in count.items():
            tot = sum(v)
            if tot < reference and len(v)==2:
                reference = tot
                candidate = [k]
            elif tot == reference and len(v)==2:
                candidate.append(k)
        return ((candidate))