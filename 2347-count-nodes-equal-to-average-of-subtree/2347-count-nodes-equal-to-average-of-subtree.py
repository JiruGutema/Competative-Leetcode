# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = None
#         self.right = None

class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        self.count = 0

        def check(root):
            if not root:
                return (0,0)
            
            right_sum, right_nodes = check(root.right)
            left_sum, left_nodes = check(root.left)

            tot = right_sum + left_sum + root.val
            tot_nodes = right_nodes+left_nodes +1

            if tot//tot_nodes == root.val:
                self.count += 1
            return (tot, tot_nodes)
        check(root)
        return self.count


