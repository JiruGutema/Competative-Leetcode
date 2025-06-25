# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans = []
        path = []

        if not root:
            return []
        def isLeaf(node):

            if not node.right and not node.left:
                return True
            return False

        def backtrack(root, currSum):

            if not root:
                return
            currSum += root.val
            path.append(root.val)

            if isLeaf(root):
                if currSum == targetSum:
                    ans.append(path[:])

            backtrack(root.left, currSum)
            backtrack(root.right, currSum)
            path.pop()

        backtrack(root, 0)

        return ans

            
            
