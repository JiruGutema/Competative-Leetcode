
# Definition for a Node.
# class Node:
#     def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
#         self.val = val
#         self.children = children
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        ans = []

        def do(node):
            if not root:
                return []
            ans.append(node.val)
            if node.children:
                for child in node.children:
                    do(child)
        do(root)
        return ans

