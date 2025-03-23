class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        path = []
        res = []

        def backtrack(node):
            if not node:
                return
                
            path.append(str(node.val))
            if not node.left and not node.right:
                res.append(int("".join(path)))
            backtrack(node.left)
            backtrack(node.right)
            path.pop()

        backtrack(root)
        return sum(res)