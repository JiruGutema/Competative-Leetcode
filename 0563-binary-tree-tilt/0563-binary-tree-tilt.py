# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(node):
            if not node:
                return 0
            tot_left = dfs(node.left)
            tot_right = dfs(node.right)

            nonlocal res
            res += abs(tot_left - tot_right)

            return tot_left + tot_right + node.val
        dfs(root)
        return res