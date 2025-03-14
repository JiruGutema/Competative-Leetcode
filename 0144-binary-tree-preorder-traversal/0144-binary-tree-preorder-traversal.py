# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        # if not root:
        #     return []
        
        # self.ans.append(root.val)
        # if root.left:
        #     self.preorderTraversal(root.left)

        # if root.right:
        #     self.preorderTraversal(root.right)

        # return self.ans

        def helper(root):
            if root:
                result.append(root.val)
                helper(root.left)
                helper(root.right)
            return result
        return helper(root)
        
        

        

        
