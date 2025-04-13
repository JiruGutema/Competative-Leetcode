# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        value_to_index = {val: i for i, val in enumerate(postorder)}
        N = len(preorder)
        
        def construct(pre_l, pre_r, post_l, post_r):
            if pre_l > pre_r or post_l > post_r:
                return None
            
            root = TreeNode(preorder[pre_l])
            if pre_l == pre_r:
                return root
            
           
            left_child_val = preorder[pre_l + 1]
            idx = value_to_index[left_child_val] 
            
           
            left_size = idx - post_l + 1
            
           
            root.left = construct(pre_l + 1, pre_l + left_size, post_l, idx)
            root.right = construct(pre_l + left_size + 1, pre_r, idx + 1, post_r - 1)
            
            return root
        
        return construct(0, N - 1, 0, N - 1)
