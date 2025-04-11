# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = defaultdict(list)
        count = 0
        def bfs(root, count):
            if not root:
                return 
            ans[count].append(root.val)
            bfs(root.left, count + 1)
            bfs(root.right, count + 1)
        bfs(root, count)

        res = []
        for k, v in ans.items():
            res.append(v)
        return res
        

