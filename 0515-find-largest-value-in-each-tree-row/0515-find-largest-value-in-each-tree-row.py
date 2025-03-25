class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        idx_max = defaultdict(lambda: float('-inf'))  

        def find_maximum(node, level):
            if not node:
                return
            idx_max[level] = max(idx_max[level], node.val)
            find_maximum(node.left, level + 1)
            find_maximum(node.right, level + 1)

        find_maximum(root, 0)

        return [idx_max[i] for i in sorted(idx_max.keys())]
