# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def searchBST(self, node: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # if not node:
        #     return None
        # if node.val == val:
        #     return node
        # if node.val > val:
        #     return self.searchBST(node.left, val)
        # return self.searchBST(node.right, val)

        while node:
            if node.val > val:
                node = node.left
            elif node.val < val:
                node = node.right
            else:
                return node
        

        
