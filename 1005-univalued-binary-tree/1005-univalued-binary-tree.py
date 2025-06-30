# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:

        queue = deque()
        queue.append(root)
        if root:
            pre = root.val

        while queue:
            loc = queue[0].val
            if loc != pre:
                return False
            pre = loc
            for idx in range(len(queue)):
                node = queue.popleft()
                if node.val != loc:
                    return False
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return True

        # if not root:
        #     return True
        # rel = root.val
        # boolean = True

        # def dfs(root):
        #     if not root:
        #         return
        #     nonlocal boolean
        #     if root.val != rel:
        #         boolean = False
        #     dfs(root.left)
        #     dfs(root.right)
        # dfs(root)
        # return boolean



            