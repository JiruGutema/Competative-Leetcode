"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        queue = deque()
        queue.append(root)
        ans = []
        if not root:
            return []
        while queue:
            cand = []
            for i in range(len(queue)):
                node =  queue.popleft()
                cand.append(node.val)
                if node:
                    for child in node.children:
                        if child:
                            queue.append(child)
            ans.append(cand)
          
        return ans
            