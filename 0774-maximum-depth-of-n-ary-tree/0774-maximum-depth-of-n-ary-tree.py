"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        gl_depth = 0
        
        def dfs(node, depth):
            nonlocal gl_depth
            gl_depth = max(depth, gl_depth)
            if not node:
                return
            for n in node.children:
                dfs(n, depth + 1)
              

            

        dfs(root, 0)
        return   gl_depth + 1 if root else gl_depth