# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        values = []

        def get_values(node):
            if not node:
                return
            get_values(node.left)
            values.append(node.val)
            get_values(node.right)

        get_values(root)

        def construct(arr):
            if not arr:
                return None
            mid = len(arr) // 2
            root = TreeNode(arr[mid])
            root.left = construct(arr[:mid])
            root.right = construct(arr[mid + 1:])
            return root

        return construct(values)


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def __init__(self):
#         self.nodeValues = []
#         self.first = True

#     def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

#         def getValues(root):
#             if not root:
#                 self.nodeValues.append(None)
#                 return
#             if root.left:
#                 getValues(root.left)
#             self.nodeValues.append(root.val)
#             if root.right:
#                 getValues(root.right)
#         if self.first:
#             getValues(root)
#             self.first = False

#         def construct(self, arr):
#             if not arr:
#                 return
#             mid = len(arr)//2

#             root = TreeNode(arr[mid])
#             root.left = construct(self, arr[:mid])
#             root.right = construct(self, arr[mid+1:])
#             return root
            
#         return construct(self, self.nodeValues)
