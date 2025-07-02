# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # height = 0
        # def dfs(root, height):
        #     if not root:
        #         return 0
        #     return max(dfs(root.left, height), dfs(root.right, height)) + 1
               
        # return dfs(root, height)

        queue = deque()
        queue.append(root)
        depth = 0

        while queue:
            depth += 1
            for _ in range(len(queue)):
                node = queue.popleft()
                if node:
                    queue.append(node.left)
                    queue.append(node.right)
        return depth - 1


       
   
    