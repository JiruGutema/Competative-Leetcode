# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        height = 0
        def dfs(node, h):
            nonlocal height
            height = max(height, h)
            if node.left:
                dfs(node.left, h+1)
            if node.right:    
                dfs(node.right, h+1)
        dfs(root, 0)

        m = height + 1
        n = 2 ** (height + 1) - 1
        
        res = [["" for _ in range(n)] for _ in range(m)]
        
        q = deque()
        q.append((root, 0, (n - 1) // 2))
        
        while q:
            for _ in range(len(q)):
                node, r, c = q.popleft()
                res[r][c] = str(node.val)
                offset = 2 ** (height - r - 1)
                if node.left:
                    q.append((node.left, r + 1, c - offset))
                if node.right:
                    q.append((node.right, r + 1, c + offset))
        
        return res
