class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        space = []
        for i in range(1,n+1):
            space.append(str(i))
        return [int(i) for i in sorted(space)]
