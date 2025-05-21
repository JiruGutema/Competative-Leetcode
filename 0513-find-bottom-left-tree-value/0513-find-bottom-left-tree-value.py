# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        
        queue = deque()
        queue.append(root)
        cand = None
        while queue:

            for i in range(len(queue)):
                node =  queue.popleft()

                if i == 0:
                    cand = node
                if node:
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
          

            if not queue:
                return cand.val
            
