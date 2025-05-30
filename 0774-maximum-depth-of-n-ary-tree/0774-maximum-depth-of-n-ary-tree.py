class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        
        def dfs(node):
            if not node.children:
                return 1
            return 1 + max(dfs(child) for child in node.children)
        
        return dfs(root)
